---
id: "wwdc2020-10636"
event: "wwdc2020"
title: "What's new in streaming audio for Apple Watch"
url: "https://developer.apple.com/videos/play/wwdc2020/10636"
language: "eng"
words: 783
---

# What's new in streaming audio for Apple Watch — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2020/10636) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:03]** Hello and welcome to WWDC. My name is Suresh Koppisetty and I'm an engineer on the Streaming Media team. Today, I'm going to give you some updates on What's New in Streaming Audio on Apple Watch. Last year in watchOS 6, we introduced the ability to stream audio content directly on Apple Watch. As a developer, you could use Apple's very own AVPlayer or your own custom audio protocols for streaming audio content on Apple Watch. This year with watchOS 7, we are bringing the support for new audio codec in AVPLayer. Extended high efficiency advanced audio

**[0:51]** coding xHE-AAC gives us the ability to deliver equivalent quality at lower bitrate or you can choose to deliver higher quality at equivalent bitrate as compared to other codecs in AAC family. Now given that Watch has highly variable network conditions, we should aim to deliver high quality audio content with as low bitrate as possible. Hence, we recommend using xHE-AAC for encoding all your audio assets. Having said that for interoperability reasons, we also want you to include AAC-LC, HE-AAC

**[1:36]** or HE-AACv2 variants in the manifest and let the AVPlayer decide what's the best variant to play. That's all about new codecs on watchOS. In case you want to learn more, we have an amazing talk, Deliver a better HLS Audio Experience by my colleague Simon. OK great. Now you got streaming audio on Apple Watch working and you also have this new highly efficient codec to help you improve user experience, but there is still one thing missing. That's access to protected content. Developers have these vast, ever growing

**[2:22]** catalog of protected content that they would love to be able to deliver on Apple Watch. To support this, we are happy to bring FairPlay Streaming to watchOS 7. FairPlay Streaming was first introduced on iOS in 2015. It's a specification which describes the set of steps an app needs to follow in order to securely deliver content decryption keys so the platform could decrypt and playback encrypted media. While delivering FairPlay Streaming keys your app works as a liaison between the platform and your key server. AVContentKeySession is an AVFoundation class designed specifically for

**[3:09]** handling decryption keys. When the application receives an on demand key loading request from AVFoundation, it handles the various steps in key loading process and responds back to AVFoundation with an encrypted key response. With this, AVFoundation can start decryption and playback. Now watchOS 7, we are bringing support for AVContentKeySession for all your key handling needs. AVContentKeySession is not tied to lifecycle of an asset. This decouples key loading from media loading and playback. Hence, applications can have better control on the lifecycle of keys.

**[3:57]** AVContentKeySession allows applications to initiate key loading on their own at any point in time. This gives applications the ability to optimize key delivery and improve different aspects of playback experience. To know more about AVContentKeySession please refer to AVContentKeySession best practices doc. That's all about the new things and watchOS 7. Next, I would like to highlight some of the best practices specific to streaming on Apple Watch for improving the user experience even further. Streaming on watchOS is not the same as streaming on iOS. Watch is a

**[4:47]** low-power wearable device and due to its increased user mobility the network conditions on what are highly variable. This presents us with some interesting challenges for building streaming applications. With that in mind, we recommend avoiding unnecessary network round trips including HTTP redirects on any of the resources needed for playback. Any additional HTTP redirects would directly contribute to start up time. Pre-fetch resources like keys and certificates -- this will reduce the number of network requests during critical part of playback start. You could use the newly introduced AVContentKeySession for pre-fetching content keys.

**[5:36]** It also helps if you cache the certificate. You could use the expiry tag from HTTP responses to decide how long to cache. Since Watch is only dealing with audio-only content, we recommend using a higher target duration of around 20 seconds to be more resilient to network mobility and battery performance without having a drastic impact on playback startup time. To summarize, we have introduced a new audio codec that helps you deliver audio content more efficiently. We have added the ability to stream protected

**[6:23]** content on Watch with FairPlay Streaming. We also talked about some of the best practices specific to streaming on Apple Watch for improving streaming performance. I hope you use these new additions and tips to build amazing audio apps on Watch and bring normal audio content to our customers. If you need more information on best practices for building audio streaming apps on watchOS,
