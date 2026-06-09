---
id: "wwdc2019-254"
event: "wwdc2019"
title: "Writing Great Accessibility Labels"
url: "https://developer.apple.com/videos/play/wwdc2019/254"
language: "eng"
words: 1211
---

# Writing Great Accessibility Labels — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2019/254) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:13]** Good morning everyone. Good morning. My name is Jordyn Castor and I work here at Apple on the Accessibility Design and Quality Team. I'm so excited to be here today. Accessibility is built into our hardware and software design here at Apple. We believe accessibility is a human right and it's one of our core values. When I download an app, there's an expectation that it just works. And I'm able to access all of the buttons, controls, and information using VoiceOver. To be honest, I give an app a

**[0:59]** first 30 second glance and if I can't access any of the functionality, I delete it. Now, I really, really want to use your applications. I do. But, one of the most crucial aspects to our built-in features like VoiceOver, Speak Screen, and Voice Control being able to access the functionality of your app is by the labeling of your buttons, and text fields, controls, and other elements. So today, I'm going to talk to you about what an accessibility label is, understanding the context for writing great labels, and best practices.

**[1:44]** So, let's -- so what is an accessibility label? Well, the definition is pretty short. It's a localized string that succinctly identifies the accessibility element. But let's unpack that a bit. Identifies the accessibility element. What does that mean exactly? It's a human readable, human understandable label that gives context and meaning for the elements in your app. And writing the code is pretty simple too. It's just getting or setting a string. But I get it.

**[2:29]** It's actually pretty difficult to accurately label the elements in your app. And as it turns out, that's all about the context. So that's what I'm going to help you understand in the next few minutes, is the importance of understanding context. So, let's dive right in. What should the label of this button be in your app? Well, by default it might be called plus. And I might be able to figure out what you meant. But, let's look at that with a bit more context. What about in a nav bar across

**[3:15]** from a back button? This is pretty common in iOS apps. What should the label of this button be here? Add? Well, that might be just dandy. If I'm in a notes app and I hear the word add, I'm going to know that that's going to add a new note. But remember, these labels are supposed to be succinct. In a shopping context I might need to clarify that a bit further to distinguish this app button from other actions like Add to Favorites. So, we might need to call that Add to Cart. And, what if there were dozens of Add to Cart buttons?

**[4:00]** In this context I might expect VoiceOver to say, add peanut butter to cart. And hopefully it's not crunchy peanut butter. To bring it back to the original example, what should the label of this button be in your app? Well, that all depends on the context. So, now let's talk about some best practices when considering what a label should be. First and foremost, always, always remember to add labels to your apps. This is crucial. If a label's not added, VoiceOver might speak something like.

**[4:45]** Button, button, button. And for all I know guys, that could be the Delete hard drive Partition button and I wouldn't want to press that. If there is no label added and if there's an image in the button or if there's an image within the button, VoiceOver might speak something like -- Plus underscore icon underscore outline underscore hash nine, nine, nine, nine, nine, nine, dot. What? What does that even mean? So please, please guys, add labels. VoiceOver knows what the element in your apps is based on the element type. So, it's redundant to add text

**[5:30]** to your string like button or tab. And if you do, VoiceOver would read out the label like -- Add button button. Hearing this though -- Add button. Makes much more sense. Remember to update the label when the UI changes. So, if you have an add button -- Add button. That changes to a delete button -- Delete button. Remember to update your UI so that the label, so that VoiceOver will speak the correct state of the button. When there's multiple buttons with the same action like adding an item to the cart, remember to provide the context.

**[6:16]** Here it's not clear what I'm adding. Add button. Am I adding the peanut butter, the bananas, or the cookies? Oh, I love cookies. The context is much more clear here. Add peanut butter button. Oh, we're adding the peanut butter. Hopefully it's not crunchy. Avoid redundant labels. So, if I'm in a music player the context is clear that we're dealing with songs. So, having VoiceOver speak -- Play song button. Or next song, is unnecessary.

**[7:01]** I'd much rather hear VoiceOver speak -- Play button. Just the word play. It's also great to add labels to your animations, such as your spinners. So that VoiceOver will let me know that the content in your app is -- Loading. Loading. That's really important. So, this -- Delete items from the current folder and add it to the trash button. That is too verbose. Remember, we want these labels to be as succinct as possible. And, the context really makes things in your app clear. So, this -- Delete button. Would be just fine.

**[7:48]** But verbosity isn't always a bad thing though. Oftentimes verbose descriptions when in appropriate situations is really what makes your app fun and memorable. The developers of the Cookie Monster sticker packs have added verbose but really fun labels to their stickers. So now, VoiceOver speaks -- Me happy face eat small cookie, om nom nom button. I love that. That is so awesome. These Cookie Monster stickers are intended to be fun and just make a person smile. Whether you can see the sticker or you hear the label. So, let's review. Remember to add labels so that

**[8:35]** VoiceOver doesn't speak "button, button, button." Don't include the element type in your label because VoiceOver gathers that info already. So, hearing add button button is unnecessary. Update the labels when your UI changes. So, when you have that add button that changes to a delete button, remember to update your label so VoiceOver reads the correct state of the button. Avoid redundancy like play song, next song, previous song. In a music player, remember to provide enough context so I know whether I'm adding peanut butter, bananas, or those awesome cookies to my cart.

**[9:24]** Add labels to your meaningful animations like spinners, so that VoiceOver will read that the content in your app is loading or in progress. Avoid verbose labels like delete current item from the trash and move it. Unless you have a great reason like those awesome Cookie Monster stickers. I really hope you've enjoyed learning about best practices for labeling your apps. But if you're ever curious what your app would sound like to a VoiceOver user, I really encourage you to turn it on and swipe around. It's really a great opportunity to improve your app for everyone.
