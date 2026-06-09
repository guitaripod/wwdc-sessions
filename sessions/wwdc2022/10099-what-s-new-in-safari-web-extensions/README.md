---
id: "wwdc2022-10099"
event: "wwdc2022"
year: 2022
title: "What’s new in Safari Web Extensions"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10099"
topics: ["Safari & Web"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What’s new in Safari Web Extensions

**Event:** WWDC22 · **Topic:** Safari & Web · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10099](https://developer.apple.com/videos/play/wwdc2022/10099)

Learn how you can use the latest improvements to Safari Web Extensions to create even better experiences for people browsing the web. We'll show you how to upgrade to manifest version 3, adopt the latest APIs for Web Extensions, and sync extensions across devices.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,291 words)

## Documentation & Resources

- [Modernizing Safari Web Extensions](https://developer.apple.com/documentation/SafariServices/modernizing-safari-web-extensions) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SafariServices/modernizing-safari-web-extensions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SafariServices/modernizing-safari-web-extensions.json
- [Messaging a Web Extension’s Native App](https://developer.apple.com/documentation/SafariServices/messaging-a-web-extension-s-native-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SafariServices/messaging-a-web-extension-s-native-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SafariServices/messaging-a-web-extension-s-native-app.json
- [Developing a Safari Web Extension](https://developer.apple.com/documentation/SafariServices/developing-a-safari-web-extension) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SafariServices/developing-a-safari-web-extension
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SafariServices/developing-a-safari-web-extension.json
- [Learn more about bug reporting](https://developer.apple.com/bug-reporting/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/bug-reporting/
- [MDN Web Docs - Web Extensions API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API) _documentation_
- [Safari web extensions](https://developer.apple.com/documentation/SafariServices/safari-web-extensions) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SafariServices/safari-web-extensions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SafariServices/safari-web-extensions.json

## Code Snippets

### Executing script on webpages — [2:43]

```json
// Manifest version 2
browser.tabs.executeScript(1, {
  frameId: 1,
  code: "document.body.style.background = 'blue';"
});
```

### scripting.executeScript API — [3:00]

```javascript
// Manifest version 3
function changeBackgroundColor(color) {
  document.body.style.background = color;
};

browser.scripting.executeScript({
  target: { tabId: 1, frameIds: [ 1 ] },
  func: changeBackgroundColor,
  args: [ "blue" ]
});
```

### tabs.executeScript file — [4:02]

```javascript
// Manifest version 2
browser.tabs.executeScript({ 1,
  file: "file.js"
});
```

### scripting.executeScript API files — [4:09]

```javascript
// Manifest version 3
browser.scripting.executeScript({
  target: { tabId: 1 },
  files: [ "file.js", "file2.js" ]
});
```

### scripting.insertCSS — [4:15]

```javascript
// Add styling
browser.scripting.insertCSS({
  target: { tabId: 1, frameIds: [ 1, 2, 3 ] },
  files: [ "file.css", "file2.css" ]
});
```

### scripting.removeCSS — [4:21]

```javascript
// Remove styling
browser.scripting.removeCSS({
  target: { tabId: 1, frameIds: [ 1, 2, 3 ] },
  files: [ "file.css", "file2.css" ]
});
```

### Manifest version 3 web_accessible_resources — [5:08]

```json
// Manifest version 3
"web_accessible_resources": [
    {
      "resources": [ "pie.png" ],
      "matches": [ "*://*.apple.com/*" ]
    },
    {
      "resources": [ "cookie.png" ],
      "matches": [ "*://*.webkit.org/*" ]
    }
]
```

### Manifest version 3 action — [5:42]

```json
// Manifest version 3
"action": {
  "default_icon": {
    "16": "Images/icon16.png"
  },
  "default_title": "defaultTitle"
}
```

### Manifest version 2 content_security_policy — [5:57]

```json
// Manifest version 2

"content_security_policy" : "script-src 'unsafe-eval' https://*apple.com 'self'"
```

### Manifest version 3 content_security_policy — [6:08]

```json
// Manifest version 3

"content_security_policy" : { "extension_pages" : "script-src 'unsafe-eval' 'self'" }
```

### Specifying a ruleset — [10:31]

```json
// manifest.json

"permissions": [ "declarativeNetRequest" ],

"declarative_net_request": {
  "rule_resources": [
    {
      "id": "my_ruleset",
      "enabled": true,
      "path": "rules.json"
    }
  ]
}
```

### updateSessionRules — [11:44]

```javascript
// Rules that won't persist

browser.declarativeNetRequest.updateSessionRules({ addRules: [ rule ] });

// Rules that will persist

browser.declarativeNetRequest.updateDynamicRules({ addRules: [ rule ] });
```

### externally connectable — [14:33]

```javascript
// In the webpage
let extensionID = "com.apple.Sea-Creator.Extension (GJT7Q2TVD9)";

browser.runtime.sendMessage(extensionID, { greeting: "Hello!" },
 function(response) {
    console.log("Received response from the background page:");
    console.log(response.farewell);
});
```

### Message from webpage to extension (in the webpage) — [15:00]

```javascript
// In the webpage
let extensionID = "com.apple.Sea-Creator.Extension (GJT7Q2TVD9)";

browser.runtime.sendMessage(extensionID, { greeting: "Hello!" },
 function(response) {
    console.log("Received response from the background page:");
    console.log(response.farewell);
});
```

### Message from webpage to extension (in the background page) — [15:33]

```swift
// In the background page
browser.runtime.onMessageExternal.addListener(function(message, sender, sendResponse) {
    console.log("Received message from the sender:");
    console.log(message.greeting);
    sendResponse({ farewell: "Goodbye!" });
});
```

### Determining the correct identifier — [16:17]

```swift
// Determining the correct identifier

function determineExtensionID(extensionID) {
  return new Promise((resolve) => {
    try {
      browser.runtime.sendMessage(extensionID, { action: 'determineID' }, function(response) {
        if (response)
          resolve({ extensionID: extensionID, isInstalled: true, response: response });
        else 
          resolve({ extensionID: extensionID, isInstalled: false });
      });
    }
  });
};
```

### background.js — [17:09]

```javascript
// background.js

browser.runtime.onMessageExternal.addListener(function(message, sender, sendResponse) {
  if (message.action == "determineID") {
    sendResponse({ "Installed" });
  }
});
```

### Unlimited storage — [18:07]

```json
// manifest.json

"permissions": [ "storage", "unlimitedStorage" ]
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10099/5/AE8329C9-B427-49CF-95BE-71C9B5F49627/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10099/5/AE8329C9-B427-49CF-95BE-71C9B5F49627/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10099) — developer.apple.com. Indexed for agent consumption._
