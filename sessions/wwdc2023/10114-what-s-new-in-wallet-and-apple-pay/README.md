---
id: "wwdc2023-10114"
event: "wwdc2023"
year: 2023
title: "What’s new in Wallet and Apple Pay"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10114"
topics: ["App Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in Wallet and Apple Pay

**Event:** WWDC23 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10114](https://developer.apple.com/videos/play/wwdc2023/10114)

Discover the latest updates to Wallet and Apple Pay. Learn how to take advantage of preauthorized payments, funds transfer, and Apple Pay Later merchandising to create great Apple Pay experiences in your app or for the web. Explore improved support for Mail, Messages, Safari, and third-party apps in Wallet Order Tracking, and find out how you can add more information to an order’s transaction or receipt details. And we’ll introduce you to Tap to Present ID on iPhone (or ID Verifier), a new way to accept IDs in Wallet using iPhone — no additional hardware needed.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,143 words)

## Documentation & Resources

- [Generating reader tokens for the Verifier API](https://developer.apple.com/documentation/ProximityReader/generating-reader-tokens-for-the-verifier-api) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ProximityReader/generating-reader-tokens-for-the-verifier-api
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ProximityReader/generating-reader-tokens-for-the-verifier-api.json
- [Checking IDs with the Verifier API](https://developer.apple.com/documentation/ProximityReader/checking-ids-with-the-verifier-api) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ProximityReader/checking-ids-with-the-verifier-api
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ProximityReader/checking-ids-with-the-verifier-api.json
- [Adopting the Verifier API in your iPhone app](https://developer.apple.com/documentation/ProximityReader/adopting-the-verifier-api-in-your-iphone-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ProximityReader/adopting-the-verifier-api-in-your-iphone-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ProximityReader/adopting-the-verifier-api-in-your-iphone-app.json

## Code Snippets

### Performing a display request to verify age — [28:51]

```swift
import ProximityReader

// Check the current device supports mobile document reading.
guard MobileDocumentReader.isSupported else { return }

let reader = MobileDocumentReader()

let readerSession: MobileDocumentReaderSession = try await reader.prepare()

let request = MobileDriversLicenseDisplayRequest(elements: [.ageAtLeast(21)])

try await readerSession.requestDocument(request)
```

### Displaying brand information during a document request — [30:55]

```swift
let reader = MobileDocumentReader()

let identifier = try await reader.configuration.readerInstanceIdentifier
let readerToken = try await WebService().fetchToken(for: identifier)

let readerSession = try await reader.prepare(using: .init(readerToken))

let request = MobileDriversLicenseDisplayRequest(elements: [.ageAtLeast(21)])

try await readerSession.requestDocument(request)
```

### Performing a data request — [31:50]

```swift
let session: MobileDocumentReaderSession = /* ... */

var request = MobileDriversLicenseDataRequest()
request.retainedElements = [.givenName, .familyName, .dateOfBirth, .portrait]
request.nonRetainedElements = [.address, .documentExpirationDate, .drivingPrivileges]

let response = try await session.requestDocument(request)

// Process document elements from document response.
self.processResponse(response.documentElements)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10114/5/208CF134-3A8A-417E-8DF3-0B8A1F60B130/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10114/5/208CF134-3A8A-417E-8DF3-0B8A1F60B130/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10114) — developer.apple.com. Indexed for agent consumption._
