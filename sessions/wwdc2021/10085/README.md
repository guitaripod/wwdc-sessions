---
id: "wwdc2021-10085"
event: "wwdc2021"
year: 2021
title: "Apple’s privacy pillars in focus"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10085"
topics: ["Essentials", "Privacy & Security"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Apple’s privacy pillars in focus

**Event:** WWDC21 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10085](https://developer.apple.com/videos/play/wwdc2021/10085)

At Apple, we believe that privacy is a fundamental human right. Learn about our four pillars of privacy, how we brought these principles together to design iCloud Private Relay, and how you can approach building privacy in your app in line with those fundamentals. Explore how you can build data minimization, on-device processing, transparency and control, and security protections right into your app.

**Keywords:** `app privacy report`, `app tracking transparency`, `apptrackingtransparency.framework`, `att`, `createml framework`, `focus`, `hide my email`, `location button`, `private relay`, `siri`, `skadnetwork`, `tracking`, `transparency`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,060 words)

## Documentation & Resources

- [App Store Guidelines: User Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/app-store/user-privacy-and-data-use/
- [Human Interface Guidelines: Accessing User Data](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/ios/app-architecture/accessing-user-data/
- [Introducing Private Click Measurement, PCM](https://webkit.org/blog/11529/introducing-private-click-measurement-pcm/) _documentation_

## Code Snippets

### Encrypt/decrypt data with CKModifyRecordsOperation — [23:59]

```swift
// Device 1: Encrypt data before calling CKModifyRecordsOperation.

myRecord.encryptedValues["encryptedStringField"] = "Sensitive value"


// Device 2: Decrypt data after calling CKFetchRecordsOperation.

let decryptedString = myRecord.encryptedValues["encryptedStringField"] as? String
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10085/7/588BAC34-15EB-4FCE-AF4F-5934A7DD4024/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10085/7/588BAC34-15EB-4FCE-AF4F-5934A7DD4024/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10085) — developer.apple.com. Indexed for agent consumption._