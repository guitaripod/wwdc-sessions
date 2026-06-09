---
id: "tech-talks-110338"
event: "tech-talks"
title: "Add SharePlay to your multiplayer game with Game Center"
url: "https://developer.apple.com/videos/play/tech-talks/110338"
language: "eng"
words: 632
---

# Add SharePlay to your multiplayer game with Game Center — Transcript

[Session page](https://developer.apple.com/videos/play/tech-talks/110338) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:00]** Hello, everyone. I am Zhehong from Game Center Engineering team. Today, I'm really excited to walk you through how SharePlay has been integrated with Game Center. Game Center is Apple's social gaming platform. Players can add friends, compete on leaderboards, earn achievements, and see everything in one place with Player Activity. Game Center also supports great multiplayer experiences for players, including invitation, matchmaking, real-time gameplay, and voice chat. This year, we're excited to bring SharePlay support to Game Center. Players can already invite friends, contacts, and nearby players to play together.

**[0:45]** SharePlay enables them to share gaming experiences right in the moment. Now, if your players are on a FaceTime call or a Messages group, they can immediately jump into a game together. Imagine your players are in a Messages group with some friends, and they want to play a game. They can simply start an audio call from the group chat. Their friends will receive the invitation as a FaceTime call. Then it's time to launch your game. Let's take NBA 2K23 Arcade Edition as an example. We can click Play Now in the title screen and select Multiplayer. Then tap the Play With Friends button. After that, clicking Online NBA button

**[1:31]** will bring you the game Settings page. Let's set it to four quarters and two minutes for each quarter. Click on Next. This brings up the Game Center multiplayer UI, where players will see the brand-new mode selection screen that includes the SharePlay option. Tapping the Start SharePlay button will activate a group activity. Players can join and play together by simply tapping the Open button on their end. If you already use Game Center to support multiplayer in your game, you will get full SharePlay integration with just one small update. Now, I will show you how to enable SharePlay for your game. Currently, if you present the GKMatchmakerViewController, players will see the mode selection screen by default.

**[2:19]** If you want to adopt SharePlay integration, the first step is to add the entitlement of Group Activities to your game. You can do that by going to the project settings, and in the Signing & Capabilities tab, just search for Group Activities and select it. With GroupActivities capability enabled, the mode selection screen will show the SharePlay option. If you are using Game Center Multiplayer UI provided by GKMatchmakerViewController, that is the only step you have to do. You are done! On the other hand, if you are building your own multiplayer UI using Game Center APIs, you could choose to integrate with SharePlay's APIs directly. But since you're using Game Center APIs,

**[3:06]** we've also got you covered. It's still really easy. You already added GroupActivities capability in Xcode. Now you want to call some GameKit APIs. You can call the API to start a Group Activity on SharePlay. Then, add the players to the recipient list. And finally, call the API to start a match. Let's jump into the code. First, call GKMatchmaker .shared.startGroupActivity so that GameKit can notify your game when a player from the FaceTime call wants to join a match. Then, add the player to the recipient list. Finally, call GKMatchmaker.shared.findMatch to start a match.

**[3:51]** With just these steps, your game is now supporting SharePlay. As simple as that. To wrap up, Game Center's integration with SharePlay makes it easier for players to start games with friends. If you're using Game Center UI to build a multiplayer experience, you just need to add a GroupActivities capability in Xcode. If you are building your own custom UI, use the new APIs provided in GKMatchmaker. If you're new to using Game Center to build multiplayer experiences, I suggest you watch this video: "Tap into Game Center: Leaderboards, Achievements, and Multiplayer" from WWDC 2020. Thank you for watching.
