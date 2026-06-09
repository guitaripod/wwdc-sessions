---
id: "wwdc2020-10604"
event: "wwdc2020"
year: 2020
title: "Shop online with AR Quick Look"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10604"
topics: ["App Services", "Graphics & Games", "Safari & Web", "Spatial Computing"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Shop online with AR Quick Look

**Event:** WWDC20 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10604](https://developer.apple.com/videos/play/wwdc2020/10604)

AR Quick Look adds a new dimension to online shopping: We'll show you how to easily showcase your products in augmented reality for a "try before you buy" experience. Discover how to display a product banner in AR Quick Look, integrate Apple Pay, or display custom actions like "add to cart".

To get the most out of this session, we recommend you familiarize yourself with “Advances in AR Quick Look” from WWDC 2019. 

Once you’ve discovered the potential of AR Quick Look and Apple Pay to create interactive online shopping experiences, learn more about creating 3D objects and attaching interactions to them by watching “What's new in USD.”

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,800 words)

## Documentation & Resources

- [Acceptable Use Guidelines for Apple Pay on the Web](https://developer.apple.com/apple-pay/acceptable-use-guidelines-for-websites/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/apple-pay/acceptable-use-guidelines-for-websites/
- [Adding an Apple Pay Button or a Custom Action in AR Quick Look](https://developer.apple.com/documentation/ARKit/adding-an-apple-pay-button-or-a-custom-action-in-ar-quick-look) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit/adding-an-apple-pay-button-or-a-custom-action-in-ar-quick-look
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit/adding-an-apple-pay-button-or-a-custom-action-in-ar-quick-look.json
- [AR Quick Look Gallery](https://developer.apple.com/arkit/gallery) _download_
  - Markdown (sosumi.ai): https://sosumi.ai/arkit/gallery
- [ARKit](https://developer.apple.com/documentation/ARKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ARKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ARKit.json

## Code Snippets

### Customization Options - Recap — [5:47]

```javascript
<a rel="ar" href="alarm-clock.usdz#canonicalWebPageURL=https://developer.apple.com/alarm-clock-product-page/&allowsContentScaling=0">
    <img src="alarm-clock-thumbnail.jpg">
</a>
```

### Apple Pay Banner — [8:53]

```javascript
<a rel="ar" id="ar-link" href="alarm-clock.usdz#applePayButtonType=plain&checkoutTitle=Retro%20Alarm%20Clock&checkoutSubtitle=Charming%20old-school%20look%20with%20built-in%20FM%20tuner&price=$92.50">
    <img src="alarm-clock-thumbnail.jpg">
</a>
```

### Custom Action Banner — [11:42]

```javascript
<a rel="ar" id="ar-link" href="kids-slide.usdz#callToAction=Preorder&checkoutTitle=Kids%20Slide&checkoutSubtitle=Enjoy%20the%20playground,%20right%20from%20your%20home&price=$145">
    <img src="kids-slide-thumbnail.jpg">
</a>
```

### Custom Banner — [13:39]

```javascript
<a rel="ar" id="ar-link" href="solar-panels.usdz#custom=https://developer.apple.com/solar_panels_banner.html&customHeight=small">
    <img src="solar-panels-thumbnail.jpg">
</a>
```

### Custom Banner - Medium Height — [14:04]

```javascript
<a rel="ar" id="ar-link" href="solar-panels.usdz#custom=https://developer.apple.com/solar_panels_banner.html&customHeight=medium">
    <img src="solar-panels-thumbnail.jpg">
</a>
```

### Custom Banner - Large Height — [14:09]

```javascript
<a rel="ar" id="ar-link" href="solar-panels.usdz#custom=https://developer.apple.com/solar_panels_banner.html&customHeight=large">
    <img src="solar-panels-thumbnail.jpg">
</a>
```

### Full Apple Pay with Event Listener Example — [16:31]

```javascript
<a rel="ar" id="ar-link" href="alarm-clock.usdz#applePayButtonType=plain&checkoutTitle=Retro%20Alarm%20Clock&checkoutSubtitle=Charming%20old-school%20look%20with%20built-in%20FM%20tuner&price=$92.50">
    <img src="alarm-clock-thumbnail.jpg">
</a>



<script type="application/javascript">
    const linkElement = document.getElementById("ar-link");
    linkElement.addEventListener("message", function (event) {
        if (event.data == "_apple_ar_quicklook_button_tapped") {
            // handle the user tap.   
        }
    }, false);
</script>
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10604/7/5565A027-6950-4B1D-804F-2A555245FBA3/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10604) — developer.apple.com. Indexed for agent consumption._