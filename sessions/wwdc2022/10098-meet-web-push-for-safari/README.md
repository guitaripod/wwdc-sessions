---
id: "wwdc2022-10098"
event: "wwdc2022"
year: 2022
title: "Meet Web Push for Safari"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10098"
topics: ["Safari & Web"]
platforms: ["macOS"]
hasTranscript: true
---

# Meet Web Push for Safari

**Event:** WWDC22 · **Topic:** Safari & Web · **Platforms:** macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10098](https://developer.apple.com/videos/play/wwdc2022/10098)

Bring better notifications to your websites and web apps in Safari on macOS with Web Push. We’ll show you how you can remotely send notifications to people through the web standards-based combination of Push API, Notifications API, and Service Workers.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,380 words)

## Documentation & Resources

- [Push API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API) _documentation_
- [Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API) _documentation_
- [Sending web push notifications in web apps and browsers](https://developer.apple.com/documentation/UserNotifications/sending-web-push-notifications-in-web-apps-and-browsers) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications/sending-web-push-notifications-in-web-apps-and-browsers
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications/sending-web-push-notifications-in-web-apps-and-browsers.json
- [Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) _documentation_
- [Learn more about bug reporting](https://developer.apple.com/bug-reporting/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/bug-reporting/

## Code Snippets

### BrowserPetsWorker.js — [8:27]

```javascript
// BrowserPetsWorker.js

function handleMessageEvent(event) {
    // ...
};
self.addEventListener('message', (event) => {
    handleMessageEvent(event);
});

function primeCaches() {
    // ...
};
self.addEventListener('install', (event) => {
    primeCaches();
});

self.addEventListener('fetch', (event) => {
    event.respondWith(caches.match(event.request));
});
```

### BrowserPetsMain.js — [8:42]

```javascript
// BrowserPetsMain.js

var registration;
if ('serviceWorker' in navigator) {
    let registration = await navigator.serviceWorker.getRegistration();
    if (!registration)
        registration = await navigator.serviceWorker.register('BrowserPetsWorker.js');
}
```

### BrowserPetsMain.js subscribeToPush() — [9:00]

```javascript
// BrowserPetsMain.js

async function subscribeToPush() {
    // ...
}

// BrowserPetsMain.html

<button onclick="subscribeToPush()">Register for Updates</button>
```

### BrowserPetsMain.js subscribe — [9:19]

```javascript
// BrowserPetsMain.js

async function subscribeToPush() {
    let serverPublicKey = VAPID_PUBLIC_KEY; 

    let subscriptionOptions = {
        userVisibleOnly: true,
        applicationServerKey: serverPublicKey
    };

    let subscription = await swRegistration.pushManager.subscribe(subscriptionOptions);

    sendSubcriptionToServer(subscription);
}
```

### BrowserPetsMain.js subscriptionOptions — [9:36]

```javascript
// BrowserPetsMain.js

async function subscribeToPush() {
    let serverPublicKey = VAPID_PUBLIC_KEY; 

    let subscriptionOptions = {
        userVisibleOnly: true,
        applicationServerKey: serverPublicKey
    };

    let subscription = await swRegistration.pushManager.subscribe(subscriptionOptions);

    sendSubcriptionToServer(subscription);
}
```

### BrowserPetsMain.js request permission to push — [10:21]

```swift
// BrowserPetsMain.js

async function subscribeToPush() {
    let serverPublicKey = VAPID_PUBLIC_KEY; 

    let subscriptionOptions = {
        userVisibleOnly: true,
        applicationServerKey: serverPublicKey
    };

    let subscription = await swRegistration.pushManager.subscribe(subscriptionOptions);

    sendSubcriptionToServer(subscription);
}
```

### BrowserPetsWorker.js push — [11:13]

```javascript
// BrowserPetsWorker.js

self.addEventListener('push', (event) => {
    let pushMessageJSON = event.data.json();

    // Our server puts everything needed to show the notification
    // in our JSON data.
    event.waitUntil(self.registration.showNotification(pushMessageJSON.title, {
        body: pushMessageJSON.body,
        tag: pushMessageJSON.tag,
        actions: [{
            action: pushMessageJSON.actionURL,
            title: pushMessageJSON.actionTitle,
        }]
    }));
}
```

### BrowserPetsWorker.js notification click — [12:06]

```javascript
// BrowserPetsWorker.js

self.addEventListener('notificationclick', async function(event) {
    if (!event.action)
        return;

    // This always opens a new browser tab,
    // even if the URL happens to already be open in a tab.
    clients.openWindow(event.action);
});
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10098/4/0243E8FF-8341-4FD5-BACD-CEB81B4730DF/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10098/4/0243E8FF-8341-4FD5-BACD-CEB81B4730DF/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10098) — developer.apple.com. Indexed for agent consumption._
