---
id: "wwdc2024-10105"
event: "wwdc2024"
year: 2024
title: "What’s new in Quick Look for visionOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10105"
topics: ["Graphics & Games", "Safari & Web", "Spatial Computing"]
platforms: ["visionOS"]
hasTranscript: true
---

# What’s new in Quick Look for visionOS

**Event:** WWDC24 · **Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2024-06-13 · **Session:** [wwdc2024-10105](https://developer.apple.com/videos/play/wwdc2024/10105)

Explore how Quick Look in visionOS can elevate file preview and editing experiences in your app. We’ll cover the integration of in-app and windowed Quick Look, as well as a brand-new API that customizes the windowed Quick Look experience in your app. We’ll also share the latest enhancements to viewing 3D models within Quick Look.

**Keywords:** `quick look`, `reality`, `reality composer pro`, `spatial computing`, `spatial tracking`, `usdz`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,839 words)

## Documentation & Resources

- [Forum: Spatial Computing](https://developer.apple.com/forums/topics/spatial-computing?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/spatial-computing?cid=vf-a-0010

## Code Snippets

### Variants USDZ — [12:22]

```objectivec
#usda 1.0
(
	defaultPrim = "iPhone"
)

def Xform "iPhone" (
	variants = {
		string Color = "Black_Titanium"
	}
	prepend variantSets = ["Color"]
)
{
	variantSet "Color" = {
		"Black_Titanium" { }
		"Blue_Titanium" { }
		"Natural_Titanium" { }
		"White_Titanium" { }
 }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10105/5/9DD1E3E1-8BCD-498A-9045-F2251FFDF077/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10105/5/9DD1E3E1-8BCD-498A-9045-F2251FFDF077/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10105) — developer.apple.com. Indexed for agent consumption._