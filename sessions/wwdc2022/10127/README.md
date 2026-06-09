---
id: "wwdc2022-10127"
event: "wwdc2022"
year: 2022
title: "Create parametric 3D room scans with RoomPlan"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10127"
topics: ["Photos & Camera", "Spatial Computing"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Create parametric 3D room scans with RoomPlan

**Event:** WWDC22 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10127](https://developer.apple.com/videos/play/wwdc2022/10127)

RoomPlan can help your app quickly create simplified parametric 3D scans of a room. Learn how you can use this API to easily add a room scanning experience. We'll show you how to adopt this API, explore the 3D parametric output, and share best practices to help your app get great results with every scan.

**Keywords:** `ar`, `arkit`, `augmented reality`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,140 words)

## Documentation & Resources

- [Create a 3D model of an interior room by guiding the user through an AR experience](https://developer.apple.com/documentation/RoomPlan/create-a-3d-model-of-an-interior-room-by-guiding-the-user-through-an-ar-experience) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RoomPlan/create-a-3d-model-of-an-interior-room-by-guiding-the-user-through-an-ar-experience
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RoomPlan/create-a-3d-model-of-an-interior-room-by-guiding-the-user-through-an-ar-experience.json
- [RoomPlan](https://developer.apple.com/documentation/RoomPlan) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RoomPlan
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RoomPlan.json

## Code Snippets

### RoomCaptureView API - Scan & Process — [4:36]

```swift
// RoomCaptureView API - Scan & Process

import UIKit
import RoomPlan

class RoomCaptureViewController: UIViewController {

    var roomCaptureView: RoomCaptureView
    var captureSessionConfig: RoomCaptureSession.Configuration

   private func startSession() {
        roomCaptureView?.captureSession.run(configuration: captureSessionConfig)
     }

    private func stopSession() {
        roomCaptureView?.captureSession.stop()
	}
}
```

### RoomCaptureView API - Export — [5:00]

```swift
// RoomCaptureView API - Export

import UIKit
import RoomPlan

class RoomCaptureViewController: UIViewController {
  …
  func captureView(shouldPresent roomDataForProcessing: CapturedRoomData, error: Error?) -> Bool {
    // Optionally opt out of post processed scan results.
    return false
  }

  func captureView(didPresent processedResult: CapturedRoom, error: Error?) {
    // Handle final, post processed results and optional error.
    // Export processedResults
    …
    try processedResult.export(to: destinationURL)
    …
  }
}
```

### RoomCaptureSession - setup previewVisualizer — [6:50]

```swift
import UIKit
import RealityKit
import RoomPlan
import ARKit

class ViewController: UIViewController {
    @IBOutlet weak var arView: ARView!
    var previewVisualizer: Visualizer!
    lazy var captureSession: RoomCaptureSession = {
        let captureSession = RoomCaptureSession()
        arView.session = captureSession.arSession
        return captureSession
    }()
    override func viewDidLoad() {
        super.viewDidLoad()
        captureSession.delegate = self
        // set up previewVisualizer
    }
}
```

### RoomCaptureSession - live results and user instructions — [7:40]

```swift
// Getting live results and user instructions

extension ViewController: RoomCaptureSessionDelegate {

    func captureSession(_ session: RoomCaptureSession,
                        didUpdate room: CapturedRoom) {
        previewVisualizer.update(model: room)
    }

    func captureSession(_ session: RoomCaptureSession,
                   didProvide instruction: Instruction) {
        previewVisualizer.provide(instruction)
    }
}
```

### Setup RoomBuilder — [9:12]

```swift
// RoomBuilder
import UIKit
import RealityKit
import RoomPlan
import ARKit

class ViewController: UIViewController {

    @IBOutlet weak var arView: ARView!
    var previewVisualizer: Visualizer!

    // set up RoomBuilder
    var roomBuilder = RoomBuilder(options: [.beautifyObjects])
}
```

### RoomBuilder - generate final 3D CapturedRoom — [9:30]

```swift
// RoomBuilder with the latest CapturedRoomData to generate final 3D CapturedRoom

extension ViewController: RoomCaptureSessionDelegate
{
    func captureSession(_ session: RoomCaptureSession, 
                        didEndWith data: CapturedRoomData, error: Error?)
    {
        if let error = error {
            print("Error: \(error)")
        }
        Task {
            let finalRoom = try! await roomBuilder.capturedRoom(from: data)
            previewVisualizer.update(model: finalRoom)
        }
    }
}
```

### CapturedRoom and export — [11:20]

```swift
// CapturedRoom and export

public struct CapturedRoom: Codable, Sendable
{
    public let walls: [Surface]
    public let doors: [Surface]
    public let windows: [Surface]
    public let openings: [Surface]
    public let objects: [Object]

    public func export(to url: URL) throws

    // Surface definitions ...

    // Object definitions ...
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10127/3/C6A70FDB-501E-42BB-A50E-9794D4050C07/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10127/3/C6A70FDB-501E-42BB-A50E-9794D4050C07/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10127) — developer.apple.com. Indexed for agent consumption._