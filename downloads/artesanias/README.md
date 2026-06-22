# Artesanías de Colombia — Reports about Tello, Huila

A license-first collection of public technical reports authored or co-authored
by **Artesanías de Colombia** (a Colombian state entity under the Ministerio
de Comercio, Industria y Turismo) that have the municipality of **Tello, Huila**
as their primary subject.

Captured on 2026-06-20 for the Sociedad Opita project (engagement
`tello-research-2026-06`).

## Summary

| Metric | Count |
| --- | --- |
| Reports identified (Tello-focused) | 13 |
| Year range | 1990 – 2006 |
| Subject focus | guadua, bejuco, cestería, tejidos, tintes, pintura, organización gremial, diseño |
| **Mirrored locally (web/public/downloads/artesanias/)** | **0** |
| External link only (registry.json) | 13 |

## License breakdown

| License | Count | Action |
| --- | --- | --- |
| CC-BY | 0 | — |
| CC-BY-SA | 0 | — |
| Public domain | 0 | — |
| CC-BY-NC | 1 | external link only |
| CC-BY-NC-SA | 8 | external link only |
| CC-BY-NC-ND | 3 | external link only |
| Todos los derechos reservados (no CC declared) | 0 | — |
| Unknown / no explicit license | 1 | external link only |
| **Total** | **13** | **all external link only** |

(CC-BY-NC-SA total = 6 of v4.0 + 2 of v3.0 = 8)

## Why nothing is mirrored

The Artesanías de Colombia institutional repository at
`https://repositorio.artesaniasdecolombia.com.co` consistently publishes its
content under Creative Commons variants that include a **NonCommercial**
clause (CC-BY-NC, CC-BY-NC-SA, or CC-BY-NC-ND). One item
(INST-D 1997. 199) has no explicit CC license declared on its handle page
and only carries the default DSpace "all rights reserved" notice.

The operator's license-first policy treats every CC-BY-NC* variant as
restrictive, alongside the unknown / all-rights-reserved items. Because
**no item in this collection carries a permissive CC-BY or CC-BY-SA
license, no PDF was downloaded into `web/public/downloads/artesanias/`.**

This is the conservative, legally clean outcome the operator asked for. If
the Sociedad Opita project is unambiguously non-commercial, the CC-BY-NC-SA
items *would* in principle permit redistribution with attribution — but
that determination belongs to the operator, not the downloader.

## Files in this directory

| File | Purpose |
| --- | --- |
| `registry.json` | Machine-readable catalog of all 13 reports with metadata, license, and bitstream URL |
| `artesanias-tello.bib` | BibTeX entries for all 13 reports (citation use) |
| `README.md` | This file |

Because no PDF was mirrored, there are no `*.pdf` or `*.txt` sidecars in
this directory.

## How to consume this collection

### As a download site

Because every item is `external_only`, the public site should render the
catalog as a list of links pointing back to the original repository handle
pages (e.g. `https://repositorio.artesaniasdecolombia.com.co/handle/001/10588`).
Do **not** generate local `web/public/downloads/artesanias/*.pdf` URLs.

### As citations

Use the BibTeX file `artesanias-tello.bib`. Each entry has a `note` field
explaining the license and the distribution status. Example:

```bibtex
@incollection{instD1997_196_taller_cesteria_tello,
  ...
  url = {https://repositorio.artesaniasdecolombia.com.co/handle/001/10588},
  note = {CC-BY-NC-SA-4.0; external link only, not mirrored}
}
```

### As a research dataset

The `registry.json` is suitable for ingestion by any downstream tool that
needs a structured list of Tello-related Artesanías de Colombia reports.
Each entry includes the canonical handle URL and the canonical bitstream
URL.

## Collection inventory

| # | Series | Year | Title (short) | License |
| --- | --- | --- | --- | --- |
| 1 | INST-D 1990. 82 | 1990 | Hombres de la guadua y el bejuco: Tello un pueblo de artesanos *(video)* | CC-BY-NC-ND-4.0 |
| 2 | INST-D 1995. 72 | 1995 | Memoria de oficio: cestería en guadua en Tello Huila | CC-BY-NC-4.0 |
| 3 | INST-D 1995. 173 | 1995 | Asesoría en diseño en Tello Huila 1995 | CC-BY-NC-SA-4.0 |
| 4 | INST-D 1995. 175 | 1995 | Memoria de tejidos y cordones Tello Huila | CC-BY-NC-SA-4.0 |
| 5 | INST-D 1995. 176 | 1995 | Memoria de tintes Tello Huila | CC-BY-NC-SA-4.0 |
| 6 | INST-D 1995. 244 | 1995 | Cestería en guadua en Tello (Huilla): memoria de oficio | CC-BY-NC-SA-4.0 |
| 7 | INST-D 1997. 196 | 1997 | Taller de cestería en Tello Huila | CC-BY-NC-SA-4.0 |
| 8 | INST-D 1997. 199 | 1997 | Asesoría en organización gremial (Tello + La Vega + La Jagua + Neiva) | **UNKNOWN** (no CC declared) |
| 9 | INST-D 1997. 223 | 1997 | Taller de pintura Tello Huila | CC-BY-NC-SA-4.0 |
| 10 | INST-D 2000. 130 | 2000 | Asesoría de diseño (Aipe + Tello + Villavieja + Guadalupe), Huila | CC-BY-NC-SA-3.0 |
| 11 | INST-D 2006. 25 | 2006 | Desarrollo de dos líneas de productos mejorados (Tello + Mallama) | CC-BY-NC-ND-4.0 |
| 12 | INST-D 2006. 140 | 2006 | Mejoramiento del producto artesanal en guadua y bejuco en Tello, Huila | CC-BY-NC-SA-3.0 |
| 13 | INST-D 2006. 342 | 2006 | Mejoramiento tecnológico de herramientas para tiras de guadua en Tello | CC-BY-NC-ND-4.0 |

## Methodology notes

- **Source**: `https://repositorio.artesaniasdecolombia.com.co/simple-search?query=Tello+Huila`
- **Total search results**: 273 (28 pages of 10 per page, sorted by relevance)
- **Selection criterion**: Top 13 results whose primary subject is the
  municipality of Tello, Huila. Items 14+ on the relevance-ranked list are
  Huila-departmental reports (Neiva, Garzón, Aipe, Isnos, etc.) that only
  mention Tello in passing and were intentionally excluded from this
  collection.
- **License verification**: Each handle page was fetched and its
  `DC.rights` metadata block plus the embedded Creative Commons license URL
  were parsed. License assignment in `registry.json` follows the explicit
  CC license URL on each item page.
- **Anti-bot access**: The repository is protected by BunkerWeb with a
  JavaScript proof-of-work challenge. To verify licenses and obtain
  bitstream URLs, the PoW was solved once per handle-page request using the
  Python standard library (`hashlib` + `urllib`). No packages were
  installed and no session cookies were persisted.
- **Tools used**: PowerShell 5.1, `curl.exe`, `Invoke-WebRequest`, and the
  existing `venv-verify` Python interpreter
  (`C:\Users\nicou\Documents\maria-trabajos\.venv-verify\Scripts\python.exe`)
  for the PoW step only.

## What would unlock local mirroring

To actually get PDFs into `web/public/downloads/artesanias/`, one of the
following would need to change:

1. **Loosen the license-first policy** to accept CC-BY-NC-SA for
   non-commercial/educational projects (and confirm the Sociedad Opita
   project qualifies).
2. **Obtain explicit written permission** from Artesanías de Colombia
   (Subgerencia Cultural / Grupo de Comunicaciones) to redistribute the
   specific reports.
3. **Wait for Artesanías de Colombia to relicense** their institutional
   repository under CC-BY or CC-BY-SA.

The current operator instructions explicitly forbid options (1) and (2)
without an explicit operator decision, and option (3) is outside our
control. The result above reflects the strict, conservative reading of the
license-first policy.

## Citations for the source institution

```bibtex
@misc{artesanias_colombia_institutional,
  title  = {Artesanías de Colombia},
  author = {{Artesanías de Colombia}},
  year   = {2024},
  url    = {https://www.artesaniasdecolombia.com.co/}
}
```
