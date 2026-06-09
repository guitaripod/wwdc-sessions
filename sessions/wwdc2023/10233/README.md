---
id: "wwdc2023-10233"
event: "wwdc2023"
year: 2023
title: "Enhance your app’s audio experience with AirPods"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10233"
topics: ["Spatial Computing", "Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Enhance your app’s audio experience with AirPods

**Event:** WWDC23 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10233](https://developer.apple.com/videos/play/wwdc2023/10233)

Discover how you can create transformative audio experiences in your app using AirPods. Learn how to incorporate AirPods Automatic Switching, use AVAudioApplication to support Mute Control, and take advantage of Spatial Audio to create immersive soundscapes in your app or game.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,708 words)

## Code Snippets

### Press to Mute and Unmute API — [8:25]

```swift
// Adopting AVAudioApplication into your App
import AVFAudio

// Get the started instance 
let instance = AVAudioApplication.shared

// Register for mute gesture notifications on Notification Center 
AVAudioApplication.inputMuteStateChangeNotification

// Key for mute state
AVAudioApplication.muteStateKey

// Updating AVAudioApplication’s mute state
instance.setInputMuted(...)

// Reading AVAudioApplication’s mute state
instance.isInputMuted
```

### Configure the Input Mute State Change handler (macOS only) — [10:52]

```swift
// Configure the Input Mute State Change handler (macOS only)
instance.setInputMuteStateChangeHandler { isMuted in
	//...
	return didSucceed
}

// Optional: let CoreAudio mute your input for you (macOS only)
// Define the Core Audio property
var inputeMutePropertyAddress = AudioObjectPropertyAddress(
	mSelector: kAudioHardwarePropertyProcessInputMute,
	mScope: kAudioObjectPropertyScopeInput,
	mElement:kAudioObjectPropertyElementMain)

// Enable this property when you want to mute your input
UInt32 isMuted = 1; // 1 = muted, 0 = unmuted
AudioObjectSetPropertyData(kAudioObjectSystemObject,
						   &inputeMutePropertyAddress,
						   0,
						   nil,
						   UInt32(MemoryLayout.size(ofValue: isMuted),
						   &isMuted)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10233/4/67656F5A-221D-451B-9BD0-45BCA4922204/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10233/4/67656F5A-221D-451B-9BD0-45BCA4922204/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10233) — developer.apple.com. Indexed for agent consumption._