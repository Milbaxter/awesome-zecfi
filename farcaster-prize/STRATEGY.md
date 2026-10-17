# Strategy: Balaji's "$2048 for Farcaster clients" prize

Researched 2026-10-17. Facts come from reading the source of `farcasterxyz/snapchain` at v0.14.3 (2026-10-15), `farcasterxyz/hub-monorepo`, `farcasterxyz/contracts`, the npm packages (`@farcaster/core` 0.20.0, `@farcaster/hub-nodejs` 0.17.0) and news coverage. Items marked **(inferred)** were not checked against a live system. Farcaster hosts were unreachable from the research environment, so nothing here was tested against mainnet yet.

## 1. What wins

The prize text tells us how it will be judged:

1. **Human vouches are the strongest signal.** One vouch is needed to qualify; "getting more humans to vouch … will be the most powerful signal". Recruiting testers is the critical path, not the code.
2. **"Not AI slop."** Balaji's other open bounties are getting inflated, AI-generated submissions (for example the "Cloud Cartography" entries with hardcoded fake data). The way to stand out is real terminal output, real costs, real timings, real failure modes, all from actually running it.
3. **Three commands that really work** on a bare cloud account, with no API keys.
4. **A correct protocol explanation.** The brief contains two assumptions that are now out of date (see §2). Explaining them correctly, while still delivering what the brief asks for, shows we understand the protocol better than people who copied the old docs.

Gates to qualify (all required): a microsite URL, an MIT GitHub repo, and a voucher's public Farcaster cast. All three go in one reply to the prize cast **within 7 days of the cast's timestamp** (confirm the exact timestamp and set a deadline alarm 12 h earlier).

## 2. Facts that change the plan

| Brief says | Reality (Snapchain v0.14.3) | What we do |
|---|---|---|
| Issue an app key with "one small Optimism transaction" | Since engine V16 (mainnet 2026-05-07), **gasless signers** exist: a `KEY_ADD` message signed by the custody key over EIP-712, with no tx and no ETH. The official guide labels the onchain `KeyGateway.add` path "deprecated" (`site/docs/pages/guides/writing-messages.mdx`). | Default to the **onchain path** to match the brief literally (~200–300k gas, well under $0.05 on OP **(inferred)**), and offer `--gasless` with a clear explanation of the tradeoffs (scopes, 90-day sliding TTL, nonce). Both are worth teaching. |
| "A read node … does not accept writes" | Read nodes **do accept** `SubmitMessage`: they validate it against local state, then gossip it on the `mempool` topic to validators and keep nothing (`node-types.mdx`, `src/mempool/mempool.rs` `ReadNodeMempool`). A success response means "relayed", not "in a block". There is **no public keyless validator write endpoint** (`crackle.farcaster.xyz` is password-protected; Neynar's validators are not public). | Submit to your own read node and explain that it **relays to the 7 validators** (5-of-7 quorum). The client confirms by reading the message back or watching for `MERGE_MESSAGE`, and resubmits if it doesn't appear. This is the "how writes reach validators" section the brief asks for. |
| "No API keys from anyone" | The read node needs **no** Ethereum RPC: read mode does not start the onchain watchers, and onchain events arrive inside blocks. Only the onchain key tx and the `idOf` lookup need OP RPC. | Use the public `https://mainnet.optimism.io` RPC (overridable). The official guide tells you to use Alchemy/Infura; we don't. |

Other verified gotchas we must handle (each one becomes a "why this step exists" note in the tutorial):

- **The official installer is interactive.** `snapchain-bootstrap.sh` reads from `/dev/tty`, asks you to type "Yes" to a "no rewards" prompt, and asks for your FID. It breaks under cloud-init and non-interactive SSH. Fix: write `docker-compose.mainnet.yml` + `validators.toml` ourselves, or pre-seed `.env` with `AGREE_NO_REWARDS_FOR_ME=true`, `HUB_OPERATOR_FID=…`, `SKIP_CRONTAB=true`.
- **`validators.toml` changed on 2026-10-15** (registry v18: Uno and Degen out, "moria" and "isengard" in, at shard-0 height 48,632,000). A stale copy cannot verify new blocks. Pull it from the release tag that matches the pinned image.
- **Pin the image** (`farcasterxyz/snapchain:0.14.3`), not `:latest` with `pull_policy: always`, so the tutorial is reproducible. Document how to upgrade.
- **Disk:** the DB is ~549 GB, and the snapshot is staged in `.rocks.snapshot/` before extraction. **Provision 2 TB.** Put the data on the big volume (issue #497 filled the root disk).
- **Snapshot download needs no credentials.** It fetches `chunk_*.bin` files over plain HTTP from a public R2 bucket. The AWS/R2 keys in the compose file are for *uploading* only. A failed download panics and the container restart-loops; recovery is to wipe `.rocks` and retry.
- **Post-snapshot sync can be slow** (open issue #704). Measure real timings on our own runs and publish them.
- **Grafana listens on :3000 with admin/admin**, and the official cron runs a host-wide `docker system prune --volumes`. Our script must not expose the first or install the second.
- **Ports:** 3382/udp gossip must be open inbound. 3381 (HTTP) and 3383 (gRPC) should only be opened if needed; default to localhost access plus an SSH tunnel.
- **Mixed content:** the node serves plain HTTP. A browser client hosted on HTTPS cannot call it, so the client runs locally (CLI + local web UI) through an SSH tunnel, or we put Caddy with TLS in front.
- **Smart-wallet custody** (for example Coinbase-Wallet-created accounts) has no seed phrase, and gasless `KEY_ADD` only recovers ECDSA signatures. Document it as unsupported, with the workaround.
- **Seed phrase derivation** is `m/44'/60'/0'/0/0` (viem `mnemonicToAccount`). Verify with `IdRegistry.idOf(address) == fid`. The Farcaster app's in-app spending wallet is a different key.
- **Gasless deadline vs onchain deadline:** the gasless one is in *Farcaster-epoch* seconds, the onchain one in *Unix* seconds. The two EIP-712 domains also differ. This is easy to get wrong; the tutorial should call it out.

## 3. What to build

A new public repo (MIT), separate from this ZecFi repo, for example `snapchain-quickstart`.

```
provision.sh      # (0) create a server: Hetzner hcloud default; --provider do|vultr|ssh
node.sh           # (1) non-interactive Snapchain read node, pinned version, waits for sync
client/           # (2) TypeScript CLI + local web UI (Node 20+, @farcaster/hub-nodejs, viem)
site/             # microsite: quickstart + tutorial, EN + 中文
destroy.sh        # tear it all down (cost control for testers)
```

### The three commands (the quickstart)

```bash
# 0. Provision: 4 vCPU / 16 GB / 2 TB, firewall 22/tcp + 3382/udp, cloud-init installs Docker
HCLOUD_TOKEN=… curl -fsSL https://<site>/provision.sh | bash

# 1. Read node: runs on the server, returns when shards are in sync (progress bar from /v1/info blockDelay)
ssh root@<ip> 'curl -fsSL https://<site>/node.sh | bash'

# 2. Client: on your laptop, tunnels to the node, imports seed, adds app key, opens the client
npx snapchain-client@<ver> --node <ip>
```

(The cloud token is "furnishing compute", not an API key from a protocol party. Say so explicitly.)

### Client feature checklist (maps 1:1 to the brief)

- [ ] Import seed phrase, derive the custody address, look up the FID via `idOf`, and check storage (`/v1/storageLimitsByFid`); refuse with a clear message if the FID has no storage.
- [ ] Generate an ed25519 app key and register it: onchain `KeyGateway.add` (default, one OP tx, prints the tx link and cost) or `--gasless` `KEY_ADD`. Wait until the node shows the signer. Store only the app key locally (chmod 600); **never persist the seed phrase**, and say so.
- [ ] Feed: `linksByFid` (follows), then `castsByFid` per followee, merged by timestamp; profile names from `userDataByFid`; live updates from `/v1/events`.
- [ ] Post (`CastAdd`, including replies and embeds), delete (`CastRemove`), follow and unfollow (`LinkAdd`/`LinkRemove`), like and recast (`ReactionAdd`/`ReactionRemove`). The official `fc` CLI has no reactions or feed, so this is a visible gap we fill.
- [ ] Confirm each write by reading it back from our own node, and resubmit if it was dropped.
- [ ] **Per-client include/exclude:** map each cast's `signer` to the app FID that registered that key (`/v1/signer`: `requestFid` for gasless keys, ABI-decoded `SignedKeyRequestMetadata.requestFid` from the `onChainEvent` for onchain keys; use `onChainEventsByFid?event_type=EVENT_TYPE_SIGNER` for keys removed later). Show an "app" badge on every cast and give `--include-apps` / `--exclude-apps` filters. Ship a small, sourced table of known app FIDs (Farcaster app, others) and label everything else "fid N".
- [ ] Optional app FID: by default the key is self-signed (`requestFid` = your own FID). Explain that this makes casts from our client indistinguishable from other self-signed tools, and offer `--app-fid` for people who register an app identity.

### Microsite

- Quickstart at the top (three commands, copy buttons, expected output, time and cost).
- Then the tutorial, which explains concepts **at the moment they're needed**: FID and IdRegistry; custody address and recovery; app keys (onchain vs gasless, scopes, TTL); Snapchain messages (protobuf, `data_bytes`, blake3-160 hash, ed25519 signature, Farcaster epoch, network id); shards and routing; read node vs validator (5-of-7, gossip relay, why a 200 OK doesn't mean merged); storage rent (unit generations and limits, expiry, pruning, how to check); events and the 3-day retention; the trust model of the new owner (the protocol is open, app-level bans don't stop a self-built client; nothing in Snapchain validation checks the access NFT as of v0.14.3).
- Troubleshooting, built from errors we actually hit.
- Static site (Astro or plain HTML), mobile-first, dark/light, no tracking. Chinese translation reviewed by a native speaker (don't ship machine-only text; that is slop risk). A 59 s vertical screen recording of the real three commands, sped up during sync.

## 4. Getting vouchers (the critical path)

- **Cost:** a tester can run the whole thing for a few hours and then `destroy.sh`. Hetzner bills hourly. CPX42 + 2 TB volume is roughly €185/month, i.e. about €0.25/hour (prices are from search results and need checking). State the real cost up front, and offer to reimburse the first testers' cloud bill. That removes the main reason people say no.
- **Who:** 5–10 Farcaster developers. Ask directly and in /dev-type channels from day 2–3 onward, as soon as a rough version works end to end. Each vouch needs to be a public cast that ideally shows their own node's `/v1/info` and a cast posted from the client.
- **Make vouching easy:** at the end of the tutorial, the client offers to post "Just booted my own Snapchain read node + client with <site>" **from the tester's own client**. That proves it worked and doubles as the vouch. The tester must write their own words; don't auto-generate the endorsement.
- **Feedback loop:** fix every snag a tester hits the same day, and credit testers on the site.

## 5. Seven-day plan

| Day | Work |
|---|---|
| 1 | Start a real node on Hetzner now (sync takes hours). Write `node.sh` around the pinned compose file. Write the client's key registration + post path against it. |
| 2 | Feed, follow, react, delete, app filters. Read-back confirmation. `provision.sh` for hcloud plus a generic `--ssh` mode. Second clean run from zero, timing every step. |
| 3 | Microsite draft with real transcripts. First 2–3 testers start. |
| 4 | Fix tester issues. Concept sections. DigitalOcean provider. Diagrams. |
| 5 | More testers; collect vouches. Chinese translation review. Video. |
| 6 | Polish, troubleshooting page, final fresh-account run-through. |
| 7 | Submit the reply with three URLs **early in the day**, not at the deadline. Later vouches can be added to the site. |

## 6. Risks

- **Protocol churn under the new owner.** Validators moved to new operators on 2026-10-15, and the onchain `SnapchainConfigRegistry` could add rules. Pin versions, re-test the day before submitting, and put a "last verified" date on the site.
- **Slow sync** (issue #704) or snapshot bucket outage. Start the reference node on day 1. If sync is slow on network volumes, test local-NVMe instances.
- **Hetzner Volume (network Ceph) I/O** may be too slow for RocksDB **(inferred)**. Benchmark on day 1–2 and change the default provider if needed.
- **Testers' accounts with smart-wallet custody.** Pick testers who hold a seed phrase, and document the limitation.
- **Competition** expected from Hypersnap (Quilibrium fork with a feed API on the node), vrypan (`fargo`, `fc-appkey`) and hypecast (closest existing client, but it uses third-party hubs). None had submitted as of 2026-10-17. Our differentiators: stock Snapchain, exactly three commands, correct write-path explanation, and verified human runs.

## 7. Reference implementations to study

- `farcasterxyz/snapchain`: `scripts/snapchain.sh`, `docker-compose.mainnet.yml`, `site/docs/pages/{node-types,managing-a-node,guides/writing-messages}.mdx`, `src/network/http_server.rs` (all `/v1/*` routes).
- `farcasterxyz/hub-monorepo`: `packages/core/src/builders.ts` (`makeKeyAddBody`, `makeCastAdd`, …), `packages/hub-nodejs/examples/hello-world`.
- `farcasterxyz/contracts`: `src/KeyGateway.sol`, `src/validators/SignedKeyRequestValidator.sol`. OP mainnet addresses: KeyGateway `0x00000000fC56947c7E7183f8Ca4B62398CaAdf0B`, IdRegistry `0x00000000Fc6c5F01Fc30151999387Bb99A9f489b`, KeyRegistry `0x00000000fc1237824fb747abde0ff18990e59b7e`, SignedKeyRequestValidator `0x00000000FC700472606ED4fA22623Acf62c60553`.
- `pierce403/hypecast` (seed import + signing in a PWA) and `farcasterorg/hypersnap` (node-side feed API).

## Sources

- Snapchain repo and docs source: https://github.com/farcasterxyz/snapchain (v0.14.3)
- Hub monorepo: https://github.com/farcasterxyz/hub-monorepo
- Contracts: https://github.com/farcasterxyz/contracts
- Slow-sync issue: https://github.com/farcasterxyz/snapchain/issues/704
- Acquisition: https://www.theblock.co/news/ecosystems/2026-10-15-network-school-acquires-farcaster-from-neynar-418720, https://cointelegraph.com/news/balajis-singapore-of-social-media-begins-with-a-wave-of-bans, https://cryptobriefing.com/network-school-acquires-farcaster-network-state-protocol
- Example of the AI-generated bounty submissions we must not resemble: https://github.com/chiuhehe1-design/conm/issues/28
