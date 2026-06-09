---
id: "wwdc2021-10189"
event: "wwdc2021"
year: 2021
title: "Coordinate media playback in Safari with Group Activities"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10189"
topics: ["Audio & Video", "Safari & Web"]
platforms: ["macOS"]
hasTranscript: true
---

# Coordinate media playback in Safari with Group Activities

**Event:** WWDC21 · **Topic:** Safari & Web · **Platforms:** macOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10189](https://developer.apple.com/videos/play/wwdc2021/10189)

Create SharePlay experiences that people can enjoy on the web and in your companion app. Learn how you can use the Group Activities framework in combination with a companion website to bring SharePlay to Safari, letting people connect with each other for enjoyable group interactions — even if they haven’t yet downloaded your app from the App Store.

**Keywords:** `facetime`, `face time`, `groupactivities`, `group activities`, `groupsession`, `media`, `safari`, `shareplay`, `share play`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,873 words)

## Documentation & Resources

- [Supporting coordinated media playback](https://developer.apple.com/documentation/AVFoundation/supporting-coordinated-media-playback) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AVFoundation/supporting-coordinated-media-playback
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AVFoundation/supporting-coordinated-media-playback.json
- [Group Activities](https://developer.apple.com/documentation/GroupActivities) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/GroupActivities
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/GroupActivities.json

## Code Snippets

### Preparing your app — [2:50]

```swift
struct WatchTogether: GroupActivity {

    var contentIdentifier: String

    func metadata() async -> GroupActivityMetadata {
        var metadata = ActivityMetadata()
        metadata.fallbackURL = URL(string: "https://example.com/title/\(contentIdentifier)")
        return metadata
    }
}
```

### Adopting Media Session — [5:29]

```javascript
if (navigator.mediaSession) {
    navigator.mediaSession.setActionHandler('play', () => video.play() );
    navigator.mediaSession.setActionHandler('pause', () => video.pause() );
    navigator.mediaSession.setActionHandler('seekto', details => {
        video.currentTime = details.seekTime;
    });
}

let updateMediaSessionState = function() {
    if (!navigator.mediaSession)
        return;
    let playbackState = video.paused ? 'paused' : 'playing';
    navigator.mediaSession.playbackState = playbackState;

    let positionState = { video.duration, video.playbackRate, video.currentTime };
    navigator.mediaSession.setPositionState(positionState);
};

for (var event of ['playing', 'pause', 'durationchange', 'ratechange', 'timechange'])
    video.addEventListener(event, updateMediaSessionState);

navigator.mediaSession.metadata = new MediaMetadata({
    title: myPlayer.titleString,
    artwork: [{ src: myPlayer.artworkURL }]
});
```

### Adopting Coordinator — [9:32]

```javascript
navigator.mediaSession.addEventListener('coordinatorchange', coordinator => {
    if (coordinator)
        coordinator.join();
    controls.inSessionIcon.style.hidden = !coordinator;
});

controls.inSessionIcon.addEventListener('click', event => {
    let coordinator = navigator.mediaSession.coordinator;
    if (coordinator && coordinator.state == 'joined')
        navigator.mediaSession.coordinator.leave();
});

controls.playButton.addEventHandler('click', event => {
    if (navigator.mediaSession.coordinator)
        navigator.mediaSession.coordinator.play();
    else
        video.play();
});
controls.pauseButton.addEventHandler('click', event => {
    if (navigator.mediaSession.coordinator)
        navigator.mediaSession.coordinator.pause();
    else
        video.pause();
});
controls.timeline.addEventHandler('onchange', event => {
    if (navigator.mediaSession.coordinator)
        navigator.mediaSession.coordinator.seekTo(event.target.value);
    else
        video.currentTime = event.target.value;
});
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10189/6/94D452D6-3731-4C08-8EFA-BD8F6B8853ED/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10189/6/94D452D6-3731-4C08-8EFA-BD8F6B8853ED/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10189) — developer.apple.com. Indexed for agent consumption._