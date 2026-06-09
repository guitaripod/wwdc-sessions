---
id: "wwdc2020-10074"
event: "wwdc2020"
title: "Decipher and deal with common Siri errors"
url: "https://developer.apple.com/videos/play/wwdc2020/10074"
language: "eng"
words: 321
---

# Decipher and deal with common Siri errors — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2020/10074) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:03]** Hello and welcome to WWDC. My name is Roman, and I'm a Shortcuts engineer at Apple. Today, I'm going to share some tips on how to efficiently debug your Siri and Shortcuts support. Let's start by taking a look at how you can automate Siri queries using the scheme editor in Xcode. You can provide the Siri intent query from the get-go, so you don't actually have to trigger Siri and speak to it when you debug your extension. When you're attaching to your Intents extension, you have an option to choose between Siri and the Shortcuts app as the host process. Sometimes you might wonder why you don't hit breakpoints in your Intents UI extension while you're being attached to an Intents extension in Xcode.

**[0:48]** This is because both of these extensions are separate processes. You can use the Xcode debug menu to attach to multiple processes at the same time. So, you implemented SiriKit support in your app but you're getting, "Sorry there was a problem with the app" when you execute your intent in Siri. Now what can you do about this? First, make sure that you call your completion handlers of your intent handling protocol methods before the 10-second time-out. You also need to make sure that you call the completion handlers only once, otherwise an exception will be thrown in your process. You should also verify that your process is not crashing in the middle of the request. Open Devices and Simulators in Xcode and click the "View Device Logs" button

**[1:33]** and scan it for crashes in your processes. Using os_log statements and the Console.app can help you understand how multiple processes work together. When composing your os_log statements you can prefix them with an emoji or some other unique keyword and then use the Console.app to filter by your unique keyword to get an accurate timeline of events in all processes involved. Thanks for watching.
