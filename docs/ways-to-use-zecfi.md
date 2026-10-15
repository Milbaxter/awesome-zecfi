# Ways to use ZecFi

[Back to Awesome ZecFi](../README.md) · Snapshot: October 15, 2026

ZecFi is an umbrella term, not a single architecture. Most Zcash finance activity happens in two places: **inside Zcash**, where shielded transfers are possible, and **outside Zcash**, where ZEC is represented by a bridged token, an exchange balance or a fund share. Privacy usually ends at that boundary. This map groups **activities**, while the [directory](directory.md) groups **projects and infrastructure**.

These are descriptions of mechanisms, not recommended allocations. Examples identify relevant projects; they do not imply that a market is open, available in your jurisdiction, or appropriate for you.

## Activity map

| Approach | What you do / hold | Where the benefit comes from | Examples | Main tradeoffs |
| --- | --- | --- | --- | --- |
| Hold and send shielded ZEC | Native ZEC in a shielded pool, from a self-custodial wallet | Transaction privacy for amounts, addresses and memos | [Zodl](directory.md#zodl-wallet), [Zingo](directory.md#zingo-wallet), [Zkool](directory.md#zkool), [Ironwood](directory.md#ironwood-nu6-3) | Wallet must support the current pool; sync, backups and metadata such as timing and network-level leaks |
| Use hardware signing for shielded ZEC | Keep spend keys on a device | Key isolation | [Ledger](directory.md#ledger-zcash), [Keystone](directory.md#keystone-hardware-wallet) | Shielded support differs by device and companion app; Trezor is transparent-only |
| Accept ZEC payments | Generate payment requests or run a processor | Payment receipts without card rails | [BTCPay Zcash plugin](directory.md#btcpay-zcash-plugin), [CipherPay](directory.md#cipherpay), [ZIP 321](directory.md#zip-321) | Ironwood support, viewing-key handling, custody of received funds and conversion |
| Spend through a merchant network | Pay merchants through an integrated wallet | Convenience | [Flexa](directory.md#flexa-zec), [Pay With Zcash directory](directory.md#paywithzcash-directory) | Network operator and merchant coverage; check which pool is used |
| Swap into or out of ZEC across chains | Exchange ZEC for another chain's asset | Access to another asset or market, not yield | [NEAR Intents](directory.md#near-intents-zec), [Maya](directory.md#maya-protocol-zec), [SwapKit](directory.md#swapkit-zec), [Zodl swaps](directory.md#zodl-swaps-crosspay) | Routes are generally transparent on the Zcash side; refund rules, solvers and bridge custody |
| Hold ZEC on another chain | A bridged token such as zec.omft.near, Omni ZEC, zenZEC or UZEC | Composability with that chain's applications | [ZEC on NEAR](directory.md#zec-on-near-poa), [Omni ZEC on Solana](directory.md#omni-bridge-zec-solana), [zenZEC](directory.md#zenzec), [UZEC](directory.md#unit-zec-hyperliquid) | Not shielded; bridge custodian or signer risk; redemption path back to native ZEC |
| Borrow against bridged ZEC | Post a ZEC token as collateral | Stablecoin liquidity without selling | [Kamino ZCASH Market](directory.md#kamino-zcash-market) | Liquidation, oracle, curator and bridge risk; the collateral is a wrapper |
| Provide AMM liquidity | Supply a ZEC token and another asset to a pool | Trading fees and sometimes incentives | [Raydium](directory.md#raydium-zec-pools), [Maya](directory.md#maya-protocol-zec) | Impermanent loss, wrapper risk and pool depth |
| Trade ZEC perpetuals | Hold a derivative position settled in stablecoins | Price exposure, hedging or leverage | [Hyperliquid](directory.md#hyperliquid-zec-perp), [dYdX](directory.md#dydx-zec-perp), [Lighter](directory.md#lighter-zec-perp), [Aster](directory.md#aster-zec-perp) | No ZEC is held; funding, liquidation and venue risk |
| Gain regulated fund exposure | Shares of an exchange-traded product | Brokerage access and custody handled by the fund | [ZCSH](directory.md#the-zcash-etf-zcsh), [Winklevoss ETF (proposed)](directory.md#winklevoss-zcash-etf) | Fees, cash-only creation/redemption, custodian concentration; no shielded use |
| Hold ZEC at an exchange or custodian | A centralized account balance | Convenience, fiat ramps, institutional custody | [Coinbase](directory.md#coinbase-exchange-zec), [Gemini](directory.md#gemini-zec), [Cobo](directory.md#cobo-zec-custody) | Counterparty risk; shielded deposits and withdrawals vary by venue |
| Participate in proof-of-stake research | Run or test staking software | Testnet experience; no mainnet rewards | [Crosslink](directory.md#crosslink) | Feature-net only; parameters and economics are not final |

## Questions to ask before moving ZEC

1. **Which pool or address type is this?** Transparent, Sapling, Orchard (spend-out only) or Ironwood.
2. **Does privacy survive the next step?** Bridges, exchanges and most swaps see transparent ZEC.
3. **Who can move the underlying ZEC?** A bridge signer set, a custodian, a solver, or only your keys.
4. **How do I get back to native ZEC?** Redemption path, fees, minimums and whether anyone can freeze it.
5. **What changed in 2026?** Check that the wallet or service no longer depends on zcashd and supports Ironwood.
