# Evidence coverage and review queue

Snapshot: **2026-10-15** · [Method](methodology.md) · [Browse](browse.md) · [Material changes](research-notes.md)

Generated from the dataset. Counts describe research coverage, not project quality or safety. Several sources from one publisher are not independent corroboration.

| Measure | Count |
| --- | ---: |
| Total entries | 81 |
| Entries with one cited source | 23 |
| Entries citing only their listed website/resource URL | 13 |
| Evidence: code-only | 11 |
| Evidence: direct-source | 66 |
| Evidence: ecosystem-only | 4 |

A website/resource URL can be a technical document or repository, so the URL-only count is a triage signal, not a claim that all those sources are marketing pages.

## Entries needing stronger direct evidence

| Entry | Evidence | Specific unresolved point |
| --- | --- | --- |
| [Zkool](directory.md#zkool) | code-only | The README lists only transparent, Sapling and Orchard, and Ironwood support is unconfirmed from that source. The UI is described as basic, and some features are missing. |
| [Edge](directory.md#edge-wallet) | ecosystem-only | Edge's own site does not state shielded support; the 'shielded by default' claim comes from the z.cash directory. Swaps go through third-party exchange partners. |
| [Zebra](directory.md#zebra) | code-only | ZIP 258 says Zebra is expected to be the only full validator that follows the chain from NU6.3. Forks (Zakura, ZODL's zebra, Crosslink staging) also exist. |
| [Zaino](directory.md#zaino) | code-only | Light-client servers can see client IPs and query patterns unless used over Tor. |
| [lightwalletd](directory.md#lightwalletd) | code-only | The README security disclaimer still references ECC's security team, which is out of date after the 2026 team move. |
| [librustzcash](directory.md#librustzcash) | code-only | Forks exist (QEDIT ZSA branch, zodl-inc zakura-wallet-libraries). |
| [Zcash Android and iOS (Swift) wallet SDKs](directory.md#zcash-mobile-sdks) | code-only | Both the zcash/ and zodl-inc/ SDK repositories are active. The zcash/ READMEs carry beta and ECC-review disclaimers that look out of date. |
| [zingolib](directory.md#zingolib) | code-only | Frequent major-version bumps (v5 June 2026, v6 Sept 2026). |
| [Omni Bridge ZEC on Solana](directory.md#omni-bridge-zec-solana) | code-only | Possibly a double-wrapped IOU (Zcash, then a NEAR bridge token, then an Omni-minted SPL). Holding or lending it on Solana is fully transparent. Its backing depends on NEAR bridge operators, not on the Zcash protocol. |
| [Bitfrost Native ZEC (BZEC) on Hyperliquid](directory.md#bitfrost-bzec) | ecosystem-only | The issuer site was unreachable during review, so redemption status is unknown and should be treated as high-risk until Bitfrost confirms it. This is not evidence of a shutdown. Like other wrapped ZEC, BZEC carries no shielded privacy. |
| [THORChain ZEC pool](directory.md#thorchain-zec) | code-only | Primary evidence is code only; the pool launch reached us through press quoting THORChain's X post, and swap go-live is unconfirmed (a single 9 Oct 2026 report claims it). Vaults are transparent, so swaps break the shielded link. |
| [Ztarknet](directory.md#ztarknet) | code-only | Research or proof-of-concept only. There is no ZEC on it and no bridge, and since the TZE is transparent, the privacy of any future ZEC moved to it is unclear. |
| [Wrapped ZEC (WZEC, Ethereum)](directory.md#wzec-ethereum) | code-only | A custodial IOU with unclear current redemption. The issuer's site no longer references it, but there is no publisher shutdown notice. It never had Zcash privacy on Ethereum. |
| [ZGo](directory.md#zgo) | ecosystem-only | Publisher site rendered no substantive content on fetch; details come from ZecHub only. |
| [ZecHub payment processor list](directory.md#zechub-payment-processors) | ecosystem-only | Useful cross-check but community-maintained; rows lack per-entry dates. |

## Coverage still missing

Deeper coverage is still needed for exchange-by-exchange shielded deposit and withdrawal support, Ironwood support in each wallet and payment tool, additional ZEC venues on Solana and NEAR, and regional regulated access. The list also lacks a systematic deployment-by-deployment audit and incident history. These gaps remain open; entry count is not a measure of completeness.

## Next review priorities

1. Resolve the ecosystem-only and code-only entries above with dated product documentation.
2. Recheck redemptions, changed strategies, closures and permissioned bridge roles.
3. Add deployment-specific audit scope and incident/recovery sources where independently verified.
4. Review the HTTP failures in [link health](../data/link-health.json), without inferring closure from access errors.
