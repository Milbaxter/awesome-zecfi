# Material changes and terminology traps

[Back to Awesome ZecFi](../README.md) · Reviewed October 15, 2026

This is a selective research log, not a complete incident database. It records changes that materially affected how entries were classified.

| Finding | Directory treatment | Evidence |
| --- | --- | --- |
| The Electric Coin Company team left in January 2026 and formed ZODL (Zcash Open Development Lab); Zashi was renamed Zodl in v3.0.0 | ECC and Zashi `changed`; attribute current wallet and librustzcash work to ZODL | [ZODL about](https://zodl.com/about/), [ZODL seed announcement](https://zodl.com/zodl-raises-25m-in-seed-funding/) |
| zcashd halted on July 18, 2026 at block 3,417,100; successors are Zebra/Zakura (node) and Zallet (wallet) | [zcashd](directory.md#zcashd) `discontinued`; flag services that still document zcashd RPC | [zcashd end-of-life page](https://zcash.github.io/zcash/user/end-of-life.html) |
| A soundness bug in the Orchard circuit was found in May 2026 and remediated by emergency upgrades in early June; the publisher reports no evidence of exploitation | Described as a remediated vulnerability, not an exploit | [ZODL remediation notice](https://zodl.com/orchard-vulnerability-successfully-remediated/) |
| NU6.3 (Ironwood) activated a new shielded pool; Orchard became spend-out-only, with a turnstile into Ironwood | [Orchard](directory.md#orchard-shielded-pool) `deprecated`; [Ironwood](directory.md#ironwood-nu6-3) `mainnet-announced`; ask every wallet and payment tool about Ironwood support | [ZIP 258](https://zips.z.cash/zip-0258), [ZODL Ironwood post](https://zodl.com/ironwood-a-new-shielded-pool-for-zcash/) |
| NU7 is activated on testnet only; Zcash Shielded Assets are not part of NU7 and remain on QEDIT's separate test network | [NU7](directory.md#nu7-network-upgrade) and [ZSA](directory.md#zcash-shielded-assets) `testnet` | [ZIP 259](https://zips.z.cash/zip-0259) |
| The NU6 lockbox stopped accruing at block 3,146,400; NU6.1 funds Zcash Community Grants (8%) and a coinholder-controlled fund (12%) until block 4,406,400 | Single [dev fund](directory.md#dev-fund-coinholder-fund) entry; report ZIP status as displayed | [ZIP 1015](https://zips.z.cash/zip-1015), [ZIP 1016](https://zips.z.cash/zip-1016) |
| Ywallet dropped Zcash after Ironwood and points users to Zkool | [Ywallet](directory.md#ywallet) `discontinued` for Zcash | [Ywallet repository](https://github.com/hhanh00/zwallet) |
| Nighthawk's current releases target DarkFi; its last Zcash release was in November 2024 | [Nighthawk](directory.md#nighthawk-wallet) `changed`; historical section | [Nighthawk Android repository](https://github.com/nighthawk-apps/nighthawk-android-wallet) |
| Grayscale's Zcash Trust converted into an exchange-listed ETF (ZCSH); a Winklevoss Zcash ETF S-1 was filed October 6, 2026 and is preliminary | [ZCSH](directory.md#the-zcash-etf-zcsh) `changed`; [WINK](directory.md#winklevoss-zcash-etf) described as proposed | [ZCSH prospectus](https://www.sec.gov/Archives/edgar/data/0001720265/000119312526364568/zcsh__424b3_08.25.2026.htm), [WINK S-1](https://www.sec.gov/Archives/edgar/data/0002158471/000110465926113940/tm2626975-1_s1.htm) |
| Ledger added native shielded ZEC in Ledger Wallet Desktop (September 2026); Trezor remains transparent-only | Hardware wallet entries state shielded versus transparent support separately | [Ledger entry sources](directory.md#ledger-zcash), [Trezor entry sources](directory.md#trezor-zcash) |

## Names and claims that can mislead

- **“Shielded”** now means Sapling or Ironwood for new funds. Orchard receivers in old unified addresses still work for migration, but Orchard no longer accepts new value.
- **Zashi / Zodl / ZODL:** Zodl is the wallet (formerly Zashi); ZODL is the company formed by former ECC staff. “CashZ” appears only in early secondary coverage.
- **ECC:** still exists as an entity and is named in dev-fund governance, but no longer employs the team that built Zashi and librustzcash.
- **zcashd versus Zebra, Zakura and Zallet:** zcashd no longer runs; Zebra and Zakura are full nodes, Zallet is the wallet that replaced zcashd's wallet.
- **ZEC on NEAR, Solana, Hyperliquid, Starknet and Aptos:** bridged representations (zec.omft.near, Omni Bridge ZEC, zenZEC, UZEC, BZEC), not shielded ZEC. Identify the issuer and bridge before treating two “ZEC” tokens as the same asset.
- **Maya's “shielded” swap memo:** the swap value still moves through a transparent vault and Maya publishes the viewing key for the memo; this is not private routing. See [Maya](directory.md#maya-protocol-zec).
- **NEAR Intents:** its documentation marks Zcash as transparent-only; wallets that shield before or after a swap add that step themselves. See [NEAR Intents](directory.md#near-intents-zec).
- **TEX addresses (ZIP 320):** exist so exchanges can reject shielded-source deposits; a TEX address is transparent by design. See [ZIP 320](directory.md#zip-320-tex-addresses).
- **EU rules:** the restriction on anonymity-enhancing coins comes from the AMLR (Regulation (EU) 2024/1624, Article 79), which applies to service providers from July 10, 2027. It is not a MiCA delisting that has already happened. [Regulation text](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1624).
- **Coinbase:** a secondary claim of an April 2026 ZEC delisting was not corroborated; Coinbase is custodian and prime broker in the August 2026 ZCSH prospectus. Withdrawals have historically been transparent-only. See [Coinbase](directory.md#coinbase-exchange-zec).
- **SEC and the Zcash Foundation:** the January 2026 closure of an SEC inquiry is foundation-reported via [secondary coverage](https://www.theblock.co/post/385629/zcash-foundation-says-sec-has-closed-book-on-years-long-prob), not an SEC finding.
- **Halvings:** keyed to block height. The second was at block 2,726,400 (November 2024); the third is scheduled at block 4,406,400 (roughly late 2028), and NU7 block-time proposals could move the calendar date.

## Interpreting a current homepage

A homepage update establishes a change in public description, not proof that a feature works end to end. Wallets in particular may list “shielded” support from before Ironwood. This is why the directory records **which pool** a source names and leaves lifecycle `unverified` unless the publisher makes a specific claim.

Historical entries remain visible to make older Zcash guides easier to interpret. No deposit instructions are provided for closed or deprecated projects.
