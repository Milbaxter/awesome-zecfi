# Research method and scope

[Back to Awesome ZecFi](../README.md) · Initial research snapshot: **2026-10-15**

## Scope

ZecFi here means financial uses of ZEC and the infrastructure directly enabling them. Coverage includes the Zcash protocol and its shielded pools, network upgrades and funding mechanisms, wallets, ZEC representations on other chains, cross-chain swaps, trading and derivatives, lending, payments, centralized and institutional access, developer tooling and research organizations.

This is **not a claim to enumerate every Zcash project**. Networks, protocols, products, standards and organizations are all counted as **entries**, not as unique companies. Every exchange listing, every liquidity pool and every merchant are outside the core catalog; directories of them are linked instead.

## Research process

1. Discover candidates through the ZIP index, ZecHub, the Zcash Foundation, ZODL, Shielded Labs, wallet and bridge documentation, and web search.
2. Read project websites, documentation, code repositories, ZIPs, SEC filings and official announcements. Prefer a technical page over marketing where practical.
3. Record the mechanism rather than copying superlatives. Identify which pool or address type is used, where ZEC is held, and which questions the documentation leaves open.
4. Look for 2026 changes: zcashd's end of life, the Orchard remediation, NU6.3 (Ironwood), renames and wallet deprecations.
5. Attach at least one dated primary source to every entry. Use `ecosystem-only` when only an ecosystem listing supports inclusion and `code-only` when the evidence is a repository.
6. Run a separate HTTP reachability pass and structural checks. Neither is a protocol audit.

The review used public online sources. Some pages blocked automated access and were not used as evidence. **Reviewed on October 15 is not a claim that every page was updated that day.**

<a id="evidence-and-lifecycle"></a>
## Evidence and lifecycle

These are **independent dimensions**, not a rating scale. Every entry has both.

| Evidence label | Meaning |
| --- | --- |
| `direct-source` | A publisher description, ZIP, filing, original technical document or other direct evidence was reviewed; depth varies |
| `ecosystem-only` | Inclusion rests on an ecosystem or directory listing, without direct product documentation reviewed |
| `code-only` | The cited evidence is source repositories; it does not establish a deployed service |

| Lifecycle label | Meaning |
| --- | --- |
| `unverified` | Current end-to-end operation was not established; this is the default, not a finding of inactivity |
| `mainnet-announced` | Publisher material explicitly advertises mainnet availability; not transaction-tested |
| `testnet` | Reviewed material identifies a testnet or feature net for the listed product |
| `research` | A proposal, concept or proof of concept rather than a deployed product |
| `changed` | Current material differs materially from older descriptions (rename, pivot, conversion) |
| `deprecated` | Publisher or consensus material points to retirement, such as a spend-out-only pool |
| `discontinued` | Publisher explicitly announced closure or end of support |
| `not-applicable` | A standard, developer tool, organization or reference resource rather than a financial service |

`review_note` explains qualifications, especially shielded versus transparent support. None of these labels verifies solvency, successful withdrawals, privacy guarantees or code safety.

## Evidence and source hierarchy

- **Primary:** the project's own website, documentation, code repository, a ZIP, an SEC filing, or the authors' research. A governance post is primary for its own decision, not for every third-party claim it repeats.
- **Secondary:** independent reporting, clearly labelled. Used sparingly, mainly for dates or context the publisher did not state.

No wallets were connected, deposits made, swaps executed or withdrawals tested for this research.

## Dataset fields

The canonical source is [data/projects.json](../data/projects.json). The README listings, detailed catalog, browse indexes and evidence-coverage report are generated from it.

| Field | Meaning |
| --- | --- |
| `id` | Stable lowercase identifier used by catalog links |
| `name` | Project, product, protocol or resource name |
| `category` | One primary category |
| `website` | Canonical resource link; can be documentation where that is more useful |
| `networks` | Relevant ecosystems, not a certified deployment list |
| `kind` | Protocol, standard, network, asset, bridge, application, wallet, tool, infrastructure, organization, data, exchange or service |
| `description` | Short neutral explanation of relevance |
| `zcash_mechanism` | How ZEC is held or moved, and in which pool or address type |
| `review_focus` | Important implementation and economic questions for further diligence |
| `evidence`, `lifecycle`, `review_note` | Evidence basis, lifecycle qualification and explanatory note |
| `sources` | Source URLs, source type and review date; optional descriptive `title` |
| `last_reviewed` | Date of the most recent substantive review of that record |

The schema matches [Awesome BTCFi](https://github.com/Milbaxter/awesome-btcfi), with `zcash_mechanism` in place of `bitcoin_mechanism`.

## Link checking

[The report](../data/link-health.json) stores public URL status, redirects and the time of the HTTP check. A `200` can be a soft 404 or a historical notice; a `403`, timeout or DNS failure can reflect access protection. Failures require human review, not automatic deletion.

## Known gaps

Shielded deposit and withdrawal support has not been checked exchange by exchange. Ironwood support is unconfirmed for several wallets. Lending and yield markets for ZEC are thin, and only one is listed. The [generated review queue](coverage.md) keeps thinly sourced entries visible. No continuous monitoring is promised by this static snapshot.
