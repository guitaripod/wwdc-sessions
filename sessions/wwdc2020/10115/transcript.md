---
id: "wwdc2020-10115"
event: "wwdc2020"
title: "AutoFill everywhere"
url: "https://developer.apple.com/videos/play/wwdc2020/10115"
language: "eng"
words: 1127
---

# AutoFill everywhere — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2020/10115) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:03]** Hello and welcome to WWDC. Hello, everyone. My name's Zeheng Chen, and I'm a keyboard engineer. Today I'm going to talk about AutoFill. I'm going to share some tips about how you can help your users complete some everyday tasks in your app. I'm going to talk about AutoFilling recent addresses, contact information, as well as passwords and security codes. If your app requires a log in or a new account setup, I will also talk about some best practices for that. Now let me start with an example of how AutoFill can use recent addresses.

**[0:49]** If you are building a navigation app, there maybe a text field expecting an address. As soon as the user taps that text field, iOS will intelligently suggest an appropriate location. For example, you just checked out a restaurant and now the keyboard will suggest a restaurant address right in the in QuickType bar. So, your user is only one tap away from inputting the address. If you are interested in promoting locations from your app to the system, you can watch the WWDC 2016 session "Increase Usage of Your App with Proactive Suggestions."

**[1:39]** Another example: You have a Calendar event coming up and now the keyboard will suggest event location. Or maybe you want to go home, and the keyboard will suggest your home address. Now you may be wondering: How do I do this in my app? Well, the good news is it's easy. Let me show you. You can adopt this in code. You just need to annotate your text field with the UITextContentType API, which provides the semantic meaning of these text fields to iOS. Here we are setting the Content Type to fullStreetAddress,

**[2:25]** which is all you need to get recent address AutoFill from the previous example. It's that simple. You can also set the Content Type for a UITextView or a UITextField directly in the Xcode Attributes inspector. One thing to pay attention to is the expected semantic meaning for each text field should be identified as precisely as possible. You can't combine multiple values for one Text Content Type property. So think about your specific use case and find the appropriate one. For example:

**[3:11]** for a navigation app, a full street address might be the right granularity, but for a weather app, a city address is likely enough. I want to pause here and take a moment to talk about privacy. At Apple, it's one of our core values. Our devices are essential to so many parts of our lives. What we share and who we share with should be entirely up to us. We design our products to protect our users' privacy and give them control over their information. It's not always easy. Sometimes building a great experience

**[3:58]** might need some level of access to personal information. Let's take a look at an example. Here I'm building a payment app that allows users to send money to their friends. How can I help my users find their intended recipient quickly? Should I bring up a Contact Picker and let them choose, or should I suggest Contacts as they type? Either way, I probably need to request access to their Contacts, right? But is asking for Contact access a good idea?

**[4:45]** If I ask for their Contacts, users will be prompted to allow access. This is not only going to interrupt their flow, they might not even feel comfortable sharing their Contacts. Besides, even if they do choose to share their Contacts with my app, my app now has a greater risk for potential privacy exposure because I have access to their personal information. A better approach is to use the Contact Picker API. By using this API, the app does not need access to Contacts and users will not be prompted to grant permission.

**[5:33]** There's no prompt because the app only has access to the specific information that the user chooses to share with the app. In iOS 14, we are now suggesting Contact information in the QuickType keyboard while the user types. Just like the previous example, the app has no access to Contacts and so there will be no prompt here either. Nothing is shared with the app until the user taps the QuickType bar and inserts the text. So, how do we accomplish this?

**[6:18]** The adoption of this new Contact AutoFill feature may look familiar to you. Similar to recent address AutoFill, you just set the Content Type to email or telephone number to get Contact AutoFill in your app. To reiterate, if your app requires access to users' Contacts, try to use these two solutions first. This way you don't have the potential liability of holding users' data, you don't have to prompt users, and you don't have to maintain custom UI for Contact selection and suggestions.

**[7:04]** Now let's talk about Password AutoFill. Even if your app has adopted Sign in with Apple, which is the best way to get users signed in with an account quickly, Password AutoFill may be important to your app if your app has a way to log in with usernames and passwords. And, fortunately, it's easy to make Password AutoFill work great in your apps. For Password AutoFill, you just need to tag the username and password fields with the corresponding content type, username: password. The keyboard will automatically suggest the corresponding username

**[7:53]** and password saved in iCloud Keychain or another password manager. For security codes, the Content Type you want to use is One Time Code. Automatic Strong Passwords can hugely simplify the onboarding flow in your app. By suggesting unique strong passwords and automatically saving them to iCloud Keychain, this is not only quick and easy for the user, it also helps increase your app's security. An adoption couldn't be easier as shown in the example here, where we are using the newPassword Content Type.

**[8:41]** The last step is to associate your app with a domain. To learn how to do this, check out "Automatic Strong Passwords and Security Code AutoFill" from WWDC 2018. Let's talk about the Mac. New to macOS Big Sur, Catalyst apps now have security code AutoFill. If security code AutoFill works in your iPad apps, it will work great on macOS. And also new to macOS Big Sur, AppKit based apps have full support for password and security code AutoFill. AppKit now has a NSTextContentType, which is similar to UITextContentType

**[9:28]** in UIKit. Currently the supported values are .username, .password and .oneTimeCode. And one more thing that's cool is that macOS Big Sur also supports password manager apps as a data source for AutoFill. Last, but not least, if you get one thing out of this talk, it should be: Tag every text field in your app.
