---
id: "wwdc2020-10209"
event: "wwdc2020"
title: "What's new in Core NFC"
url: "https://developer.apple.com/videos/play/wwdc2020/10209"
language: "eng"
words: 652
---

# What's new in Core NFC — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2020/10209) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:03]** Hello and welcome to WWDC. Hi, my name is Lawrence and I work on NFC software here at Apple. Today we will go over the changes in our existing APIs. These changes follow some of the new published Swift guidelines. We have also expanded our APIs for the ISO15693 tag used in NFCTagReaderSession. First, let's start with an overview of Core NFC. You may recall our creative salmon from our last year WWDC presentation. By the way, his name is Kevin. Today I have brought Kevin with me and here is the coupon tag.

**[0:53]** Core NFC allows your app to read this NFC tag using an iPhone. NFC is also used in other places, such as on parking meters, scooter rental, electric car charging station, ordering menu in restaurant, et cetera. Core NFC allows an app to read an NFC tag in a session lasting up to 60 seconds. This has been supported on iPhones since the iPhone 7. Beginning on the iPhone XS, tags can also be read in the background while the screen is on, if the NFC forum NDEF message contains a universal link.

**[1:38]** Once the user has tapped on the notification banner shown on screen that NDEF message will be sent to your application as an NSUserActivity via UIApplicationDelegate restorationHandler. Texts may contain a NFC forum NDEF message or other proprietary data set. Core NFC supports NDEF reading and writing as well as other native tag protocols. The easiest path for tag access is to use the NFCNDEFReaderSession. Core NFC supports NDEF reading and writing as well as other native tag protocols. The easiest path for tag access is to use the NFCNDEFReaderSession.

**[2:27]** But Core NFC also supports raw tag communication via ISO7816, FeliCa, MIFARE and ISO15693. Next, let's talk about some changes to the Swift syntax to make it easier to understand your Core NFC code. Core NFC now adopts the use of the Result enum in our tag APIs, specifically how parameters are returned in our completion handler. Let's look at the ISO7816-tag-send-command as an example. Before iOS 14, the method signature accepts a closure with four arguments as the completion handler.

**[3:12]** Your application will need to check the optional error object to determine if an error occurs. If the operation succeeds, you may then parse the rest of arguments to collect the results. The new signature in iOS 14 returns a Result enum of either a NFCISO7816-Response-APDU object on success, which is the result of reading the tag, or an error object on a failure. The Result enum can be easily handled using a switch statement as shown. Now let me show you how it looks in Xcode. I've opened the NFCFishTag sample project from WWDC 2019. Here, in CouponViewController,

**[3:57]** the write function is shown in its existing form. Let's replace the send-MIFARE-command using its new Result signature. Here, in the new code, the data object is handled in this section of a switch statement. An error is handled over here. We have also made a few changes to the existing enum values to improve readability. For example, the ResolveFlag enum has been changed to refer specifically to ISO15693. Some other new enums have been added as well. Please refer to the documentation for more details. Now we will talk about new capabilities we've added to the NFC-ISO15693 tag protocol.

**[4:47]** We have added the enhancement defined by the ISO15693 specification third edition 2019. These functions are useful for tags with larger memory sizes and security operations. We have also included a new generic send command if you would like to send arbitrary data packets for your application. Here is a complete list of the enhancement function signatures under the NFC-ISO15693Tag protocol. We now support the following operations: fast reading multiple blocks, extended write multiple blocks, authenticate, key update, challenge, read buffer, extended get multiple blocks security status,

**[5:33]** extended fast read multiple blocks and send request.
