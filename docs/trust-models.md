# Trust models and due diligence

[Back to Awesome ZecFi](../README.md)

This directory does not assign numerical safety or privacy scores. A single score hides the fact that custody, privacy, settlement and economic exposure can fail independently. A product can be self-custodial and still leak metadata, or private on Zcash and fully transparent after a bridge.

## Compare the mechanism

| Mechanism | What controls the ZEC or claim? | Questions that distinguish implementations |
| --- | --- | --- |
| Shielded pool (Sapling, Ironwood) | Zcash consensus rules and the user's spending key | Does the wallet support the current pool? How are viewing keys shared? What metadata (timing, IP, light-client server) leaks? |
| Deprecated pool (Sprout, Orchard) | Consensus rules that only allow value to leave | Does my wallet still scan and migrate these notes? Is the turnstile accounting published? |
| Transparent address / TEX | Zcash consensus rules, like Bitcoin-style UTXOs | Everything is public. Is this address type required by the counterparty? |
| Light wallet via lightwalletd or Zaino | User keys plus a server that serves compact blocks | Can I choose or run my own server? What does the server learn about my activity? |
| Proof-of-authority bridge (NEAR Intents POA) | A set of bridge authorities holding ZEC at transparent addresses | Who are the signers? Is there proof of reserves? Who can pause or freeze? |
| Chain-signature or MPC bridge (Omni, Zenrock) | A network of signers or MPC nodes, plus contracts on the destination chain | Signer set and threshold, upgrade keys, redemption limits, incident history |
| Native-asset AMM (Maya, THORChain) | A network-controlled vault on Zcash and the network's validators | Is the Zcash vault transparent? What are slashing, solvency and halt rules? |
| Intent / solver routing | Solvers or market makers filling quotes, plus a verifier contract | Refund rules, minimums, failure handling and which bridge holds funds in transit |
| Wrapped token on a money market | Bridge issuer plus the lending protocol's contracts and oracle | Liquidation path, oracle source, curator powers and wrapper depeg handling |
| Perpetual futures | The venue's margin engine, oracle and insurance fund | No ZEC is held; what are funding, liquidation and auto-deleveraging rules? |
| Exchange or custodian | A company holding ZEC on your behalf | Shielded deposit/withdrawal support, jurisdiction, freezes and proof of reserves |
| Exchange-traded product | Fund sponsor, custodian and authorized participants | Fees, creation/redemption in cash or kind, custodian concentration |

## Privacy is a property of a path, not a coin

Every hop is a separate question. A shielded wallet that sends to a transparent bridge deposit address reveals the amount and destination of that hop. A swap that pays out to a shielded address hides only what happens after the payout. Review the full route.

## Due-diligence checklist

1. Identify the exact asset: native ZEC in a named pool, or a token with a contract address and issuer.
2. Identify who can move, freeze or upgrade it, and how many independent parties that requires.
3. Check that the service works after zcashd's end of life and supports Ironwood.
4. Read incident and migration notices: Orchard remediation, bridge or venue migrations, and wallet deprecations.
5. Confirm the exit: how you return to self-custodied shielded ZEC, at what cost and with what minimums.
6. Separate rewards from real fees. Incentive programs, fund fees and perpetual funding rates are distinct sources.
