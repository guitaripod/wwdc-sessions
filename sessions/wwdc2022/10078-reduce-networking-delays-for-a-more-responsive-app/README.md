---
id: "wwdc2022-10078"
event: "wwdc2022"
year: 2022
title: "Reduce networking delays for a more responsive app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10078"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Reduce networking delays for a more responsive app

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10078](https://developer.apple.com/videos/play/wwdc2022/10078)

Find out how network latency can affect your apps when trying to get full benefit out of modern network throughput rates. Learn about changes you can make in your app and on your server to boost responsiveness, and prepare your app for improvements coming to the Internet that will offer even lower end-to-end delays.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,016 words)

## Documentation & Resources

- [Network Speedtest by Ookla](https://apps.apple.com/us/app/speedtest-by-ookla/id300704847) _download_
- [Network Quality test in Go](https://github.com/network-quality/goresponsiveness) _download_
- [Waveform bufferbloat test](https://www.waveform.com/tools/bufferbloat) _download_
- [Responsiveness Test Server configuration instructions](https://github.com/network-quality/server) _download_

## Code Snippets

### Enable connection migration on URLSessionConfiguration for HTTP/3 — [6:21]

```swift
let configuration = URLSessionConfiguration.default
configuration.multipathServiceType = .handover
```

### Enable connection migration on NWParameters for QUIC — [6:29]

```swift
let parameters = NWParameters.quic(alpn: ["myproto"])
parameters.multipathServiceType = .handover
```

### Opt-in to QUIC datagrams — [7:08]

```swift
// Only one datagram flow can be created per connection
let options = NWProtocolQUIC.Options()
options.isDatagram = true
options.maxDatagramFrameSize = 65535
```

### Network quality tool in MacOS — [8:12]

```bash
networkQuality -s -C https://myserver.example.com/config
```

### Recommended configuration for Apache Traffic Server — [10:59]

```markdown
% cat /opt/ats/etc/trafficserver/records.config

# Set not-sent low-water mark trigger threshold to 128 kilobytes
CONFIG proxy.config.net.sock_notsent_lowat INT 131072

# Set Socket Options flag to the sum of the options we want
# TCP_NODELAY(1) + TCP_FASTOPEN(8) + TCP_NOTSENT_LOWAT(64) = 73
CONFIG proxy.config.net.sock_option_flag_in INT 73

...

# Enable Dynamic TLS record sizes
CONFIG proxy.config.ssl.max_record_size INT -1

...

# Reduce low-water mark and buffer block size for HTTP/2
CONFIG proxy.config.http2.default_buffer_water_mark INT  32768
CONFIG proxy.config.http2.write_buffer_block_size   INT 262144
```

### Responsiveness tests — [12:52]

```markdown
https://www.waveform.com/tools/bufferbloat
https://github.com/network-quality/goresponsiveness
https://www.speedtest.net/
```

### Enable L4S for QUIC on Mac — [17:12]

```bash
defaults write -g network_enable_l4s -bool true
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10078/4/688F144C-0F4D-4F7B-B77A-F10A56978C49/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10078/4/688F144C-0F4D-4F7B-B77A-F10A56978C49/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10078) — developer.apple.com. Indexed for agent consumption._
