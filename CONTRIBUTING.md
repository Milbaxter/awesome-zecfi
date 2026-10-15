# Contributing

Thank you for helping keep Awesome ZecFi useful and accurate. Additions, corrections, current status evidence and better technical sources are welcome.

## Add or update an entry

1. Search existing entries to avoid duplicates. Name distinct products clearly; do not add every token, pool or exchange listing as a separate project.
2. Edit [data/projects.json](data/projects.json). Use an existing category and a stable, unique lowercase `id`.
3. Provide a neutral description, Zcash mechanism, concrete review questions, separate evidence and lifecycle labels and at least one dated primary source.
4. State which pool or address type is involved (transparent, Sapling, Orchard, Ironwood, unified address, TEX). Do not call a product “private” or “shielded” without that qualification.
5. Use `ecosystem-only` or `code-only` for limited evidence, and `unverified` lifecycle unless a specific lifecycle claim is supported. Do not use a reachable website as proof of an operating financial product.
6. Update the record's review date only after reading its sources. Advance the snapshot date when needed; leave untouched records' dates intact.
7. Run `python3 scripts/build.py` and `python3 scripts/validate.py`. Include the generated README and catalog changes in the pull request.

Use Python 3.10 or newer. No third-party dependencies are required. The optional network check is `python3 scripts/check_links.py`; keep genuine access failures visible and explain redirects or inaccessible sources in the PR.

## Editorial standards

- Prefer documentation, source repositories, ZIPs, official release/closure notices and direct research papers. Attribute secondary analysis explicitly.
- Explain the actual asset and mechanism. Do not repeat “fully private,” “untraceable,” “risk-free” or “guaranteed yield” without precise qualifications and evidence.
- Separate production components, proposals, testnets and marketing. A ZIP in Draft or a roadmap is not a deployment.
- Do not add referral links, airdrop campaigns, paid rankings, price predictions or unsourced APY/TVL figures.
- Preserve discontinued projects when they help explain the ecosystem. Never convert a temporary HTTP error into a closure claim.
- Source code being public does not prove a project is open source. Verify its license before making that claim.
- Cite incident and recovery claims carefully. This repository is not an exhaustive security incident database.

By contributing, you agree that your original contribution is licensed under the repository's [MIT License](LICENSE). Do not copy third-party articles or large documentation excerpts into the dataset.
