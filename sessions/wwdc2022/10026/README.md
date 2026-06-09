---
id: "wwdc2022-10026"
event: "wwdc2022"
year: 2022
title: "Add Live Text interaction to your app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10026"
topics: ["Photos & Camera", "App Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Add Live Text interaction to your app

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10026](https://developer.apple.com/videos/play/wwdc2022/10026)

Learn how you can bring Live Text support for still photos or paused video frames to your app. We'll share how you can easily enable text interactions, translation, data detection, and QR code scanning within any image view on iOS, iPadOS, or macOS. We'll also go over how to control interaction types, manage the supplementary interface, and resolve potential gesture conflicts.

To learn more about capturing and interacting with detected data in live camera feeds, watch "Capture machine-readable codes and text with VisionKit" from WWDC22.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,205 words)

## Documentation & Resources

- [Enabling Live Text interactions with images](https://developer.apple.com/documentation/VisionKit/enabling-live-text-interactions-with-images) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/VisionKit/enabling-live-text-interactions-with-images
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/VisionKit/enabling-live-text-interactions-with-images.json

## Code Snippets

### Live Text Sample Adoption — [2:37]

```swift
import UIKit
import VisionKit

class LiveTextDemoController: BaseController, ImageAnalysisInteractionDelegate, UIGestureRecognizerDelegate {

    let analyzer = ImageAnalyzer()
    let interaction = ImageAnalysisInteraction()

    override func viewDidLoad() {
        super.viewDidLoad()
        imageview.addInteraction(interaction)
    }

    override var image: UIImage? {
        didSet {
            interaction.preferredInteractionTypes = []
            interaction.analysis = nil
            analyzeCurrentImage()
        }
    }

    func analyzeCurrentImage() {
        if let image = image {
            Task {
               let configuration = ImageAnalyzer.Configuration([.text, .machineReadableCode])
                do {
                    let analysis = try await analyzer.analyze(image, configuration: configuration)
                    if let analysis = analysis, image == self.image {
                        interaction.analysis = analysis;
                        interaction.preferredInteractionTypes = .automatic
                    }
                }
                catch {
                    // Handle error…
                }
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10026/3/346C760E-A60C-4D64-89A7-26C888CBBE0E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10026/3/346C760E-A60C-4D64-89A7-26C888CBBE0E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10026) — developer.apple.com. Indexed for agent consumption._