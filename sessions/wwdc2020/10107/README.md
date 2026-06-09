---
id: "wwdc2020-10107"
event: "wwdc2020"
year: 2020
title: "What's new in PencilKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10107"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# What's new in PencilKit

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10107](https://developer.apple.com/videos/play/wwdc2020/10107)

PencilKit helps power creativity, writing, drawing, and animation in your iPad apps. Explore the latest improvements to our drawing and annotation framework, and discover how you can take advantage of APIs like PKToolPicker, PKCanvasView, and PKStroke to support new features in illustration and writing apps. 

To get the most out of this session, you should have a basic understanding of PencilKit. If you want to a refresher, “Introduction to PencilKit” from WWDC19 is a great place to start.

**Keywords:** `color`, `engine`, `handwriting`, `palette`, `pallette`, `pencil`, `pencilkit`, `pkstrokes`, `scribble`, `strokes`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,542 words)

## Documentation & Resources

- [Drawing with PencilKit](https://developer.apple.com/documentation/PencilKit/drawing-with-pencilkit) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PencilKit/drawing-with-pencilkit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PencilKit/drawing-with-pencilkit.json

## Code Snippets

### PKCanvasView drawingPolicy — [5:21]

```swift
var drawingPolicy: PKCanvasViewDrawingPolicy
```

### PKToolPicker showDrawingPolicyControls — [7:06]

```swift
PKToolPicker.showsDrawingPolicyControls
```

### Toolpicker per canvas — [8:40]

```swift
notesCanvas.drawingPolicy = .default
notesToolPicker.showsDrawingPolicyControls = true
notesToolPicker.selectedTool = PKInkingTool(.pen, color: .black, width: 2)

drawingCanvas.drawingPolicy = .anyInput
drawingToolPicker.showsDrawingPolicyControls = false
drawingToolPicker.selectedTool = PKInkingTool(.marker, color: .purple, width: 20)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10107/4/91342955-14B4-436D-AE84-4FAA3BCC547F/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10107) — developer.apple.com. Indexed for agent consumption._