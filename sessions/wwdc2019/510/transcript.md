---
id: "wwdc2019-510"
event: "wwdc2019"
title: "What's New in AVAudioEngine"
url: "https://developer.apple.com/videos/play/wwdc2019/510"
language: "eng"
words: 1052
---

# What's New in AVAudioEngine — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2019/510) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:07]** Hello, and welcome to our session about audio API updates. My name is Peter Vasil, and I am a software engineer in the Core Audio team. Let's start with what's new in AVAudioEngine. We have added a couple of enhancements and new APIs to AVAudioEngine. We now have a voice processing support. We have added two new nodes, AVAudioSourceNode and AVAudioSinkNode, and we have made some improvements to spatial audio rendering. Now, let's dive into the details. AVAudioEngine now has a voice processing mode. The main use case for the mode is echo cancellation and

**[0:53]** voice-over IP applications. What does this mean? When enabled, extra signal processing is applied on the incoming audio, and any audio that is coming from the device is taken out. This requires that both input and output nodes are in the voice processing mode. Therefore, when enabling the mode on either of the I/O nodes, the engine takes care that both I/O nodes exist and that they are switched to the voice processing mode. Voice processing is only available when rendering to an audio device, not a manual rendering mode. To enable or disable voice processing, we can use set voice

**[1:38]** processing enabled on either the input or output node. Voice processing cannot be enabled dynamically, which means the engine needs to be in a stop state when enabling the mode. The AV Echo Touch Sample Code project demonstrates how to use voice processing with AVAudioEngine in detail. Let's look at the new nodes in AVAudioEngine, AVAudioSourceNode and AVAudioSinkNode. Both nodes wrap a user-defined blog that allows apps to send or receive audio from AVAudioEngine. When rendering to an audio device, the block operates under real-time constraints, which means that within the block there shouldn't be any blocking

**[2:24]** calls like memory allocations, call to lib dispatch, or blocking on a mutex. With AVAudioSourceNode, we pass or render block to the node, which sends audio data to its output. This makes it very easy to create generated nodes without having to implement a full audio unit and wrap it with AVAudio unit. The node can be used in both real time and manual rendering mode. AVAudioSourceNode support linear PCM conversions such as sample rate or bit depth conversions and has one output but no input.

**[3:09]** This short code snippet shows how to use AVAudioSourceNode. As we can see, the block is passed as an initializer argument, and after creating the node, it can be connected just like any other node. A more detailed example can be found in our Signal Generator Sample Code project. Let's look at AVAudioSinkNode. AVAudioSinkNode is a symmetrical counterpart of AVAudioSourceNode. It wraps a user-defined block that receives the input audio from the node chain that is connected to its input. AVAudioSinkNode is restricted to the input chain. In other words, it must be connected downstream of the

**[3:54]** input node. It does not support format conversions, and the format within the block has to be the same as the hardware input format. The node can be useful for voice-over IP application when the input needs to be processed in real time, in which case installing a regular tap would not be sufficient because the tap doesn't operate in a real-time context. Here is a code snippet demonstrating how to create an AVAudioSinkNode. It is quite similar to AVAudioSourceNode. The main steps to note here are to initialize the node with a blog, attach it to the engine, and connect it to a node downstream of the input node.

**[4:42]** Now let's see the spatial rendering improvements. We have introduced an automatic spatial rendering algorithm, and AVAudioPlayerNode now supports spatialization of multichannel audio content. With the automatic spatial rendering algorithm, the most appropriate spatialization algorithm is selected for the current route. This means developers don't need to figure out what algorithms are suitable for headphones or different speaker configurations. This adds near-field and in-head rendering for headphones and virtual surround for built-in speakers is available starting with iOS devices and laptops from 2018 and newer.

**[5:32]** Here we see the new API in the AVAudio3DMixing protocol. The AVAudio3DMixing rendering algorithm enum has a new entry, auto. Additionally, we can specify the output type with the output type property. With the property set to auto, the output type can be automatically detected in real-time mode but not in manual rendering mode. With the ability to spatialize multichannel streams, we support point-source and ambience bed rendering. We also support channel-based formats and higher-order Ambisonics up to the third order.

**[6:19]** We have added two new spatialization properties to the AVAudio3DMixing protocol, source mode and pointSource and head mode. SpatializeIfMono is legacy behavior. This is the same as bypass for any multichannel stream, which means a pass through or downmix to the output format. With pointSource, the audio is sum to mono and render at the location of the player node. And with ambienceBed, the audio is anchored to the 3D world and is rotatable with the player node's position relative to the listener orientation. Here we see an example of ambienceBed source mode with automatic rendering algorithm.

**[7:05]** After setting the properties, it is important to make sure the format that is used for the connection between player node and the environment node contains the multichannel layout. Now let's talk about what's new in AVAudioSession. AVAudioSessionPromptStyle is a hint to apps that play voice prompts in order to modify the style of the played prompt. For example, if Siri is speaking or a phone call is ongoing, verbal navigation prompts is a confusing user experience. We also don't want Siri to record a navigation prompt. Navigation apps, for example, are encouraged to pay attention

**[7:51]** to prompt style changes and modify the prompts for better user experience. We have three prompt styles, none, short, and normal. We can now indicate to disable prompts completely, play shortened prompts, or play the regular prompts. Let's look at other AVAudioSession enhancements. The default policy is to mute haptics and system sounds when audio recording is active. A new property, allow haptics and system sounds during recording, allows system sounds and haptics to play while the session is actively using an audio input. It can be set using the setter set allow haptics and system sounds during recording.

**[8:37]** For more information, please visit the developer website.
