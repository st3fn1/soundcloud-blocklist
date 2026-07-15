# DNS Blocklist — SoundCloud Ads

A small custom blocklist for use with [Technitium DNS Server](https://technitium.com/dns/), 
targeting the AdsWizz ad-serving domains SoundCloud uses to inject audio ads between tracks.

## Usage
Add the raw URL to Technitium under **Settings → Block Lists → Block List URLs**:

[](https://raw.githubusercontent.com/st3fn1/soundcloud-blocklist/refs/heads/main/soundcloud-ads.txt)

Technitium will pull and apply it automatically, refreshing every 24 hours.

## Notes
- Blocking these domains stops ad audio requests, but SoundCloud may show a brief 
  silence/gap instead of a seamless skip.
- AdsWizz serves ads for many other publishers too, so this may reduce ads elsewhere as a side effect.
