---
id: "wwdc2017-247"
event: "wwdc2017"
title: "Extend Your App's Presence With Sharing"
url: "https://developer.apple.com/videos/play/wwdc2017/247"
language: "eng"
words: 758
---

# Extend Your App's Presence With Sharing — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2017/247) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:29]** Whether looking for the latest TV show to watch or the best place to grab lunch, you rely on the people around you for recommendations. By offering the ability to share on Your App, you can empower your users to give contextual recommendations. But there are some important things to consider before you offer the ability to share. First is the content. In Your App, what will you want your user to share? Is it an image or a video, or maybe even an experience that they've had in Your App? Next is placement. Where in Your App is the best place to offer the ability to share? If you share from a certain screen, is it contextual? Will the user know exactly what will be passed to the recipient? Timing is another important aspect to building a great

**[1:14]** sharing experience. It needs to be, when a user is completely connected to the content they are wanting to share; and at that moment, think, "My friend Kate would love this." The developers of Crossy Road have a great implementation that has narrowed all three of these areas. They started with an experience. Now, it's quite common to share your progress in a game, but losing in Crossy Road is actually quite comical. They quickly realized that people are going to want to share that moment and created a photograph representation and previewed it, ready for sharing. The timing, content and placement were all great. Think about the user of Your App. When are they most emotionally attached to the experience and going to want to share it? Another important aspect of sharing is placement. It doesn't make sense for a

**[1:59]** sharing button in a list view here; but on a detail view, it does. As I find a session I'm interested in, I might think of someone else that could be interested and can very quickly share it. The way you offer the ability to share in Your App is with an action button. This is the universal control used by all apps to access sharing. A great place for an action button in a detail view like this is in the title bar. It helps communicate to the user that you can share all the information in this view. On tapping that button, you can call a UIActivityViewController. This will display the user's sharing options. By default, the system has some built-in sharing options, like messages, mail and notes; but other options will populate here from apps that have implemented

**[2:45]** a share extension. When creating the UIActivityViewController, you can parse in pretty much any object, like a string, image or URL. But the best way to share the content of Your App is to use the universal link. A universal link looks like a URL, but instead launches Your App. At this stage, you might be asking, "Why share a URL? This is not a Web page." Well, you have to consider the person receiving the shared information. They may not have Your App installed; so when tapping a universal link when Your App is not installed, it will fall back to Safari, making it possible for people with Your App to share content with new people that do not need Your App to view the content. Then if a new user receives a link to the content in Your App,

**[3:30]** an app banner can be displayed in Safari, and it's a great way to increase awareness of innovative experience to draw new users of Your App. Another way you can increase the sharing experience for the recipient is to use Mockup in Open Graph. Then the content shared in iMessage can be displayed in a rich format; so instead of looking like this, it can look like this -- with an image preview and title. The recipient of this message is much more likely to tap and follow this link. So in summary, think about the content and experiences in Your App. What will your user like to share; and when is the most meaningful time to share? Do they know enough about the content to want to share it? Use the action button to launch sharing and consider the placement of that button for

**[4:15]** context. Universal links will work with recipients that don't have Your App, and app banners can guide them to Your App. Finally, mock up your Web page with Open Graph for rich sharing in iMessage. For more information, see the resources section of this video. Thank you, and feel free to
