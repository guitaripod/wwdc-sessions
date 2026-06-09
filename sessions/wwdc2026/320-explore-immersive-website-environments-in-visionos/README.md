---
id: "wwdc2026-320"
event: "wwdc2026"
year: 2026
title: "Explore immersive website environments in visionOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/320"
topics: ["Spatial Computing", "Safari & Web"]
platforms: ["visionOS"]
hasTranscript: true
---

# Explore immersive website environments in visionOS

**Event:** WWDC26 · **Topic:** Safari & Web · **Platforms:** visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-320](https://developer.apple.com/videos/play/wwdc2026/320)

Transport your website’s visitors into virtual environments in Apple Vision Pro using the new Immersive API in JavaScript. Explore how to request immersive transitions from an inline model element, create compelling immersive experiences using features like video docking, and optimize performance for rich, real-world-scale experiences — all with just a few lines of code running on your website.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,966 words)

## Documentation & Resources

- [Download - Immersive model add-on for Blender](https://developer.apple.com/download/files/web-env-blender-plugin.zip) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/download/files/web-env-blender-plugin.zip
- [WebKit.org - Theater Ticket Sales immersive website environment demo for Apple Vision Pro](https://webkit.org/demos/model-demos/ticket-sales.html) _documentation_
- [WebKit.org - Escape Game immersive website demo for Apple Vision Pro](https://webkit.org/demos/model-demos/escape-room.html) _documentation_
- [GitHub: Spatial Backdrop explainer](https://github.com/WebKit/explainers/tree/main/spatial-backdrop) _documentation_
- [WebKit.org – Report issues to the WebKit open-source project](https://bugs.webkit.org) _documentation_
- [Submit feedback](http://feedbackassistant.apple.com) _documentation_

## Code Snippets

### Basic model element — [1:51]

```xml
<model src="teapot.usdz">
</model>
```

### Model element with environment map — [2:06]

```xml
<model src="teapot.usdz"
	environmentmap="kitchen.hdr">
</model>
```

### Adding the environment model on the page for inline preview — [4:40]

```xml
<div class="seat-preview">
	<model id="theater"
		   src="theater-model.usdz"
		   environmentmap="theater-lighting.hdr">
	</model>
</div>
```

### Reset the model entity transform — [5:14]

```javascript
const theater = document.getElementById("theater");

async function updateModelTransform() {
	// Make sure the model is loaded
	await theater.ready;
	// Create a transform matrix
	const identity = new DOMMatrix();
	// Apply the transform matrix to the model
	theater.entityTransform = identity;
}

updateModelTransform();
```

### Translate the model down — [5:42]

```javascript
const theater = document.getElementById("theater");

async function updateModelTransform() {
	// Make sure the model is loaded
	await theater.ready;
	// Create a transform matrix
	const transform = new DOMMatrix();
	// Translate model down, for eye level preview
	transform.translateSelf(
		0, 			// x
		-1.0, 	// y
		0 			// z
	);
	// Apply the transform matrix to the model
	theater.entityTransform = transform;
}

updateModelTransform();
```

### Build the seat transform — [6:40]

```javascript
function buildTransform(seat) {
	const transform = new DOMMatrix();
	const { x, y, z, ry } = seat;
	// Rotate and translate the model to match 
  // the seat's origin and orientation
	transform.rotateSelf(0, -ry, 0);
	transform.translateSelf(-x, -y, -z);
	// Translate the model down, for eye level preview
	transform.translateSelf(0, -1.0, 0);
	return transform;
}
```

### Detect feature availability — [7:16]

```javascript
if (document.immersiveEnabled) {
	immersiveButton.hidden = false;
}
```

### Request the immersive transition on the model — [7:34]

```javascript
immersiveButton.addEventListener("click", async () => {
	await model.requestImmersive();
});
```

### Build immersive transform — [8:24]

```javascript
function buildTransform(seat, immersive) {
	const transform = new DOMMatrix();
	// [...] Seat transform logic
	if (immersive) {
		// Rotate to the left
		transform.rotateSelf(
			0,		// x
			45,		// y
			0			// z
		);
	} else {
		// [...] Eye level translation
	}
	return transform;
}
```

### Update the entity transform and the layout on immersive state updates — [9:01]

```javascript
theater.addEventListener("immersivechange", () => {
	const isImmersive = !!document.immersiveElement;
	const transform = buildTransform(isImmersive, currentSeat);
	theater.entityTransform = transform;
  document.body.classList.toggle("immersive", isImmersive);
});
```

### Hide the inline preview — [10:53]

```xml
<model id="escapeRoom"
	   src="escape-room.usdz"
	   environmentmap="room-lighting.hdr"
	   style="display: none">
</model>
```

### Request an immersive transition on the escape room model — [11:25]

```javascript
const enterButton = document.getElementById("enterButton");
const escapeRoom = document.getElementById("escapeRoom");

enterButton.addEventListener("click", () => {
    await escapeRoom.requestImmersive();
});
```

### Handle the request result and show a loading animation — [11:52]

```javascript
enterButton.addEventListener("click", async () => {
	showLoadingAnimation();            
	try {
		await escapeRoom.requestImmersive();
	} catch (error) {
		console.log(error);
	} finally {
		hideLoadingAnimation();
	}
});
```

### Dock the video in the environment with the fullscreen API — [13:16]

```javascript
const trailerVideo = document.getElementById("trailerVideo");
const demoButton = document.getElementById("demoButton");

demoButton.addEventListener("click", async () => {
	await trailerVideo.requestFullscreen();
});
```

### Play the model animation — [14:01]

```javascript
const trailerVideo = document.getElementById("trailerVideo");
const escapeRoom = document.getElementById("escapeRoom");

trailerVideo.addEventListener("ended", async () => {
	await document.exitFullscreen();
	escapeRoom.play();
});
```

### Compress your USDZ with usdcrush — [16:38]

```bash
usdcrush model.usdz -o optimized.usdz
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/320/4/e1844891-477b-4612-ad8d-10e55bf395ba/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/320/4/e1844891-477b-4612-ad8d-10e55bf395ba/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/320) — developer.apple.com. Indexed for agent consumption._
