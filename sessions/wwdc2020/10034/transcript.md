---
id: "wwdc2020-10034"
event: "wwdc2020"
title: "Widgets Code-along, part 1: The adventure begins"
url: "https://developer.apple.com/videos/play/wwdc2020/10034"
language: "eng"
words: 1087
---

# Widgets Code-along, part 1: The adventure begins — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2020/10034) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:03]** Hello and welcome to WWDC. Hi, I'm Izzy. I'm an engineer on the iOS System Experience team. Thanks for joining me. Let's take a look at what we will be covering today. This is a code-along, a new format for WWDC 2020. We'll go over what that means and how you can participate, we'll cover the core concept of what a widget is, and then we'll build our first widget together. I'm excited. Let's get started. This session is a code-along. There's a project available on the developer portal we'll start with, and we will build a widget for it from scratch together. I invite you to start that download now, and while that's going, we'll cover a couple concepts. What is a widget at its core?

**[0:48]** A widget is just a SwiftUI view. SwiftUI. So it's the same declarative code that generates gorgeous native views on iOS, iPadOS, and macOS. And it's a SwiftUI view that updates over time. Exactly how and when it updates is what we'll be looking at in this code-along. So, this is the download project. We're in the first part of our code-along, so let's open that project. Before we get into the widget, let's build and run this to see what we have. This is the Emoji Rangers app.

**[1:33]** It lets us keep track of our favorite Emoji Rangers. You can see we have Power Panda, Spouty and Egghead. Let's look at their details. Here we see that our Emoji Rangers are saving the world from waves of attacks. Power Panda is recharging right now but will be ready soon. I've seen the keynote, I've watched "Welcome to WidgetKit," and I'd really like a widget for this game. It looks like we have the perfect view for it already. The status square in the top left looks ideal for a widget, so let's make it one. Let's check out how this view works in code first. Here's our SwiftUI AvatarView. If you're new to SwiftUI, widgets are a perfect place to get started. You can see we have just a few lines of code to generate the widget we want,

**[2:20]** and because we're expressing the layout semantically with Stacks, SwiftUI knows how to set the padding just right for us. You'll also notice on the right-hand side, there's a SwiftUI preview, which is a live representation overview that updates as we type. It kind of looks like a widget already. Let's go ahead and make it one for real. First, we need to create a widget target. I do that by going to File, New, Target, and search for a widget. Let's name it "EmojiRanger Widget." And finish. Activate our target.

**[3:05]** Now that we have our target, I know we want that view from earlier in it, and I'm going to add the files that I want to the target. SwiftUI previews work for widgets as well. Let's take a look. You can click the Create Preview to automatically insert a preview for us, and we can use that AvatarView. In order to see exactly what it'll look like as a widget, we use the WidgetPreviewContext as an argument to the previewContext.

**[4:15]** That looks great. It's almost like we already have a widget. Making it real is just a matter of filling in some information. We have a DisplayName and a Description that are easy to fill in. Now let's look at our main EntryView... the EmojiRangerWidgetEntryView. Let's use that AvatarView, which is what we previewed before. Now, it wants me to pass a character in here, so where should that character come from? The EmojiRangersWidgetEntryView already comes with an entry,

**[5:02]** so let's add it to the entry. And now I can pass it directly into my AvatarView. But where does this entry come from? Entries come from a timeline provider, which is the core engine of a widget. The timeline provider provides snapshots when WidgetKit wants just one entry, like in the Widget Gallery, and it provides a full timeline when the user has added a configured widget to their device. So here, for the snapshot, all we need to do is pass a character. We can pass our character in here.

**[5:48]** Timeline is used once a user has actually added a widget from the gallery. We don't need a full timeline right now, so let's just use one entry again. Okay, that's great. Let's build and run, and see what we have. I built my widget target, and it automatically added the widget to my Home Screen for me. We have a full widget now, but I noticed some things I'd like to tweak. First, in the Add sheet... ...our widget has a small, medium, and large size. These work okay, but it's not the best use of space right now,

**[6:34]** and I'm not ready to support those yet. So let's set our supported families. That's just an extra modifier on our widget configuration. One other thing you may have noticed is that there's this PlaceholderView in our template. Our widget is so fast that we can't actually see it, but this is what shows up while WidgetKit is waiting on a timeline. We want it to be our AvatarView, and we can preview what that looks like with SwiftUI previews. Let's make it our AvatarView. There's no entry for the PlaceholderView, so we can pass in Panda again.

**[7:19]** And now in our preview... we can make this a group... and we can add in our placeholder. Now we have two views that look the same, but we want our placeholder to indicate pending content, not our actual content. So there's new SwiftUI API that makes this super easy. It's just the isPlaceholder modifier. Now you can see in our previews,

**[8:05]** we have our full widget and a placeholder with our text automatically replaced with gray, rounded rectangles, and our image is automatically replaced as well. Amazing. Let's take one last look at our new widget. Here's our Emoji Rangers app. Now when I go to the Widget Gallery, I can see the single supported size, and I can add it right on my Home Screen. Perfect. For insight on how to approach widget design, see the "Designing Great Widgets" talk, and my teammate Nils is giving a talk about how to make the most of SwiftUI and widgets to really nail those designs. I'd also love for you to join me in the next section of this code-along.

**[8:52]** Thanks for joining me, and have a great WWDC.
