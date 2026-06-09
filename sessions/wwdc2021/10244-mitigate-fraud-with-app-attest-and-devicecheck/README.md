---
id: "wwdc2021-10244"
event: "wwdc2021"
year: 2021
title: "Mitigate fraud with App Attest and DeviceCheck"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10244"
topics: ["Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Mitigate fraud with App Attest and DeviceCheck

**Event:** WWDC21 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10244](https://developer.apple.com/videos/play/wwdc2021/10244)

Discover how to use App Attest and DeviceCheck, Apple’s powerful anti-fraud tools, created to safeguard your apps and content. Unlock the secrets of deploying App Attest by incorporating it into your app to block unauthorized modifications of your app and content. We'll also show you how to use DeviceCheck to ensure you can distinguish between customers who have received premium content in your app, and those who have attained it through illegitimate means.

**Keywords:** `abuse`, `aggregator`, `appattest`, `app clip`, `artificial`, `assertion`, `boost`, `cheat`, `compromised`, `devicecheck`, `fake`, `fraud`, `free trial`, `genuine`, `islikelyrealuser`, `legitimate`, `modified`, `premium content`, `promotion`, `protect`, `receipt verification`, `risk assessment`, `safeguard`, `safety`, `scraping`, `secure`, `sign in with apple`, `trust`, `trust &amp; safety`, `verified`, `verify`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,248 words)

## Documentation & Resources

- [Establishing your app’s integrity](https://developer.apple.com/documentation/DeviceCheck/establishing-your-app-s-integrity) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/DeviceCheck/establishing-your-app-s-integrity
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/DeviceCheck/establishing-your-app-s-integrity.json
- [Assessing fraud risk](https://developer.apple.com/documentation/DeviceCheck/assessing-fraud-risk) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/DeviceCheck/assessing-fraud-risk
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/DeviceCheck/assessing-fraud-risk.json
- [Validating apps that connect to your server](https://developer.apple.com/documentation/DeviceCheck/validating-apps-that-connect-to-your-server) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/DeviceCheck/validating-apps-that-connect-to-your-server
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/DeviceCheck/validating-apps-that-connect-to-your-server.json
- [Accessing and modifying per-device data](https://developer.apple.com/documentation/DeviceCheck/accessing-and-modifying-per-device-data) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/DeviceCheck/accessing-and-modifying-per-device-data
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/DeviceCheck/accessing-and-modifying-per-device-data.json

## Code Snippets

### Create an App Attest key — [8:02]

```swift
let appAttestService = DCAppAttestService.shared

if appAttestService.isSupported {
    appAttestService.generateKey { keyId, error in
        guard error == nil else { /* Handle the error. */ }
        // Cache keyId for subsequent operations.
    }
} else {
   // Handle fallback as untrusted device
}
```

### Generate key attestation — [9:34]

```swift
appAttestService.attestKey(keyId, clientDataHash: clientDataHash) { attestationObject, error in
    guard error == nil else { /* Handle error. */ }

    // Send the attestation object to your server for verification.
}
```

### Generate assertion — [13:14]

```swift
appAttestService.generateAssertion(keyId, clientDataHash: clientDataHash) { assertionObject, error in
    guard error == nil else { /* Handle error. */ }

    // Send assertion object with your data to your server for verification
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10244/5/5C0B3E9F-163D-4DCB-AC48-F92DBE33E112/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10244/5/5C0B3E9F-163D-4DCB-AC48-F92DBE33E112/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10244) — developer.apple.com. Indexed for agent consumption._
