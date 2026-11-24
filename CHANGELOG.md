# Changelog

## v2.0.0
- **soundcloud-ads.txt** now also covers more AdsWizz hosts, Google Ad Manager display ads, and the
  header-bidding exchanges (Amazon, Xandr, Magnite, PubMatic, OpenX, Index Exchange, Criteo).
  The URL is unchanged, so v1 users are upgraded automatically.
- New **soundcloud-trackers.txt**: optional list of ad verification and measurement trackers.
- New **allowlist.txt**: domains SoundCloud needs, to stop other blocklists from breaking playback.
- New `scripts/validate.py` plus a GitHub Actions check: rejects malformed or duplicate entries
  and anything that would block a SoundCloud domain.
- Lists now have comment headers grouped by purpose.
- Rewritten README with setup, safety notes and troubleshooting.

## v1.0.0
- Initial AdsWizz audio ad blocklist.
