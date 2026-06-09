---
id: "wwdc2025-237"
event: "wwdc2025"
year: 2025
title: "What’s new for the spatial web"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/237"
topics: ["Spatial Computing", "Safari & Web"]
platforms: ["visionOS"]
hasTranscript: true
---

# What’s new for the spatial web

**Event:** WWDC25 · **Topic:** Safari & Web · **Platforms:** visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-237](https://developer.apple.com/videos/play/wwdc2025/237)

Discover the latest spatial features for the web on visionOS 26. We’ll cover how to display inline 3D models with the brand new HTML model element. And we’ll share powerful features, including model lighting, interactions, and animations. Learn how to embed newly supported immersive media on your web site, such as 360-degree video and Apple Immersive Video. And get a sneak peek at adding a custom environment to your web pages.

**Keywords:** `animation`, `javascript`, `model`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,437 words)

## Documentation & Resources

- [The HTML model element in Apple Vision Pro](https://webkit.org/blog/17118/a-step-into-the-spatial-web-the-html-model-element-in-apple-vision-pro/) _documentation_
- [GitHub: model element samples](https://immersive-web.github.io/model-element-samples/) _samplecode_
- [GitHub: Spatial Backdrop explainer](https://github.com/WebKit/explainers/tree/main/spatial-backdrop) _documentation_
- [GitHub: <model> element that displays 3D explainer](https://github.com/immersive-web/model-element/blob/main/explainer.md) _documentation_
- [MDN: Properly configuring server MIME types](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Configuring_server_MIME_types) _documentation_
- [QuickLook example files](https://developer.apple.com/augmented-reality/quick-look/) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/augmented-reality/quick-look/
- [Learn more about Reality Composer](https://developer.apple.com/augmented-reality/reality-composer/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/augmented-reality/reality-composer/

## Code Snippets

### Embed 3D models - Basic syntax — [1:00]

```xml
<model src="teapot.usdz"></model>
```

### Embed 3D models with source element — [4:15]

```xml
<model>
  <source src="teapot.usdz" type="model/vnd.usdz+zip">
</model>
```

### Example server configurations to add USDZ MIME type support — [5:30]

```markdown
# Apache

```
AddType model/vnd.usdz+zip .usdz
```

# NGINX mime.types

```
types {
  ...
  model/vnd.usdz+zip usdz;
}
```

# Python HTTP server

```
import http.server
Handler = http.server.SimpleHTTPRequestHandle
Handler.extensions_map = { ".usdz": "model/vnd.usdz+zip" }
httpd = http.server.HTTPServer(("", 8000), Handler)
httpd.serve_forever()
```
```

### Specify a fall back image for <model> element — [5:51]

```xml
<model src="camera.usdz">
  <img src="camera.png">
</model>
```

### Example 2D rendering fallback experience — [6:17]

```xml
<!-- <model-viewer> library from https://modelviewer.dev/ -->
<script type="module" 
  src="https://ajax.googleapis.com/ajax/libs/model-viewer/4.0.0/model-viewer.min.js">
</script>

<model src="camera.usdz">
  <!-- Fallback experience for backward compatibility -->  
  <model-viewer src="camera.glb"></model-viewer>
</model>
```

### Detect if the model element is supported — [6:52]

```javascript
if (window.HTMLModelElement) {
  // Supported by this browser
} else {
  // Not supported by this browser
}
```

### Implementing a loading indicator using .ready promise — [7:32]

```xml
<model src="camera.usdz" id="mymodel"></model>

<script>
const mymodel = document.getElementById("mymodel");

if (window.HTMLModelElement) {
  mymodel.ready.then(result => {
	// Hide the loading indicator
	// Show the model
 }).catch(error => {
	// Loading error occurred, show a retry button
 });
}
</script>
```

### CSS example for setting the color of the virtual space — [8:23]

```xml
<body>
  <!-- page content here -->
  <model src="camera.usdz" class="my_model"></model>
</body>

<style>
:root {
  --main-bg-color: rgb(240, 240, 240);
}

body {
  background-color: var(--main-bg-color);
}

.my_model {
  /* set the virtual space color */
  background-color: var(--main-bg-color); 
}
</style>
```

### CSS example for frosted glass panel on top of a <model> — [9:21]

```xml
<div class="container">
  <model src="camera.usdz"></model>
  <div class="panel"> ... </div>
</div>

<style>
.container {
  position: relative;
}

.panel {
  position: absolute;
  left: 60%;
  backdrop-filter: blur(20px);
  background: linear-gradient(to right,
                              rgba(240, 240, 240, 0.8),
                              rgba(240, 240, 240, 0.5) 4px);
}
</style>
```

### Setting image-based lighting (IBL) with environmentmap — [10:56]

```xml
<model src="camera.usdz" environmentmap="sunset.exr"></model>
```

### Allowing inline rotation with stagemode — [12:41]

```xml
<model src="teapot.usdz" stagemode="orbit"></model>
```

### Customize placement with JavaScript entityTransform — [13:31]

```xml
<model src="teapot.usdz" id="mymodel"></model>

<script>
const mymodel = document.getElementById("mymodel");
mymodel.ready.then(result => {
  const matrix = mymodel.entityTransform; // DOMMatrixReadOnly
});
</script>
```

### Make the model face right with entityTransform — [13:49]

```xml
<model src="teapot.usdz" id="mymodel"></model>
<a onclick="turnRight()">Right</a>

<script>
const mymodel = document.getElementById("mymodel");
function turnRight() {
  const matrix = mymodel.entityTransform; // DOMMatrixReadOnly
  const newMatrix = matrix.rotateAxisAngle(0, 1, 0, 90);
  mymodel.entityTransform = newMatrix;
}
</script>
```

### Setting the entityTransform to an identity matrix — [15:03]

```javascript
model.entityTransform = new DOMMatrix();
```

### Basic animation control — [16:31]

```xml
<model src="toy.usdz" id="mymodel" loop autoplay></model>
<button onclick="toggleAnimation()">Play/Pause</button>

<script>
const mymodel = document.getElementById("mymodel");

function toggleAnimation() {
  if (mymodel.paused) {
	mymodel.play();
  } else {
	mymodel.pause();
  }
}
</script>
```

### Jump to animation timestamp using .currentTime property — [17:35]

```xml
<model src="camera.usdz" id="mymodel"></model>

<script>
const mymodel = document.getElementById("mymodel");

function openFlash() {
  mymodel.currentTime = 1; // Unit is seconds
}

function openScreen() {
  mymodel.currentTime = 3; // Unit is seconds
}
</script>
```

### Update .currentTime with a slider — [18:11]

```xml
<model src="camera.usdz" id="mymodel"></model>
<input type="range" id="slider" min="2" max="3" step="any" value="2">


<script>
const mymodel = document.getElementById("mymodel");

slider.addEventListener("input", (event) => {
  mymodel.currentTime = event.target.value;
});
</script>
```

### Generate USDZ with three.js and display with <model> — [19:35]

```javascript
import * as THREE from "three";
import { USDZExporter } from "three/examples/exporters/USDZExporter.js";

async function generateModel() {
	const scene = new THREE.Scene();
	// ... create a really nice scene procedurally ...

	const bytes = await new USDZExporter().parseAsync(scene);
	const objURL = URL.createObjectURL(new Blob([bytes]));

	const mymodel = document.getElementById("mymodel");
	mymodel.setAttribute("src", objURL);
}
```

### Embed immersive media — [23:10]

```xml
<video src="spatial_video.mov"></video>  <!-- Single file -->
<video src="360_video.m3u8"></video>  <!-- HTTP Live Streaming -->
```

### Going full screen with Javascript for <video> elements — [24:25]

```xml
<video src="360_video.m3u8" id="player" controls></video>

<script>
const player = document.getElementById("player");
player.requestFullScreen();
</script>
```

### Embed panoramas and offer full screen with Javascript — [24:35]

```xml
<picture>
  <source media="(max-width: 799px)" srcset="thumbnail.jpg">
  <source media="(min-width: 800px)" srcset="panorama.jpg">
  <img src="panorama.jpg" id="pano">
</picture>

<script>
const pano = document.getElementById("pano");
pano.requestFullScreen();
</script>
```

### Embed spatial photos and offer full screen with Javascript — [24:57]

```xml
<img src="spatial.heic" id="img">

<script>
const img = document.getElementById("img");
img.requestFullScreen();
</script>
```

### Embed spatial photos with the new "controls" attribute — [25:21]

```xml
<img src="spatial.heic" id="img" controls>
```

### Provide a custom environment — [26:49]

```xml
<link rel="spatial-backdrop" href="office.usdz" environmentmap="lighting.hdr">
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/237/5/f5fcabf4-e9fa-420b-a1a8-3e4868fccca9/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/237/5/f5fcabf4-e9fa-420b-a1a8-3e4868fccca9/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/237) — developer.apple.com. Indexed for agent consumption._
