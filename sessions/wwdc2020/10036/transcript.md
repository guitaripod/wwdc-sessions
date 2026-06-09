---
id: "wwdc2020-10036"
event: "wwdc2020"
title: "Widgets Code-along, part 3: Advancing timelines"
url: "https://developer.apple.com/videos/play/wwdc2020/10036"
language: "eng"
words: 1125
---

# Widgets Code-along, part 3: Advancing timelines — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2020/10036) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:03]** Hello and welcome to WWDC. Hi, I'm Izzy. I'm an engineer on the iOS System Experience team. This is the last in our series of widget code-alongs. We'll cover using URL sessions from a widget extension. It should be familiar, but there's some new API just for widgets. We'll use SwiftUI's Link API to make regions of a widget tappable. We'll add a widget bundle. We can provide multiple kinds of widget from the same extension, which is super convenient. And we'll look at how to provide a dynamic set of options for a widget configuration. This session's a code-along. We're picking up from where we left off in the widgets code-along session, so if you've been following along so far, you're in the right spot. If not, don't worry. You can pick from the part-three target in the sample project.

**[0:51]** Since we're covering a lot of subjects in this session, I made a checklist for us. We're starting at part three, so let's jump in. I've actually gone ahead and added another widget to this project: the Leaderboard widget. Let's take a look. We can see that it gives us a list of characters sorted by health. Let's talk about how it's doing that for a minute. Making network requests is one of the fundamental ways that a widget can get data. You may have already noticed, but the timeline provider API is built with completion handlers instead of return values

**[1:39]** specifically to make doing asynchronous tasks, like network fetches, easy. Here we have a loadLeaderboardData asynchronous request on our CharacterDetail object. Let's take a look at the implementation. You'll notice that this is a normal URL session making a normal data task request. We're simulating a remote fetch with a local file, but you'd typically call a remote Web service here. The key thing to note is that this is the normal in-process URL session API, and it works just the same as you would expect. But what about background sessions? You may be familiar with other extension types

**[2:26]** where a background URL session will launch the extension's hosting app when it completes. That's not true for widgets. The widget responds to all the URL sessions it creates, including background session. But there's no app delegate. So how does a widget know what to do? There's a modifier on widget configuration called onbackgroundURLSessionEvents, and that's analogous to the application delegate method. You're provided the sessionIdentifier... and a completion block. And you'd manage those just the same as you'd manage them in an app.

**[3:11]** That's URL sessions. Let's add our Leaderboard widget to the Home Screen. So this is nice, but like the Character Detail widget, I want to be able to tap each character to launch to their specific detail screen. Like widget URL, this is super simple. All we have to do is use the SwiftUI Link API. Our leaderboard widget uses this AllCharactersView. So let's jump to the definition of that. I can see by clicking this HStack and the blue outlines that are reflected in the SwiftUI preview that my rows are this HStack. And all we have to do is embed this in a link...

**[3:59]** with a destination of our character's URL. Now let's build and run. And now when I click my widget... you can see that it highlights that specific row, and when I tap, I go directly to that character's information. That was Spouty, and now Egghead. So that's using Link. One thing you may have noticed is that when I pulled up the widget gallery, I only have a Leaderboard widget. And that's because I moved the main attribute

**[4:46]** from the Ranger Detail widget onto the Leaderboard widget. By definition, there can only be one main per process, so we can't just add it in both places. But what we can do is make a widget bundle. So all we have to do is add both of our widgets to the widget bundle and move our main attribute from the Leaderboard widget... onto the bundle. Now, when I build and run... and go the widget gallery... I have my Leaderboard widget and my Ranger Detail widget. Great. That's widget bundles.

**[5:31]** In our previous session, we made a widget configurable using a hard-coded list. But what if we don't know all of the options up front? Because our configuration is a SiriKit intent, we can provide a dynamic list of options with an Intent Extension the same way we would for other intent-based features. I've already added the extension to this project, but here's how you do it. First you go to File, New, Target... search for "Intent"... and add an Intents Extension. Pick Swift as a language. Make sure your starting point is "none." And that's all you need to do. Now let's look at our Intent Definition. It looks very similar to our previous static Intent,

**[6:17]** but "type" is now a custom type instead of an enum. Let's take a look at what properties it comes with. It has two properties: identifier and displayString. These are the default properties a custom Intent type has, but now, where do these values come from? They come from the IntentHandler. Here is where we provide our dynamic set of options. Note that this is an asynchronous call like our timeline method. We're already returning a default set of characters, but CharacterDetail has a remoteCharacters list as well, so let's add that here.

**[7:04]** This would be like fetching more information from the network. Now let's update our widget to use the dynamic Intent. We can Edit All in Scope our character selection Intent. Because we no longer have an enum value, we don't need this method anymore. And our selected character is the characterFromName. And the name is the Intent identifier. Let's see what this looks like.

**[8:01]** Now, when I go to configure my Character Detail widget... I have our original options of Power Panda, Egghead and Spouty, but you can see we also have Mr. Spook, Cake and Octo. So Cake... Okay. But I want to keep an eye on Mr. Spook. So I'm gonna put him on my Home Screen. So now we have a widget that uses URL sessions, uses the new SwiftUI Link API, has a bundle with two kinds of widgets in it, and we support dynamic configuration. For a design perspective on how to build great widgets, see the "Design Great Widgets" talk, and for applying those design guidelines in SwiftUI,

**[8:46]** see the "Build SwiftUI Views for Widgets," both talks from this year's WWDC. Thanks so much for joining me. You now have all the tools you need to build amazing widgets. I can't wait to see what you come up with.
