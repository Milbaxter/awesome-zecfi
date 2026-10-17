# Detailed ZecFi directory

Snapshot: **2026-10-18**. [Method and status definitions](methodology.md) · [Awesome list](../README.md)

Descriptions summarize publisher documentation. Review focuses are editorial questions, not completed security assessments. Network tags describe relevance, not a certified list of live deployments.

## Zcash protocol, shielded pools and upgrades

<a id="crosslink"></a>
### Crosslink (hybrid PoW/PoS finality)

**Type:** protocol · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `testnet`

A Shielded Labs proposal to add a proof-of-stake BFT finality layer on top of Zcash's proof-of-work chain, now running as a prototype 'Feature Net'.

- **Zcash mechanism:** Miners keep producing PoW blocks while ZEC-staking finalizers vote to finalize them; the feature net includes staking actions, finalizer commissions and slashing tests using test ZEC.
- **Review focus:** Is the feature net incentivized and with what rewards? Which parts would be upstreamed to Zebra? What are staking custody and slashing risks for delegators? Is there any activation proposal or ZIP?
- **Evidence and availability qualification:** Runs only on a prototype feature net with code the README calls non-production, and has no mainnet ZIP or activation height. Whether the feature net is incentivized is reported only by secondary sources.
- **Project/resource:** [Crosslink (hybrid PoW/PoS finality)](https://shieldedlabs.net/crosslink/)
- **Source 1:** [crosslink_monolith releases v14 (2026-10-01), v15 (2026-10-13, feature-net upgrade at PoW height 55,296)](https://github.com/ShieldedLabs/crosslink_monolith/releases) — primary; reviewed 2026-10-15.
- **Source 2:** [Shielded Labs roadmap: Productionization phase Q2 2026–Q2 2027](https://shieldedlabs.net/roadmap/) — primary; reviewed 2026-10-15.
- **Source 3:** [Shielded Labs Crosslink page ('proposed upgrade')](https://shieldedlabs.net/crosslink/) — primary; reviewed 2026-10-15.
- **Source 4:** [Crosslink Incentivized Feature Net Season 1, from 15 Apr 2026](https://forum.zcashcommunity.com/t/crosslink-incentivized-feature-net/55210) — primary; reviewed 2026-10-15.
- **Source 5:** [zebra-crosslink repository](https://github.com/ShieldedLabs/zebra-crosslink) — primary; reviewed 2026-10-15.

<a id="dev-fund-coinholder-fund"></a>
### Dev fund, lockbox and Coinholder-Controlled Fund (NU6.1)

**Type:** protocol · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `mainnet-announced`

The post-2025 Zcash development funding model, which sends 8% of block rewards to Zcash Community Grants and 12% to a coinholder-voted fund seeded by the deferred lockbox.

- **Zcash mechanism:** Protocol funding streams send 8% of block subsidy to ZCG and continue a 12% lockbox stream (FS_CCF_H3) governed by ZIP 1016 coinholder votes (quarterly, 420,000 ZEC quorum); at NU6.1 the one-time 78,750 ZEC lockbox balance was paid to a 2-of-3 multisig of ZF, ECC and Shielded Labs.
- **Review focus:** Who holds the multisig keys now that ECC's team has left? Are key-holder funds shielded as ZIP 271 requires? What have coinholder votes funded, and how does NU7's 25s block time shift the funding-stream end heights?
- **Evidence and availability qualification:** NU6.1 activated at mainnet height 3,146,400 (ZIP 255 Final), but ZIPs 1016/271 still show 'Proposed' status. Electric Coin Company is still named as a key-holder organization after its team left for ZODL, which is an open governance question.
- **Project/resource:** [Dev fund, lockbox and Coinholder-Controlled Fund (NU6.1)](https://zips.z.cash/zip-1016)
- **Source 1:** [ZIP 1016: Community and Coinholder Funding Model (Proposed)](https://zips.z.cash/zip-1016) — primary; reviewed 2026-10-15.
- **Source 2:** [ZIP 271: Dev Fund Extension and One-Time Disbursement (78,750 ZEC lockbox at NU6.1)](https://zips.z.cash/zip-0271) — primary; reviewed 2026-10-15.
- **Source 3:** [ZIP index: ZIP 255 NU6.1 deployment Final](https://zips.z.cash/) — primary; reviewed 2026-10-15.
- **Source 4:** [ZIP 1015 (Status: Final)](https://zips.z.cash/zip-1015) — primary; reviewed 2026-10-15.

<a id="ironwood-nu6-3"></a>
### Ironwood shielded pool (NU6.3)

**Type:** protocol · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `mainnet-announced`

A new shielded pool, introduced by the NU6.3 network upgrade, that reuses the corrected Orchard protocol with formal verification and receives funds migrated from Orchard.

- **Zcash mechanism:** Orchard-protocol receivers (including existing unified addresses) receive into Ironwood; value leaving Orchard passes a turnstile so total migrated supply is auditable; Ironwood outputs use the ZIP 2005 quantum-recoverable note format.
- **Review focus:** Does your wallet actually create Ironwood outputs (ZIP 326 says wallets MUST NOT send to Orchard-pool receivers after NU6.3)? How is use_qsk key derivation handled on seed restore? What share of Orchard has migrated?
- **Evidence and availability qualification:** The ZIP index lists NU6.3 as a settled upgrade at mainnet block 3,428,143 (late July 2026), although ZIP 258 itself is still marked Draft. zcashd does not implement NU6.3, so Zebra-family nodes are the only validators that follow it.
- **Project/resource:** [Ironwood shielded pool (NU6.3)](https://zodl.com/ironwood-a-new-shielded-pool-for-zcash/)
- **Source 1:** [ZIP 258: NU6.3 deployment, mainnet height 3,428,143](https://zips.z.cash/zip-0258) — primary; reviewed 2026-10-15.
- **Source 2:** [ZIP 326: NU6.3 Consequences for Wallets (Draft)](https://zips.z.cash/zip-0326) — primary; reviewed 2026-10-15.
- **Source 3:** [ZODL: Ironwood, a new shielded pool for Zcash (June 2026)](https://zodl.com/ironwood-a-new-shielded-pool-for-zcash/) — primary; reviewed 2026-10-15.
- **Source 4:** [ZIP index (settled upgrades, ZIP statuses)](https://zips.z.cash/) — primary; reviewed 2026-10-15.

<a id="nu7-network-upgrade"></a>
### NU7 network upgrade

**Type:** protocol · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `testnet`

A pending Zcash network upgrade that shortens block time to 25 seconds, disallows v4 transactions, and adds Network Sustainability Mechanism fee burning and issuance changes.

- **Zcash mechanism:** Changes the consensus rules for all ZEC (ZIP 218 25-second blocks, ZIP 2003 no v4 txs, ZIP 235 burns 60% of fees, ZIP 237 halving-preserving NSM, funding-stream height updates). It adds no new transaction format and no ZSA.
- **Review focus:** Was the mainnet activation height set on 20 Oct 2026 as planned? How do 25-second blocks affect confirmation counts at exchanges and bridges? Are wallet fee and expiry assumptions updated?
- **Evidence and availability qualification:** Live on testnet at height 4,465,026, but ZIP 259 had no mainnet height as of 15 Oct 2026 (to be set 20 Oct), so the press-reported 5 Nov date is provisional. ZIPs 233/234 (other NSM variants) are excluded.
- **Project/resource:** [NU7 network upgrade](https://zips.z.cash/zip-0259)
- **Source 1:** [ZIP 259: Deployment of NU7 (Draft, created 2026-09-15; mainnet height 'TBD, to be set on Oct 20')](https://zips.z.cash/zip-0259) — primary; reviewed 2026-10-15.
- **Source 2:** [Zebra v7.0.0-rc.0 (2026-10-02)](https://github.com/ZcashFoundation/zebra/releases) — primary; reviewed 2026-10-15.
- **Source 3:** [ZIP index (settled upgrades, ZIP statuses)](https://zips.z.cash/) — primary; reviewed 2026-10-15.

<a id="orchard-shielded-pool"></a>
### Orchard shielded pool (incl. NU6.2 mitigation)

**Type:** protocol · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `deprecated`

The Halo 2-based shielded pool (NU5, 2022) that was restricted to withdrawals-only by NU6.3 after a 2026 circuit soundness bug.

- **Zcash mechanism:** After NU6.3, Orchard notes can only be spent out (including into Ironwood via the turnstile); no new value may enter Orchard and cross-address transfers inside Orchard are disabled.
- **Review focus:** Has all Orchard value been migrated or is any stuck? What did the turnstile accounting show about possible counterfeiting? Do wallets still scan Orchard for older accounts?
- **Evidence and availability qualification:** An Orchard circuit vulnerability was disclosed on 1 Jun 2026, mitigated in NU6.2 (ZIP 257), and since NU6.3 (mainnet block 3,428,143) Orchard is spend-only. ZODL reports no evidence of exploitation, while press reports note that shielding means cryptography alone cannot rule it out.
- **Project/resource:** [Orchard shielded pool (incl. NU6.2 mitigation)](https://zips.z.cash/zip-0258)
- **Source 1:** [ZIP 258: Deployment of NU6.3 (Draft, created 2026-06-19)](https://zips.z.cash/zip-0258) — primary; reviewed 2026-10-15.
- **Source 2:** [ZIP index: ZIP 257 Orchard Temporary Vulnerability Mitigation and NU6.2 (Final)](https://zips.z.cash/) — primary; reviewed 2026-10-15.
- **Source 3:** [zcashd End of Life page (Orchard vulnerability disclosed 1 Jun 2026)](https://zcash.github.io/zcash/user/end-of-life.html) — primary; reviewed 2026-10-15.
- **Source 4:** [ZODL: Orchard vulnerability successfully remediated (2026-06-02)](https://zodl.com/orchard-vulnerability-successfully-remediated/) — primary; reviewed 2026-10-15.
- **Source 5:** [ZODL: Ironwood, a new shielded pool for Zcash (2026-06-06)](https://zodl.com/ironwood-a-new-shielded-pool-for-zcash/) — primary; reviewed 2026-10-15.

<a id="project-tachyon"></a>
### Project Tachyon

**Type:** research · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `research`

A proposed Zcash scaling upgrade aimed at much smaller shielded transactions, oblivious wallet sync and bounded validator state, with post-quantum privacy as a side effect.

- **Zcash mechanism:** Would change how shielded transactions are proven and how wallets sync; early code (e.g. recursive-proof work) is being merged into Zakura Common libraries.
- **Review focus:** Which ZIPs specify it? What is the trust model for oblivious sync services? Which throughput targets are measured rather than projected?
- **Evidence and availability qualification:** Still a proposal, with no activation scheduled. Throughput figures quoted in the press (10k–50k TPS) are targets, not measurements.
- **Project/resource:** [Project Tachyon](https://tachyon.z.cash/)
- **Source 1:** [Project Tachyon site (proposal; requires community approval)](https://tachyon.z.cash/) — primary; reviewed 2026-10-15.
- **Source 2:** [ZODL Ironwood post listing Tachyon among the proposing organizations](https://zodl.com/ironwood-a-new-shielded-pool-for-zcash/) — primary; reviewed 2026-10-15.

<a id="sapling-shielded-pool"></a>
### Sapling shielded pool

**Type:** protocol · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

The Groth16-based shielded pool introduced in 2018 and still usable alongside the newer pools.

- **Zcash mechanism:** Shielded notes with encrypted amounts, addresses and memos; addresses are 'zs' Sapling addresses or Sapling receivers in a unified address.
- **Review focus:** Which wallets still default to Sapling? Is any deprecation of Sapling proposed in current ZIPs? How much ZEC remains in Sapling?
- **Evidence and availability qualification:** Not affected by the 2026 Orchard bug or the NU6.3 Orchard closure as far as the ZIPs reviewed show; wallets increasingly label it 'legacy shielded'.
- **Project/resource:** [Sapling shielded pool](https://zips.z.cash/)
- **Source 1:** [ZIP index (settled upgrades, ZIP statuses)](https://zips.z.cash/) — primary; reviewed 2026-10-15.
- **Source 2:** [Cake Wallet Zcash docs (lists 'Legacy Shielded (Sapling)')](https://docs.cakewallet.com/cryptos/zcash/) — primary; reviewed 2026-10-15.

<a id="shielded-memos"></a>
### Shielded memos (ZIP 302)

**Type:** standard · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

The encrypted 512-byte memo field carried by shielded Zcash outputs, used for payment references and private messages.

- **Zcash mechanism:** Memos are encrypted to the recipient of a shielded output and are readable only with the matching viewing key; transparent outputs carry no memo.
- **Review focus:** Which structured memo formats do wallets support? Are memos visible to anyone who has been given a viewing key? How do exchanges handle memo-based deposit IDs?
- **Evidence and availability qualification:** Memo privacy depends on the output being shielded and on who holds viewing keys.
- **Project/resource:** [Shielded memos (ZIP 302)](https://zips.z.cash/zip-0302)
- **Source 1:** [ZIP 302: Standardized Memo Field Format (Draft)](https://zips.z.cash/zip-0302) — primary; reviewed 2026-10-15.
- **Source 2:** [Zodl site: encrypted shielded notes/messages](https://zodl.com/) — primary; reviewed 2026-10-15.

<a id="unified-addresses"></a>
### Unified Addresses (ZIP 316)

**Type:** standard · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

The Zcash address and viewing-key encoding that bundles receivers for several pools (transparent, Sapling, Orchard-protocol) into one string.

- **Zcash mechanism:** The sender's wallet picks the most private receiver it supports. After NU6.3, Orchard-protocol receivers in existing UAs receive into Ironwood.
- **Review focus:** Does the wallet verify all receivers in a UA (e.g. Keystone cannot fully verify Sapling receivers)? Does a UA that includes a transparent receiver leak linkability? How are TEX addresses handled?
- **Evidence and availability qualification:** A UA that contains a transparent receiver can still be paid transparently by wallets without shielded support.
- **Project/resource:** [Unified Addresses (ZIP 316)](https://zips.z.cash/zip-0316)
- **Source 1:** [ZIP 316: Unified Addresses (Rev 0 Active, Rev 2 Draft)](https://zips.z.cash/zip-0316) — primary; reviewed 2026-10-15.
- **Source 2:** [ZIP 326: Orchard receivers receive Ironwood funds](https://zips.z.cash/zip-0326) — primary; reviewed 2026-10-15.

<a id="viewing-keys"></a>
### Viewing keys and HD derivation (ZIP 32 / ZIP 310)

**Type:** standard · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Zcash key hierarchy that lets a holder share incoming or full viewing keys to disclose shielded activity without giving spend authority.

- **Zcash mechanism:** Full/incoming viewing keys decrypt shielded notes for audit or compliance; ZIP 32 defines HD derivation for shielded keys. Ironwood adds a use_qsk derivation flag (ZIP 2005 / ZIP 326).
- **Review focus:** What exactly does a shared viewing key reveal (history, memos, future receipts)? Can it be revoked (no, only by moving funds)? Does the wallet handle use_qsk correctly on restore?
- **Evidence and availability qualification:** Viewing-key disclosure is selective but irreversible for past activity.
- **Project/resource:** [Viewing keys and HD derivation (ZIP 32 / ZIP 310)](https://zips.z.cash/zip-0032)
- **Source 1:** [ZIP 32: Shielded Hierarchical Deterministic Wallets (Final)](https://zips.z.cash/zip-0032) — primary; reviewed 2026-10-15.
- **Source 2:** [ZIP 310: Security Properties of Sapling Viewing Keys (Draft)](https://zips.z.cash/zip-0310) — primary; reviewed 2026-10-15.
- **Source 3:** [ZIP 326 use_qsk scanning rules](https://zips.z.cash/zip-0326) — primary; reviewed 2026-10-15.

<a id="zcash-improvement-proposals"></a>
### Zcash Improvement Proposals (ZIPs)

**Type:** standard · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

The specification process and repository for Zcash consensus, wallet and governance changes.

- **Zcash mechanism:** Defines every pool, address format, upgrade and funding rule that ZEC holders and integrators depend on.
- **Review focus:** Check the status mismatch for deployed upgrades (e.g. NU6.3 settled while ZIP 258 is still Draft) and which editors approve changes.
- **Evidence and availability qualification:** ZIP status labels lag deployment in several cases (ZIP 258, 271, 1016).
- **Project/resource:** [Zcash Improvement Proposals (ZIPs)](https://zips.z.cash/)
- **Source 1:** [ZIP index (settled upgrades, ZIP statuses)](https://zips.z.cash/) — primary; reviewed 2026-10-15.
- **Source 2:** [zcash/zips GitHub repository](https://github.com/zcash/zips) — primary; reviewed 2026-10-15.

<a id="zcash-shielded-assets"></a>
### Zcash Shielded Assets (ZSA / OrchardZSA)

**Type:** protocol · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `testnet`

A proposed extension of the Orchard protocol, led by QEDIT, that would let assets other than ZEC be issued, transferred and burned inside a shielded pool.

- **Zcash mechanism:** Specified in ZIP 226 (transfer and burn) and ZIP 227 (issuance) using v6 transactions; QEDIT runs a separate ZSA test network with its own Zebra fork and explorer.
- **Review focus:** How does ZSA relate to Ironwood now that Orchard is closed? Which upgrade (if any) is targeted? Have the audits been redone after the 2026 Orchard circuit bug?
- **Evidence and availability qualification:** ZSA is not in NU7 per ZIP 259; earlier 2026 reporting that NU7 would carry ZSA is outdated. Exists only on QEDIT's ZSA testnet, and no mainnet activation is scheduled.
- **Project/resource:** [Zcash Shielded Assets (ZSA / OrchardZSA)](https://github.com/QED-it)
- **Source 1:** [ZIP index: ZIP 226/227 Draft, ZIP 220 Withdrawn](https://zips.z.cash/) — primary; reviewed 2026-10-15.
- **Source 2:** [ZIP 259: NU7 does not include ZSA](https://zips.z.cash/zip-0259) — primary; reviewed 2026-10-15.
- **Source 3:** [QEDIT Zipherscan README (ZSA testnet explorer at test-zsa.org)](https://github.com/QED-it/zipherscan) — primary; reviewed 2026-10-15.
- **Source 4:** [ZIP 226: Transfer and Burn of ZSAs, Status Draft](https://zips.z.cash/zip-0226) — primary; reviewed 2026-10-15.
- **Source 5:** [ZIP 227: Issuance of ZSAs, Status Draft](https://zips.z.cash/zip-0227) — primary; reviewed 2026-10-15.

## ZEC representations and bridges

<a id="bitfrost-bzec"></a>
### Bitfrost Native ZEC (BZEC) on Hyperliquid

**Type:** asset · **Networks:** Zcash, Hyperliquid · **Reviewed:** 2026-10-15

**Evidence:** `ecosystem-only` · **Lifecycle:** `unverified`

Hyperliquid spot token named 'Bitfrost Native ZEC' (BZEC), with a HyperEVM contract, that third-party guides describe as ZEC bridged by Bitfrost's HYPE-staked validator set.

- **Zcash mechanism:** Reportedly, native ZEC is deposited to the Bitfrost bridge and BZEC is credited on HyperCore. The issuer's mechanism and custody could not be checked against a primary source because the bitfrost.xyz site returned an S3 NoSuchBucket error on 2026-10-15. Transparent on Hyperliquid.
- **Review focus:** Is the Bitfrost bridge still operating and redeeming BZEC? Who are the validators and what secures the Zcash keys? Where are the official docs now? Is there a published reserve address? Are users holding BZEC able to withdraw?
- **Evidence and availability qualification:** The issuer site was unreachable during review, so redemption status is unknown and should be treated as high-risk until Bitfrost confirms it. This is not evidence of a shutdown. Like other wrapped ZEC, BZEC carries no shielded privacy.
- **Project/resource:** [Bitfrost Native ZEC (BZEC) on Hyperliquid](https://app.hyperliquid.xyz/explorer/token/0x33b2c5252e8ea8431808129c41668129)
- **Source 1:** [Hyperliquid API POST {type:spotMeta}: BZEC 'Bitfrost Native ZEC', evm 0xbe068bb3…](https://api.hyperliquid.xyz/info) — primary; reviewed 2026-10-15.
- **Source 2:** [bitfrost.xyz returned S3 NoSuchBucket (site unreachable) on 2026-10-15](https://bitfrost.xyz) — primary; reviewed 2026-10-15.

<a id="omni-bridge-zec-solana"></a>
### Omni Bridge ZEC on Solana

**Type:** asset · **Networks:** Zcash, NEAR, Solana · **Reviewed:** 2026-10-15

**Evidence:** `code-only` · **Lifecycle:** `unverified`

SPL token named Zcash (ZEC), mint A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS, whose mint authority is the NEAR Omni Bridge Solana program's authority PDA; it is the ZEC listed by NEAR Intents on Solana and used by Kamino's ZCASH market.

- **Zcash mechanism:** Omni Bridge mints the SPL token on Solana against ZEC held on the NEAR side. The NEAR-side backing token is not confirmed here; NEAR Intents docs say Zcash enters via the POA Bridge, while docs.near.org lists Zcash as an Omni Bridge chain (light client plus Chain Signatures). This may be two bridge layers deep. Transparent on Solana.
- **Review focus:** Which NEAR token backs the Solana mint: zec.omft.near (POA) or an Omni-native Zcash connector? How many bridge layers sit between the SPL token and native ZEC? Who can upgrade the Omni Bridge Solana program? Is the Wormhole leg used for Solana messages?
- **Evidence and availability qualification:** Possibly a double-wrapped IOU (Zcash, then a NEAR bridge token, then an Omni-minted SPL). Holding or lending it on Solana is fully transparent. Its backing depends on NEAR bridge operators, not on the Zcash protocol.
- **Project/resource:** [Omni Bridge ZEC on Solana](https://docs.near.org/chain-abstraction/omnibridge/overview)
- **Source 1:** [NEAR docs Omni Bridge overview: lists Zcash (light client + Chain Signatures)](https://docs.near.org/chain-abstraction/omnibridge/overview) — primary; reviewed 2026-10-15.
- **Source 2:** [NEAR Intents docs: Omni Bridge chains (Zcash not listed; other chains use POA/HOT)](https://docs.near-intents.org/learn/omni-bridge/overview) — primary; reviewed 2026-10-15.
- **Source 3:** [NEAR Intents 1Click token list (GET), lists nep141:zec.omft.near and ZEC on Solana/Starknet/Aptos, 2026-10-15](https://1click.chaindefuser.com/v0/tokens) — primary; reviewed 2026-10-15.
- **Source 4:** [Solana RPC getAccountInfo(A7bdiYdS…XaS, jsonParsed): mintAuthority FvULawNPGBbuwYus74ECaQoV1oH9Tk6XPN7VPN51NYds](https://api.mainnet-beta.solana.com) — primary; reviewed 2026-10-15.
- **Source 5:** [near/omni-cli-rs: FvULaw… is the Omni bridge program 'authority' PDA](https://github.com/near/omni-cli-rs/blob/main/src/chains/svm/idl.rs) — primary; reviewed 2026-10-15.

<a id="unit-zec-hyperliquid"></a>
### Unit Zcash (UZEC) on Hyperliquid

**Type:** bridge · **Networks:** Zcash, Hyperliquid · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `mainnet-announced`

Unit's asset-tokenization layer, which credits deposits of native ZEC as the HIP-1 spot token UZEC (Unit Zcash) on Hyperliquid's HyperCore and fulfils withdrawals back to Zcash.

- **Zcash mechanism:** Users deposit to a Zcash address generated by Unit's MPC Guardian Network and tied to their Hyperliquid address. Withdrawals are paid from Unit's Zcash treasury address, which is transparent (t1…). Deposits need 100 Zcash confirmations.
- **Review focus:** Who are Unit's guardians and what is the signing threshold? Can deposits come from shielded addresses, or only transparent ones? Are treasury reserves auditable on-chain against UZEC supply? Who controls the multisig that deployed the HyperCore token?
- **Evidence and availability qualification:** UZEC is custodied by Unit's MPC guardian set, so it is an IOU. Deposit and withdrawal flows go through transparent Zcash addresses, and trading UZEC on Hyperliquid is fully public.
- **Project/resource:** [Unit Zcash (UZEC) on Hyperliquid](https://hyperunit.xyz)
- **Source 1:** [Unit docs: mainnet token table (ZEC/UZEC, Zcash Mainnet), Zcash treasury t1KbKk…, 100 confirmations](https://docs.hyperunit.xyz/llms-full.txt) — primary; reviewed 2026-10-15.
- **Source 2:** [Hyperliquid API POST {type:spotMeta}: UZEC 'Unit Zcash' token 0x1c994ad3…](https://api.hyperliquid.xyz/info) — primary; reviewed 2026-10-15.

<a id="zec-on-near-poa"></a>
### ZEC on NEAR Intents (zec.omft.near, POA Bridge)

**Type:** asset · **Networks:** Zcash, NEAR, Starknet, Aptos · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `mainnet-announced`

Bridged ZEC token (nep141:zec.omft.near) issued by the NEAR Intents Proof-of-Authority bridge, also listed by the 1Click API as ZEC on Starknet and Aptos.

- **Zcash mechanism:** Native ZEC is held at transparent Zcash addresses by the POA Bridge, which credits zec.omft.near on NEAR; the Starknet and Aptos ZEC tokens listed by the API are further bridged representations. None of these tokens are shielded.
- **Review focus:** Is there published proof of reserves for the Zcash side? How many POA signers exist and who are they? How are the Starknet and Aptos ZEC tokens minted and redeemed, and by which bridge? Is there a pause or freeze authority?
- **Evidence and availability qualification:** A Proof-of-Authority (trusted-operator) IOU for ZEC; holders depend on the bridge operators for redemption. Wrapped ZEC on NEAR, Starknet or Aptos is a transparent token on those chains and has no Zcash shielded privacy.
- **Project/resource:** [ZEC on NEAR Intents (zec.omft.near, POA Bridge)](https://docs.near-intents.org/integration/bridging/overview)
- **Source 1:** [NEAR Intents token bridges: POA Bridge covers Zcash](https://docs.near-intents.org/integration/bridging/overview) — primary; reviewed 2026-10-15.
- **Source 2:** [NEAR Intents 1Click token list (GET), lists nep141:zec.omft.near and ZEC on Solana/Starknet/Aptos, 2026-10-15](https://1click.chaindefuser.com/v0/tokens) — primary; reviewed 2026-10-15.
- **Source 3:** [NEAR Intents chain support: Zcash partially supported, transparent addresses only](https://docs.near-intents.org/resources/chain-support) — primary; reviewed 2026-10-15.

<a id="zenzec"></a>
### zenZEC (Zenrock)

**Type:** asset · **Networks:** Zcash, Solana · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Zenrock's Decentralized Custody Token for Zcash, minted on Solana (mint JDt9rRGaieF6aN1cJkXFeUmsy7ZE4yY3CZb8tVMXVroS) against ZEC locked in Zenrock's decentralized MPC custody network.

- **Zcash mechanism:** Native ZEC is deposited to addresses controlled by Zenrock's dMPC signer network (zrChain), and zenZEC is minted 1:1 on Solana. Whether deposits or redemptions can use shielded addresses is not documented on the fetched page. zenZEC on Solana is transparent.
- **Review focus:** Who runs the dMPC signer nodes, what is the signing threshold, and can the set be changed? Are deposit and redemption addresses transparent or shielded? Is there a public proof of reserves? Who holds the Solana mint authority (6kgpWR…)? Zenrock's docs site returned DEPLOYMENT_DISABLED on 2026-10-15; where is the current documentation?
- **Evidence and availability qualification:** Custody sits with Zenrock's MPC network rather than one custodian, but holders still trust that signer set. The homepage offers minting, but the fetched pages do not state explicitly that zenZEC is live, so it is kept unverified. On Solana it is a transparent token with no Zcash privacy.
- **Project/resource:** [zenZEC (Zenrock)](https://www.zenrocklabs.io)
- **Source 1:** [Zenrock homepage: 'Mint zenZEC – Zcash on Solana', DCT standard, dMPC custody](https://www.zenrocklabs.io/) — primary; reviewed 2026-10-15.
- **Source 2:** [Jupiter token API: 'Zenrock ZEC' zenZEC, verified tag](https://lite-api.jup.ag/tokens/v2/search?query=JDt9rRGaieF6aN1cJkXFeUmsy7ZE4yY3CZb8tVMXVroS) — primary; reviewed 2026-10-15.
- **Source 3:** [Raydium API: zenZEC CLMM pools (USDC, WSOL, USD1, ZEC)](https://api-v3.raydium.io/pools/info/mint?mint1=JDt9rRGaieF6aN1cJkXFeUmsy7ZE4yY3CZb8tVMXVroS) — primary; reviewed 2026-10-15.

<a id="ztarknet"></a>
### Ztarknet

**Type:** network · **Networks:** Zcash, Starknet · **Reviewed:** 2026-10-15

**Evidence:** `code-only` · **Lifecycle:** `research`

Proposed Starknet-style L2 that runs Cairo programs and settles to Zcash L1 through a draft Transparent Zcash Extension that verifies Circle STARK proofs.

- **Zcash mechanism:** Settlement would rely on a draft TZE ZIP (zcash/zips PR 1107) on a Zebra fork. No ZEC bridge or deposit mechanism is specified. A developer quickstart references a faucet-funded network, but the faucet was unreachable on 2026-10-15.
- **Review focus:** How would ZEC move into and out of the L2, and with what custody? Has the TZE ZIP any path to activation? What is the data-availability design? Is there an operating devnet, and who runs the sequencer?
- **Evidence and availability qualification:** Research or proof-of-concept only. There is no ZEC on it and no bridge, and since the TZE is transparent, the privacy of any future ZEC moved to it is unclear.
- **Project/resource:** [Ztarknet](https://ztarknet.cash)
- **Source 1:** [Ztarknet README: 'Status: concept + references for a PoC'](https://github.com/Ztarknet/ztarknet) — primary; reviewed 2026-10-15.
- **Source 2:** [Ztarknet quickstart: deploy a Noir app with a faucet-funded account](https://github.com/Ztarknet/quickstart) — primary; reviewed 2026-10-15.

## Cross-chain swaps and routing

<a id="maya-protocol-zec"></a>
### Maya Protocol (MAYAChain) ZEC pool

**Type:** protocol · **Networks:** Zcash, Bitcoin, Ethereum, Arbitrum, Cardano, Dash, THORChain · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

THORChain-fork cross-chain AMM with a native ZEC.ZEC pool that swaps ZEC against assets such as BTC, ETH and stablecoins without wrapped tokens.

- **Zcash mechanism:** ZEC is held in a transparent threshold-signature vault (t1 inbound address). Maya also accepts a shielded memo: the deposit sends value to the transparent vault plus a 0-value shielded note carrying the swap memo to Maya's unified address. Maya publishes the incoming viewing key (UIVK) for that address, so anyone can decrypt the memo.
- **Review focus:** How many nodes sign the ZEC vault, and what bond or slash backs them? Can outbound payouts go to shielded (u1) addresses? Is publishing the UIVK understood by users, given it makes the memo public? What are the halt and solvency-check controls (HALTZECCHAIN, SOLVENCYHALTZECCHAIN)?
- **Evidence and availability qualification:** Operational per the MAYANode API on 2026-10-15. Funds in flight sit in a bonded-node vault, not with a single custodian. The value output always hits a transparent vault, and the 'shielded' memo can be read by anyone holding the published viewing key, so the swap is not private.
- **Project/resource:** [Maya Protocol (MAYAChain) ZEC pool](https://www.mayaprotocol.com)
- **Source 1:** [MAYANode pools: ZEC.ZEC status Available, 2026-10-15](https://mayanode.mayachain.info/mayachain/pools) — primary; reviewed 2026-10-15.
- **Source 2:** [MAYANode inbound_addresses: ZEC vault t1bRYL…, shielded_memo_config enabled with published UIVK](https://mayanode.mayachain.info/mayachain/inbound_addresses) — primary; reviewed 2026-10-15.
- **Source 3:** [MAYANode mimir: HALTZECTRADING 0, ZECSHIELDEDMEMOENABLED 1](https://mayanode.mayachain.info/mayachain/mimir) — primary; reviewed 2026-10-15.
- **Source 4:** [Maya Protocol homepage and Academy (states Zcash integration)](https://www.mayaprotocol.com/) — primary; reviewed 2026-10-15.

<a id="near-intents-zec"></a>
### NEAR Intents (ZEC routes)

**Type:** protocol · **Networks:** Zcash, NEAR, Ethereum, Solana, Bitcoin, Starknet, Aptos · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `mainnet-announced`

Intent-based cross-chain swap network whose 1Click API quotes swaps into and out of native ZEC, settled by market makers through a verifier contract on NEAR.

- **Zcash mechanism:** Users send ZEC to a transparent (t1/t3) deposit address controlled by the POA Bridge; ZEC is represented on NEAR as nep141:zec.omft.near and paid out to a transparent Zcash address. The docs mark Zcash as transparent-only.
- **Review focus:** Who are the POA Bridge authorities and how are the Zcash deposit keys held? What happens to a deposit sent from or to a shielded address? What are the refund rules and thresholds for failed or mis-addressed swaps? Which market makers quote ZEC, and can quotes be censored?
- **Evidence and availability qualification:** Custodial in practice: ZEC sits with the Proof-of-Authority bridge operators while in Intents. Every route crosses a transparent Zcash address, so shielded privacy does not carry across; wallets can only reduce linkability by shielding before and after.
- **Project/resource:** [NEAR Intents (ZEC routes)](https://near-intents.org)
- **Source 1:** [NEAR Intents chain support: Zcash partially supported, transparent addresses only](https://docs.near-intents.org/resources/chain-support) — primary; reviewed 2026-10-15.
- **Source 2:** [NEAR Intents token bridges: POA Bridge covers Zcash](https://docs.near-intents.org/integration/bridging/overview) — primary; reviewed 2026-10-15.
- **Source 3:** [NEAR Intents 1Click token list (GET), lists nep141:zec.omft.near and ZEC on Solana/Starknet/Aptos, 2026-10-15](https://1click.chaindefuser.com/v0/tokens) — primary; reviewed 2026-10-15.

<a id="swapkit-zec"></a>
### SwapKit (ZEC routes)

**Type:** developer-tool · **Networks:** Zcash, MAYAChain, NEAR, Bitcoin, Ethereum, Solana · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `mainnet-announced`

Swap aggregation API and SDK used by wallets, which routes ZEC swaps through MAYAChain and NEAR Intents.

- **Zcash mechanism:** Transparent t1/t3 sources route through MAYAChain or NEAR Intents. Unified (u1/Orchard) sources route only through MAYAChain: the wallet builds a transaction sending value to a transparent inbound address plus a 0-value shielded memo note. Sapling (zs) addresses are rejected.
- **Review focus:** Which provider does each quote use, and is that disclosed to users? How are refund addresses handled for shielded sources? Does SwapKit do address screening on transparent swaps? What data does the API log about users?
- **Evidence and availability qualification:** Non-custodial aggregator, but funds pass through the custody of the underlying provider (Maya vault or POA bridge). Even the 'unified' route sends value to a transparent vault, so privacy is limited.
- **Project/resource:** [SwapKit (ZEC routes)](https://swapkit.dev)
- **Source 1:** [SwapKit docs: Zcash shielded and unified addresses (MAYAChain only for u1)](https://docs.swapkit.dev/spotlights/chain-specific-guides/zcash-shielded-and-unified-addresses) — primary; reviewed 2026-10-15.
- **Source 2:** [SwapKit blog: Zcash integration via Maya and NEAR Intents (transparent at launch)](https://swapkit.dev/blog/swapkit-zcash-integration/) — primary; reviewed 2026-10-15.

<a id="thorchain-zec"></a>
### THORChain ZEC pool

**Type:** protocol · **Networks:** Zcash, THORChain, Bitcoin, Ethereum · **Reviewed:** 2026-10-15

**Evidence:** `code-only` · **Lifecycle:** `unverified`

Cross-chain AMM network that added a Zcash chain client in THORNode and reportedly activated a ZEC liquidity pool on 2026-10-02 ahead of native ZEC swaps.

- **Zcash mechanism:** THORNode's Bifrost includes a Zcash UTXO client that observes and signs ZEC transactions from node-controlled TSS vaults. No shielded, Sapling or Orchard handling was found in zcash.go, so the integration appears to be transparent-only.
- **Review focus:** Are ZEC swaps (not just the pool) enabled now? How deep is the pool, given the publisher warned that liquidity is shallow? Are inbound and outbound addresses transparent only? What halt controls exist for ZEC? Has the Zcash client been audited?
- **Evidence and availability qualification:** Primary evidence is code only; the pool launch reached us through press quoting THORChain's X post, and swap go-live is unconfirmed (a single 9 Oct 2026 report claims it). Vaults are transparent, so swaps break the shielded link.
- **Project/resource:** [THORChain ZEC pool](https://thorchain.org)
- **Source 1:** [THORNode develop: utxo/zcash.go, zcash_signer, zcash_consolidation files](https://gitlab.com/thorchain/thornode/-/tree/develop/bifrost/pkg/chainclients/utxo) — primary; reviewed 2026-10-15.
- **Source 2:** [THORNode common/chain.go: ZECChain defined among UTXO chains](https://gitlab.com/thorchain/thornode/-/blob/develop/common/chain.go) — primary; reviewed 2026-10-15.
- **Source 3:** [crypto.news quoting THORChain X post: ZEC pool live, 'Trading is the next step', 2 Oct 2026](https://crypto.news/thorchain-launches-zcash-pool-trading-comes-next/) — secondary; reviewed 2026-10-15.

<a id="zodl-swaps-crosspay"></a>
### Zodl (formerly Zashi) Swaps and CrossPay

**Type:** wallet · **Networks:** Zcash, NEAR, Bitcoin, Ethereum, Solana · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `mainnet-announced`

Self-custodial Zcash mobile wallet (renamed from Zashi to Zodl in 3.0.0, Feb 2026) with built-in swaps to and from ZEC and CrossPay payments from shielded ZEC to other chains, both powered by NEAR Intents.

- **Zcash mechanism:** The wallet spends from its shielded balance to a NEAR Intents transparent deposit address (swap out, added in 2.2.0 on 2025-08-27) or receives swapped ZEC and shields it (swap in, added in 2.4.0 on 2025-09-30). CrossPay pays the recipient in another asset on a NEAR-supported chain.
- **Review focus:** How are ephemeral transparent addresses used for swap-in, and are they reused? Users should note that NEAR does not refund swaps under $300 sent to a wrong address or network (warning added 2026-09-15). What data reaches NEAR Intents and the market makers? Is Tor used for quote requests?
- **Evidence and availability qualification:** The wallet is self-custodial, but during a swap funds are in NEAR Intents and POA bridge custody. The Zcash side of the route uses a transparent deposit address, so the swap is linkable on the other chain even though the Zodl balance stays shielded.
- **Project/resource:** [Zodl (formerly Zashi) Swaps and CrossPay](https://zodl.com)
- **Source 1:** [Zodl homepage: Swaps and CrossPay powered by NEAR Intents](https://zodl.com/) — primary; reviewed 2026-10-15.
- **Source 2:** [zodl-android CHANGELOG: 2.2.0 (2025-08-27) swap shielded ZEC out; 2.4.0 (2025-09-30) swap to ZEC; 3.0.0 rebrand to Zodl; 3.13.0 $300 refund warning](https://github.com/zodl-inc/zodl-android/blob/main/CHANGELOG.md) — primary; reviewed 2026-10-15.

## Trading and derivatives

<a id="aster-zec-perp"></a>
### Aster ZECUSDT perpetual

**Type:** exchange · **Networks:** BNB Chain · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

ZECUSDT perpetual futures market on the Aster perp DEX.

- **Zcash mechanism:** Synthetic, USDT-margined perpetual; no ZEC is held or transferred.
- **Review focus:** Which oracle and index price ZECUSDT? How custodial is the margin-account model? What are the liquidation and insurance-fund mechanics?
- **Evidence and availability qualification:** Listed per Aster's exchangeInfo API on 2026-10-15. This is synthetic exposure with no Zcash custody or privacy.
- **Project/resource:** [Aster ZECUSDT perpetual](https://www.asterdex.com)
- **Source 1:** [Aster futures exchangeInfo: ZECUSDT listed, 2026-10-15](https://fapi.asterdex.com/fapi/v1/exchangeInfo) — primary; reviewed 2026-10-15.

<a id="dydx-zec-perp"></a>
### dYdX ZEC-USD perpetual

**Type:** exchange · **Networks:** dYdX Chain · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

ZEC-USD perpetual market on the dYdX Chain order book.

- **Zcash mechanism:** Synthetic, USDC-margined perpetual; no ZEC is held or transferred. Positions are public on dYdX Chain.
- **Review focus:** How was the market listed (governance or permissionless)? Which oracle feeds price ZEC? What are the margin fractions and liquidation rules? How deep is liquidity relative to position limits?
- **Evidence and availability qualification:** Operational per the dYdX indexer on 2026-10-15. This is synthetic price exposure with no Zcash custody and no privacy.
- **Project/resource:** [dYdX ZEC-USD perpetual](https://dydx.trade)
- **Source 1:** [dYdX indexer: ZEC-USD status ACTIVE, 2026-10-15](https://indexer.dydx.trade/v4/perpetualMarkets?ticker=ZEC-USD) — primary; reviewed 2026-10-15.

<a id="hyperliquid-zec-perp"></a>
### Hyperliquid ZEC perpetual

**Type:** exchange · **Networks:** Hyperliquid · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

USDC-margined ZEC perpetual futures market in Hyperliquid's core (non-HIP-3) perp universe, alongside ZEC spot pairs that use bridged tokens such as UZEC.

- **Zcash mechanism:** Synthetic exposure only: the perp is margined in USDC and priced by oracle, so no ZEC is held or moved. Spot ZEC on Hyperliquid uses bridged tokens (see the Unit and Bitfrost records). All positions are public.
- **Review focus:** Which oracle sources price ZEC, and how robust is it to thin spot markets? What leverage and margin tiers apply? What is the liquidation and auto-deleveraging policy? How exposed are users to the validator set and the bridge?
- **Evidence and availability qualification:** Operational per the Hyperliquid info API on 2026-10-15. This is price exposure, not ZEC custody. Trades, positions and liquidations are fully public on-chain, the opposite of shielded use.
- **Project/resource:** [Hyperliquid ZEC perpetual](https://hyperliquid.xyz)
- **Source 1:** [Hyperliquid API POST {type:meta}: ZEC in core perp universe (maxLeverage field present), 2026-10-15](https://api.hyperliquid.xyz/info) — primary; reviewed 2026-10-15.

<a id="lighter-zec-perp"></a>
### Lighter ZEC perpetual

**Type:** exchange · **Networks:** Ethereum · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

ZEC perpetual market on Lighter, a ZK-rollup order-book perp exchange.

- **Zcash mechanism:** Synthetic, USDC-margined perpetual; no ZEC is held or transferred.
- **Review focus:** Which oracle prices ZEC? What escape-hatch or forced-withdrawal path exists if the sequencer halts? What leverage limits apply to ZEC? How does liquidation work?
- **Evidence and availability qualification:** Operational per the Lighter API on 2026-10-15. This is synthetic exposure only. Zcash privacy does not apply.
- **Project/resource:** [Lighter ZEC perpetual](https://lighter.xyz)
- **Source 1:** [Lighter API orderBooks: ZEC status active, 2026-10-15](https://mainnet.zklighter.elliot.ai/api/v1/orderBooks) — primary; reviewed 2026-10-15.

<a id="raydium-zec-pools"></a>
### Raydium ZEC and zenZEC pools

**Type:** protocol · **Networks:** Solana · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Permissionless Solana AMM hosting concentrated-liquidity pools for both the Omni-bridged ZEC SPL token and Zenrock's zenZEC.

- **Zcash mechanism:** Trades bridged SPL representations of ZEC; no native ZEC moves. All activity is public on Solana.
- **Review focus:** Which ZEC mint is in a given pool? Many similarly named tokens exist on Solana, so how can users verify the mint? How deep is liquidity, and which pools are permissionless or unverified?
- **Evidence and availability qualification:** Operational per the Raydium API on 2026-10-15. There are many imitation 'ZEC' tokens on Solana, so users must check the mint. These pools offer no Zcash privacy.
- **Project/resource:** [Raydium ZEC and zenZEC pools](https://raydium.io)
- **Source 1:** [Raydium API: CLMM/standard pools with Omni ZEC](https://api-v3.raydium.io/pools/info/mint?mint1=A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS) — primary; reviewed 2026-10-15.
- **Source 2:** [Raydium API: CLMM pools with zenZEC](https://api-v3.raydium.io/pools/info/mint?mint1=JDt9rRGaieF6aN1cJkXFeUmsy7ZE4yY3CZb8tVMXVroS) — primary; reviewed 2026-10-15.

## Lending, staking and yield

<a id="kamino-zcash-market"></a>
### Kamino ZCASH Market

**Type:** protocol · **Networks:** Solana · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Curated isolated lending market on Kamino (Solana) with ZEC as collateral and USDC as the borrowable asset, reported as launched in September 2026 and curated by Allez Labs.

- **Zcash mechanism:** Collateral is the Omni Bridge ZEC SPL token (mint A7bdiYdS…XaS), not native ZEC. No ZEC moves on Zcash. Positions are public on Solana.
- **Review focus:** What oracle prices ZEC on Solana, and how is it protected against thin liquidity? What are the risk parameters, and who can change them? How would a bridge failure (Omni or POA) be handled for this collateral? Who is the curator, and what are their powers?
- **Evidence and availability qualification:** Operational per the Kamino API on 2026-10-15. Users stack lending risk on top of bridge risk (possibly two bridges deep). Collateral and loans are fully transparent on Solana, so there are no Zcash privacy properties.
- **Project/resource:** [Kamino ZCASH Market](https://kamino.com)
- **Source 1:** [Kamino API: 'ZCASH Market' GBJ3bzUi…, isCurated true](https://api.kamino.finance/v2/kamino-market) — primary; reviewed 2026-10-15.
- **Source 2:** [Kamino API reserves: ZEC (A7bdiYdS…) and USDC](https://api.kamino.finance/kamino-market/GBJ3bzUiMfwC9ugaF3MM68EXMDyTUb5UryRRAcVjEowd/reserves/metrics) — primary; reviewed 2026-10-15.
- **Source 3:** [Crypto Briefing: Kamino ZEC-backed borrowing, 7 Sep 2026](https://cryptobriefing.com/kamino-zec-backed-borrowing-solana-usdc/) — secondary; reviewed 2026-10-15.

## Payments and merchant tools

<a id="btcpay-zcash-plugin"></a>
### BTCPay Server Zcash plugin

**Type:** developer-tool · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Community plugin that adds ZEC invoice payments to self-hosted BTCPay Server instances.

- **Zcash mechanism:** Merchant runs Zebra plus lightwalletd and a wallet RPC; ZecHub lists it as shielded-only (Sapling, Orchard, Unified Address). The repo README itself does not state address types.
- **Review focus:** Since zcashd halted at block 3,417,100 (2026-07-18) and NU6.3 made Orchard spend-only at block 3,428,143 (2026-07-28), does it detect payments to Ironwood receivers and run without zcashd? Which address types are actually issued on invoices? The README warns one Zcash wallet is shared across all stores on an instance; who has access to that wallet? Who maintains the btcpay-zcash org?
- **Evidence and availability qualification:** Latest Plugin Builder build (1.1.0, 2026-10-07) is marked pre-release and requires BTCPay Server 2.3.7+; GitHub shows no tagged releases.
- **Project/resource:** [BTCPay Server Zcash plugin](https://github.com/btcpay-zcash/btcpayserver-zcash-plugin)
- **Source 1:** [BTCPay Plugin Builder: ZCash Support v1.1.0 (pre-release, 2026-10-07)](https://plugin-builder.btcpayserver.org/public/plugins/zcash-plugin) — primary; reviewed 2026-10-15.
- **Source 2:** [btcpay-zcash/btcpayserver-zcash-plugin README](https://github.com/btcpay-zcash/btcpayserver-zcash-plugin) — primary; reviewed 2026-10-15.
- **Source 3:** [ZecHub payment processors list](https://zechub.wiki/payment-processors) — secondary; reviewed 2026-10-15.

<a id="cipherpay"></a>
### CipherPay

**Type:** service · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Non-custodial ZEC payment service with hosted checkout, payment links, POS app, API, and Shopify/WooCommerce integrations.

- **Zcash mechanism:** Merchant supplies a Unified Full Viewing Key (uview...) so the service can detect incoming shielded payments; funds go directly to the merchant's wallet. Docs say all payments are shielded.
- **Review focus:** Since zcashd halted at block 3,417,100 (2026-07-18) and NU6.3 made Orchard spend-only at block 3,428,143 (2026-07-28), does it detect payments to Ironwood receivers and run without zcashd? What data does the operator retain from the viewing key (amounts, memos, timing)? What are the fees (docs section is empty)? Is the server code open source and self-hostable as the WooCommerce listing claims?
- **Evidence and availability qualification:** Operator appears to be Atmosphere Labs per site footer and GitHub link; fees, license and launch status not stated on fetched pages.
- **Project/resource:** [CipherPay](https://www.cipherpay.app)
- **Source 1:** [CipherPay homepage (footer: (c) 2026 Atmosphere Labs)](https://www.cipherpay.app) — primary; reviewed 2026-10-15.
- **Source 2:** [CipherPay docs](https://www.cipherpay.app/docs) — primary; reviewed 2026-10-15.
- **Source 3:** [ZecHub payment processors list](https://zechub.wiki/payment-processors) — secondary; reviewed 2026-10-15.

<a id="flexa-zec"></a>
### Flexa (ZEC via Zashi/Zodl)

**Type:** network · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Retail payment network integrated into the Zashi wallet in November 2024 so users can pay ZEC at Flexa-enabled US stores.

- **Zcash mechanism:** User spends from a shielded balance in the wallet; Flexa settles merchants in their chosen currency. Merchant-side ZEC handling is not documented.
- **Review focus:** Is the integration still live in the renamed Zodl wallet after NU6.3? Which regions and merchants currently accept? What KYC/data does Flexa collect from spenders?
- **Evidence and availability qualification:** Only a 2024 launch announcement was verified; current merchant coverage unconfirmed.
- **Project/resource:** [Flexa (ZEC via Zashi/Zodl)](https://flexa.co/)
- **Source 1:** [Flexa newsroom: Flexa and Electric Coin Co. integration with Zashi (2024-11-26)](https://flexa.co/newsroom/zashi) — primary; reviewed 2026-10-15.

<a id="nowpayments-zec"></a>
### NOWPayments (ZEC)

**Type:** service · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Multi-coin crypto payment gateway that lists ZEC among accepted coins.

- **Zcash mechanism:** Merchant registers a ZEC payout wallet; the NOWPayments page does not state address type, and ZecHub lists it as transparent-only.
- **Review focus:** Does it accept or pay out to shielded/Unified addresses at all? Is the 'non-custodial' claim accurate given funds pass through the processor before payout? KYC and conversion handling? Since zcashd halted at block 3,417,100 (2026-07-18) and NU6.3 made Orchard spend-only at block 3,428,143 (2026-07-28), does it detect payments to Ironwood receivers and run without zcashd?
- **Evidence and availability qualification:** Publisher page markets Zcash privacy generically but does not document shielded support; treat as transparent until shown otherwise.
- **Project/resource:** [NOWPayments (ZEC)](https://nowpayments.io/supported-coins/zcash-payments)
- **Source 1:** [NOWPayments: Accept Zcash payments](https://nowpayments.io/supported-coins/zcash-payments) — primary; reviewed 2026-10-15.
- **Source 2:** [ZecHub payment processors list](https://zechub.wiki/payment-processors) — secondary; reviewed 2026-10-15.

<a id="paywithzcash-directory"></a>
### Pay With Zcash directory

**Type:** data · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Community directory of businesses and organizations that say they accept ZEC, plus an ATM finder.

- **Zcash mechanism:** Listings only; does not process payments or state whether each merchant takes shielded ZEC.
- **Review focus:** Who runs it and how are listings verified or expired? Do listed merchants still accept ZEC, and shielded or transparent?
- **Evidence and availability qualification:** Operator, verification process and last-update date are not stated on the page.
- **Project/resource:** [Pay With Zcash directory](https://paywithz.cash)
- **Source 1:** [Discover Where to Pay With Zcash](https://paywithz.cash) — primary; reviewed 2026-10-15.

<a id="plisio-zec"></a>
### Plisio (ZEC)

**Type:** service · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Crypto payment gateway that lists Zcash among accepted currencies.

- **Zcash mechanism:** Merchant receives ZEC via the gateway and withdraws to own wallet; address type not documented by Plisio, ZecHub lists it as transparent.
- **Review focus:** Custody model during settlement window? Shielded support? Fee schedule beyond the stated 0.5%? Since zcashd halted at block 3,417,100 (2026-07-18) and NU6.3 made Orchard spend-only at block 3,428,143 (2026-07-28), does it detect payments to Ironwood receivers and run without zcashd?
- **Evidence and availability qualification:** Publisher page does not state custody or address type.
- **Project/resource:** [Plisio (ZEC)](https://plisio.net/accept-zcash)
- **Source 1:** [Plisio: Accept Zcash](https://plisio.net/accept-zcash) — primary; reviewed 2026-10-15.
- **Source 2:** [ZecHub payment processors list](https://zechub.wiki/payment-processors) — secondary; reviewed 2026-10-15.

<a id="zechub-payment-processors"></a>
### ZecHub payment processor list

**Type:** data · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `ecosystem-only` · **Lifecycle:** `not-applicable`

Community wiki page comparing ZEC payment processors by shielded support.

- **Zcash mechanism:** Reference only; classifies processors as shielded, transparent or undocumented.
- **Review focus:** When was each row last checked, particularly after NU6.3? Are claims sourced to processor docs?
- **Evidence and availability qualification:** Useful cross-check but community-maintained; rows lack per-entry dates.
- **Project/resource:** [ZecHub payment processor list](https://zechub.wiki/payment-processors)
- **Source 1:** [ZecHub: Payment processors](https://zechub.wiki/payment-processors) — primary; reviewed 2026-10-15.

<a id="zgo"></a>
### ZGo

**Type:** application · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `ecosystem-only` · **Lifecycle:** `unverified`

Zcash point-of-sale payments app.

- **Zcash mechanism:** ZecHub lists Sapling and Orchard shielded support; the fetched publisher page returned only its title.
- **Review focus:** Is it still maintained? Since zcashd halted at block 3,417,100 (2026-07-18) and NU6.3 made Orchard spend-only at block 3,428,143 (2026-07-28), does it detect payments to Ironwood receivers and run without zcashd? Who operates it and is it custodial?
- **Evidence and availability qualification:** Publisher site rendered no substantive content on fetch; details come from ZecHub only.
- **Project/resource:** [ZGo](https://zgo.cash/)
- **Source 1:** [ZGo - The Zcash Payments App (title only rendered)](https://zgo.cash/) — primary; reviewed 2026-10-15.
- **Source 2:** [ZecHub payment processors list](https://zechub.wiki/payment-processors) — secondary; reviewed 2026-10-15.

<a id="zip-321"></a>
### ZIP 321: Payment Request URIs

**Type:** standard · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Zcash standard for zcash: payment-request URIs and QR codes, including multi-recipient requests.

- **Zcash mechanism:** Supports Sapling, Unified and transparent recipients; memos only for shielded recipients; Sprout excluded.
- **Review focus:** Do target wallets and processors implement multi-payment (paramindex) requests and Unified Addresses with Ironwood receivers?
- **Evidence and availability qualification:** Standard, not a product; status Active.
- **Project/resource:** [ZIP 321: Payment Request URIs](https://zips.z.cash/zip-0321)
- **Source 1:** [ZIP 321 (Status: Active)](https://zips.z.cash/zip-0321) — primary; reviewed 2026-10-15.

## Wallets and access

<a id="brave-wallet"></a>
### Brave Wallet

**Type:** wallet · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

The browser-integrated wallet in Brave, which added shielded Zcash transactions on desktop in v1.77 (April 2025).

- **Zcash mechanism:** Built-in ZEC send and receive with shielded transactions on desktop; mobile shielded support was announced as coming.
- **Review focus:** Has Brave added Ironwood after NU6.3? Is shielded support on Android and iOS shipped? Where are proofs computed, and which servers are queried?
- **Evidence and availability qualification:** The only primary source predates Ironwood, so current NU6.3 support and mobile shielded support are unconfirmed.
- **Project/resource:** [Brave Wallet](https://brave.com/blog/shielded-zcash/)
- **Source 1:** [Brave: shielded Zcash on desktop (2025-04-02)](https://brave.com/blog/shielded-zcash/) — primary; reviewed 2026-10-15.

<a id="cake-wallet"></a>
### Cake Wallet

**Type:** wallet · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

A multi-coin, privacy-oriented self-custody wallet with Zcash support that defaults to Ironwood shielded addresses.

- **Zcash mechanism:** Address options: Shielded (Ironwood, default), Unified, Legacy Shielded (Sapling), rotating transparent, and static transparent. Transparent receipts above 0.005 ZEC are auto-shielded.
- **Review focus:** Are small transparent balances (≤0.005 ZEC) left unshielded? How do built-in exchange features handle ZEC?
- **Evidence and availability qualification:** One of the few wallets whose own docs confirm Ironwood as the default. Transparent options are still offered.
- **Project/resource:** [Cake Wallet](https://docs.cakewallet.com/cryptos/zcash/)
- **Source 1:** [Cake Wallet Zcash docs](https://docs.cakewallet.com/cryptos/zcash/) — primary; reviewed 2026-10-15.
- **Source 2:** [Cake Wallet site (ZEC listed)](https://cakewallet.com/) — primary; reviewed 2026-10-15.
- **Source 3:** [Cake Wallet blog: Zcash is Now Live in Cake Wallet, 20 Jan 2026](https://blog.cakewallet.com/zcash-is-now-live-in-cake-wallet/) — primary; reviewed 2026-10-15.
- **Source 4:** [Cake Wallet blog index (Zcash posts Jan to Feb 2026)](https://blog.cakewallet.com/) — primary; reviewed 2026-10-15.

<a id="edge-wallet"></a>
### Edge

**Type:** wallet · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `ecosystem-only` · **Lifecycle:** `unverified`

A multi-asset self-custody mobile wallet that lists Zcash among its supported assets.

- **Zcash mechanism:** Holds ZEC; the z.cash wallet directory labels Edge 'Shielded by default', and Edge offers in-app swaps via partners (ChangeNow, SideShift, Exolix).
- **Review focus:** Which pools does Edge send to after NU6.3? Do swap partners receive transparent ZEC? How does username/password cloud backup affect key security?
- **Evidence and availability qualification:** Edge's own site does not state shielded support; the 'shielded by default' claim comes from the z.cash directory. Swaps go through third-party exchange partners.
- **Project/resource:** [Edge](https://edge.app/)
- **Source 1:** [Edge site](https://edge.app/) — primary; reviewed 2026-10-15.
- **Source 2:** [z.cash wallet directory ('Shielded by default' badge)](https://z.cash/wallets/) — primary; reviewed 2026-10-15.

<a id="keystone-hardware-wallet"></a>
### Keystone

**Type:** wallet · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

An air-gapped QR-signing hardware wallet that supports shielded ZEC through companion wallets.

- **Zcash mechanism:** Signs shielded ZEC with Zodl (firmware ≥2.0.2 Cypherpunk), Vizor and Noir (≥2.5.0); Keystone Nexus is transparent-only; there is an Ironwood migration workflow.
- **Review focus:** Which companion wallet and firmware combination supports Ironwood today? Keystone cannot yet fully verify Sapling receivers in a UA, so what does that mean for address verification?
- **Evidence and availability qualification:** Shielded support depends on the companion wallet; Keystone Nexus is transparent-only.
- **Project/resource:** [Keystone](https://keyst.one/zcash)
- **Source 1:** [Keystone Zcash page](https://keyst.one/zcash) — primary; reviewed 2026-10-15.
- **Source 2:** [Zodl support: Ironwood migration](https://support.zodl.com/article/58-when-will-the-migration-to-ironwood-be-complete) — primary; reviewed 2026-10-15.

<a id="ledger-zcash"></a>
### Ledger (Zcash support)

**Type:** wallet · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Hardware signer that added native shielded ZEC (Ironwood) management in Ledger Wallet Desktop in September 2026, alongside transparent ZEC.

- **Zcash mechanism:** Keys stay on the Ledger device while the desktop app builds shielded Ironwood transactions. A separate, earlier Zondax 'Zcash Shielded' app (Nov 2024) targeted Nano S Plus/Stax/Flex with ZecWallet and did not support Orchard.
- **Review focus:** Which device models support Ironwood in Ledger Wallet Desktop? When will mobile ship? How does the 2024 Zondax app relate to the new native support?
- **Evidence and availability qualification:** Shielded support is desktop-only (mobile 'coming soon') and Ledger lists no device models. Jurisdiction-dependent availability.
- **Project/resource:** [Ledger (Zcash support)](https://www.ledger.com/blog-native-shielded-zcash-support)
- **Source 1:** [Ledger: native shielded Zcash support (2026-09-23)](https://www.ledger.com/blog-native-shielded-zcash-support) — primary; reviewed 2026-10-15.
- **Source 2:** [Zondax: Zcash Shielded app for Ledger (2024-11-13)](https://zondax.ch/blog/unlocking-privacy-the-new-zcash-shielded-app-for-ledger) — primary; reviewed 2026-10-15.

<a id="trezor-zcash"></a>
### Trezor (Zcash support)

**Type:** wallet · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Hardware wallet family that supports transparent ZEC through Trezor Suite.

- **Zcash mechanism:** Transparent t-address transactions only; shielded z-address transactions are not supported.
- **Review focus:** Users who need shielded ZEC must use another signer. Check which models are listed (Safe 3/5/7 vs 'all').
- **Evidence and availability qualification:** Transparent only: balances and transfers are public on-chain.
- **Project/resource:** [Trezor (Zcash support)](https://trezor.io/coins/wallet/zcash)
- **Source 1:** [Trezor Zcash page](https://trezor.io/coins/wallet/zcash) — primary; reviewed 2026-10-15.

<a id="unstoppable-wallet"></a>
### Unstoppable Wallet

**Type:** wallet · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

A multi-coin, non-custodial mobile wallet that supports Zcash alongside Bitcoin and Ethereum.

- **Zcash mechanism:** Supports shielded ZEC per a partner endorsement on its site.
- **Review focus:** Does it support Ironwood and unified addresses today? Which lightwalletd server does it use? Is transparent ZEC auto-shielded?
- **Evidence and availability qualification:** The 'fully shielded Zcash' wording is an older ECC partner quote, not a current technical spec. Ironwood support is unconfirmed.
- **Project/resource:** [Unstoppable Wallet](https://unstoppable.money/)
- **Source 1:** [Unstoppable site (partner quote about shielded Zcash)](https://unstoppable.money/) — primary; reviewed 2026-10-15.

<a id="zingo-wallet"></a>
### Zingo

**Type:** wallet · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

An iOS and Android shielded Zcash wallet from Zingo Labs, built on zingolib with its pepper-sync engine.

- **Zcash mechanism:** Self-custodial shielded wallet supporting unified, TEX and Orchard-protocol addresses with encrypted memos.
- **Review focus:** Has Zingo shipped Ironwood (NU6.3) sending and receiving? Which lightwalletd or Zaino servers does it use by default?
- **Evidence and availability qualification:** Its own page does not mention Ironwood, so NU6.3 support is unconfirmed.
- **Project/resource:** [Zingo](https://zingolabs.org/zingo)
- **Source 1:** [Zingo wallet page](https://zingolabs.org/zingo) — primary; reviewed 2026-10-15.
- **Source 2:** [zingolib v6.0.0 (2026-09-08)](https://github.com/zingolabs/zingolib/releases) — primary; reviewed 2026-10-15.

<a id="zkool"></a>
### Zkool

**Type:** wallet · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `code-only` · **Lifecycle:** `unverified`

A multi-account Zcash wallet by the Ywallet developer (hhanh00), positioned as Ywallet's successor, with FROST shielded multisig.

- **Zcash mechanism:** Supports transparent, Sapling and Orchard pools, FROST multisig with distributed key generation, and Tor/Nym transport; can import Ywallet accounts.
- **Review focus:** Does the current release send to Ironwood? Is the FROST multisig implementation audited? Which platforms are production builds?
- **Evidence and availability qualification:** The README lists only transparent, Sapling and Orchard, and Ironwood support is unconfirmed from that source. The UI is described as basic, and some features are missing.
- **Project/resource:** [Zkool](https://github.com/hhanh00/zkool2)
- **Source 1:** [zkool2 README](https://github.com/hhanh00/zkool2) — primary; reviewed 2026-10-15.
- **Source 2:** [zkool-v6.34.0 (2026-10-11)](https://github.com/hhanh00/zkool2/releases) — primary; reviewed 2026-10-15.

<a id="zodl-wallet"></a>
### Zodl (formerly Zashi)

**Type:** wallet · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `changed`

A mobile Zcash wallet, formerly ECC's Zashi, now developed by ZODL and focused on shielded ZEC, with built-in swaps and Keystone signing.

- **Zcash mechanism:** Shielded-focused wallet that receives transparent ZEC and prompts one-tap shielding; supports Ironwood migration; swaps and CrossPay to and from shielded ZEC via NEAR Intents; Flexa merchant payments.
- **Review focus:** How are swaps routed, and what does NEAR Intents or the solver see? Is the Ironwood migration complete for your account? What metadata reaches lightwalletd servers? What is the custody model (self-custody seed)?
- **Evidence and availability qualification:** Renamed from Zashi to Zodl in early 2026 after ECC's team left to form ZODL, with no seed migration needed per ZODL. Swaps rely on third-party NEAR Intents infrastructure, which is a separate trust surface from shielded ZEC.
- **Project/resource:** [Zodl (formerly Zashi)](https://zodl.com/)
- **Source 1:** [Zodl site ('Zashi is now Zodl')](https://zodl.com/) — primary; reviewed 2026-10-15.
- **Source 2:** [Zodl support: Ironwood migration (updated 2026-08-07)](https://support.zodl.com/article/58-when-will-the-migration-to-ironwood-be-complete) — primary; reviewed 2026-10-15.
- **Source 3:** [zodl-android 3.17.0 (2026-10-13)](https://github.com/zodl-inc/zodl-android/releases) — primary; reviewed 2026-10-15.
- **Source 4:** [ZODL raises $25M in seed funding (2026-03-09)](https://zodl.com/zodl-raises-25m-in-seed-funding/) — primary; reviewed 2026-10-15.

## Nodes, SDKs and developer tools

<a id="librustzcash"></a>
### librustzcash

**Type:** developer-tool · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `code-only` · **Lifecycle:** `not-applicable`

The core set of Rust crates (zcash_primitives, zcash_client_backend, zcash_address, etc.) used by Zcash nodes, wallets and SDKs.

- **Zcash mechanism:** Implements transaction building, note handling, addresses and wallet scanning for transparent and shielded pools.
- **Review focus:** Which crate versions support Ironwood/use_qsk? Note the README warning that these crates do not check consensus validity.
- **Evidence and availability qualification:** Forks exist (QEDIT ZSA branch, zodl-inc zakura-wallet-libraries).
- **Project/resource:** [librustzcash](https://github.com/zcash/librustzcash)
- **Source 1:** [zcash/librustzcash README](https://github.com/zcash/librustzcash) — primary; reviewed 2026-10-15.

<a id="lightwalletd"></a>
### lightwalletd

**Type:** infrastructure · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `code-only` · **Lifecycle:** `not-applicable`

The Go backend that serves compact blocks over gRPC to Zcash light wallets.

- **Zcash mechanism:** Lets mobile wallets scan shielded outputs without running a full node; the server sees connection metadata but not decrypted notes.
- **Review focus:** Which backend node does it require after zcashd EOL? Who operates the default public servers? ZCG has an open RFP for lightwalletd maintenance; who maintains it now?
- **Evidence and availability qualification:** The README security disclaimer still references ECC's security team, which is out of date after the 2026 team move.
- **Project/resource:** [lightwalletd](https://github.com/zcash/lightwalletd)
- **Source 1:** [lightwalletd v0.5.5 (2026-10-10)](https://github.com/zcash/lightwalletd/releases) — primary; reviewed 2026-10-15.
- **Source 2:** [ZCG open RFP: lightwalletd infrastructure](https://zcashcommunitygrants.org/) — primary; reviewed 2026-10-15.

<a id="zaino"></a>
### Zaino

**Type:** infrastructure · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `code-only` · **Lifecycle:** `not-applicable`

A Rust indexer from Zingo Labs that serves light and full clients and is intended to replace lightwalletd and zcashd indexing roles.

- **Zcash mechanism:** Indexes Zcash blocks and compact blocks from a Zebra backend for wallets, Zallet and explorers.
- **Review focus:** Is the release you deploy a blessed stable 'cycle' tag or an RC? NU7 readiness? Privacy of queries to hosted instances?
- **Evidence and availability qualification:** Light-client servers can see client IPs and query patterns unless used over Tor.
- **Project/resource:** [Zaino](https://github.com/zingolabs/zaino)
- **Source 1:** [Zaino README (gated release pipeline)](https://github.com/zingolabs/zaino) — primary; reviewed 2026-10-15.
- **Source 2:** [Zaino 0.10.1 (2026-09-29)](https://github.com/zingolabs/zaino/releases) — primary; reviewed 2026-10-15.

<a id="zakura"></a>
### Zakura

**Type:** infrastructure · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

A consensus-compatible Rust Zcash full node forked from Zebra, aimed at faster sync, pruning and a zcashd-compatible RPC mode.

- **Zcash mechanism:** Validates the Zcash chain; offers zcashd-compatibility mode for legacy integrations; shared Zakura Common crypto libraries host Tachyon-related work.
- **Review focus:** Who maintains it and how is it funded? Is the experimental P2P v2 stack off on mainnet (yes, per README) and audited? Has its consensus behaviour been cross-tested against Zebra?
- **Evidence and availability qualification:** Performance claims are self-reported and the P2P v2 stack is 'not yet production-hardened'. Repos also appear under zodl-inc, but Zakura's own pages do not name a maintainer organization.
- **Project/resource:** [Zakura](https://zakura.com/)
- **Source 1:** [Zakura site (Sean Bowe, Dev Ojha)](https://zakura.com/) — primary; reviewed 2026-10-15.
- **Source 2:** [zakura-core/zakura README](https://github.com/zakura-core/zakura) — primary; reviewed 2026-10-15.
- **Source 3:** [zcashd README naming Zakura as a successor node](https://github.com/zcash/zcash) — primary; reviewed 2026-10-15.

<a id="zallet"></a>
### Zallet

**Type:** developer-tool · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

A Rust full-node RPC wallet designed to replace the zcashd embedded wallet, including import of zcashd wallet.dat files.

- **Zcash mechanism:** Holds transparent and shielded ZEC behind a zcashd-style JSON-RPC interface on top of Zebra/Zaino.
- **Review focus:** Which zcashd RPC methods are still missing? Is Ironwood fully supported? Has it been externally audited (docs say not fully reviewed)?
- **Evidence and availability qualification:** Beta software with breaking changes possible. The zcashd EOL page calls it 'Alpha.4' while GitHub shows v0.1.0-beta.3; we used the GitHub version.
- **Project/resource:** [Zallet](https://zcash.github.io/zallet/)
- **Source 1:** [Zallet docs (beta, not fully reviewed)](https://zcash.github.io/zallet/) — primary; reviewed 2026-10-15.
- **Source 2:** [zcash/zallet v0.1.0-beta.3 (2026-08-26)](https://github.com/zcash/zallet/releases) — primary; reviewed 2026-10-15.
- **Source 3:** [zcashd EOL page: migrate wallet.dat to Zallet](https://zcash.github.io/zcash/user/end-of-life.html) — primary; reviewed 2026-10-15.

<a id="zcash-mobile-sdks"></a>
### Zcash Android and iOS (Swift) wallet SDKs

**Type:** developer-tool · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `code-only` · **Lifecycle:** `not-applicable`

Light-client SDKs for building Android and iOS apps that send and receive shielded ZEC via lightwalletd.

- **Zcash mechanism:** Wrap librustzcash for on-device shielded scanning and transaction creation.
- **Review focus:** Should integrators track zcash/ or zodl-inc/ repositories? What is the audit status (READMEs still say not externally audited)? Ironwood support versions?
- **Evidence and availability qualification:** Both the zcash/ and zodl-inc/ SDK repositories are active. The zcash/ READMEs carry beta and ECC-review disclaimers that look out of date.
- **Project/resource:** [Zcash Android and iOS (Swift) wallet SDKs](https://github.com/zcash/zcash-android-wallet-sdk)
- **Source 1:** [zcash-android-wallet-sdk README](https://github.com/zcash/zcash-android-wallet-sdk) — primary; reviewed 2026-10-15.
- **Source 2:** [zcash-swift-wallet-sdk 3.0.0 (2026-08-29)](https://github.com/zcash/zcash-swift-wallet-sdk/releases) — primary; reviewed 2026-10-15.
- **Source 3:** [zodl-inc GitHub org (zodl-android/swift-wallet-sdk forks)](https://github.com/zodl-inc) — primary; reviewed 2026-10-15.

<a id="zebra"></a>
### Zebra

**Type:** infrastructure · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `code-only` · **Lifecycle:** `not-applicable`

The Zcash Foundation's Rust consensus node, now the reference full validator after zcashd's end of life.

- **Zcash mechanism:** Validates all Zcash pools and upgrades including NU6.3/Ironwood; v7.0.0-rc.0 carries the NU7 testnet activation.
- **Review focus:** Which version is required for NU7 mainnet once the height is set? RPC parity with zcashd for exchanges? Audit status of recent releases?
- **Evidence and availability qualification:** ZIP 258 says Zebra is expected to be the only full validator that follows the chain from NU6.3. Forks (Zakura, ZODL's zebra, Crosslink staging) also exist.
- **Project/resource:** [Zebra](https://github.com/ZcashFoundation/zebra)
- **Source 1:** [Zebra releases: v6.4.2 (2026-09-25), v7.0.0-rc.0 (2026-10-02)](https://github.com/ZcashFoundation/zebra/releases) — primary; reviewed 2026-10-15.
- **Source 2:** [zcashd EOL page naming Zebra as successor](https://zcash.github.io/zcash/user/end-of-life.html) — primary; reviewed 2026-10-15.

<a id="frost-zcash"></a>
### ZF FROST

**Type:** developer-tool · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

The Zcash Foundation's Rust reference implementation of FROST threshold Schnorr signatures, used for shielded multisig.

- **Zcash mechanism:** Enables t-of-n signing of shielded (RedPallas) spends; used by wallets such as Zkool for shielded multisig.
- **Review focus:** Audit coverage of the Zcash-specific ciphersuites; how DKG and signing coordination are handled in the wallets that use it.
- **Evidence and availability qualification:** A library, not a product; security depends on each wallet's integration.
- **Project/resource:** [ZF FROST](https://zfnd.org/)
- **Source 1:** [Zcash Foundation site (ZF FROST)](https://zfnd.org/) — primary; reviewed 2026-10-15.
- **Source 2:** [Zkool README (FROST shielded multisig)](https://github.com/hhanh00/zkool2) — primary; reviewed 2026-10-15.

<a id="zingolib"></a>
### zingolib

**Type:** developer-tool · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `code-only` · **Lifecycle:** `not-applicable`

Zingo Labs' Rust library and CLI exposing Zcash wallet functionality to apps, underlying the Zingo wallet.

- **Zcash mechanism:** Shielded wallet logic, sync (pepper-sync) and transaction creation for apps.
- **Review focus:** Ironwood support status in v6.x? API stability between major versions?
- **Evidence and availability qualification:** Frequent major-version bumps (v5 June 2026, v6 Sept 2026).
- **Project/resource:** [zingolib](https://github.com/zingolabs/zingolib)
- **Source 1:** [zingolib v6.0.0 (2026-09-08)](https://github.com/zingolabs/zingolib/releases) — primary; reviewed 2026-10-15.

## Organizations, research and data

<a id="electric-coin-company"></a>
### Electric Coin Company (ECC)

**Type:** organization · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `changed`

The company, owned by the nonprofit Bootstrap, that originally developed zcashd and Zashi; its development team left in January 2026 to form ZODL.

- **Zcash mechanism:** Historically built zcashd, librustzcash, SDKs and Zashi; still named as a dev-fund key-holder organization in ZIP 271.
- **Review focus:** What does ECC do now without its former team? Who exercises its key-holder role? Are electriccoin.co resources still maintained?
- **Evidence and availability qualification:** ECC's site shows no posts after Dec 2025 and only footer links to Zodl. Its current operations are unclear from primary sources.
- **Project/resource:** [Electric Coin Company (ECC)](https://electriccoin.co/)
- **Source 1:** [ECC site (latest post Dec 2025)](https://electriccoin.co/) — primary; reviewed 2026-10-15.
- **Source 2:** [ZODL: team left ECC; core protocol development moved to ZODL](https://zodl.com/about/) — primary; reviewed 2026-10-15.
- **Source 3:** [The Block: Zcash developers quit, form new company (2026-01-08)](https://www.theblock.co/post/384737/zcash-developers-form-new-company) — secondary; reviewed 2026-10-15.
- **Source 4:** [ZODL seed announcement (2026-03-09)](https://zodl.com/zodl-raises-25m-in-seed-funding/) — primary; reviewed 2026-10-15.
- **Source 5:** [Zcash ETF 424B3 naming both ECC and ZODL (2026-08-24)](https://www.sec.gov/Archives/edgar/data/0001720265/000119312526364568/zcsh__424b3_08.25.2026.htm) — primary; reviewed 2026-10-15.

<a id="ironwood-migration-tracker"></a>
### Ironwood Migration tracker (Zodl)

**Type:** data · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

A ZODL dashboard that tracks how much ZEC has moved from the Orchard pool into Ironwood.

- **Zcash mechanism:** Reads chain value-pool data to show Orchard→Ironwood migration through the turnstile.
- **Review focus:** ZODL itself states it measures adoption, not supply verification. Cross-check against a self-run Zebra node's value-pool totals.
- **Evidence and availability qualification:** Figures did not render in our fetch. Per ZODL, migration will never reach 100% because some coins are permanently inaccessible.
- **Project/resource:** [Ironwood Migration tracker (Zodl)](https://ironwood.zodl.com/)
- **Source 1:** [Ironwood Migration | Zcash Supply Dashboard](https://ironwood.zodl.com/) — primary; reviewed 2026-10-15.
- **Source 2:** [Zodl support: tracker does not verify total supply](https://support.zodl.com/article/58-when-will-the-migration-to-ironwood-be-complete) — primary; reviewed 2026-10-15.

<a id="shielded-labs"></a>
### Shielded Labs

**Type:** organization · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

A Swiss, donation-funded Zcash support organization working on Crosslink, the Network Sustainability Mechanism, dynamic fees and Ironwood.

- **Zcash mechanism:** Researches and prototypes consensus changes (Crosslink feature net, NSM) and is a dev-fund key-holder; supported the security work that found the 2026 Orchard bug, per press reports.
- **Review focus:** Donor transparency; status of Crosslink upstreaming; scope of its 'Zero' enterprise project.
- **Evidence and availability qualification:** Shielded Labs is an independent organization and is not part of ZF or ZODL.
- **Project/resource:** [Shielded Labs](https://shieldedlabs.net/)
- **Source 1:** [Shielded Labs site](https://shieldedlabs.net/) — primary; reviewed 2026-10-15.
- **Source 2:** [Shielded Labs roadmap](https://shieldedlabs.net/roadmap/) — primary; reviewed 2026-10-15.
- **Source 3:** [ShieldedLabs GitHub org](https://github.com/ShieldedLabs) — primary; reviewed 2026-10-15.

<a id="zcash-block-explorer-nighthawk"></a>
### Zcash Block Explorer (zcashexplorer.app)

**Type:** data · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

An open-source Zcash block explorer credited to Nighthawk Apps, with transaction-type tags and viewing-key tools.

- **Zcash mechanism:** Shows transparent amounts and classifies transactions as shielded, mixed, deshielding or public; displays an Orchard pool total.
- **Review focus:** Is it maintained after Nighthawk's DarkFi pivot? Does it track Ironwood? Avoid pasting viewing keys into hosted tools.
- **Evidence and availability qualification:** When fetched it showed only an 'Orchard Pool' total and no Ironwood figure, which may be stale after NU6.3. Shielded amounts are not visible by design.
- **Project/resource:** [Zcash Block Explorer (zcashexplorer.app)](https://mainnet.zcashexplorer.app/)
- **Source 1:** [Zcash Block Explorer](https://mainnet.zcashexplorer.app/) — primary; reviewed 2026-10-15.

<a id="zcash-community-grants"></a>
### Zcash Community Grants (ZCG)

**Type:** organization · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

A community-elected five-person committee that awards grants from the 8% ZCG dev-fund slice to independent Zcash teams.

- **Zcash mechanism:** Funded by protocol funding streams paid in ZEC (ZIP 1015/1016); publishes RFPs (e.g. lightwalletd maintenance).
- **Review focus:** Grant reporting and milestone verification; how its stream interacts with the coinholder-controlled fund; conflict-of-interest rules.
- **Evidence and availability qualification:** The site's USD treasury figures use an old ZEC price; check its dashboard for current balances.
- **Project/resource:** [Zcash Community Grants (ZCG)](https://zcashcommunitygrants.org/)
- **Source 1:** [ZCG site](https://zcashcommunitygrants.org/) — primary; reviewed 2026-10-15.
- **Source 2:** [ZIP 1016: 8% to ZCG](https://zips.z.cash/zip-1016) — primary; reviewed 2026-10-15.

<a id="zcash-foundation"></a>
### Zcash Foundation

**Type:** organization · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

A US 501(c)(3) public charity that builds Zebra and ZF FROST and runs Zcon and Zcash dev summits.

- **Zcash mechanism:** Maintains the reference consensus node, publishes audits and reports, and is a key-holder of the dev fund multisig.
- **Review focus:** Funding sources and runway; board composition (chair Andrew Miller per site); role in NU7 coordination.
- **Evidence and availability qualification:** Publishes Form 990s and quarterly reports.
- **Project/resource:** [Zcash Foundation](https://zfnd.org/)
- **Source 1:** [Zcash Foundation site](https://zfnd.org/) — primary; reviewed 2026-10-15.
- **Source 2:** [ZIP 271 key-holder organizations](https://zips.z.cash/zip-0271) — primary; reviewed 2026-10-15.

<a id="zodl"></a>
### Zcash Open Development Lab (ZODL)

**Type:** organization · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `changed`

A company formed in early 2026 by the former Electric Coin Company team, which continues Zcash core protocol work and the Zodl wallet.

- **Zcash mechanism:** Develops the Zodl wallet, protocol code and SDK forks; co-proposed Ironwood; maintains Zallet per the zcashd EOL page.
- **Review focus:** Corporate structure and funding (the press reports a $25M venture round, not verified here); how it relates to ECC, Bootstrap and the dev-fund key-holder role; open-source licensing of its forks.
- **Evidence and availability qualification:** A new for-profit entity: it is a successor team, not a renamed ECC. Its formation date and funding are taken from press reports, not from ZODL's own pages.
- **Project/resource:** [Zcash Open Development Lab (ZODL)](https://zodl.com/about/)
- **Source 1:** [ZODL about page](https://zodl.com/about/) — primary; reviewed 2026-10-15.
- **Source 2:** [The Block: Zcash developers quit, form new company (2026-01-08)](https://www.theblock.co/post/384737/zcash-developers-form-new-company) — secondary; reviewed 2026-10-15.
- **Source 3:** [zcashd EOL page: Zallet from ZODL](https://zcash.github.io/zcash/user/end-of-life.html) — primary; reviewed 2026-10-15.
- **Source 4:** [zodl-inc GitHub org](https://github.com/zodl-inc) — primary; reviewed 2026-10-15.

<a id="zec-view"></a>
### ZEC View

**Type:** data · **Networks:** Zcash · **Reviewed:** 2026-10-18

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Independent, source-linked Zcash market, shielded-pool and ZCSH research pages with dated observations and browser-based calculators.

- **Zcash mechanism:** Read-only documentation and provider observations of native ZEC and source-defined shielded-pool balances; distinguishes transparent and shielded receiver types. It is not a wallet, bridge or independent consensus node.
- **Review focus:** Check source observation dates, pool definitions and wallet-documentation dates; distinguish fund valuation dates from live quotes and aggregate balances from individual privacy.
- **Evidence and availability qualification:** Reviewed the publisher's public pages and stated methodology, not the underlying data pipeline or wallet compatibility through transaction testing. Provider data may be delayed or incomplete. The site describes no custody, trading or wallet connection. Proposed by a maintainer; inclusion is not an endorsement.
- **Project/resource:** [ZEC View](https://zecview.com/)
- **Source 1:** [ZEC View public dashboard and research navigation](https://zecview.com/) — primary; reviewed 2026-10-18.
- **Source 2:** [Publisher methodology: source dates, network aggregation and no independent node](https://zecview.com/methodology/) — primary; reviewed 2026-10-18.
- **Source 3:** [Publisher address-type explanation with ZIP 316 references](https://zecview.com/privacy/address-types/) — primary; reviewed 2026-10-18.

<a id="zecblock-explorer"></a>
### ZecBlock (formerly CipherScan)

**Type:** data · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `changed`

A Zcash block explorer and privacy-analytics site with mainnet, testnet and Crosslink feature-net views.

- **Zcash mechanism:** Indexes blocks and transactions, with shielded-pool and Ironwood analytics sections; amounts inside shielded transactions are masked.
- **Review focus:** Who operates it (GitHub Kenbak/zecblock, Atmosphere Labs)? What methodology does it use for pool metrics? How do linked CipherSwap/CipherPay services handle custody?
- **Evidence and availability qualification:** The only evidence of the rename is cipherscan.app's 301 redirect to zecblock.com; ZecBlock's page does not mention a former name.
- **Project/resource:** [ZecBlock (formerly CipherScan)](https://zecblock.com/)
- **Source 1:** [ZecBlock explorer](https://zecblock.com/) — primary; reviewed 2026-10-15.
- **Source 2:** [Zipherscan README: fork of CipherScan](https://github.com/QED-it/zipherscan) — primary; reviewed 2026-10-15.

<a id="zechub"></a>
### ZecHub

**Type:** organization · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

A community-run Zcash education wiki and hub with guides, newsletters and ecosystem directories.

- **Zcash mechanism:** Educational content on shielded use, wallets and upgrades; links to community tools (ZecMap, Free2Z).
- **Review focus:** Content is community-written, so check dates against primary sources, especially after the 2026 Ironwood changes.
- **Evidence and availability qualification:** Its dashboard page did not render data when fetched, so we cannot rely on it for metrics.
- **Project/resource:** [ZecHub](https://zechub.wiki/)
- **Source 1:** [ZecHub wiki](https://zechub.wiki/) — primary; reviewed 2026-10-15.

## Centralized and institutional access

<a id="cobo-zec-custody"></a>
### Cobo (ZEC custody)

**Type:** service · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Institutional custody and wallet-infrastructure provider that announced support for the NU6.3 Ironwood upgrade.

- **Zcash mechanism:** Custodial ZEC deposits/withdrawals; paused services during NU6.3 and required consensus branch ID 0x37A5165B.
- **Review focus:** Which address types does it support post-NU6.3? Shielded withdrawal support? Jurisdictions and licensing?
- **Evidence and availability qualification:** Evidence covers upgrade handling only, not shielded support.
- **Project/resource:** [Cobo (ZEC custody)](https://www.cobo.com/)
- **Source 1:** [Cobo: support for Zcash Ironwood (NU6.3) upgrade (2026-07-27)](https://www.cobo.com/post/ZEC_Ironwood_Network_Upgrade-2026-07-27-1536) — primary; reviewed 2026-10-15.

<a id="coinbase-custody-zec"></a>
### Coinbase Custody Trust Company (ZEC)

**Type:** service · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Qualified custodian named as ZEC custodian for The Zcash ETF, with Coinbase, Inc. as prime broker.

- **Zcash mechanism:** Holds ETF ZEC in offline cold storage per the prospectus; address type not disclosed.
- **Review focus:** Shielded vs transparent custody? Upgrade handling (NU6.3 migration out of Orchard if any holdings were there)? Availability of custody to non-ETF institutions.
- **Evidence and availability qualification:** Evidence is the ETF prospectus, not a Coinbase product page.
- **Project/resource:** [Coinbase Custody Trust Company (ZEC)](https://www.coinbase.com/)
- **Source 1:** [The Zcash ETF Form 424B3 (2026-08-24)](https://www.sec.gov/Archives/edgar/data/0001720265/000119312526364568/zcsh__424b3_08.25.2026.htm) — primary; reviewed 2026-10-15.

<a id="coinbase-exchange-zec"></a>
### Coinbase exchange (ZEC)

**Type:** exchange · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

US exchange that listed ZEC in 2018 with shielded deposits but transparent-only withdrawals.

- **Zcash mechanism:** 2018 policy: deposits from transparent and shielded addresses accepted, withdrawals to transparent only; no later change found.
- **Review focus:** Is the withdrawal policy still transparent-only? Regional availability (Coinbase UK removed ZEC in 2019)? Ironwood/Unified Address deposit support?
- **Evidence and availability qualification:** Coinbase's own blog and price page returned 403; a third-party claim of a 2026 delisting is unverified and contradicted by Coinbase's ETF custody role.
- **Project/resource:** [Coinbase exchange (ZEC)](https://www.coinbase.com/)
- **Source 1:** [ECC (archived on zodl.com): Coinbase announces support for Zcash (2018-11-29)](https://zodl.com/coinbase-announces-support-for-zcash/) — primary; reviewed 2026-10-15.

<a id="cypherpunk-technologies"></a>
### Cypherpunk Technologies (CYPH)

**Type:** organization · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Nasdaq-listed company, formerly Leap Therapeutics, that holds a ZEC treasury and operates Zcash mining.

- **Zcash mechanism:** Corporate balance-sheet ZEC holdings plus mining; company states a goal of accumulating 5% of the Zcash network.
- **Review focus:** Custody arrangement and address type for treasury ZEC? Accounting treatment (filings refer to a ZEC receivable)? Dilution and financing terms? Related-party links (Winklevoss Capital, ZODL investment).
- **Evidence and availability qualification:** Holdings figures change frequently; check latest 10-Q/8-K rather than this entry.
- **Project/resource:** [Cypherpunk Technologies (CYPH)](https://cypherpunk.com)
- **Source 1:** [SEC EDGAR submissions: former name Leap Therapeutics until 2025-11-12](https://data.sec.gov/submissions/CIK0001509745.json) — primary; reviewed 2026-10-15.
- **Source 2:** [Cypherpunk 8-K Ex.99.1 (2025-12-30)](https://www.sec.gov/Archives/edgar/data/1509745/000110465925125039/tm2534480d2_ex99-1.htm) — primary; reviewed 2026-10-15.
- **Source 3:** [Cypherpunk Technologies website](https://cypherpunk.com) — primary; reviewed 2026-10-15.

<a id="gemini-zec"></a>
### Gemini (ZEC exchange and custody)

**Type:** exchange · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

US exchange that added shielded ZEC withdrawals in 2020 and is named custodian for the proposed Winklevoss Zcash ETF.

- **Zcash mechanism:** 2020: holds customer ZEC in transparent addresses, accepts shielded deposits and allows withdrawals to z-addresses.
- **Review focus:** Does shielded withdrawal still work, and to which pools (Sapling, Unified/Ironwood)? Post-NU6.3 deposit handling? Affiliate conflicts with the WINK ETF.
- **Evidence and availability qualification:** Shielded-withdrawal evidence is from 2020; current support not re-confirmed.
- **Project/resource:** [Gemini (ZEC exchange and custody)](https://www.gemini.com/)
- **Source 1:** [Gemini blog: shielded ZEC withdrawals (2020-09-29)](https://www.gemini.com/blog/youre-one-step-closer-to-financial-freedom-with-shielded-zec-withdrawals) — primary; reviewed 2026-10-15.
- **Source 2:** [Winklevoss Zcash ETF S-1 (2026-10-06)](https://www.sec.gov/Archives/edgar/data/0002158471/000110465926113940/tm2626975-1_s1.htm) — primary; reviewed 2026-10-15.

<a id="gemini-credit-card-zcash-edition"></a>
### Gemini Credit Card: Zcash Edition

**Type:** service · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Limited-edition Gemini credit card, issued by WebBank, that pays card rewards in ZEC by default.

- **Zcash mechanism:** Rewards credited as ZEC to the user's Gemini custodial account; spending is in fiat, not ZEC.
- **Review focus:** Not a ZEC spending card. Where are rewards held and can they be withdrawn shielded? Eligibility and jurisdiction limits?
- **Evidence and availability qualification:** Reward rates intentionally omitted; terms may change.
- **Project/resource:** [Gemini Credit Card: Zcash Edition](https://gemini.com/zcash)
- **Source 1:** [Gemini Credit Card: Zcash Edition page (2026)](https://gemini.com/zcash) — primary; reviewed 2026-10-15.

<a id="the-zcash-etf-zcsh"></a>
### The Zcash ETF (ZCSH), formerly Grayscale Zcash Trust

**Type:** asset · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `changed`

Grayscale-sponsored exchange-traded product holding ZEC, listed on NYSE Arca after conversion from the OTCQX-quoted Grayscale Zcash Trust.

- **Zcash mechanism:** Trust holds ZEC in cold storage with Coinbase Custody Trust Company (Coinbase, Inc. prime broker); prospectus does not say whether holdings are in shielded or transparent addresses. Creations cash or in-kind; redemptions cash-only as of prospectus date.
- **Review focus:** Shielded or transparent custody addresses? How did the custodian handle the Orchard soft fork and NU6.3? When will in-kind redemptions be allowed? Concentration of the custodian/prime broker role.
- **Evidence and availability qualification:** Converted from a trust to an exchange-listed ETP in August 2026; sponsor fee not confirmed from the fetched prospectus portion and omitted here.
- **Project/resource:** [The Zcash ETF (ZCSH), formerly Grayscale Zcash Trust](https://www.grayscale.com/)
- **Source 1:** [The Zcash ETF Form 424B3 prospectus (2026-08-24)](https://www.sec.gov/Archives/edgar/data/0001720265/000119312526364568/zcsh__424b3_08.25.2026.htm) — primary; reviewed 2026-10-15.
- **Source 2:** [GlobeNewswire release reprint: ZCSH begins trading on NYSE Arca (2026-08-25)](https://www.taiwannews.com.tw/en/news/6427603) — secondary; reviewed 2026-10-15.

<a id="winklevoss-zcash-etf"></a>
### Winklevoss Zcash ETF (proposed, WINK)

**Type:** asset · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `unverified`

Proposed spot ZEC exchange-traded product sponsored by Winklevoss Asset Services, filed on Form S-1 for a Nasdaq listing.

- **Zcash mechanism:** Would hold ZEC directly in segregated cold-storage addresses with Gemini Trust Company (sponsor affiliate) as custodian; S-1 does not say shielded or transparent.
- **Review focus:** Registration not effective; will it be? Affiliate custodian conflicts. Address type of custody holdings. Pricing benchmark (reported blank).
- **Evidence and availability qualification:** Preliminary prospectus, subject to completion; not a listed product. 0.25% unified fee per S-1.
- **Project/resource:** [Winklevoss Zcash ETF (proposed, WINK)](https://www.sec.gov/Archives/edgar/data/0002158471/000110465926113940/tm2626975-1_s1.htm)
- **Source 1:** [Winklevoss Zcash ETF Form S-1, preliminary (2026-10-06)](https://www.sec.gov/Archives/edgar/data/0002158471/000110465926113940/tm2626975-1_s1.htm) — primary; reviewed 2026-10-15.

<a id="zip-320-tex-addresses"></a>
### ZIP 320: TEX (transparent-source-only) addresses

**Type:** standard · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `not-applicable`

Address encoding that tells wallets to send only from transparent funds, created after Binance required identifiable deposit sources.

- **Zcash mechanism:** Bech32m re-encoding (tex prefix) of a transparent P2PKH address; wallet-side rule, not consensus.
- **Review focus:** Which exchanges require TEX deposits today? Does the user's wallet deshield automatically (privacy leak) when paying a TEX address?
- **Evidence and availability qualification:** Exchange-compliance standard; not enforced by consensus.
- **Project/resource:** [ZIP 320: TEX (transparent-source-only) addresses](https://zips.z.cash/zip-0320)
- **Source 1:** [ZIP 320 (Status: Active)](https://zips.z.cash/zip-0320) — primary; reviewed 2026-10-15.

## Discontinued, deprecated and changed projects

<a id="nighthawk-wallet"></a>
### Nighthawk Wallet

**Type:** wallet · **Networks:** Zcash, DarkFi · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `changed`

A formerly Zcash-focused mobile wallet whose current releases and website target the DarkFi testnet.

- **Zcash mechanism:** Earlier versions (v2.x, last stable Nov 2024) were shielded Zcash wallets; v3.0 is for DarkFi's DRK token.
- **Review focus:** Is the v2 Zcash app still maintained or compatible with Ironwood? Users should verify funds can be restored into a current Zcash wallet.
- **Evidence and availability qualification:** Pivoted to DarkFi. The publisher does not state whether Zcash support has ended, but no Zcash release has appeared since v2.2.16 (Nov 2024).
- **Project/resource:** [Nighthawk Wallet](https://nighthawkwallet.com/)
- **Source 1:** [Nighthawk Android repo: 'Nighthawk Wallet 3.0 for DarkFi Testnet'](https://github.com/nighthawk-apps/nighthawk-android-wallet) — primary; reviewed 2026-10-15.
- **Source 2:** [Nighthawk site (DarkFi focus)](https://nighthawkwallet.com/) — primary; reviewed 2026-10-15.

<a id="renzec"></a>
### renZEC (Ren 1.0)

**Type:** asset · **Networks:** Zcash, Ethereum · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `discontinued`

ZEC representation minted by the Ren 1.0 MPC bridge network on Ethereum and other chains; Ren announced the sunset of Ren 1.0 in November 2022 after Alameda's bankruptcy.

- **Zcash mechanism:** ZEC was held by the RenVM darknode MPC network at transparent addresses, and renZEC was minted on host chains. Minting was disabled and the network was to shut down 30 days later.
- **Review focus:** Are any renZEC balances still unredeemable? Did Ren 2.0 ever support Zcash? Are legacy renZEC liquidity pools still live and trapping users?
- **Evidence and availability qualification:** Discontinued by the publisher; any remaining renZEC is unbacked or at risk. It never preserved shielded privacy.
- **Project/resource:** [renZEC (Ren 1.0)](https://medium.com/renprotocol)
- **Source 1:** [Ren: Moving on from Alameda, 18 Nov 2022 (disable minting, shut down Ren 1.0 after 30 days)](https://medium.com/renprotocol/moving-on-from-alameda-da62a823ce93) — primary; reviewed 2026-10-15.

<a id="sprout-shielded-pool"></a>
### Sprout shielded pool

**Type:** protocol · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `deprecated`

The original 2016 Zcash shielded pool, closed to new value by ZIP 211.

- **Zcash mechanism:** Sprout notes can only be moved out of the pool; no new ZEC can be shielded into Sprout.
- **Review focus:** Do any wallets still support migrating residual Sprout funds? Which tooling replaced zcashd's Sprout migration after zcashd's end of life?
- **Evidence and availability qualification:** Closed to new deposits since Canopy; residual funds can only be withdrawn. zcashd, the main Sprout-capable wallet, reached end of life on 18 Jul 2026.
- **Project/resource:** [Sprout shielded pool](https://zips.z.cash/zip-0211)
- **Source 1:** [ZIP 211: Disabling Addition of New Value to the Sprout Chain Value Pool (Final)](https://zips.z.cash/zip-0211) — primary; reviewed 2026-10-15.
- **Source 2:** [ZIP index (settled upgrades, ZIP statuses)](https://zips.z.cash/) — primary; reviewed 2026-10-15.

<a id="wzec-ethereum"></a>
### Wrapped ZEC (WZEC, Ethereum)

**Type:** asset · **Networks:** Zcash, Ethereum · **Reviewed:** 2026-10-15

**Evidence:** `code-only` · **Lifecycle:** `unverified`

Custodial ERC-20 representation of ZEC launched in October 2020 by Tokensoft's 'Wrapped' with Anchorage custody; the contract 0x4A64…6E10 still reports name 'Wrapped ZEC'.

- **Zcash mechanism:** Native ZEC was held by a qualified custodian (Anchorage), with WZEC minted and burned on Ethereum by the issuer. WZEC on Ethereum is fully transparent.
- **Review focus:** Is redemption to ZEC still offered? wrapped.com now markets RWA services and does not mention WZEC. Who holds the mint and burn roles today? Is there any attestation of reserves?
- **Evidence and availability qualification:** A custodial IOU with unclear current redemption. The issuer's site no longer references it, but there is no publisher shutdown notice. It never had Zcash privacy on Ethereum.
- **Project/resource:** [Wrapped ZEC (WZEC, Ethereum)](https://www.wrapped.com)
- **Source 1:** [Ethereum eth_call on 0x4A64515E5E1d1073e83f30cB97BEd20400b66E10: name 'Wrapped ZEC', symbol 'WZEC', nonzero supply](https://ethereum-rpc.publicnode.com) — primary; reviewed 2026-10-15.
- **Source 2:** [wrapped.com homepage (2026): RWA/stablecoin services, no WZEC mention](https://www.wrapped.com) — primary; reviewed 2026-10-15.
- **Source 3:** [Token list entry attributing the contract to WZEC](https://github.com/MyEtherWallet/ethereum-lists/blob/master/src/tokens/eth/0x4A64515E5E1d1073e83f30cB97BEd20400b66E10.json) — secondary; reviewed 2026-10-15.
- **Source 4:** [CoinDesk: Wrapped Zcash on Ethereum via Tokensoft/Anchorage, Oct 2020](https://www.coindesk.com/wrapped-zcash-ethereum-tokensoft-anchorage) — secondary; reviewed 2026-10-15.

<a id="ywallet"></a>
### Ywallet

**Type:** wallet · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `discontinued`

A Zcash and Ycash light wallet by hhanh00 that no longer supports Zcash after the Ironwood upgrade.

- **Zcash mechanism:** Previously supported shielded ZEC (Sapling/Orchard, unified addresses); Zcash users are directed to migrate to Zkool.
- **Review focus:** Users should import accounts into Zkool or another Ironwood-capable wallet; Ycash support continues.
- **Evidence and availability qualification:** Discontinued for Zcash only, per its README ('no longer supports Zcash since the Ironwood update'); Ycash support continues.
- **Project/resource:** [Ywallet](https://github.com/hhanh00/zwallet)
- **Source 1:** [zwallet README (deprecation notice)](https://github.com/hhanh00/zwallet) — primary; reviewed 2026-10-15.

<a id="zcashd"></a>
### zcashd

**Type:** infrastructure · **Networks:** Zcash · **Reviewed:** 2026-10-15

**Evidence:** `direct-source` · **Lifecycle:** `discontinued`

The original C++ Zcash full node and embedded wallet, which reached end of life with a hard halt at block 3,417,100 on 18 July 2026.

- **Zcash mechanism:** Was the reference node and wallet for all pools; it does not implement NU6.3, so it cannot follow the current chain.
- **Review focus:** Anyone still running it must migrate: Zebra or Zakura for nodes, Zallet for wallet.dat. Check exchange and integrator dependencies on zcashd RPCs.
- **Evidence and availability qualification:** The repository is archived. The final release (6.20.0) shut down at the end-of-support height, and the wind-down was brought forward because of the Orchard vulnerability.
- **Project/resource:** [zcashd](https://github.com/zcash/zcash)
- **Source 1:** [zcash/zcash README (End of Life notice; repo archived)](https://github.com/zcash/zcash) — primary; reviewed 2026-10-15.
- **Source 2:** [zcashd End of Life page](https://zcash.github.io/zcash/user/end-of-life.html) — primary; reviewed 2026-10-15.
