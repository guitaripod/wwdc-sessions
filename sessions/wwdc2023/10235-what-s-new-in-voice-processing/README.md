---
id: "wwdc2023-10235"
event: "wwdc2023"
year: 2023
title: "What’s new in voice processing"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10235"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# What’s new in voice processing

**Event:** WWDC23 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10235](https://developer.apple.com/videos/play/wwdc2023/10235)

Learn how to use the Apple voice processing APIs to achieve the best possible audio experience in your VoIP apps. We’ll show you how to detect when someone is talking while muted, adjust ducking behavior of other audio, and more.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,963 words)

## Code Snippets

### Other audio ducking — [5:50]

```swift
// Insert code snipp297struct AUVoiceIOOtherAudioDuckingConfiguration {
	Boolean mEnableAdvancedDucking;
	AUVoiceIOOtherAudioDuckingLevel  mDuckingLevel;
};et.
typedef CF_ENUM(UInt32, AUVoiceIOOtherAudioDuckingLevel) {
	kAUVoiceIOOtherAudioDuckingLevelDefault = 0,
	kAUVoiceIOOtherAudioDuckingLevelMin = 10,
	kAUVoiceIOOtherAudioDuckingLevelMid = 20,
	kAUVoiceIOOtherAudioDuckingLevelMax = 30
};
```

### Other audio ducking — [6:48]

```swift
const AUVoiceIOOtherAudioDuckingConfiguration duckingConfig = {
	.mEnableAdvancedDucking = true,
	.mDuckingLevel = AUVoiceIOOtherAudioDuckingLevel::kAUVoiceIOOtherAudioDuckingLevelMin
};
// AUVoiceIO creation code omitted
OSStatus err = AudioUnitSetProperty(auVoiceIO, kAUVoiceIOProperty_OtherAudioDuckingConfiguration, kAudioUnitScope_Global, 0, &duckingConfig, sizeof(duckingConfig));
```

### Other audio ducking — [6:50]

```swift
const AUVoiceIOOtherAudioDuckingConfiguration duckingConfig = {
	.mEnableAdvancedDucking = true,
	.mDuckingLevel = AUVoiceIOOtherAudioDuckingLevel::kAUVoiceIOOtherAudioDuckingLevelMin
};
// AUVoiceIO creation code omitted
OSStatus err = AudioUnitSetProperty(auVoiceIO, kAUVoiceIOProperty_OtherAudioDuckingConfiguration, kAudioUnitScope_Global, 0, &duckingConfig, sizeof(duckingConfig));
```

### Other audio ducking — [7:20]

```swift
public struct AVAudioVoiceProcessingOtherAudioDuckingConfiguration {
	public var enableAdvancedDucking: ObjCBool 
	public var duckingLevel: AVAudioVoiceProcessingOtherAudioDuckingConfiguration.Level
}
extension AVAudioVoiceProcessingOtherAudioDuckingConfiguration {
	public enum Level : Int, @unchecked Sendable {
		case `default` = 0
		case min = 10
		case mid = 20
		case max = 30
	}
}
```

### Other audio ducking — [7:31]

```swift
let engine = AVAudioEngine()
let inputNode = engine.inputNode
do {
	try inputNode.setVoiceProcessingEnabled(true)
} catch {
	print("Could not enable voice processing \(error)")
}
let duckingConfig = AVAudioVoiceProcessingOtherAudioDuckingConfiguration(mEnableAdvancedDucking: false, mDuckingLevel: .max)
inputNode.voiceProcessingOtherAudioDuckingConfiguration = duckingConfig
```

### Muted talker detection AUVoiceIO — [7:32]

```swift
AUVoiceIOMutedSpeechActivityEventListener listener =  ^(AUVoiceIOMutedSpeechActivityEvent event) {		
    if (event == kAUVoiceIOSpeechActivityHasStarted) {
		// User has started talking while muted. Prompt the user to un-mute
	} else if (event == kAUVoiceIOSpeechActivityHasEnded) {
		// User has stopped talking while muted
	}
};
OSStatus err = AudioUnitSetProperty(auVoiceIO, kAUVoiceIOProperty_MutedSpeechActivityEventListener, kAudioUnitScope_Global, 0, &listener,  sizeof(AUVoiceIOMutedSpeechActivityEventListener));
// When user mutes
UInt32 muteUplinkOutput = 1;
result = AudioUnitSetProperty(auVoiceIO, kAUVoiceIOProperty_MuteOutput, kAudioUnitScope_Global, 0, &muteUplinkOutput, sizeof(muteUplinkOutput));
```

### Muted talker detection AVAudioEngine — [11:08]

```swift
let listener =  { (event : AVAudioVoiceProcessingSpeechActivityEvent) in
	if (event == AVAudioVoiceProcessingSpeechActivityEvent.started) {
		// User has started talking while muted. Prompt the user to un-mute
	} else if (event == AVAudioVoiceProcessingSpeechActivityEvent.ended) {
		// User has stopped talking while muted
	}
}
inputNode.setMutedSpeechActivityEventListener(listener)
// When user mutes
inputNode.isVoiceProcessingInputMuted = true
```

### Voice activity detection - implementation with HAL APIs — [12:31]

```swift
// Enable Voice Activity Detection on the input device
const AudioObjectPropertyAddress kVoiceActivityDetectionEnable{
        kAudioDevicePropertyVoiceActivityDetectionEnable,
        kAudioDevicePropertyScopeInput,
        kAudioObjectPropertyElementMain };
OSStatus status = kAudioHardwareNoError;
UInt32 shouldEnable = 1;
status = AudioObjectSetPropertyData(deviceID, &kVoiceActivityDetectionEnable, 0, NULL, sizeof(UInt32), &shouldEnable);
// Register a listener on the Voice Activity Detection State property
const AudioObjectPropertyAddress kVoiceActivityDetectionState{
        kAudioDevicePropertyVoiceActivityDetectionState,
        kAudioDevicePropertyScopeInput,
        kAudioObjectPropertyElementMain };
status = AudioObjectAddPropertyListener(deviceID, &kVoiceActivityDetectionState, (AudioObjectPropertyListenerProc)listener_callback, NULL); // “listener_callback” is the name of your listener function
```

### Voice activity detection - listener_callback implementation — [13:13]

```swift
OSStatus listener_callback(
    AudioObjectID                 inObjectID,
    UInt32                        inNumberAddresses,
    const AudioObjectPropertyAddress*   __nullable inAddresses,
    void* __nullable              inClientData)
{
  // Assuming this is the only property we are listening for, therefore no need to go through inAddresses
       UInt32 voiceDetected = 0;
     UInt32 propertySize = sizeof(UInt32);
     OSStatus status = AudioObjectGetPropertyData(inObjectID, &kVoiceActivityState, 0, NULL, &propertySize, &voiceDetected);

       if (kAudioHardwareNoError == status) {
 if (voiceDetected == 1) {
    // voice activity detected
	} else if (voiceDetected == 0) {
		    // voice activity not detected
	}
 }
 return status;
};
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10235/4/78AFC6EE-45CE-4229-AB90-1DE57152E4BA/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10235/4/78AFC6EE-45CE-4229-AB90-1DE57152E4BA/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10235) — developer.apple.com. Indexed for agent consumption._
