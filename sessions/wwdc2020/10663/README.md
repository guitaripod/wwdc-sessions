---
id: "wwdc2020-10663"
event: "wwdc2020"
year: 2020
title: "What's new for web developers"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10663"
topics: ["Safari & Web"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# What's new for web developers

**Event:** WWDC20 · **Topic:** Safari & Web · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10663](https://developer.apple.com/videos/play/wwdc2020/10663)

Explore the latest features and improvements for Safari and WebKit. We’ll walk you through updated web APIs, CSS and media features, JavaScript syntax, and more to help you build great experiences for people when they use your website, home screen web apps, or embedded WebKit views.

**Keywords:** `airplay`, `animate`, `app-clip-bundle-id`, `app clips`, `apple-itunes-app`, `apple pay`, `ar quick look`, `aspect ratio`, `async clipboard`, `attribute`, `bigint`, `clipboard`, `constructor`, `copy`, `css`, `css animations`, `css shadow part`, `css transitions`, `custom elements`, `customevent`, `dom`, `dynamic-range`, `element`, `emsg`, `enterkeyhint`, `eventtarget`, `exif`, `ext-x-daterange`, `face id`, `fetch`, `fmp4`, `font-family`, `graphics tab`, `hdr`, `high dynamic range`, `html`, `html banner`, `image-orientation`, `instant back`, `javascript`, `keyframeeffect`, `line-break`, `logical assignment`, `metadata`, `nullish coalescing`, `observe`, `operators`, `optional chaining`, `paste`, `pdf`, `performance`, `picture-in-picture`, `pointer events`, `pseudo-selector`, `public class fields`, `readtext`, `remote playback`, `replaceall`, `resizeobserver`, `safari technology preview`, `security key`, `service workers`, `svg`, `system-ui`, `texttrackcue`, `touch id`, `ui-sans-serif`, `ui-serif`, `usb key`, `web animations`, `web api`, `web assembly`, `web authentication`, `webauthn`, `web component`, `web inspector`, `webp`, `writetext`, `xhr`, `yubikey`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,336 words)

## Documentation & Resources

- [Safari Technology Preview](https://developer.apple.com/safari/technology-preview/) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/safari/technology-preview/
- [Safari Release Notes](https://developer.apple.com/documentation/safari-release-notes) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/safari-release-notes
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/safari-release-notes.json
- [WebKit Open Source Project](https://webkit.org) _guide_
- [Web Inspector Reference](https://webkit.org/web-inspector/) _documentation_

## Code Snippets

### Web Animations API code example — [4:22]

```javascript
// Web Animations API Code Example

let needle = document.getElementById("needle");
let logo = document.getElementById("logo");
logo.addEventListener("click", () => {
    needle.animate({
        transform: [
            "rotateX(35deg) rotateZ(13deg)", 
            "rotateX(35deg) rotateZ(733deg)",
        ],
        easing: ["ease-out"],
    }, 800);
});
```

### Resize observer example — [6:43]

```javascript
// Resize Observer Example

let formatPanelObserver = new ResizeObserver((entries) => {
    entries.forEach((entry) => {
        let container = entry.target;
        container.classList.toggle("small", entry.contentRect.width < 175);
   }
});

formatPanelObserver.observe(document.getElementById("format-panel"));
```

### Async Clipboard API plain text programmatic copy — [8:15]

```javascript
// Programmatic copy
copyButtonElement.addEventListener("click", (event) => {
    navigator.clipboard.writeText("Plain text to copy.").then(() => {
       // Successful copy
    }, () => {
       // Copy failed
    });
});
```

### Async Clipboard API plain text examples — [8:22]

```javascript
// Programmatic copy
copyButtonElement.addEventListener("click", (event) => {
    navigator.clipboard.writeText("Plain text to copy.").then(() => {
       // Successful copy
    }, () => {
       // Copy failed
    });
});

// Programmatic paste
pasteButtonElement.addEventListener("click", (event) => {
    navigator.clipboard.readText().then((clipText) => {
        document.querySelector(".editor").innerText += clipText);
    });
});
```

### Web Component example markup — [10:25]

```xml
<template id="format-button">
    <button class="format">
        <span class="icon"></span>
        <span class="label"></span>
    </button>
</template>
```

### Registering the Web Component — [10:36]

```javascript
let template = document.getElementById("format-button");
window.customElements.define(template.id, class extends HTMLElement {
    constructor() {
        super();

        this.attachShadow({mode: "open"});
        let newButtonElement = template.content.cloneNode(true);

        let parts = newButtonElement.querySelectorAll("span");
        parts[0].textContent = this.getAttribute("data-icon");
        parts[1].textContent = this.textContent;

        this.shadowRoot.appendChild(newButtonElement);
        this.addEventListener("click", this.handleClick.bind(this));
    }
});
```

### Web Component custom elements — [11:02]

```xml
<format-button id="bold" data-icon="B">Bold</format-button>
<format-button id="italic" data-icon="I">Italic</format-button>
<format-button id="underline" data-icon="U">Underline</format-button>
<format-button id="strikethrough" data-icon="S">Strikethrough</format-button>
<format-button id="paste" data-icon="&#x1f4cb;">Paste</format-button>
```

### Original example Web Component template — [12:28]

```xml
<template id="format-button">
    <button class="format">
        <span class="icon"></span>
        <span class="label"></span>
    </button>
</template>
```

### Example Web Component template with CSS Shadow Parts — [12:30]

```xml
<template id="format-button">
    <button class="format">
        <span part="icon" class="icon"></span>
        <span part="label" class="label"></span>
    </button>
</template>
```

### CSS Shadow Part styles — [12:38]

```swift
#bold::part(icon) {
    color: var(--formatting-button-icon-color);
    font-weight: bold;
}

#italic::part(icon) {
    color: var(--formatting-button-icon-color);
    font-style: italic;
}

#underline::part(icon) {
    color: var(--formatting-button-icon-color);
    text-decoration: underline;
}
```

### HTML enterkeyhint attribute — [13:16]

```xml
<div id="editor" contenteditable="true" enterkeyhint="send"></div>
```

### System font families — [14:32]

```swift
font-family: system-ui;
font-family: ui-sans-serif;
font-family: ui-serif;
font-family: ui-monospace;
font-family: ui-rounded;
```

### San Francisco font family — [14:45]

```swift
body {
    font-family: system-ui;
    font-family: ui-sans-serif;
}
```

### New York font family — [14:53]

```swift
body {
   font-family: ui-serif;
}
```

### SF Mono font family — [14:58]

```swift
body {
   font-family: ui-monospace;
}
```

### SF Rounded font family — [15:03]

```swift
body {
   font-family: ui-rounded;
}
```

### line-break: auto — [16:07]

```swift
code {
    line-break: auto;
}
```

### line-break: anywhere — [16:43]

```swift
code {
    line-break: anywhere;
}
```

### Removing margins from subsequent headings — [17:25]

```swift
h1, h2, h3, h4, h5, h6 {
    margin-top: 3em;
}

h1 + h2,
h2 + h3,
h3 + h4,
h4 + h5,
h5 + h6 {
    margin-top: 0;
}
```

### Removing margins from any subsequent headings — [17:56]

```swift
h1, h2, h3, h4, h5, h6 {
    margin-top: 3em;
}

h1 + h2, h1 + h3, h1 + h4, h1 + h5, h1 + h6,
h2 + h3, h2 + h3, h2 + h4, h2 + h5, h2 + h6,
h3 + h4, h3 + h3, h3 + h4, h3 + h5, h3 + h6,
h4 + h5, h4 + h3, h4 + h4, h4 + h5, h4 + h6,
h5 + h6, h5 + h3, h5 + h4, h5 + h5, h5 + h6 {
    margin-top: 0;
}
```

### Using :is() to remove margins from subsequent headings — [18:02]

```swift
h1, h2, h3, h4, h5, h6 {
    margin-top: 3em;
}

:is(h1, h2, h3, h4, h5, h6) + :is(h1, h2, h3, h4, h5, h6) {
    margin-top: 0;
}
```

### :is() specificity prevents the override from working — [18:31]

```swift
:is(.intro, .pullquote, #hero) + p {
    text-transform: uppercase;
}

h2 + p,
h3 + p,
h4 + p,
h5 + p,
h6 + p {
    text-transform: none;
}
```

### :where () resets specificity — [19:07]

```swift
:where(.intro, .pullquote, #hero) + p {
    text-transform: uppercase;
}
h2 + p,
h3 + p,
h4 + p,
h5 + p,
h6 + p {
    text-transform: none;
}
```

### WebP graceful fallback to JPG — [19:53]

```xml
<picture>
  <source srcset="example.webp" type="image/webp">
  <img src="example.jpg" alt="Example Image">
</picture>
```

### WebP graceful fallback to JPG and server-side detection — [19:54]

```xml
<picture>
  <source srcset="example.webp" type="image/webp">
  <img src="example.jpg" alt="Example Image">
</picture>

Accept: image/webp,image/png,image/svg+xml,image/*;…
```

### Image with no size attributes — [21:17]

```xml
<img src="MexicoCity.png">
```

### Image with size attributes — [21:19]

```xml
<img src="MexicoCity.png" width="560" height="747">
```

### Respect EXIF image orientation default behavior — [21:49]

```swift
image-orientation: from-image;
```

### Override image orientation to use the raw image capture — [22:13]

```swift
image-orientation: none;
```

### HDR display CSS media query — [22:37]

```xml
<style>
@media only screen (dynamic-range: high) {
    /* HDR-only CSS rules */
}
</style>
```

### HDR display CSS media query and JavaScript matchMedia detection — [22:42]

```xml
<style>
@media only screen (dynamic-range: high) {
    /* HDR-only CSS rules */
}
</style>

<script>
if (window.matchMedia("dynamic-range: high")) {
    // HDR-specific JavaScript
}
</script>
```

### Remote Playback API example — [23:19]

```xml
<video id="videoElement" src="https://site.example/video.mp4"></video>
<button id="deviceButton">Send video to a remote device</button>

<script>
    let videoElement = document.getElementById("videoElement");
    let deviceButton = document.getElementById("deviceButton");
    deviceButton.addEventListener("click", (event) => {
        videoElement.remote.prompt().then(updateRemotePlaybackState);
    });
</script>
```

### Picture in Picture example — [24:20]

```xml
<video id="videoElement" src="https://site.example/video.mp4"></video>
<button id="pipButton">Enter picture-in-picture mode</button>

<script>
    let videoElement = document.getElementById("videoElement");
    let pipButton = document.getElementById("pipButton");
    pipButton.addEventListener("click", (event) => {
        videoElement.requestPictureInPicture().then(handlePictureInPicture);
    });
</script>
```

### BigInt example with division examples — [27:11]

```javascript
let bigInt = BigInt(Number.MAX_SAFE_INTEGER);
// 9007199254740991n

console.log(8n / 2n);
// 4n

console.log(9n / 2n);
// 4n
```

### Nullish coalescing operator — [28:02]

```javascript
class Person {
    constructor(firstName, lastName, age) {
        this.firstName = firstName ?? "Unknown";
        this.lastName = lastName ?? "Unknown";
        this.age = age ?? NaN;
   }
}

console.log(new Person());  
// { firstName: "Unknown", lastName: "Unknown", age: NaN }

console.log(new Person(false, false, true));
// { firstName: false, lastName: false, age: true }

console.log(new Person("John", "", 0));  
// { firstName: "John", lastName: "", age: 0 }

console.log(new Person("John", "Appleseed", 42));  
// { firstName: "John", lastName: "Appleseed", age: 42 }
```

### JavaScript optional chaining example — [29:09]

```javascript
class Person {
    constructor(firstName, lastName, age) {
        this.firstName = firstName ?? "Unknown";
        this.lastName = lastName ?? "Unknown";
        this.age = age ?? NaN;
        this.name = { firstName: this.firstName, lastName: this.lastName };
  }
}

function register(person) {
    // Before optional chaining
    if (person !== undefined && person.name !== undefined)
        console.log(person.name.firstName);
}

register(new Person());
// undefined

register(new Person("John", "Appleseed"));
// "John"
```

### JavaScript optional chaining example — [29:41]

```javascript
class Person {
    constructor(firstName, lastName, age) {
        this.firstName = firstName ?? "Unknown";
        this.lastName = lastName ?? "Unknown";
        this.age = age ?? NaN;
        this.name = { firstName: this.firstName, lastName: this.lastName };
  }
}

function register(person) {
    // With optional chaining
    console.log(person?.name.firstName);
}

register(new Person());
􀆊 undefined

register(new Person("John", "Appleseed"));
􀆊 "John"
```

### JavaScript optional chaining with indexes — [29:49]

```javascript
// Without optional chaining
console.log(person.children[0]);
// TypeError: undefined is not an object

// With optional chaining
console.log(person.children?.[0]);
// undefined
```

### JavaScript optional chaining with methods — [30:02]

```javascript
// Without optional chaining
console.log(person.fullName());
􀆊 TypeError: person.fullName is not a function.

// With optional chaining
console.log(person.fullName?.());
􀆊 undefined
```

### Logical assignment operators — [30:23]

```javascript
a &&= b // and assignment operator
a ||= b // or assignment operator
a ??= b // nullish assignment operator
```

### Nullish coalescing approach — [30:44]

```javascript
// Nullish coalescing approach
element.innerHTML = element.innerHTML ?? "Hello World!"
```

### Logical assignment operator — [30:52]

```swift
a &&= b // and assignment operator
a ||= b // or assignment operator
a ??= b // nullish assignment operator

// Nullish coalescing approach
element.innerHTML = element.innerHTML ?? "Hello World!"

// Logical assignment operator
element.innerHTML ??= "Hello World!"
```

### Public class fields — [30:53]

```javascript
class Person {
    firstName = "";
    lastName = "";
    age = NaN;
    children = [];

    constructor(firstName, lastName, age) {
        this.firstName = firstName ?? "Unknown";
        this.lastName = lastName ?? "Unknown";
        this.age = age ?? NaN;
    }
}
```

### String.prototype.replace example — [31:58]

```javascript
"This doesn't work, and doesn't make sense".replace ("doesn't", "does");
› This does work, and doesn't make sense
```

### String.prototype.replaceAll example — [32:09]

```javascript
"This doesn't work, and doesn't make sense".replaceAll("doesn't",
"does");
› This does work, and does make sense
```

### App Clips banner — [33:53]

```xml
<meta name="apple-itunes-app"
content="app-id=myAppStoreID,
         app-clip-bundle-id=clipBundleID,
         affiliate-data=myAffiliateData,
         app-argument=myURL">
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10663/5/07AE41F3-7DC1-47F7-BD89-EF68948C4935/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10663) — developer.apple.com. Indexed for agent consumption._