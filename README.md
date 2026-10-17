# Awesome ZecFi

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> An awesome list of Zcash finance projects, protocols, tools and ways to use ZEC.

Explore **shielded pools and network upgrades, wallets, ZEC on other chains, cross-chain swaps, trading, lending, payments and institutional access**, plus the nodes and SDKs that make them possible.

**Research snapshot: October 18, 2026.** Individual entries retain their own review dates; this update reviews the new ZEC View entry, not every existing source. This is a broad, curated directory, not an exhaustive census, ranking, audit or investment recommendation. “Awesome” names the list format; inclusion is not an endorsement. Open source refers to **this repository**; listed projects have their own licensing and custody models.

## Start here

- [Browse by network, evidence, lifecycle or type](docs/browse.md) — no tools needed.
- [Evidence coverage and review queue](docs/coverage.md) — see exactly where the research is thin.
- [Ways to use ZecFi](docs/ways-to-use-zecfi.md) — what each approach does, and when your ZEC stops being shielded.
- [Detailed directory](docs/directory.md) — mechanisms, review questions, status notes and dated sources for every entry.
- [Trust models and due diligence](docs/trust-models.md) — compare custody, privacy, exits and counterparties.
- [Research method and scope](docs/methodology.md) — what was reviewed, what the labels mean, and the limits of this snapshot.
- [Material changes found](docs/research-notes.md) — the 2026 upgrades, renames and terminology traps.
- [Machine-readable dataset](data/projects.json) — structured records for reuse.
- [HTTP link-check results](data/link-health.json) — reachability evidence, separate from project-status research.
- [Contribute an addition or correction](CONTRIBUTING.md).

**Shielded is not the default once ZEC leaves Zcash.** Bridged, wrapped and exchange-held ZEC is generally transparent; most cross-chain routes deposit to and pay out from transparent addresses. Each entry's mechanism says which pool or address type is involved.

**2026 changed the basics.** zcashd halted on July 18, 2026; NU6.3 (Ironwood) made Orchard withdraw-only and added a new shielded pool; the Electric Coin Company team now works as ZODL and Zashi is now Zodl. Older guides that assume zcashd, Orchard-by-default or ECC-maintained wallets are out of date. See [material changes](docs/research-notes.md).

**Evidence and availability are separate.** `direct-source` means publisher documentation or other original evidence was reviewed; it does not establish that a service is operating. `ecosystem-only` and `code-only` flag narrower evidence. Lifecycle is **unverified unless explicitly stated otherwise**; `mainnet-announced` is a publisher claim. This README shows exceptional labels only; an unbadged listing is not a verified-live or safety designation. See [definitions](docs/methodology.md#evidence-and-lifecycle).

These short descriptions deliberately omit APY, TVL and price figures, which go stale and are frequently incomparable.

<!-- DIRECTORY:START -->

**82 entries · 11 categories · reviewed 2026-10-18**

## Contents

- [Zcash protocol, shielded pools and upgrades](#zcash-protocol) (12)
- [ZEC representations and bridges](#zec-assets) (6)
- [Cross-chain swaps and routing](#swaps) (5)
- [Trading and derivatives](#trading) (5)
- [Lending, staking and yield](#lending-yield) (1)
- [Payments and merchant tools](#payments) (9)
- [Wallets and access](#wallets) (10)
- [Nodes, SDKs and developer tools](#builders) (9)
- [Organizations, research and data](#research) (10)
- [Centralized and institutional access](#centralized) (9)
- [Discontinued, deprecated and changed projects](#historical) (6)

<a id="zcash-protocol"></a>
## Zcash protocol, shielded pools and upgrades

- [Crosslink (hybrid PoW/PoS finality)](https://shieldedlabs.net/crosslink/) — A Shielded Labs proposal to add a proof-of-stake BFT finality layer on top of Zcash's proof-of-work chain, now running as a prototype 'Feature Net'. `testnet` · [Details & sources](docs/directory.md#crosslink).
- [Dev fund, lockbox and Coinholder-Controlled Fund (NU6.1)](https://zips.z.cash/zip-1016) — The post-2025 Zcash development funding model, which sends 8% of block rewards to Zcash Community Grants and 12% to a coinholder-voted fund seeded by the deferred lockbox. `mainnet-announced` · [Details & sources](docs/directory.md#dev-fund-coinholder-fund).
- [Ironwood shielded pool (NU6.3)](https://zodl.com/ironwood-a-new-shielded-pool-for-zcash/) — A new shielded pool, introduced by the NU6.3 network upgrade, that reuses the corrected Orchard protocol with formal verification and receives funds migrated from Orchard. `mainnet-announced` · [Details & sources](docs/directory.md#ironwood-nu6-3).
- [NU7 network upgrade](https://zips.z.cash/zip-0259) — A pending Zcash network upgrade that shortens block time to 25 seconds, disallows v4 transactions, and adds Network Sustainability Mechanism fee burning and issuance changes. `testnet` · [Details & sources](docs/directory.md#nu7-network-upgrade).
- [Orchard shielded pool (incl. NU6.2 mitigation)](https://zips.z.cash/zip-0258) — The Halo 2-based shielded pool (NU5, 2022) that was restricted to withdrawals-only by NU6.3 after a 2026 circuit soundness bug. `deprecated` · [Details & sources](docs/directory.md#orchard-shielded-pool).
- [Project Tachyon](https://tachyon.z.cash/) — A proposed Zcash scaling upgrade aimed at much smaller shielded transactions, oblivious wallet sync and bounded validator state, with post-quantum privacy as a side effect. `research` · [Details & sources](docs/directory.md#project-tachyon).
- [Sapling shielded pool](https://zips.z.cash/) — The Groth16-based shielded pool introduced in 2018 and still usable alongside the newer pools. · [Details & sources](docs/directory.md#sapling-shielded-pool).
- [Shielded memos (ZIP 302)](https://zips.z.cash/zip-0302) — The encrypted 512-byte memo field carried by shielded Zcash outputs, used for payment references and private messages. · [Details & sources](docs/directory.md#shielded-memos).
- [Unified Addresses (ZIP 316)](https://zips.z.cash/zip-0316) — The Zcash address and viewing-key encoding that bundles receivers for several pools (transparent, Sapling, Orchard-protocol) into one string. · [Details & sources](docs/directory.md#unified-addresses).
- [Viewing keys and HD derivation (ZIP 32 / ZIP 310)](https://zips.z.cash/zip-0032) — Zcash key hierarchy that lets a holder share incoming or full viewing keys to disclose shielded activity without giving spend authority. · [Details & sources](docs/directory.md#viewing-keys).
- [Zcash Improvement Proposals (ZIPs)](https://zips.z.cash/) — The specification process and repository for Zcash consensus, wallet and governance changes. · [Details & sources](docs/directory.md#zcash-improvement-proposals).
- [Zcash Shielded Assets (ZSA / OrchardZSA)](https://github.com/QED-it) — A proposed extension of the Orchard protocol, led by QEDIT, that would let assets other than ZEC be issued, transferred and burned inside a shielded pool. `testnet` · [Details & sources](docs/directory.md#zcash-shielded-assets).

<a id="zec-assets"></a>
## ZEC representations and bridges

- [Bitfrost Native ZEC (BZEC) on Hyperliquid](https://app.hyperliquid.xyz/explorer/token/0x33b2c5252e8ea8431808129c41668129) — Hyperliquid spot token named 'Bitfrost Native ZEC' (BZEC), with a HyperEVM contract, that third-party guides describe as ZEC bridged by Bitfrost's HYPE-staked validator set. `ecosystem-only` · [Details & sources](docs/directory.md#bitfrost-bzec).
- [Omni Bridge ZEC on Solana](https://docs.near.org/chain-abstraction/omnibridge/overview) — SPL token named Zcash (ZEC), mint A7bdiYdS5GjqGFtxf17ppRHtDKPkkRqbKtR27dxvQXaS, whose mint authority is the NEAR Omni Bridge Solana program's authority PDA; it is the ZEC listed by NEAR Intents on Solana and used by Kamino's ZCASH market. `code-only` · [Details & sources](docs/directory.md#omni-bridge-zec-solana).
- [Unit Zcash (UZEC) on Hyperliquid](https://hyperunit.xyz) — Unit's asset-tokenization layer, which credits deposits of native ZEC as the HIP-1 spot token UZEC (Unit Zcash) on Hyperliquid's HyperCore and fulfils withdrawals back to Zcash. `mainnet-announced` · [Details & sources](docs/directory.md#unit-zec-hyperliquid).
- [ZEC on NEAR Intents (zec.omft.near, POA Bridge)](https://docs.near-intents.org/integration/bridging/overview) — Bridged ZEC token (nep141:zec.omft.near) issued by the NEAR Intents Proof-of-Authority bridge, also listed by the 1Click API as ZEC on Starknet and Aptos. `mainnet-announced` · [Details & sources](docs/directory.md#zec-on-near-poa).
- [zenZEC (Zenrock)](https://www.zenrocklabs.io) — Zenrock's Decentralized Custody Token for Zcash, minted on Solana (mint JDt9rRGaieF6aN1cJkXFeUmsy7ZE4yY3CZb8tVMXVroS) against ZEC locked in Zenrock's decentralized MPC custody network. · [Details & sources](docs/directory.md#zenzec).
- [Ztarknet](https://ztarknet.cash) — Proposed Starknet-style L2 that runs Cairo programs and settles to Zcash L1 through a draft Transparent Zcash Extension that verifies Circle STARK proofs. `code-only` `research` · [Details & sources](docs/directory.md#ztarknet).

<a id="swaps"></a>
## Cross-chain swaps and routing

- [Maya Protocol (MAYAChain) ZEC pool](https://www.mayaprotocol.com) — THORChain-fork cross-chain AMM with a native ZEC.ZEC pool that swaps ZEC against assets such as BTC, ETH and stablecoins without wrapped tokens. · [Details & sources](docs/directory.md#maya-protocol-zec).
- [NEAR Intents (ZEC routes)](https://near-intents.org) — Intent-based cross-chain swap network whose 1Click API quotes swaps into and out of native ZEC, settled by market makers through a verifier contract on NEAR. `mainnet-announced` · [Details & sources](docs/directory.md#near-intents-zec).
- [SwapKit (ZEC routes)](https://swapkit.dev) — Swap aggregation API and SDK used by wallets, which routes ZEC swaps through MAYAChain and NEAR Intents. `mainnet-announced` · [Details & sources](docs/directory.md#swapkit-zec).
- [THORChain ZEC pool](https://thorchain.org) — Cross-chain AMM network that added a Zcash chain client in THORNode and reportedly activated a ZEC liquidity pool on 2026-10-02 ahead of native ZEC swaps. `code-only` · [Details & sources](docs/directory.md#thorchain-zec).
- [Zodl (formerly Zashi) Swaps and CrossPay](https://zodl.com) — Self-custodial Zcash mobile wallet (renamed from Zashi to Zodl in 3.0.0, Feb 2026) with built-in swaps to and from ZEC and CrossPay payments from shielded ZEC to other chains, both powered by NEAR Intents. `mainnet-announced` · [Details & sources](docs/directory.md#zodl-swaps-crosspay).

<a id="trading"></a>
## Trading and derivatives

- [Aster ZECUSDT perpetual](https://www.asterdex.com) — ZECUSDT perpetual futures market on the Aster perp DEX. · [Details & sources](docs/directory.md#aster-zec-perp).
- [dYdX ZEC-USD perpetual](https://dydx.trade) — ZEC-USD perpetual market on the dYdX Chain order book. · [Details & sources](docs/directory.md#dydx-zec-perp).
- [Hyperliquid ZEC perpetual](https://hyperliquid.xyz) — USDC-margined ZEC perpetual futures market in Hyperliquid's core (non-HIP-3) perp universe, alongside ZEC spot pairs that use bridged tokens such as UZEC. · [Details & sources](docs/directory.md#hyperliquid-zec-perp).
- [Lighter ZEC perpetual](https://lighter.xyz) — ZEC perpetual market on Lighter, a ZK-rollup order-book perp exchange. · [Details & sources](docs/directory.md#lighter-zec-perp).
- [Raydium ZEC and zenZEC pools](https://raydium.io) — Permissionless Solana AMM hosting concentrated-liquidity pools for both the Omni-bridged ZEC SPL token and Zenrock's zenZEC. · [Details & sources](docs/directory.md#raydium-zec-pools).

<a id="lending-yield"></a>
## Lending, staking and yield

- [Kamino ZCASH Market](https://kamino.com) — Curated isolated lending market on Kamino (Solana) with ZEC as collateral and USDC as the borrowable asset, reported as launched in September 2026 and curated by Allez Labs. · [Details & sources](docs/directory.md#kamino-zcash-market).

<a id="payments"></a>
## Payments and merchant tools

- [BTCPay Server Zcash plugin](https://github.com/btcpay-zcash/btcpayserver-zcash-plugin) — Community plugin that adds ZEC invoice payments to self-hosted BTCPay Server instances. · [Details & sources](docs/directory.md#btcpay-zcash-plugin).
- [CipherPay](https://www.cipherpay.app) — Non-custodial ZEC payment service with hosted checkout, payment links, POS app, API, and Shopify/WooCommerce integrations. · [Details & sources](docs/directory.md#cipherpay).
- [Flexa (ZEC via Zashi/Zodl)](https://flexa.co/) — Retail payment network integrated into the Zashi wallet in November 2024 so users can pay ZEC at Flexa-enabled US stores. · [Details & sources](docs/directory.md#flexa-zec).
- [NOWPayments (ZEC)](https://nowpayments.io/supported-coins/zcash-payments) — Multi-coin crypto payment gateway that lists ZEC among accepted coins. · [Details & sources](docs/directory.md#nowpayments-zec).
- [Pay With Zcash directory](https://paywithz.cash) — Community directory of businesses and organizations that say they accept ZEC, plus an ATM finder. · [Details & sources](docs/directory.md#paywithzcash-directory).
- [Plisio (ZEC)](https://plisio.net/accept-zcash) — Crypto payment gateway that lists Zcash among accepted currencies. · [Details & sources](docs/directory.md#plisio-zec).
- [ZecHub payment processor list](https://zechub.wiki/payment-processors) — Community wiki page comparing ZEC payment processors by shielded support. `ecosystem-only` · [Details & sources](docs/directory.md#zechub-payment-processors).
- [ZGo](https://zgo.cash/) — Zcash point-of-sale payments app. `ecosystem-only` · [Details & sources](docs/directory.md#zgo).
- [ZIP 321: Payment Request URIs](https://zips.z.cash/zip-0321) — Zcash standard for zcash: payment-request URIs and QR codes, including multi-recipient requests. · [Details & sources](docs/directory.md#zip-321).

<a id="wallets"></a>
## Wallets and access

- [Brave Wallet](https://brave.com/blog/shielded-zcash/) — The browser-integrated wallet in Brave, which added shielded Zcash transactions on desktop in v1.77 (April 2025). · [Details & sources](docs/directory.md#brave-wallet).
- [Cake Wallet](https://docs.cakewallet.com/cryptos/zcash/) — A multi-coin, privacy-oriented self-custody wallet with Zcash support that defaults to Ironwood shielded addresses. · [Details & sources](docs/directory.md#cake-wallet).
- [Edge](https://edge.app/) — A multi-asset self-custody mobile wallet that lists Zcash among its supported assets. `ecosystem-only` · [Details & sources](docs/directory.md#edge-wallet).
- [Keystone](https://keyst.one/zcash) — An air-gapped QR-signing hardware wallet that supports shielded ZEC through companion wallets. · [Details & sources](docs/directory.md#keystone-hardware-wallet).
- [Ledger (Zcash support)](https://www.ledger.com/blog-native-shielded-zcash-support) — Hardware signer that added native shielded ZEC (Ironwood) management in Ledger Wallet Desktop in September 2026, alongside transparent ZEC. · [Details & sources](docs/directory.md#ledger-zcash).
- [Trezor (Zcash support)](https://trezor.io/coins/wallet/zcash) — Hardware wallet family that supports transparent ZEC through Trezor Suite. · [Details & sources](docs/directory.md#trezor-zcash).
- [Unstoppable Wallet](https://unstoppable.money/) — A multi-coin, non-custodial mobile wallet that supports Zcash alongside Bitcoin and Ethereum. · [Details & sources](docs/directory.md#unstoppable-wallet).
- [Zingo](https://zingolabs.org/zingo) — An iOS and Android shielded Zcash wallet from Zingo Labs, built on zingolib with its pepper-sync engine. · [Details & sources](docs/directory.md#zingo-wallet).
- [Zkool](https://github.com/hhanh00/zkool2) — A multi-account Zcash wallet by the Ywallet developer (hhanh00), positioned as Ywallet's successor, with FROST shielded multisig. `code-only` · [Details & sources](docs/directory.md#zkool).
- [Zodl (formerly Zashi)](https://zodl.com/) — A mobile Zcash wallet, formerly ECC's Zashi, now developed by ZODL and focused on shielded ZEC, with built-in swaps and Keystone signing. `changed` · [Details & sources](docs/directory.md#zodl-wallet).

<a id="builders"></a>
## Nodes, SDKs and developer tools

- [librustzcash](https://github.com/zcash/librustzcash) — The core set of Rust crates (zcash_primitives, zcash_client_backend, zcash_address, etc.) used by Zcash nodes, wallets and SDKs. `code-only` · [Details & sources](docs/directory.md#librustzcash).
- [lightwalletd](https://github.com/zcash/lightwalletd) — The Go backend that serves compact blocks over gRPC to Zcash light wallets. `code-only` · [Details & sources](docs/directory.md#lightwalletd).
- [Zaino](https://github.com/zingolabs/zaino) — A Rust indexer from Zingo Labs that serves light and full clients and is intended to replace lightwalletd and zcashd indexing roles. `code-only` · [Details & sources](docs/directory.md#zaino).
- [Zakura](https://zakura.com/) — A consensus-compatible Rust Zcash full node forked from Zebra, aimed at faster sync, pruning and a zcashd-compatible RPC mode. · [Details & sources](docs/directory.md#zakura).
- [Zallet](https://zcash.github.io/zallet/) — A Rust full-node RPC wallet designed to replace the zcashd embedded wallet, including import of zcashd wallet.dat files. · [Details & sources](docs/directory.md#zallet).
- [Zcash Android and iOS (Swift) wallet SDKs](https://github.com/zcash/zcash-android-wallet-sdk) — Light-client SDKs for building Android and iOS apps that send and receive shielded ZEC via lightwalletd. `code-only` · [Details & sources](docs/directory.md#zcash-mobile-sdks).
- [Zebra](https://github.com/ZcashFoundation/zebra) — The Zcash Foundation's Rust consensus node, now the reference full validator after zcashd's end of life. `code-only` · [Details & sources](docs/directory.md#zebra).
- [ZF FROST](https://zfnd.org/) — The Zcash Foundation's Rust reference implementation of FROST threshold Schnorr signatures, used for shielded multisig. · [Details & sources](docs/directory.md#frost-zcash).
- [zingolib](https://github.com/zingolabs/zingolib) — Zingo Labs' Rust library and CLI exposing Zcash wallet functionality to apps, underlying the Zingo wallet. `code-only` · [Details & sources](docs/directory.md#zingolib).

<a id="research"></a>
## Organizations, research and data

- [Electric Coin Company (ECC)](https://electriccoin.co/) — The company, owned by the nonprofit Bootstrap, that originally developed zcashd and Zashi; its development team left in January 2026 to form ZODL. `changed` · [Details & sources](docs/directory.md#electric-coin-company).
- [Ironwood Migration tracker (Zodl)](https://ironwood.zodl.com/) — A ZODL dashboard that tracks how much ZEC has moved from the Orchard pool into Ironwood. · [Details & sources](docs/directory.md#ironwood-migration-tracker).
- [Shielded Labs](https://shieldedlabs.net/) — A Swiss, donation-funded Zcash support organization working on Crosslink, the Network Sustainability Mechanism, dynamic fees and Ironwood. · [Details & sources](docs/directory.md#shielded-labs).
- [Zcash Block Explorer (zcashexplorer.app)](https://mainnet.zcashexplorer.app/) — An open-source Zcash block explorer credited to Nighthawk Apps, with transaction-type tags and viewing-key tools. · [Details & sources](docs/directory.md#zcash-block-explorer-nighthawk).
- [Zcash Community Grants (ZCG)](https://zcashcommunitygrants.org/) — A community-elected five-person committee that awards grants from the 8% ZCG dev-fund slice to independent Zcash teams. · [Details & sources](docs/directory.md#zcash-community-grants).
- [Zcash Foundation](https://zfnd.org/) — A US 501(c)(3) public charity that builds Zebra and ZF FROST and runs Zcon and Zcash dev summits. · [Details & sources](docs/directory.md#zcash-foundation).
- [Zcash Open Development Lab (ZODL)](https://zodl.com/about/) — A company formed in early 2026 by the former Electric Coin Company team, which continues Zcash core protocol work and the Zodl wallet. `changed` · [Details & sources](docs/directory.md#zodl).
- [ZEC View](https://zecview.com/) — Independent, source-linked Zcash market, shielded-pool and ZCSH research pages with dated observations and browser-based calculators. · [Details & sources](docs/directory.md#zec-view).
- [ZecBlock (formerly CipherScan)](https://zecblock.com/) — A Zcash block explorer and privacy-analytics site with mainnet, testnet and Crosslink feature-net views. `changed` · [Details & sources](docs/directory.md#zecblock-explorer).
- [ZecHub](https://zechub.wiki/) — A community-run Zcash education wiki and hub with guides, newsletters and ecosystem directories. · [Details & sources](docs/directory.md#zechub).

<a id="centralized"></a>
## Centralized and institutional access

- [Cobo (ZEC custody)](https://www.cobo.com/) — Institutional custody and wallet-infrastructure provider that announced support for the NU6.3 Ironwood upgrade. · [Details & sources](docs/directory.md#cobo-zec-custody).
- [Coinbase Custody Trust Company (ZEC)](https://www.coinbase.com/) — Qualified custodian named as ZEC custodian for The Zcash ETF, with Coinbase, Inc. as prime broker. · [Details & sources](docs/directory.md#coinbase-custody-zec).
- [Coinbase exchange (ZEC)](https://www.coinbase.com/) — US exchange that listed ZEC in 2018 with shielded deposits but transparent-only withdrawals. · [Details & sources](docs/directory.md#coinbase-exchange-zec).
- [Cypherpunk Technologies (CYPH)](https://cypherpunk.com) — Nasdaq-listed company, formerly Leap Therapeutics, that holds a ZEC treasury and operates Zcash mining. · [Details & sources](docs/directory.md#cypherpunk-technologies).
- [Gemini (ZEC exchange and custody)](https://www.gemini.com/) — US exchange that added shielded ZEC withdrawals in 2020 and is named custodian for the proposed Winklevoss Zcash ETF. · [Details & sources](docs/directory.md#gemini-zec).
- [Gemini Credit Card: Zcash Edition](https://gemini.com/zcash) — Limited-edition Gemini credit card, issued by WebBank, that pays card rewards in ZEC by default. · [Details & sources](docs/directory.md#gemini-credit-card-zcash-edition).
- [The Zcash ETF (ZCSH), formerly Grayscale Zcash Trust](https://www.grayscale.com/) — Grayscale-sponsored exchange-traded product holding ZEC, listed on NYSE Arca after conversion from the OTCQX-quoted Grayscale Zcash Trust. `changed` · [Details & sources](docs/directory.md#the-zcash-etf-zcsh).
- [Winklevoss Zcash ETF (proposed, WINK)](https://www.sec.gov/Archives/edgar/data/0002158471/000110465926113940/tm2626975-1_s1.htm) — Proposed spot ZEC exchange-traded product sponsored by Winklevoss Asset Services, filed on Form S-1 for a Nasdaq listing. · [Details & sources](docs/directory.md#winklevoss-zcash-etf).
- [ZIP 320: TEX (transparent-source-only) addresses](https://zips.z.cash/zip-0320) — Address encoding that tells wallets to send only from transparent funds, created after Binance required identifiable deposit sources. · [Details & sources](docs/directory.md#zip-320-tex-addresses).

<a id="historical"></a>
## Discontinued, deprecated and changed projects

- [Nighthawk Wallet](https://nighthawkwallet.com/) — A formerly Zcash-focused mobile wallet whose current releases and website target the DarkFi testnet. `changed` · [Details & sources](docs/directory.md#nighthawk-wallet).
- [renZEC (Ren 1.0)](https://medium.com/renprotocol) — ZEC representation minted by the Ren 1.0 MPC bridge network on Ethereum and other chains; Ren announced the sunset of Ren 1.0 in November 2022 after Alameda's bankruptcy. `discontinued` · [Details & sources](docs/directory.md#renzec).
- [Sprout shielded pool](https://zips.z.cash/zip-0211) — The original 2016 Zcash shielded pool, closed to new value by ZIP 211. `deprecated` · [Details & sources](docs/directory.md#sprout-shielded-pool).
- [Wrapped ZEC (WZEC, Ethereum)](https://www.wrapped.com) — Custodial ERC-20 representation of ZEC launched in October 2020 by Tokensoft's 'Wrapped' with Anchorage custody; the contract 0x4A64…6E10 still reports name 'Wrapped ZEC'. `code-only` · [Details & sources](docs/directory.md#wzec-ethereum).
- [Ywallet](https://github.com/hhanh00/zwallet) — A Zcash and Ycash light wallet by hhanh00 that no longer supports Zcash after the Ironwood upgrade. `discontinued` · [Details & sources](docs/directory.md#ywallet).
- [zcashd](https://github.com/zcash/zcash) — The original C++ Zcash full node and embedded wallet, which reached end of life with a hard halt at block 3,417,100 on 18 July 2026. `discontinued` · [Details & sources](docs/directory.md#zcashd).

<!-- DIRECTORY:END -->

## Search and reuse

Use the [clickable indexes](docs/browse.md), your browser’s Find command, or search the dataset locally with Python 3.10+:

```sh
python3 scripts/search.py shielded
python3 scripts/search.py --category swaps
python3 scripts/search.py --network Solana
python3 scripts/search.py --lifecycle discontinued
python3 scripts/search.py --evidence code-only
python3 scripts/search.py --category wallets --json
```

No package installation, API key or wallet connection is required.

## Maintain the list

Edit `data/projects.json`, then regenerate and validate:

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

To perform a fresh public HTTP check, separately:

```sh
python3 scripts/check_links.py
```

The link checker makes ordinary public GET requests. It does not connect wallets or interact with financial contracts. HTTP failures remain visible for manual review; they do not automatically delete an entry or label a project dead.

## Related

- [Awesome BTCFi](https://github.com/Milbaxter/awesome-btcfi) — the sister directory for Bitcoin finance, using the same schema and evidence labels.

## License

[MIT](LICENSE). You can copy, adapt and redistribute this directory and its tooling with the license notice. External project code, trademarks, papers and websites retain their own terms.
