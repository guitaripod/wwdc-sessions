---
id: "wwdc2023-10085"
event: "wwdc2023"
year: 2023
title: "Discover Quick Look for spatial computing"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10085"
topics: ["Spatial Computing"]
platforms: ["visionOS"]
hasTranscript: true
---

# Discover Quick Look for spatial computing

**Event:** WWDC23 · **Topic:** Spatial Computing · **Platforms:** visionOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10085](https://developer.apple.com/videos/play/wwdc2023/10085)

Learn how to use Quick Look on visionOS to add powerful previews for 3D content, spatial images and videos, and much more. We’ll show you the different ways that the system presents these experiences, demonstrate how someone can drag and drop Quick Look content from an app or website to create a separate window with that content, and explore how you can present Quick Look directly within an app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,912 words)

## Code Snippets

### drag support for quick look from apps — [5:15]

```swift
import Foundation
import SwiftUI
import UniformTypeIdentifiers

struct FileList: View {

    @State var files: [File]
    @State var previewedURL: URL? = nil
    @State var selectedFile: File? {
        didSet {
            self.previewedURL = selectedFile?.url
        }
    }

    var body: some View {
        List(files, selection: $selectedFile) { file in
            Button(file.name) {
                selectedFile = file
            }
            .onDrag {
                return NSItemProvider(contentsOf: file.url) ?? NSItemProvider()
            }
        }
    }
}
```

### swiftUI quick look preview function — [8:45]

```swift
import Foundation import SwiftUI
struct FileList: View {

@State var files: [File]
@State var previewedURL: URL? = nil
@State var selectedFile: File? {
	didSet {
		self.previewedURL = selectedFile?.url
		}
  }

var body: some View {
	List(files, selection: $selectedFile) { file in
			Button(file.name) {
				selectedFile = file
			}
		}
		.quickLookPreview($previewedURL, in: files.map { $0.url })
  	}
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10085/4/6383EC8A-F55A-4286-A743-31FE670C9CD7/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10085/4/6383EC8A-F55A-4286-A743-31FE670C9CD7/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10085) — developer.apple.com. Indexed for agent consumption._
