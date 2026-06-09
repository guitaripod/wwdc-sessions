---
id: "wwdc2019-508"
event: "wwdc2019"
title: "Modernizing Your Audio App"
url: "https://developer.apple.com/videos/play/wwdc2019/508"
language: "eng"
words: 174
---

# Modernizing Your Audio App — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2019/508) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:07]** Hello, and welcome to our session about Modernizing Your Audio App. My name is Peter Vasil, and I'm a software engineer in the Core Audio Team. Let's start with audio units. Support for Carbon-Component-Based Audio Units will be removed in a future macOS release. We encourage hosts to use the AudioComponent API for audio unit discovery. With the next OS release, AudioHardwarePlugIn-based plugins are disabled by default. We recommend using the AudioServerPlugin API instead. For now, disabled plugins can be re-enabled in the Audio MIDI Setup utility, but support will

**[0:53]** be removed completely in a future macOS release. With the next OS release, we will introduce some deprecations. AUGraph, Inter-App Audio, and OpenAL will be deprecated. We encourage developers to switch over to AVAudioEngine, as replacement for AUGraph and OpenAL. For Inter-App Audio, please use Audio Unit Extensions instead. The 3D Mixer parameters have been unified across all platforms. For details, please refer to the AudioUnitParameters header file for a list of new and deprecated parameters. For more information, please visit the developer website.
