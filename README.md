# DNS Blocklist — SoundCloud Ads (v2)

[![GitHub stars](https://img.shields.io/github/stars/st3fn1/soundcloud-blocklist?style=flat&logo=github)](https://github.com/st3fn1/soundcloud-blocklist/stargazers)
![Validate lists](https://github.com/st3fn1/soundcloud-blocklist/actions/workflows/validate.yml/badge.svg)

Custom DNS lists for [Technitium DNS Server](https://technitium.com/dns/) that remove SoundCloud's
audio ads (served by AdsWizz between tracks) and display ads, **without breaking SoundCloud**.

## The lists

| List | What it does | Use it as |
|------|--------------|-----------|
| [`soundcloud-ads.txt`](https://raw.githubusercontent.com/st3fn1/soundcloud-blocklist/refs/heads/main/soundcloud-ads.txt) | **Core.** Audio ads (AdsWizz), banner ads (Google Ad Manager) and the ad exchanges behind them | Block list |
| [`soundcloud-trackers.txt`](https://raw.githubusercontent.com/st3fn1/soundcloud-blocklist/refs/heads/main/soundcloud-trackers.txt) | *Optional.* Ad verification and measurement trackers | Block list |
| [`allowlist.txt`](https://raw.githubusercontent.com/st3fn1/soundcloud-blocklist/refs/heads/main/allowlist.txt) | Domains SoundCloud needs. Stops **other** big blocklists from breaking playback | Allowed list |

## Setup in Technitium

1. **Settings → Blocking → Block List URLs**: add
   ```
   https://raw.githubusercontent.com/st3fn1/soundcloud-blocklist/refs/heads/main/soundcloud-ads.txt
   https://raw.githubusercontent.com/st3fn1/soundcloud-blocklist/refs/heads/main/soundcloud-trackers.txt
   ```
2. *(Recommended)* **Settings → Blocking → Allow List URLs**: add
   ```
   https://raw.githubusercontent.com/st3fn1/soundcloud-blocklist/refs/heads/main/allowlist.txt
   ```
3. Click **Save**, then **Force Update Block Lists**. Technitium refreshes them every 24 hours after that.

Upgrading from v1? Nothing to change: the `soundcloud-ads.txt` URL is the same and now includes the extra domains.

The lists also work with Pi-hole and AdGuard Home (plain domain format, `#` comments).

## Will it break SoundCloud?

It shouldn't. The lists are designed to stay safe:

- **No SoundCloud domains are ever blocked.** `soundcloud.com`, `sndcdn.com` (audio + artwork) and
  `soundcloud.cloud` (streaming) are on the allowlist instead.
- **Every change is checked automatically.** `scripts/validate.py` runs on each push and fails if any
  blocked entry would block a domain SoundCloud needs.
- **Only third-party ad servers are blocked.** Ad delivery, ad auctions and ad tracking are all optional
  for SoundCloud to work.

## What to expect

- Audio ads are skipped. Occasionally you may hear a **few seconds of silence** where an ad would have played.
- Promoted tracks and "Go+" upsell banners come from SoundCloud's own servers, so DNS can't remove them
  without breaking the site.
- These ad networks serve many other sites too, so you'll see fewer ads elsewhere as a side effect.

## Troubleshooting

If something stops working, open Technitium's **Logs → Query Logs**, filter on *Blocked*, then reproduce
the problem to find the domain. Add it to Technitium's **Allowed** zone, and please
[open an issue](https://github.com/st3fn1/soundcloud-blocklist/issues) so it can be fixed for everyone.

## Star history

If this list saved you from ads, consider giving it a ⭐. It helps others find it.

<a href="https://star-history.com/#st3fn1/soundcloud-blocklist&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=st3fn1/soundcloud-blocklist&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=st3fn1/soundcloud-blocklist&type=Date" />
    <img alt="Star history chart" src="https://api.star-history.com/svg?repos=st3fn1/soundcloud-blocklist&type=Date" />
  </picture>
</a>

## Contributing

1. Edit the list: one lowercase domain per line, `#` for comments.
2. Run `python3 scripts/validate.py` before committing.

See [CHANGELOG.md](CHANGELOG.md) for release history.
