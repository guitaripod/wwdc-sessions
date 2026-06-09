---
id: "wwdc2025-244"
event: "wwdc2025"
year: 2025
title: "Get to know App Intents"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/244"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Get to know App Intents

**Event:** WWDC25 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-244](https://developer.apple.com/videos/play/wwdc2025/244)

Learn about the App Intents framework and its increasingly critical role within Apple’s developer platforms. We’ll take you through a ground-up introduction of the core concepts: intents, entities, queries, and much more. You’ll learn how these pieces fit together and let you integrate your app through Apple’s devices, from software features like Spotlight and Shortcuts to hardware features like the Action button. We’ll also walk through how App Intents is your app’s gateway to integrating with Apple Intelligence going forward.

**Keywords:** `app intents`, `machine learning`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,481 words)

## Documentation & Resources

- [Adopting App Intents to support system experiences](https://developer.apple.com/documentation/AppIntents/adopting-app-intents-to-support-system-experiences) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/adopting-app-intents-to-support-system-experiences
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/adopting-app-intents-to-support-system-experiences.json
- [Building a workout app for iPhone and iPad](https://developer.apple.com/documentation/HealthKit/building-a-workout-app-for-iphone-and-ipad) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/building-a-workout-app-for-iphone-and-ipad
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/building-a-workout-app-for-iphone-and-ipad.json
- [Accelerating app interactions with App Intents](https://developer.apple.com/documentation/AppIntents/AcceleratingAppInteractionsWithAppIntents) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/AcceleratingAppInteractionsWithAppIntents
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/AcceleratingAppInteractionsWithAppIntents.json
- [App schema domains](https://developer.apple.com/documentation/AppIntents/app-schema-domains) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/app-schema-domains
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/app-schema-domains.json
- [Creating your first app intent](https://developer.apple.com/documentation/AppIntents/Creating-your-first-app-intent) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/Creating-your-first-app-intent
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/Creating-your-first-app-intent.json
- [App Shortcuts](https://developer.apple.com/documentation/AppIntents/app-shortcuts) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/app-shortcuts
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/app-shortcuts.json
- [App Intents](https://developer.apple.com/documentation/AppIntents) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents.json

## Code Snippets

### Navigate Intent — [3:23]

```swift
struct NavigateIntent: AppIntent {
    static let title: LocalizedStringResource = "Navigate to Landmarks"

    static let supportedModes: IntentModes = .foreground

    @MainActor
    func perform() async throws -> some IntentResult {
        Navigator.shared.navigate(to: .landmarks)
        return .result()
    }
}
```

### Navigation Option App Enum — [5:02]

```swift
enum NavigationOption: String, AppEnum {
    case landmarks
    case map
    case collections

    static let typeDisplayRepresentation: TypeDisplayRepresentation = "Navigation Option"

    static let caseDisplayRepresentations: [NavigationOption: DisplayRepresentation] = [
        .landmarks: "Landmarks",
        .map: "Map",
        .collections: "Collections"
    ]
}
```

### Navigate Intent with Parameter — [5:38]

```swift
struct NavigateIntent: AppIntent {
    static let title: LocalizedStringResource = "Navigate to Section"

    static let supportedModes: IntentModes = .foreground

    @Parameter var navigationOption: NavigationOption

    @MainActor
    func perform() async throws -> some IntentResult {
        Navigator.shared.navigate(to: navigationOption)
        return .result()
    }
}
```

### Case Display Representations with Images — [6:57]

```swift
static let caseDisplayRepresentations = [
    NavigationOption.landmarks: DisplayRepresentation(
        title: "Landmarks",
        image: .init(systemName: "building.columns")
    ),
    NavigationOption.map: DisplayRepresentation(
        title: "Map",
        image: .init(systemName: "map")
    ),
    NavigationOption.collections: DisplayRepresentation(
        title: "Collections",
        image: .init(systemName: "book.closed")
    )
]
```

### Navigation Option With Parameter Summary — [7:28]

```swift
struct NavigateIntent: AppIntent {
    static let title: LocalizedStringResource = "Navigate to Section"

    static let supportedModes: IntentModes = .foreground

    static var parameterSummary: some ParameterSummary {
        Summary("Navigate to \(\.$navigationOption)")
    }

    @Parameter(
        title: "Section",
        requestValueDialog: "Which section?"
    )
    var navigationOption: NavigationOption

    @MainActor
    func perform() async throws -> some IntentResult {
        Navigator.shared.navigate(to: navigationOption)
        return .result()
    }
}
```

### App Shortcuts Provider and Navigation Intent App Shortcut — [9:22]

```swift
struct TravelTrackingAppShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: NavigateIntent(),
            phrases: [
                "Navigate in \(.applicationName)",
                "Navigate to \(\.$navigationOption) in \(.applicationName)"a
            ],                
            shortTitle: "Navigate",
            systemImageName: "arrowshape.forward"
        )
    }
}
```

### Landmark Entity — [11:02]

```swift
struct LandmarkEntity: AppEntity {
    var id: Int { landmark.id }

    @ComputedProperty
    var name: String { landmark.name }

    @ComputedProperty
    var description: String { landmark.description }

    let landmark: Landmark

    static let typeDisplayRepresentation = TypeDisplayRepresentation(name: "Landmark")

    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(title: "\(name)")
    }

    static let defaultQuery = LandmarkEntityQuery()
}
```

### Landmark Entity Query — [13:19]

```swift
struct LandmarkEntityQuery: EntityQuery {
    @Dependency var modelData: ModelData

    func entities(for identifiers: [LandmarkEntity.ID]) async throws -> [LandmarkEntity] {
        modelData
            .landmarks(for: identifiers)
            .map(LandmarkEntity.init)
    }
}
```

### App Dependency Manager — [13:50]

```swift
@main
struct LandmarksApp: App {    
    init() {
        AppDependencyManager.shared.add { ModelData() }
    }
}
```

### Closest Landmark Intent — [14:18]

```swift
struct ClosestLandmarkIntent: AppIntent {
    static let title: LocalizedStringResource = "Find Closest Landmark"

    @Dependency var modelData: ModelData

    @MainActor
    func perform() async throws 
        -> some ReturnsValue<LandmarkEntity> & ProvidesDialog & ShowsSnippetView {

        let landmark = try await modelData.findClosestLandmark()

        return .result(
            value: landmark,
            dialog: "The closest landmark to you is \(landmark.name)",
            view: ClosestLandmarkView(landmark: landmark)
        )
    }
}
```

### Closest Landmark App Shortcut — [15:18]

```swift
AppShortcut(
    intent: ClosestLandmarkIntent(),
    phrases: [
        "Find closest landmark in \(.applicationName)"
    ],
    shortTitle: "Closest landmark",
    systemImageName: "location"
)
```

### Transferable — [16:33]

```swift
extension LandmarkEntity: Transferable {
    static var transferRepresentation: some TransferRepresentation {
        DataRepresentation(exportedContentType: .image) {
            return try $0.imageRepresentationData
        }
    }
}
```

### Indexed Entity — [17:31]

```swift
struct LandmarkEntity: IndexedEntity {
    // ...

    @Property(
        indexingKey: \.displayName
    )
    var name: String

    @Property(
        indexingKey: \.contentDescription
    )
    var description: String
}
```

### Open Landmark Intent — [18:17]

```swift
struct OpenLandmarkIntent: OpenIntent, TargetContentProvidingIntent {
    static let title: LocalizedStringResource = "Open Landmark"

    @Parameter(title: "Landmark", requestValueDialog: "Which landmark?")
    var target: LandmarkEntity
}

struct LandmarksNavigationStack: View {
    @State var path: [Landmark] = []

    var body: some View {
        NavigationStack(path: $path) {}
        .onAppIntentExecution(OpenLandmarkIntent.self) { intent in
            path.append(intent.target.landmark)
        }
    }
}
```

### Open Landmark App Shortcut — [19:24]

```swift
AppShortcut(
    intent: OpenLandmarkIntent(),
    phrases: [
        "Open \(\.$target) in \(.applicationName)",
        "Open landmark in \(.applicationName)"
    ],
    shortTitle: "Open",
    systemImageName: "building.columns"
)
```

### Suggested Entities — [19:39]

```swift
struct LandmarkEntityQuery: EntityQuery {
    // ...

    func suggestedEntities() async throws -> [LandmarkEntity] {
        modelData
            .favoriteLandmarks()
            .map(LandmarkEntity.init)
    }
}
```

### Update App Shortcut Parameters — [20:06]

```swift
TravelTrackingAppShortcuts.updateAppShortcutParameters()
```

### EnumerableEntityQuery — [20:25]

```swift
extension LandmarkEntityQuery: EnumerableEntityQuery {
    func allEntities() async throws -> [LandmarkEntity] { 
        // ...
    }
}
```

### EntityPropertyQuery — [20:36]

```swift
extension LandmarkEntityQuery: EntityPropertyQuery {
    static var properties = QueryProperties {
        // ...
    }

    static var sortingOptions = SortingOptions {
        // ...
    }

    func entities(
        matching comparators: [Predicate<LandmarkEntity>],
        mode: ComparatorMode,
        sortedBy: [Sort<LandmarkEntity>],
        limit: Int?
    ) async throws -> [LandmarkEntity] {
        // ...
    }
}
```

### EntityStringQuery — [20:44]

```swift
extension LandmarkEntityQuery: EntityStringQuery {
    func entities(matching: String) async throws -> [LandmarkEntity] {
        modelData
            .landmarks
            .filter { $0.name.contains(matching) || $0.description.contains(matching) }
            .map(LandmarkEntity.init)
    }
}
```

### App Intents Package — [23:10]

```swift
// TravelTrackingKit
public struct TravelTrackingKitPackage: AppIntentsPackage {}
public structaLandmarkEntity: AppEntity {}

// TravelTracking
struct TravelTrackingPackage: AppIntentsPackage {
    static var includedPackages: [any AppIntentsPackage.Type] {
        [TravelTrackingKitPackage.self]
    }
}
struct OpenLandmarkIntent: OpenIntent {}

// TravelTrackingAppIntentsExtension
struct TravelTrackingExtensionPackage: AppIntentsPackage {
    static var includedPackages: [any AppIntentsPackage.Type] {
        [TravelTrackingKitPackage.self]
    }
}
struct FavoriteLandmarkIntent: AppIntent {}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/244/5/54cb9dae-53ff-4b7a-9091-2e1d6b3d779e/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/244/5/54cb9dae-53ff-4b7a-9091-2e1d6b3d779e/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/244) — developer.apple.com. Indexed for agent consumption._