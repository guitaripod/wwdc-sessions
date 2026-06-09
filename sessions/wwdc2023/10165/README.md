---
id: "wwdc2023-10165"
event: "wwdc2023"
year: 2023
title: "What’s new in Xcode 15"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10165"
topics: ["Essentials", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in Xcode 15

**Event:** WWDC23 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10165](https://developer.apple.com/videos/play/wwdc2023/10165)

Discover the latest productivity and performance improvements in Xcode 15. Explore enhancements to code completion and Xcode Previews, learn about the test navigator and test report, and find out more about the streamlined distribution process. We’ll also highlight improved navigation, source control management, and debugging.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,746 words)

## Documentation & Resources

- [Xcode updates](https://developer.apple.com/documentation/Updates/Xcode) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Updates/Xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Updates/Xcode.json

## Code Snippets

### Code Completion - PlantSummaryRow — [1:52]

```swift
import Foundation
import SwiftUI
import BackyardBirdsData
import LayeredArtworkLibrary

struct PlantSummaryRow: View {
    var plant: Plant
    var body: some View {
        VStack {
            ComposedPlant(plant: plant)
                .padding(4)
                .padding(.bottom, -20)
                .clipShape(.circle)
                .background(.fill.tertiary, in: .circle)
                .padding(.horizontal, 10)

            VStack {
                Text(plant.speciesName)
            }
        }
    }
}
```

### Code Completion - Latitude & Longitude — [3:28]

```swift
func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
    if let mostRecent = locations.last?.coordinate {
        logger.debug("Handled coordinate update: \(mostRecent.latitude)")
    }
}
```

### BirdIcon Documentation — [6:18]

```swift
/// Create the bird icon view.
///
/// The bird icon view is a tailored version of the ``ComposedBird`` view.
///
/// Use this initializer to display an image of a given bird.
///
/// ```swift
/// var bird: Bird
///
/// var body: some View {
///     HStack {
///         BirdIcon(bird: bird)
///             .frame(width: 60, height: 60)
///         Text(bird.speciesName)
///     }
/// }
/// ```
///
/// ![A screenshot of a view containing a bird icon with the bird's species name below it.](birdIcon)
```

### CaseDetection Macro — [7:37]

```swift
extension TokenSyntax {
    fileprivate var initialUppercased: String {
        let name = self.text
        guard let initial = name.first else {
            return name
        }

        return "\(initial.uppercased())\(name.dropFirst())"
  }
}

public struct CaseDetectionMacro: MemberMacro {
    public static func expansion<
        Declaration: DeclGroupSyntax, Context: MacroExpansionContext
    >(
        of node: AttributeSyntax,
        providingMembersOf declaration: Declaration,
        in context: Context
    ) throws -> [DeclSyntax] {
        declaration.memberBlock.members
            .compactMap { $0.decl.as(EnumCaseDeclSyntax.self) }
            .map { $0.elements.first!.identifier }
            .map { ($0, $0.initialUppercased) }
            .map { original, uppercased in
                """
                var is\(raw: uppercased): Bool {
                    if case .\(raw: original) = self {
                        return true
                    }

                    return false
                }
                """
            }
    }
}

@main
struct EnumHelperPlugin: CompilerPlugin {
    let providingMacros: [Macro.Type] = [
        CaseDetectionMacro.self,
    ]
}
```

### Using CaseDetection Macro — [8:07]

```swift
@CaseDetection
enum Element {
    case one
    case two
}

var element: Element = .one
if element.isOne {
    // Handle interesting case
}
```

### New Preview API — [8:50]

```swift
#Preview {
    AppDetailColumn(screen: .account)
        .backyardBirdsDataContainer()
}

#Preview("Placeholder View") {
    AppDetailColumn()
        .backyardBirdsDataContainer()
}
```

### UIViewController Preview — [9:22]

```swift
#Preview {
    let controller = DetailedMapViewController()

    controller.mapView.camera = MKMapCamera(
        lookingAtCenter: CLLocation(latitude: 37.335_690, longitude: -122.013_330).coordinate,
        fromDistance: 0,
        pitch: 0,
        heading: 0
    )
    return controller
}
```

### OSLog — [17:34]

```swift
import OSLog

let logger = Logger(subsystem: "BackyardBirdsData", category: "Account")

func login(password: String) -> Error? {
    var error: Error? = nil
    logger.info("Logging in user '\(username)'...")

    // ...

    if let error {
        logger.error("User '\(username)' failed to log in. Error: \(error)")
    } else {
        loggedIn = true
        logger.notice("User '\(username)' logged in successfully.")
    }
    return error
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10165/5/C61041BB-AC4B-41C2-982C-6476B513F891/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10165/5/C61041BB-AC4B-41C2-982C-6476B513F891/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10165) — developer.apple.com. Indexed for agent consumption._