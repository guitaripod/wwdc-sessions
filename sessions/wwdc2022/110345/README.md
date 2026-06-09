---
id: "wwdc2022-110345"
event: "wwdc2022"
year: 2022
title: "What’s new in Endpoint Security"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110345"
topics: ["Business & Education", "Privacy & Security"]
platforms: ["macOS"]
hasTranscript: true
---

# What’s new in Endpoint Security

**Event:** WWDC22 · **Topic:** Privacy & Security · **Platforms:** macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-110345](https://developer.apple.com/videos/play/wwdc2022/110345)

Learn how you can build reliable endpoint security products like anti-virus software, endpoint detection and response, and data leakage prevention solutions for macOS. We'll take you through the latest enhancements to Endpoint Security APIs: Learn how you can support more security events and use advanced muting capabilities in your app. We'll also explore a standalone tool to help you perform introspection from the command line.

**Keywords:** `authentication`, `eslogger`, `gatekeeper`, `kauth`, `kernel`, `login`, `logout`, `malware`, `openbsm`, `xprotect`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,362 words)

## Documentation & Resources

- [Endpoint Security](https://developer.apple.com/documentation/EndpointSecurity) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/EndpointSecurity
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/EndpointSecurity.json
- [Monitoring System Events with Endpoint Security](https://developer.apple.com/documentation/EndpointSecurity/monitoring-system-events-with-endpoint-security) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/EndpointSecurity/monitoring-system-events-with-endpoint-security
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/EndpointSecurity/monitoring-system-events-with-endpoint-security.json

## Code Snippets

### Target path muting — [4:29]

```swift
// Mute events operating on /var/log
es_mute_path(client, "/private/var/log", ES_MUTE_PATH_TYPE_TARGET_PREFIX)

// Mute write events to /dev/null
var events = [ ES_EVENT_TYPE_NOTIFY_WRITE ]
es_mute_path_events(client, "/dev/null", ES_MUTE_PATH_TYPE_TARGET_LITERAL,
                    &events, events.count)
```

### Mute inversion — [5:08]

```swift
// Invert muting for target paths
es_invert_muting(client, ES_MUTE_INVERSION_TYPE_TARGET_PATH)

// Select only events pertaining to /Library/LaunchDaemons
es_unmute_all_target_paths(client)
es_mute_path(client, "/Library/LaunchDaemons", ES_MUTE_PATH_TYPE_TARGET_PREFIX)
```

### Use eslogger to observe ssh login and logout events — [8:08]

```bash
sudo eslogger openssh_login openssh_logout >out.jsonl
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110345/4/D78059C0-3932-4CAA-8B45-098BEB4ACF45/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110345/4/D78059C0-3932-4CAA-8B45-098BEB4ACF45/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110345) — developer.apple.com. Indexed for agent consumption._