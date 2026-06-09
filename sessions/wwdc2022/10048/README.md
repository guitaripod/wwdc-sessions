---
id: "wwdc2022-10048"
event: "wwdc2022"
year: 2022
title: "What's new in Safari and WebKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10048"
topics: ["Safari & Web"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What's new in Safari and WebKit

**Event:** WWDC22 · **Topic:** Safari & Web · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10048](https://developer.apple.com/videos/play/wwdc2022/10048)

Explore the latest features in Safari and WebKit and learn how you can make better and more powerful websites. We’ll take you on a tour through the latest updates to HTML, CSS enhancements, Web Inspector tooling, Web APIs, and more.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,707 words)

## Documentation & Resources

- [Safari Technology Preview](https://developer.apple.com/safari/technology-preview/) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/safari/technology-preview/
- [Safari Release Notes](https://developer.apple.com/documentation/safari-release-notes) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/safari-release-notes
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/safari-release-notes.json
- [WebKit Open Source Project](https://webkit.org) _guide_
- [Learn more about bug reporting](https://developer.apple.com/bug-reporting/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/bug-reporting/
- [MDN Web Docs - Web Extensions API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API) _documentation_

## Code Snippets

### Dialog element — [2:59]

```xml
<!-- <dialog> element -->

<dialog method="dialog">
  <form id="dialogForm">
    <label for="givenName">Given name:</label>
    <input class="focus" type="text" name="givenName">
    <label for="familyName">Family name:</label>
    <input class="focus" type="text" name="familyName">
    <label>
      <input type="checkbox"> Can trade in person
   </label>
   <button>Send</button>
  </form>
</dialog>
```

### Backdrop pseudo-class — [3:09]

```javascript
/* ::backdrop pseudo-element */

dialog::backdrop {
  background: linear-gradient(rgba(233, 182, 76, 0.7), rgba(103, 12, 0, 0.6));
  animation: fade-in 0.5s;
}

@keyframes fade-in {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
```

### inert attribute — [3:53]

```javascript
// inert attribute

function switchToIndex(index) {
  this.items.forEach(item => item.inert = true);
  this.items[index].inert = false;
  this.currentIndex = index;
}
```

### Lazy image loading — [4:22]

```xml
<img src="images/shirt.jpg" loading="lazy"
alt="a brown polo shirt"
width="500" height="600">
```

### Container Queries — [6:46]

```javascript
/* Container queries */

.container {
  container-type: inline-size;
  container-name: clothing-card;
}
.content {
  display: grid;
  grid-template-rows: 1fr;
  gap: 1rem;
}
@container clothing-card (width > 250px) {
  .content {
    grid-template-columns: 1fr 1fr;
  }
  /* additional layout code */
}
```

### Cascade layers — [8:05]

```javascript
/* Author Styles - Layer A */
@layer utilities {
  div {
    background-color: red;
  }
}

/* Author Styles - Layer B */
@layer customizations {
  div {
    background-color: teal;
  }
}

/* Author Styles - Layer C */
@layer userDefaults {
  div {
    background-color: yellow;
  }
}
```

### :has() pseudo-class — [8:54]

```xml
<!-- :has() pseudo-class -->

<style>
  form:has(input[type="checkbox"]:checked) {
    background: #ff927a;
  }
</style>



<form class="message">
  <textarea rows="5" cols="60" name="text" 
    placeholder="Enter text"></textarea>
  <div class="checkbox">
    <input type="checkbox" value="urgent"> 
    <label>Urgent?</label>
  </div>
  <button>Send Message</button>
</form>
```

### Offset Path — [11:08]

```javascript
/* offset-path */

:is(.blue, .teal, .yellow, .red)  {
  offset-path: circle(9vw at 5vw 50%);
}

@keyframes move {
  100% { 
    offset-distance: 100%;
  }
}

/* Animation */
.clothing-header.clicked :is(.blue, .teal, .red, .yellow) {
  animation: move 1100ms ease-in-out;
}
```

### scroll-behavior: auto — [11:43]

```javascript
html {
  scroll-behavior: auto;
}
```

### scroll-behavior: smooth — [12:09]

```javascript
html {
  scroll-behavior: smooth;
}
```

### :focus-visible & accent-color — [13:10]

```javascript
/* :focus-visible & accent-color */

:focus-visible {
  outline: 4px solid var(--green);
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
}

:root {
  accent-color: var(--green);
}
```

### Font palette dark mode & light mode — [14:50]

```javascript
/* Dark mode */
font-palette: dark;

/* Light mode */
font-palette: light;
```

### Font palette custom colors — [15:01]

```javascript
/* Dark mode */
font-palette: dark;

/* Light mode */
font-palette: light;

/* Custom colors */
@font-palette-values --MyPalette {
  override-colors: 1 yellow;
}

#logo {
  font-palette: --MyPalette;
}
```

### CSS Grid — [15:55]

```javascript
/* Grid to layout cards */
main {
  display: grid;
  grid-template-columns: 
    repeat(auto-fit, minmax(225px, 1fr));
  gap: 1rem;
}

/* Grid to layout each card’s content */
article {
  display: grid;
  grid-row: span 5;
}
```

### Adding sub grid — [16:35]

```javascript
/* Grid to layout cards */
main {
  display: grid;
  grid-template-columns: 
    repeat(auto-fit, minmax(225px, 1fr));
  gap: 1rem;
}

/* Grid to layout each card’s content */
article {
  display: grid;
  grid-row: span 5;
/* Adding subgrid, tying them together */
  grid-template-rows: subgrid; 
}
```

### Web App Manifest file icons — [21:15]

```json
// Manifest file 

"icons": [
 {
   "src": "orange-icon.png",
    "sizes": "120x120",
    "type": "image/png"
  }
]
```

### apple-touch-icon — [21:29]

```xml
<!-- HTML head -->

<link rel="apple-touch-icon" href="blue-icon.png" />
```

### Broadcast Channel — [22:36]

```javascript
// State change
broadcastChannel.postMessage("Item is unavailable");
```

### Origin private file system — [23:14]

```javascript
// Accessing the origin private file system
const root = await navigator.storage.getDirectory();

// Create a file named Draft.txt under root directory
const draftHandle = await root.getFileHandle("Draft.txt", { "create": true });

// Access and read an existing file
const existingHandle = await root.getFileHandle("Draft.txt");
const existingFile = await existingHandle.getFile();
```

### Shared Worker — [25:32]

```javascript
// Create Shared Worker
let worker = new SharedWorker("SharedWorker.js");

// Listen for messages from Shared Worker
worker.port.addEventListener("message", function(event) {
  console.log("Message received from worker: " + event);
});

// Send messages to Shared Worker
worker.port.postMessage("Send message to worker");
```

### findLast() and findLastIndex() — [25:56]

```javascript
const list = ["shirt","pants","shoes","hat","shoestring","dress"];
const hasShoeString = (string) => string.includes("shoe");

console.log(list.findLast(hasAppString));
// shoestring

console.log(list.findLastIndex(hasAppString));
// 4
```

### at() — [26:17]

```javascript
const list = ["shirt","pants","shoes","hat","shoestring","dress"];

// Instead of this:
console.log(list[list.length - 2]);

// It's as easy as:
console.log(list.at(-2));
```

### strict-dynamic source expression — [29:12]

```javascript
// strict-dynamic source expression

// Without strict-dynamic
Content-Security-Policy: script-src desired-script.com dependent-script-1.com
  dependent-script-2.com dependent-script-3.com; default-src "self";

// With strict-dynamic
Content-Security-Policy: default-src "self"; script-src "nonce-desired" "strict-dynamic";
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10048/4/8DF121DF-6825-4FBB-B570-A75F5A44CCB7/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10048/4/8DF121DF-6825-4FBB-B570-A75F5A44CCB7/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10048) — developer.apple.com. Indexed for agent consumption._