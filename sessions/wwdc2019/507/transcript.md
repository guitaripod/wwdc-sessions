---
id: "wwdc2019-507"
event: "wwdc2019"
title: "HLS Authoring for AirPlay 2 Video"
url: "https://developer.apple.com/videos/play/wwdc2019/507"
language: "eng"
words: 961
---

# HLS Authoring for AirPlay 2 Video — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2019/507) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:06]** Hi, my name is Eryk Vershen. I'm an engineer on the HLS Streaming Team. Let's get started talking about HLS Authoring for AirPlay 2 Video. Ever since we introduced AirPlay on iOS users have enjoyed AirPlaying video to their Apple TVs and starting this year we're expanding that support dramatically with AirPlay built directly into TVs. Apple TV and AirPlay capable TVs both provide the highest quality video playback experience. You may remember that we have some specific requirements for content delivered to tvOS and Apple TV. These AirPlay capable TVs are a new class of devices so they have their own requirements.

**[0:53]** We have a simple agenda. I'll cover the new requirements and then I'll talk about changes we made to the validation tools to help you check for issues. We released a new version of the HLS authoring specification recently that talks about the additional requirements for AirPlay 2. Here is a condensed list. Don't worry about absorbing this list right now. I'll devote a whole slide to each line item. Let's look at the details. You need to synchronize the different variants. This makes switching easier. If these color bars represent different variants on a timeline, what we want to do is make them all line up nicely.

**[1:38]** We are recommending that you use at least millisecond precision and as always your video segments should start with IDR frames. You also want to avoid most changes of discontinuities. For example, do not switch between HEVC and H.264 or between AAC and Dolby Digital. These TVs aren't able to switch as seamlessly as iOS or Apple TV. You can change your frame rate but not arbitrarily. No switching between 25 frame per second and 30. You also want each codec to provide a good set of variance on its own. These TVs will stick with the codec they start with. So, in particular, don't try to

**[2:23]** use H.264 just for low resolution video and HEVC for high-resolution video. That works on other devices but not here. You should, of course, be using I-frame variance. They make fast-forward, rewind and seeking more effective. Because these devices don't want to switch codecs you need to have a set of I-frame variance matching the codec of the normal video. The encryption requirements listed here aren't really specific to AirPlay 2, but we wanted to call them out. The common encryption standard recommends 10% partial encryption. With FairPlay we are requiring it; other patterns will not work. For sample encryption there are two ways to market.

**[3:08]** The CMAF way with an senc box and the ISO base media file format way with a pair of saio and saiz boxes. We prefer the second form, but you can provide both. Lastly, some miscellaneous requirements. If you want to provide HDR content, your best bet is to provide multiple formats. For example, Dolby Vision and HDR 10 as TVs may support only one of the formats, use WebVTT for subtitles and we are now recommending MIME types for all your content. Let's go into little more detail about that. We've had a MIME type for HLS playlist for a long time. The MIME types we are suggesting for video and audio are what you

**[3:53]** might expect. Notice we are using text/plain for WebVTT even though the WebVTT spec says text/VTT. However, the text VTT type was not registered with the IANA and will be rejected by some clients. So use text/plain instead. Here's a list of some of the less common MIME types. Now the last 2 on this list are not applicable to AirPlay 2 content. I've listed them because we are recommending MIME types for all content not just AirPlay 2. Let's turn to how you can check your streams. Remember that there are two tools for HLS validation. These tools are complementary.

**[4:39]** Mediastreamvalidator is checking against the HLS specification. HLSreport on the other hand is checking against the authoring specification. You should always be using both tools. I suggest you make a script that runs them as a pair. We've made an important change to HLSreport. Formerly you had to run it multiple times with the dash os option if you wanted to check the rules for iOS and TVOS. Now it checks all rule sets by default including the rules for AirPlay 2. The rule set option is there to modify the sets you check but most of you won't need to use it. And while the OS option does still work, you should stop using it. Let's look at how the output

**[5:25]** from HLSreport has changed. Notice that the title line now shows all the rule sets that were checked. The rules portion is now grouped into sections for each rule set. Here we have the general requirements. There can be Must Fix and Should Fix subsections for each rule set. Now farther down in the output we have the iOS requirements. I want you to notice that rule 10 above here the last general rule is marked as Should Fix. Whereas here in the AirPlay 2 section the same rule is a Must Fix. If there are no rule violations for a section or subsection, then that section or subsection

**[6:10]** is dropped. For example, this stream has no Should F ixes for AirPlay 2. The main points to take away are we added new requirements for AirPlay 2 devices. Remember to use HLSreport so you check against the authoring specification. And HLSreport now checks all rule sets by default. This is session 507 so you know where to go for more info. We'll have links there to the authoring specification to the tools and to other information about HLS. Thanks for your attention. Have a great rest of the
