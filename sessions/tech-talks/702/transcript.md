---
id: "tech-talks-702"
event: "tech-talks"
title: "What's New in Core NFC"
url: "https://developer.apple.com/videos/play/tech-talks/702"
language: "eng"
words: 774
---

# What's New in Core NFC — Transcript

[Session page](https://developer.apple.com/videos/play/tech-talks/702) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:01]** Hi, I am Lawrence from the NFC team. Welcome to this Core NFC update. We have got a new feature for Core NFC this year that will not only enhance the NFC experience, but also greatly simplify the process of handling NFC tags within your applications. If you are new to Core NFC, I recommend that you watch the "Introduction to Core NFC" video released last year. With the new background tag reading feature, the iPhone is able to automatically read NFC tags and deliver them to the appropriate apps. The mechanism is able to perform the necessary app launch or bringing the application to the foreground state. We are excited to see how this can make the user experience even better

**[0:47]** and make it easier for apps to handle NFC tags. In this video, I will discuss the NFC tag data requirements, the expected user experience, when background tag reading is supported, and some example code snippets to get you started. Background tag reading will work with any NDEF formatted tag whose NDEF message includes a URL record. Only the first discovered URL record in the NDEF message will be processed. The URL record must contain a valid Apple Universal Link URL in order for the message to be routed to an application. iOS will route the message to the application registered with the Apple Universal Link. While the screen is on,

**[1:32]** background tag reading will scan for nearby NFC tags. Once a compatible tag is successfully read, a pop-up from the Notification Center will appear on the iPhone screen. Tapping on the notification will trigger the delivery of a NSUserActivity object to the associated application using the Apple Universal Link mechanisms. By default, Safari will handle all unregistered application links and it will only process the URL payload. There are also other URL schemes that trigger a default iOS behavior, which I will discuss later on. Any unprocessed notification will be saved in the Notification Center for future reference. Here is what happens when the user taps an NFC tag.

**[2:19]** A notification will be shown, and tapping on the notification will launch the registered application. Once the application is running, tapping on the NFC tag again will trigger a new notification. When a tag is read in the locked state, the user will be prompted to first unlock the phone before the tag data can be processed. Background tag reading is supported on iPhone XS, iPhone XS Max, and iPhone XR.

**[3:07]** The phone must first be unlocked at least once after boot up for background tag reading to be operational. After first unlock, the device will scan for NFC tags in the background whenever the display is on regardless of the lock state, except for the following conditions: a Core NFC reader session is in progress, Wallet or Apple Pay are in use, cameras are in use, or the device is in Airplane Mode. Now let us walk through the required implementation steps in your application to receive the content of the NFC tag. This is broken down into three main steps. You will need to register the associated domains for your application as per the Universal Link requirements. Then you will need to adopt the UIApplicationDelegate protocol,

**[3:55]** application(_:continue: restorationHandler:) function. Finally, you will need to extract the NDEF message from the ndefMessagePayload property of the NSUserActivity object. To register your domain in your app, open your project in Xcode and enter the server host domain in the Associated Domains section. Here is a code snippet illustrating how to receive a NSUserActivity object in your UIKit application. First, import the Core NFC framework. Implement the UIApplicationDelegate protocol method, application (_:continue: restorationHandler:). Validate the activity type is NSUserActivityTypeBrowsingWeb

**[4:43]** in the handler. Read the NFCNDEFMessage from the ndefMessagePayload property. This contains the entire NDEF message read from the NFC tag. The message contains an array of NFC NDEF payload records. Each NDEF record contains the typeNameFormat, the Type, the Identifier, and the data payload. One of the NFC NDEF payload will contain the URL record with the Universal Link that triggered the launch of your application. Please refer to the NFC Forum specifications regarding the various record type definitions. If the received NSUserActivity object

**[5:29]** did not originate from the background tag reading, then the resulting NFCNDEFMessage will contain exactly one NFC NDEF payload object with its typeNameFormat property set to NFCTypeNameFormatEmpty. If the URL record does not contain a Universal Link, iOS can still handle many of the same URI schemes as the QR code scanner such as HomeKit, SMS, GPS, and others. Here is an example of some of the various supported schemes.
