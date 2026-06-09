---
id: "wwdc2026-201"
event: "wwdc2026"
year: 2026
title: "Secure your apps with App Attest"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/201"
topics: ["App Services", "App Store, Distribution & Marketing", "Business & Education", "Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Secure your apps with App Attest

**Event:** WWDC26 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-201](https://developer.apple.com/videos/play/wwdc2026/201)

Harness App Attest to protect your app from unauthorized modification and fraud. Uncover how attackers exploit modified apps to spoof data and bypass security checks, and how App Attest defends against these threats. Learn to generate and manage App Attest keys bound to the Secure Enclave, validate attestations and assertions, and use the fraud metric to detect abuse. Discover best practices across all Apple platforms, including new signals in iOS 27 to strengthen your validation.

**Keywords:** `🎈`, `fraud`, `mitigate`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,960 words)

## Documentation & Resources

- [W3C Authenticator Data](https://www.w3.org/TR/webauthn-3/#sctn-authenticator-data) _documentation_
- [About System Integrity Protection on your Mac](https://support.apple.com/en-us/102149) _documentation_
- [DeviceCheck](https://developer.apple.com/documentation/DeviceCheck) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/DeviceCheck
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/DeviceCheck.json

## Code Snippets

### Generate a Secure Enclave–bound key — [5:07]

```swift
import DeviceCheck

let keyID = try await DCAppAttestService.shared.generateKey()
```

### Attestation API — [6:32]

```swift
import DeviceCheck

let keyId: String = ...
let clientDataHash: Data = ...
let attestation = try await DCAppAttestService.shared.attestKey(keyId: keyId, clientDataHash: clientDataHash)
```

### Assertion API — [12:33]

```swift
import DeviceCheck

let keyId: String = ...
let clientDataHash: Data = ...
let assertion = try await DCAppAttestService.shared.generateAssertion(keyId: String, clientDataHash: Data)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/201/4/d3eb2e5b-5104-4aee-a754-9985008a5b06/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/201/4/d3eb2e5b-5104-4aee-a754-9985008a5b06/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/201) — developer.apple.com. Indexed for agent consumption._