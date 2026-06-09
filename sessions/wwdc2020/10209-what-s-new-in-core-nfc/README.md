---
id: "wwdc2020-10209"
event: "wwdc2020"
year: 2020
title: "What's new in Core NFC"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10209"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# What's new in Core NFC

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10209](https://developer.apple.com/videos/play/wwdc2020/10209)

Core NFC helps you scan and write to NFC tags in your apps, helping people get more from objects like parking meters, scooter rentals, car charging stations, and more. Learn about Core NFC’s support for the ISO15693 protocol and new tag capabilities, and find out more about syntax improvements for Swift.

**Keywords:** `nfc`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(652 words)

## Documentation & Resources

- [Creating NFC Tags from Your iPhone](https://developer.apple.com/documentation/CoreNFC/creating-nfc-tags-from-your-iphone) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreNFC/creating-nfc-tags-from-your-iphone
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreNFC/creating-nfc-tags-from-your-iphone.json

## Code Snippets

### sendCommand — [3:24]

```swift
detectedTag.sendCommand(apdu: apdu) { (result: Result<NFCISO7816ResponseAPDU, Error>) in
   switch result {
   case .success(let responseAPDU):
      /// Handle NFCISO7816ResponseAPDU object.
   case .failure(let error):
      /// Handle Error object.
   }
}
```

### sendMiFareCommand — [4:06]

```swift
// You need to zero-pad the data to fill the block size
if blockData.count < blockSize {
  blockData += Data(count: blockSize - blockData.count)
}

let writeCommand = Data([writeBlockCommand, offset]) + blockData
tag.sendMiFareCommand(commandPacket: writeCommand) { (response: Result<Data, Error>) in
  switch (response) {
  case .success(let responseData):
    if responseData[0] != successCode {
      self.readerSession?.invalidate(errorMessage: "Write tag error. Please try again.")
      return
    }

    let newSize = data.count - blockSize
    if newSize > 0 {
      self.write(data.suffix(newSize), to: tag, offset: (offset + 1))
    } else {
      self.readerSession?.invalidate()
    }
  case .failure(let error):
    let message = "Write tag error: \(error.localizedDescription). Please try again."
    self.readerSession?.invalidate(errorMessage: message)
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10209/4/A0EF8CFC-5168-44DA-9F88-3ECE05F82ACE/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10209) — developer.apple.com. Indexed for agent consumption._
