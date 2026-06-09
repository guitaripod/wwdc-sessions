---
id: "wwdc2025-233"
event: "wwdc2025"
year: 2025
title: "What’s new in Safari and WebKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/233"
topics: ["App Services", "Safari & Web"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# What’s new in Safari and WebKit

**Event:** WWDC25 · **Topic:** Safari & Web · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-233](https://developer.apple.com/videos/play/wwdc2025/233)

Learn how the latest web technologies in Safari and WebKit can help you create incredible experiences. We’ll highlight different CSS features and how they work, including scroll driven animation, cross document view transitions, and anchor positioning. We’ll also explore new media support across audio, video, images, and icons.

**Keywords:** `css`, `javascript`, `typography`, `webkit`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(6,753 words)

## Documentation & Resources

- [Can I use](https://caniuse.com/) _documentation_
- [Web Speech API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) _documentation_
- [WebKit.org – Report issues to the WebKit open-source project](https://bugs.webkit.org) _documentation_
- [Safari Technology Preview](https://developer.apple.com/safari/technology-preview/) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/safari/technology-preview/
- [WebKit Open Source Project](https://webkit.org) _guide_
- [Submit feedback](http://feedbackassistant.apple.com) _documentation_

## Code Snippets

### Progress bar code scroll() example — [6:18]

```xml
footer::after {
  content: "";
  height: 1em;
  width: 100%;
  background: var(--yellow);
  left: 0;
  bottom: 0;
  position: fixed;
  transform-origin: top left;
  animation: progress-scale linear;
  animation-timeline: scroll();
}

@keyframes progress-scale {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
```

### html an css of text blocks showcasing different code topics — [8:36]

```xml
<section class="topics">
  <h3>What you can learn:</h3>
  <ul class="topics">
     <li class="topic-item">Web Development</li>
     <li class="topic-item">Computer Science</li>
     <li class="topic-item">Data Science</li>
     <!-- additional HTML... -->
  </ul>
</section>

.topic-item {
  background: var(--yellow);  
  border: 1px solid var(--gray);
  /* additional CSS... */  
}
```

### text blocks twisting from the left - animation — [9:12]

```xml
@keyframes in-from-left {
  from {
    opacity: 0;
    transform: scale(.8) rotate(-90deg)   
               translateY(15vh);
  }
}
```

### text blocks twisting from the middle - animation — [9:18]

```xml
@keyframes in-from-middle {
  from {
    opacity: 0;
    transform: scale(.8)   
               translateY(15vh);
  }
```

### text blocks twisting from the right - animation — [9:24]

```xml
@keyframes in-from-right {
  from {
    opacity: 0;
    transform: scale(.8) rotate(90deg)   
               translateY(15vh);
  }
}
```

### view() timeline example with timeline and range — [10:07]

```xml
.topic-item {
  animation-fill-mode: both;
  animation-timeline: view();
  animation-range:
  &:nth-child(3n + 1) { animation-name: in-from-left; }
  &:nth-child(3n + 2) { animation-name: in-from-middle; }
  &:nth-child(3n + 3) { animation-name: in-from-right; }
}
```

### animation range 50% — [12:20]

```xml
.topic-item {
  animation-fill-mode: both;
  animation-timeline: view();
  animation-range: 0% 50%;
  &:nth-child(3n + 1) { animation-name: in-from-left; }
  &:nth-child(3n + 2) { animation-name: in-from-middle; }
  &:nth-child(3n + 3) { animation-name: in-from-right; }
}
```

### simple cross document view transition code — [14:20]

```xml
@view-transition {
    navigation: auto;
}
```

### adding media query for reduced motion — [16:00]

```xml
@view-transition { navigation: auto; }

@media not (prefers-reduced-motion) {
  @keyframes slide-in {
    from { translate: 100vw 0; }
  }
  @keyframes slide-out {
    to { translate: -100vw 0; }
  }
}
```

### adding ids to html for cross document view transition — [16:22]

```xml
<body>
  <nav>
    <!-- additional HTML... -->
  </nav>

    <section class="hero">
      <div class="hero-image">
      <!-- additional HTML... -->
  </main>
  <footer>
    <!-- additional HTML... -->
  </footer>
<body>
```

### slide effect for cross document view transition — [16:58]

```xml
@view-transition { navigation: auto; }

@media not (prefers-reduced-motion) {
  #school-info {
    view-transition-name: main-body;
  }
  ::view-transition-old(main-body) {

  }
  ::view-transition-new(main-body) {

  }
  @keyframes slide-in {
    from { translate:e100vw 0; }
	}
}
```

### nav bar and profile menu — [19:48]

```xml
<nav>
  <h1 class="logo">A-School of Code</h1>
  <ul>
    <li>Courses</li>
    <li>Cohorts</li>
    <li class="profile">
      <img src="https://example.com/saron.jpeg" alt="woman speaking"/>
    </li>
  </ul>
</nav>

<ul class="profile-menu">
  <li>Account</li>
  <li>Settings</li>
  <li>Profile</li>
  <li>Billing</li>
</ul>
```

### adding popover attributes — [20:37]

```xml
<ul class="profile-menu" id="profile-menu" popover>
  <li>Account</li>
  <li>Settings</li>
  <li>Profile</li>
  <li>Billing</li>
</ul>
```

### adding aria to popover target — [20:51]

```xml
<nav>
  <div class="wrapper">
    <h1 class="logo">A-School of Code</h1>
    <ul>
      <li>Courses</li>
      <li>Cohorts</li>
      <li class="profile">
        <button class="profile-button" aria-haspopup="true" popovertarget="profile-menu">                                                 >
          <img src="https://example.com/saron.jpg" alt="woman speaking"/>
        </button>
      </li>
    </ul>
  </div>
</nav>
```

### establishing the anchor — [21:58]

```xml
.profile-button {
  anchor-name: --profile-button;
}

.profile-menu {
  position-anchor: --profile-button;
}
```

### setting the target to top right — [23:25]

```xml
.profile-menu {
  position-anchor: --profile-button;
  position-area: top right;
}
```

### setting the target to bottom center — [23:39]

```swift
.profile-menu {
  position-anchor: --profile-button;
  position-area: bottom center;
}
```

### setting the target to span right — [24:16]

```xml
.profile-menu {
  position-anchor: --profile-button;
  position-area: span-right;
}
```

### setting the target to span left — [24:17]

```xml
.profile-menu {
  position-anchor: --profile-button;
  position-area: span-left;
}
```

### intro to the anchor() function — [27:30]

```xml
.profile-button {
  anchor-name: --profile-button;
}

.profile-menu {
  position-anchor: --profile-button;
  position: absolute;
  top: anchor(bottom);
  left: anchor(left);
}
```

### using calc and units in anchor() function — [28:26]

```xml
.profile-button {
  anchor-name: --profile-button;
}

.profile-menu {
  position-anchor: --profile-button;
  position: absolute;
  top: anchor(bottom);
  left: calc(anchor(left) + 1.5em);
}
```

### adding a text gradient — [29:43]

```xml
.logo {
  background-image: linear-gradient(to 
                    bottom right in hsl, 
                    yellow, orange);
  background-clip: text;
  color: transparent;
}
```

### adding a gradient to border — [31:05]

```xml
.primary-btn {
  background-image: linear-gradient(to 
                    bottom right in hsl, 
                    yellow, orange);
  background-clip: border-area;
  border-color: transparent;
  background-origin: border-box;
}
```

### shorthand for adding gradient to border — [32:15]

```xml
.primary-btn {
  background: border-area linear-gradient(to bottom right in hsl, yellow, orange);
  border-color: transparent;
}
```

### arrow shape using path — [33:33]

```xml
.review-shape {
  clip-path: path("M0 0 L 500 0 L 600 
                   100 L 500 200 L 0 
                   200 Q 100 100 0 0 z");
}
```

### arrow shape using shape() — [35:01]

```xml
.review-shape {
  clip-path: shape(from top left,
    line to calc(100% - 50cqh) 0%,
    line to 100% 50cqh,
    line to calc(100% - 50cqh) 100%,
    line to bottom left,
    curve to top left with 50cqh 50cqh,
    close);
}
```

### dynamic range limit: no limit — [41:42]

```xml
img {
  dynamic-range-limit: no-limit;
}
```

### dynamic range limit: standard — [41:57]

```xml
img {
  dynamic-range-limit: standard;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/233/5/d86dec2f-e399-4978-b704-a5136136da93/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/233/5/d86dec2f-e399-4978-b704-a5136136da93/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/233) — developer.apple.com. Indexed for agent consumption._
