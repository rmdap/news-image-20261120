# Agent notes — The World in One Day, 20 November 2026

Built in a single session started after the competition opened
(20 Nov 2026 00:00 UTC).

- Research: `news-2026-11-20.md` — 42 stories verified against their own
  sources for 20 Nov 2026. Stories first reported before 20 Nov (the ICJ
  verdict itself, the US–Venezuela military deal, Haiti's Martissant raid,
  Bukele's third-term registration, the Sudan gold-mine drone strike, the
  Senegal boat capsize, Kenya's last Ebola discharge, Somalia expelling the
  UAE envoy, the US measles status loss, Estonia's border-closure
  announcement, the COP31 draft) are listed in the DATE CHECK on the image,
  not presented as 20 Nov news. The COP31 outcome was still pending at
  build time, so the card says "no deal yet" — no outcome invented.
- Image: `gen-20nov-v1.py` (PIL only) draws the front page: masthead,
  region bar, 6-number strip, 3 hero cards, 10 illustrated cards, dotted
  world map with numbered pins, ALSO ON list, DATE CHECK, sources footer.
  1024×1024, under 1 MiB.
- Entrypoint: `main.py` copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Deterministic —
  identical bytes on every run.
