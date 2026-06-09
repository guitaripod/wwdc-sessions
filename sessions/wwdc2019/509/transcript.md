---
id: "wwdc2019-509"
event: "wwdc2019"
title: "AUv3 Extensions User Presets"
url: "https://developer.apple.com/videos/play/wwdc2019/509"
language: "eng"
words: 775
---

# AUv3 Extensions User Presets — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2019/509) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:07]** Hello everyone, and welcome to our session about user preset support for audio units. My name is Bela Balazs, and I'm an engineer on the Core Audio software team. Today we would like to talk about a some of our new APIs regarding the handling of audio unit presets. First, let's start with this. What are presets and why are they useful? In an audio software context, a preset is a snapshot of the state of the audio unit's parameters at a given time. This snapshot can be saved and later restored. We already support factory presets. It's a property on the AU audio unit class and it's defined as an array of AU audio unit presets. These factory presets are built

**[0:54]** into the audio unit by the audio unit manufacturer. An audio unit developer might include a fixed number of presets with the product as a starting point or to showcase the capabilities of the audio unit. Now we are adding support for user presets. These can be accessed by using this new user presets property which returns an array of AU audio unit presets. These are presets that are created by the user and can be modified later on. The audio unit exposes them to all audio unit host applications. We have a new property called support user presets. The audio unit sets this to true to signal support. The audio unit host application

**[1:39]** has to check it before using the new functionality. This is the way to opt in to use the new features. We have methods to save and delete user presets. The audio unit host application can call the save user preset method to save the current state into a preset, or it can call the delete user preset method to delete an existing preset. The audio unit can override these to implement custom logic, or it can use the default implementations inherited from the AU audio unit base class. These default implementations store the presets in the application container folder of the audio unit extension. You can use the preset state for user preset method to retrieve the state stored in the user

**[2:25]** preset. This also has a default implementation that's superclass, but it can be overridden to suit custom needs. It returns a dictionary that you can use to restore the state of the audio unit by simply assigning it to the full state for document property of the audio unit. In addition to these, we've added a new property called isLoadedInProcess that you can use to check whether the audio unit is loaded-in process. Loading in process is a macOS only feature. The host can request it but if the audio unit is not packaged to support it, the fallback behavior is to load the audio unit out of process. Now, the host or the audio unit can use this property to verify

**[3:11]** that this operation succeeded. And now let's see it in action. So, here I have the updated AUV free host sample code, which is available both on macOS and on iOS. In this host application, I have loaded the AUV free filter demo. When I press play, we can hear the filter in action. I can drag this graph to set the cutoff and the resonance of the filter. And here I have my preset section on the right side. We have our factory presets, which came with the audio unit. We have warm, bright, and prominent.

**[3:57]** And in the other tab, we have the user preset section. Here we have my previously saved initial preset and I can save new ones. And I can switch between them. Once I no longer need one of the presets, I can simply delete it. And this is the entire functionality of the AUV free host. I encourage everyone to check it out. To summarize, we've added support for user presets for audio units to complement the functionality already provided

**[4:43]** by factory presets. These allow the user to save their favorite sounds into presets and access them in each and every audio unit host application. To take advantage of these new features, the audio unit can simply opt in and use the default implementations that we provide, or it can override the methods to implement custom functionality. The audio unit host application can query the audio unit for these presets and can create new presets or delete the existing ones by calling the right methods on the audio unit. For more information, you can check out our newly updated sample code and the resources attached to this session, which is available at developer.apple.com. That concludes our presentation.
