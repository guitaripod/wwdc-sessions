# Get started with the HTML Model Element

**Topic:** Safari & Web · **Platforms:** iOS, iPadOS, macOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-215](https://developer.apple.com/videos/play/wwdc2026/215)

Learn how the model element brings interactive 3D content to your websites — now on iOS, iPadOS, macOS, and visionOS. Discover tools for creating and optimizing 3D assets. Explore model element’s features and see how web standards are shaping the future of 3D on the web.

**Keywords:** `css`, `html`, `javascript`, `model`, `spatial`, `web`

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [WebKit.org - Theater Ticket Sales immersive website environment demo for Apple Vision Pro](https://webkit.org/demos/model-demos/ticket-sales.html) _documentation_
- [The HTML model element in Apple Vision Pro](https://webkit.org/blog/17118/a-step-into-the-spatial-web-the-html-model-element-in-apple-vision-pro/) _documentation_
- [GitHub: model element samples](https://immersive-web.github.io/model-element-samples/) _samplecode_
- [WebKit.org – Report issues to the WebKit open-source project](https://bugs.webkit.org) _documentation_
- [AOUSD – Alliance for OpenUSD](https://aousd.org) _documentation_
- [w3.org – Model element](https://immersive-web.github.io/model-element) _documentation_
- [Submit feedback](http://feedbackassistant.apple.com) _documentation_

## Code Snippets

### Load a model — [4:19]

```xml
<!-- Using the src attribute -->
<model src="mallet.usdz"></model>

<!-- Using a <source> child for MIME type -->
<model>
    <source src="mallet.usdz" type="model/vnd.usdz+zip">
</model>
```

### Image fallback — [4:39]

```xml
<model id="mallet" src="mallet.usdz">
    <img src="mallet.png"
         alt="Rubber mallet with wooden handle">
</model>
```

### Ready promise — [5:09]

```xml
<model id="mallet" src="mallet.usdz"></model>

<script>
    const model = document.getElementById("mallet");
    model.ready.then(result => {
        // Hide the loading indicator
    }).catch(error => {
        // Loading failed, show fallback
    });
</script>
```

### Polyfill fallback — [5:39]

```xml
<script type="module">
    if (!window.HTMLModelElement) {
        import("model-element-polyfill.js").then(() => {
            // Polyfill ready to use
        });
    }
</script>
```

### Model background — [6:13]

```xml
<model id="mallet" src="mallet.usdz"></model>
<style>
    model {
        background-color: #f4f1ec;
    }
</style>
```

### Stage mode — [6:47]

```xml
<model id="mallet"
       src="mallet.usdz"
       stagemode="orbit">
</model>
```

### Custom transforms — [7:31]

```xml
<model id="boot" src="boot.usdz"></model>
<button id="button-side">Side</button>
<button id="button-reset">Reset</button>

<script>
    const model = document.getElementById("boot");
    const initialTransform = model.entityTransform;

    document.getElementById("button-side")
            .addEventListener("click", () => {
        const transform = new DOMMatrix();
        transform.rotateSelf(0, 135, 0);
        model.entityTransform = transform;
    });

    document.getElementById("button-reset")
            .addEventListener("click", () => {
        model.entityTransform = initialTransform;
    });
</script>
```

### Transition animation — [8:35]

```xml
<script>
    const model = document.getElementById("boot");
    const duration = 500;
    let currentAngle = 0;
    let animationId = null;

    function animateTo(targetAngle) {
        if (animationId) cancelAnimationFrame(animationId);
        const startAngle = currentAngle;
        const startTime = performance.now();

        function step(now) {
            const progress = Math.min((now - startTime) / duration, 1);
            const ease = 1 - Math.pow(1 - progress, 3);
            currentAngle = startAngle + (targetAngle - startAngle) * ease;
            model.entityTransform = new DOMMatrix().rotateSelf(0, currentAngle, 0);
            if (progress < 1) animationId = requestAnimationFrame(step);
        }

        requestAnimationFrame(step);
    }

    document.getElementById("button-side").addEventListener("click", () => animateTo(135));
    document.getElementById("button-reset").addEventListener("click", () => animateTo(0));
</script>
```

### Animation playback — [10:07]

```xml
<model id="bottle" src="bottle.usdz"></model>
<button id="button-play" onclick="play(5)">
    Play
</button>
<button id="button-reverse" onclick="play(-5)">
    Reverse
</button>

<script>
    const model = document.getElementById("bottle");

    function play(rate) {
        model.playbackRate = rate;
        model.play();
    }
</script>
```

### AR Quick Look — [11:06]

```xml
<a rel="ar" href="bottle.usdz">
    <model id="boot" src="bottle.usdz"></model>
</a>
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/215/4/b7d159c9-ee29-45d9-80f5-87b6a1c90565/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/215/4/b7d159c9-ee29-45d9-80f5-87b6a1c90565/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._