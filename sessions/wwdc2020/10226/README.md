---
id: "wwdc2020-10226"
event: "wwdc2020"
year: 2020
title: "Record stereo audio with AVAudioSession"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10226"
topics: ["Audio & Video"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Record stereo audio with AVAudioSession

**Event:** WWDC20 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10226](https://developer.apple.com/videos/play/wwdc2020/10226)

Stereo recording is a powerful way to deliver immersive sound to listeners, fans, and family — and your app can use the built-in microphones on iPhone or iPad to record it. Discover how AVAudioSession can help you capture stereo audio from a mobile device, address the new special consideration called “input orientation,” and learn how to adopt this API in your app to provide a better recording experience.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,613 words)

## Documentation & Resources

- [Capturing stereo audio from built-In microphones](https://developer.apple.com/documentation/AVFAudio/capturing-stereo-audio-from-built-in-microphones) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFAudio/capturing-stereo-audio-from-built-in-microphones
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFAudio/capturing-stereo-audio-from-built-in-microphones.json

## Code Snippets

### How to set up recording from the built-in mic — [6:57]

```swift
// How to set up recording from the built-in mic

private func enableBuiltInMic() {
    ...   
    // Find the built-in microphone.
    guard let availableInputs = session.availableInputs,
          let builtInMic = availableInputs.first(where: { $0.portType == .builtInMic }) 
    else {
        print("The device must have a built-in microphone.")
        return
    }  
    ...   
    do {
        try session.setPreferredInput(builtInMic)
        ...  
    } catch {
        ...
    }
}
```

### Configure stereo recording — [7:16]

```swift
// Configure stereo recording

func selectDataSource(...) {
    ...
    // Set the preferred polar pattern to stereo.
    try newDataSource.setPreferredPolarPattern(.stereo)

    // Set the preferred data source and polar pattern.
    try preferredInput.setPreferredDataSource(newDataSource)

    // Update the input orientation to match the current user interface orientation.
    try session.setPreferredInputOrientation(orientation.inputOrientation)
    ...
}
```

### When to select a data source & updated the stereo input orientation — [8:22]

```swift
// When to select a data source & updated the stereo input orientation

override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
    updateDataSource()
}

@IBAction func updateDataSourceSelection(_ sender: Any) {
    updateDataSource()
}

private func updateDataSource() {
    // Don't update the data source if the app is currently recording.
    guard controller.state != .recording else { return }

    let dataSourceName = dataSources[dataSourceChooser.selectedSegmentIndex]
    controller.selectDataSource( named: dataSourceName,    
        orientation:Orientation(windowOrientation)) { layout in
        self.layoutView.layout = layout
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10226/5/C8C3C21B-7FB6-4655-A9C9-7879416D0435/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10226) — developer.apple.com. Indexed for agent consumption._