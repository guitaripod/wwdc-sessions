---
id: "wwdc2024-10135"
event: "wwdc2024"
year: 2024
title: "What’s new in Xcode 16"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10135"
topics: ["Essentials", "Swift", "SwiftUI & UI Frameworks", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in Xcode 16

**Event:** WWDC24 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10135](https://developer.apple.com/videos/play/wwdc2024/10135)

Discover the latest productivity and performance improvements in Xcode 16. Learn about enhancements to code completion, diagnostics, and Xcode Previews. Find out more about updates in builds and explore improvements in debugging and Instruments.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,994 words)

## Documentation & Resources

- [Previewing your app’s interface in Xcode](https://developer.apple.com/documentation/Xcode/previewing-your-apps-interface-in-xcode) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/previewing-your-apps-interface-in-xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/previewing-your-apps-interface-in-xcode.json
- [Xcode](https://developer.apple.com/xcode/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/xcode/
- [Forum: Developer Tools & Services](https://developer.apple.com/forums/topics/developer-tools-and-services?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/developer-tools-and-services?cid=vf-a-0010
- [Xcode updates](https://developer.apple.com/documentation/Updates/Xcode) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Updates/Xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Updates/Xcode.json

## Code Snippets

### Inline State within Preview — [3:37]

```swift
#Preview {
    @Previewable @State var currentFace = RobotFace.heart
}
```

### View using Inline State — [3:45]

```swift
RobotFaceSelectorView(currentFace: $currentFace)
```

### Complete Preview using Previewable — [3:53]

```swift
#Preview {
    @Previewable @State var currentFace = RobotFace.heart

    RobotFaceSelectorView(currentFace: $currentFace)
}
```

### Type Conforming to PreviewModifier — [4:40]

```swift
struct SampleRobotNamer: PreviewModifier {
    typealias Context = RobotNamer

    static func makeSharedContext() async throws -> Context {
        let url = URL(fileURLWithPath: "/tmp/local_names.txt")
        return try await RobotNamer(url: url)
    }

    func body(content: Content, context: Context) -> some View {
        content.environment(context)
    }
}
```

### Extension on PreviewTrait — [5:29]

```swift
extension PreviewTrait where T == Preview.ViewTraits {
    @MainActor static var sampleNamer: Self = .modifier(SampleRobotNamer())
}
```

### Preview using created PreviewModifier — [5:38]

```swift
#Preview(traits: .sampleNamer) {
    RobotNameSelectorView()
}
```

### AVPlayer Creation — [10:26]

```swift
struct BOTanistAVPlayer {
    func player(url: URL) throws -> AVPlayer {
        let player = AVPlayer(url: url)

        return player
    }
}
```

### AVPlayer Call Site — [11:28]

```swift
self.player = try? await robotVideoAVPlayer()
```

### AVPlayer Initialization — [11:57]

```swift
private nonisolated func robotVideoAVPlayer() async throws -> AVPlayer? {
    guard let url = Bundle.main.url(forResource: RobotVideo.resource, withExtension: RobotVideo.ext) else {
        throw BOTanistAppError.videoNotFound(forResource: RobotVideo.resource, withExtension: RobotVideo.ext)
    }

    let avPlayer = BOTanistAVPlayer()
    let player = try avPlayer.player(url: url)

    return player
}
```

### Initial Test Scaffolding — [13:42]

```swift
import Testing
@testable import BOTanist


// When using the default init Plant(type:) make sure the planting style is graft
@Test func plantingRoses() {
    // First create the two Plant structs


    // Verify with #expect
}
```

### Complete Test — [14:36]

```swift
import Testing
@testable import BOTanist


// When using the default init Plant(type:) make sure the planting style is graft
@Test
func plantingRoses() {
    // First create the two Plant structs
    let plant = Plant(type: .rose)
    let expected = Plant(type: .rose, style: .graft)

    // Verify with #expect
    #expect(plant == expected)
}
```

### Custom Tag — [17:35]

```swift
extension Tag {
    @Tag static var planting: Self
}
```

### Tag Usage in @Test — [17:42]

```swift
.tags(.planting)
```

### Slow Asset Loading — [20:37]

```swift
for asset in allAssets {
    asset.load()
}
```

### Fast Asset Loading — [20:54]

```swift
await withDiscardingTaskGroup { group in
    for asset in allAssets {
        group.addTask {
            asset.load()
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10135/4/A6AD3D2B-72D9-43AE-901E-8AFDBA304007/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10135/4/A6AD3D2B-72D9-43AE-901E-8AFDBA304007/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10135) — developer.apple.com. Indexed for agent consumption._
