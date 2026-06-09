---
id: "wwdc2020-10185"
event: "wwdc2020"
title: "Visually edit SwiftUI views"
url: "https://developer.apple.com/videos/play/wwdc2020/10185"
language: "eng"
words: 776
---

# Visually edit SwiftUI views — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2020/10185) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:03]** Hello and welcome to WWDC. Hi, I'm Daisy, and I work on the Xcode Previews team. In this video, I want to show you how you can use Xcode Previews to help you quickly build SwiftUI apps, whether you're new to SwiftUI or not. To do so, I'll be building the row view for our smoothie app. The view has the smoothie's name, ingredients, calorie count, and an image, along with the star count for its popularity. To begin, I'm going to use a library to add a new view to my UI. The library has SwiftUI views and modifiers, allowing you to keep your preview compiling without additional modifications. SwiftUI uses structural layouts in order to make your app adaptive. So your app looks great whether it's running on an iMac or an iPhone.

**[0:49]** Xcode Previews lets you insert your content, and get the right layout container, all in one action. Next, I can double-click on my "Hello World" view, which brings focus to the editor, allowing me to quickly modify the key component of my view, whether this is an image or text. The Xcode Previews canvas and the source editor have a tight integration. The canvas and the inspector help you write your Swift code faster, and any changes you do to source are immediately visible in the canvas. To help you build your structure even quicker, you can use Command-D to duplicate your views. Xcode Previews understands the structure of your code, so if you're duplicating a view that isn't in a container,

**[1:35]** it would insert one for you. Next, we can double-click on our third label to quickly modify it. Double-clicking on a view not only helps with replacing static content, but also makes integrating your model data a breeze. To insert my image, I'm going to bring up the library using the keyboard shortcut Command-Shift-L. The Xcode Previews canvas not only works with SwiftUI views and modifiers, but also your media, allowing you to use your images in your asset catalog with ease. Our image is larger than expected. This, however, makes sense, since SwiftUI renders your images in their true size.

**[2:21]** To remedy this, we can use the inspector to locate the appropriate modifier. Clicking on "Add Modifier" brings down a list of recommended suggestions using your current context, allowing you to quickly locate what you're looking for, and learn about modifiers commonly used with the view. The image is now resizing, though its size is not up to spec. In the inspector, I can add and edit common modifiers, allowing you to try various values without having to know the modifier's signature. This immediately updates your code and renders in the canvas. Next, I want to add the star view that indicates the smoothie's popularity. Using your project's custom SwiftUI views and modifiers in the canvas is just as easy as using those provided by the library. To see how to do this, see the session "Adding Custom Views and Modifiers to the Xcode Library."

**[3:08]** To repeat the star horizontally, Xcode Previews provides actions that embed the selected view in various containers. The actions can be brought up by holding Command and clicking on the view. In our case, we click "Embed in HStack" to embed in a horizontal container. To repeat the star view, we can bring up the same menu and click "Repeat." I'd like to make my smoothie title pop. Using the inspector, I can quickly try various font and weight values on my view, and preview the results immediately in the canvas. That doesn't look exactly how I want. To clear the modifier, I can click on the circular blue indicator next to the control. Clearing the modifier returns it to its inherited value. In this case, the font returns to the default SwiftUI font.

**[3:56]** Next, I would like to edit the other labels, which, with the inspectors, is only a few clicks. I can use the inspectors not only to edit properties of the modifiers, but also edit those of the view. Screen real estate is a hot commodity, so Xcode Previews has an in-canvas inspector allowing you to close your side panel without losing any functionality. To bring up the canvas inspector, hold Control-Option and click on the view you wish to inspect. To help you preview across different configurations, in Xcode 12 we have introduced various preview-centric capabilities. For example, we can now duplicate a preview with one click. And since previews are just views, we can inspect them too.

**[4:49]** In summary, some of the ways Xcode Previews helps you visually edit your SwiftUI views is through tight source editor integration,
