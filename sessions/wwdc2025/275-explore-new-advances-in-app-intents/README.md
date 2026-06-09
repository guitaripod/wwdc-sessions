---
id: "wwdc2025-275"
event: "wwdc2025"
year: 2025
title: "Explore new advances in App Intents"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/275"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Explore new advances in App Intents

**Event:** WWDC25 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-275](https://developer.apple.com/videos/play/wwdc2025/275)

Explore all the new enhancements available in the App Intents framework in this year’s releases. Learn about developer quality-of-life improvements like deferred properties, new capabilities like interactive app intents snippets, entity view annotations, how to integrate Visual Intelligence, and much more. We’ll take you through how App Intents is more expressive than ever, while becoming even easier and smoother to adopt. We’ll also share exciting new clients of App Intents this year like Spotlight and Visual Intelligence, and learn to write app intents that work great in those contexts.

**Keywords:** `app intents`, `machine learning`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,045 words)

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
- [PurchaseIntent](https://developer.apple.com/documentation/StoreKit/PurchaseIntent) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/PurchaseIntent
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/PurchaseIntent.json
- [App Shortcuts](https://developer.apple.com/documentation/AppIntents/app-shortcuts) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/app-shortcuts
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/app-shortcuts.json
- [App Intents](https://developer.apple.com/documentation/AppIntents) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents.json

## Code Snippets

### Returning a Snippet Intent — [4:08]

```swift
import AppIntents
import SwiftUI

struct ClosestLandmarkIntent: AppIntent {
    static let title: LocalizedStringResource = "Find Closest Landmark"

    @Dependency var modelData: ModelData

    func perform() async throws -> some ReturnsValue<LandmarkEntity> & ShowsSnippetIntent & ProvidesDialog {
        let landmark = await self.findClosestLandmark()

        return .result(
            value: landmark,
            dialog: IntentDialog(
                full: "The closest landmark is \(landmark.name).",
                supporting: "\(landmark.name) is located in \(landmark.continent)."
            ),
            snippetIntent: LandmarkSnippetIntent(landmark: landmark)
        )
    }
}
```

### Building a SnippetIntent — [4:31]

```swift
struct LandmarkSnippetIntent: SnippetIntent {
    static let title: LocalizedStringResource = "Landmark Snippet"

    @Parameter var landmark: LandmarkEntity
    @Dependency var modelData: ModelData

    func perform() async throws -> some IntentResult & ShowsSnippetView {
        let isFavorite = await modelData.isFavorite(landmark)

        return .result(
            view: LandmarkView(landmark: landmark, isFavorite: isFavorite)
        )
    }
}
```

### Associate intents with buttons — [5:45]

```swift
struct LandmarkView: View {
    let landmark: LandmarkEntity
    let isFavorite: Bool

    var body: some View {
        // ...
        Button(intent: UpdateFavoritesIntent(landmark: landmark, isFavorite: !isFavorite)) { /* ... */ }

        Button(intent: FindTicketsIntent(landmark: landmark)) { /* ... */ }
        // ...
    }
}
```

### Request confirmation snippet — [6:53]

```swift
struct FindTicketsIntent: AppIntent {

    func perform() async throws -> some IntentResult & ShowsSnippetIntent {
        let searchRequest = await searchEngine.createRequest(landmarkEntity: landmark)

        // Present a snippet that allows people to change
        // the number of tickets.
        try await requestConfirmation(
            actionName: .search,
            snippetIntent: TicketRequestSnippetIntent(searchRequest: searchRequest)
        )

        // Resume searching...
    }
}
```

### Using Entities as parameters — [7:24]

```swift
struct TicketRequestSnippetIntent: SnippetIntent {
    static let title: LocalizedStringResource = "Ticket Request Snippet"

    @Parameter var searchRequest: SearchRequestEntity

    func perform() async throws -> some IntentResult & ShowsSnippetView {
        let view = TicketRequestView(searchRequest: searchRequest)

        return .result(view: view)
    }
}
```

### Updating a snippet — [8:01]

```swift
func performRequest(request: SearchRequestEntity) async throws {
    // Set to pending status...

    TicketResultSnippetIntent.reload()

    // Kick off search...

    TicketResultSnippetIntent.reload()
}
```

### Responding to Image Search — [9:24]

```swift
struct LandmarkIntentValueQuery: IntentValueQuery {

    @Dependency var modelData: ModelData

    func values(for input: SemanticContentDescriptor) async throws -> [LandmarkEntity] {
        guard let pixelBuffer: CVReadOnlyPixelBuffer = input.pixelBuffer else {
            return []
        }

        let landmarks = try await modelData.searchLandmarks(matching: pixelBuffer)

        return landmarks
    }
}
```

### Support opening an entity — [9:51]

```swift
struct OpenLandmarkIntent: OpenIntent {
    static var title: LocalizedStringResource = "Open Landmark"

    @Parameter(title: "Landmark")
    var target: LandmarkEntity

    func perform() async throws -> some IntentResult {
        /// ...
    }
}
```

### Show search results in app — [10:53]

```swift
@AppIntent(schema: .visualIntelligence.semanticContentSearch)
struct ShowSearchResultsIntent {
    var semanticContent: SemanticContentDescriptor

    @Dependency var navigator: Navigator

    func perform() async throws -> some IntentResult {
        await navigator.showImageSearch(semanticContent.pixelBuffer)

        return .result()
    }

    // ...
}
```

### Returning multiple entity types — [11:40]

```swift
@UnionValue
enum VisualSearchResult {
    case landmark(LandmarkEntity)
    case collection(CollectionEntity)
}a

struct LandmarkIntentValueQuery: IntentValueQuery {
    func values(for input: SemanticContentDescriptor) async throws -> [VisualSearchResult] {
        // ...
    }
}

struct OpenLandmarkIntent: OpenIntent { /* ... */ }
struct OpenCollectionIntent: OpenIntent { /* ... */ }
```

### Associating a view with an AppEntity — [13:00]

```swift
struct LandmarkDetailView: View {

    let landmark: LandmarkEntity

    var body: some View {
        Group{ /* ... */ }
        .userActivity("com.landmarks.ViewingLandmark") { activity in
            activity.title = "Viewing \(landmark.name)"
            activity.appEntityIdentifier = EntityIdentifier(for: landmark)
        }
    }
}
```

### Converting AppEntity to PDF — [13:21]

```swift
import CoreTransferable
import PDFKit

extension LandmarkEntity: Transferable {
    static var transferRepresentation: some TransferRepresentation {
        DataRepresentation(exportedContentType: .pdf) {landmark in
            // Create PDF data...
            return data
        }
    }
}
```

### Associating properties with Spotlight keys — [14:05]

```swift
struct LandmarkEntity: IndexedEntity {

    // ...

    @Property(indexingKey: \.displayName)
    var name: String

    @Property(customIndexingKey: /* ... */)
    var continent: String

    // ...
}
```

### Making intents undoable — [15:49]

```swift
struct DeleteCollectionIntent: UndoableIntent {
    // ...

    func perform() async throws -> some IntentResult {

        // Confirm deletion...

        await undoManager?.registerUndo(withTarget: modelData) {modelData in
            // Restore collection...
        }
        await undoManager?.setActionName("Delete \(collection.name)")

       // Delete collection...
    }
}
```

### Multiple choice — [16:52]

```swift
struct DeleteCollectionIntent: UndoableIntent {
    func perform() async throws -> some IntentResult & ReturnsValue<CollectionEntity?> {
        let archive = Option(title: "Archive", style: .default)
        let delete = Option(title: "Delete", style: .destructive)

        let resultChoice = try await requestChoice(
            between: [.cancel, archive, delete],
            dialog: "Do you want to archive or delete \(collection.name)?",
            view: collectionSnippetView(collection)
        )

        switch resultChoice {
        case archive: // Archive collection...
        case delete: // Delete collection...
        default: // Do nothing...
        }
    }
    // ...
}
```

### Supported modes — [18:47]

```swift
struct GetCrowdStatusIntent: AppIntent {

    static let supportedModes: IntentModes = [.background, .foreground]

    func perform() async throws -> some ReturnsValue<Int> & ProvidesDialog {
        if systemContext.currentMode == .foreground {
            await navigator.navigateToCrowdStatus(landmark)
        }

        // Retrieve status and return dialog...
    }
}
```

### Supported modes — [19:30]

```swift
struct GetCrowdStatusIntent: AppIntent {
    static let supportedModes: IntentModes = [.background, .foreground(.dynamic)]

    func perform() async throws -> some ReturnsValue<Int> & ProvidesDialog {
        guard await modelData.isOpen(landmark) else { /* Exit early... */ }

        if systemContext.currentMode.canContinueInForeground {
            do {
                try await continueInForeground(alwaysConfirm: false)
                await navigator.navigateToCrowdStatus(landmark)
            } catch {
                // Open app denied.
            }
        }

        // Retrieve status and return dialog...
    }
}
```

### View Control — [21:30]

```swift
extension OpenLandmarkIntent: TargetContentProvidingIntent {}

struct LandmarksNavigationStack: View {

    @State var path: [Landmark] = []

    var body: some View {
        NavigationStack(path: $path) { /* ... */ }
        .onAppIntentExecution(OpenLandmarkIntent.self) { intent in
            self.path.append(intent.landmark)
        }
    }
}
```

### Scene activation condition — [23:13]

```swift
@main
struct AppIntentsTravelTrackerApp: App {
    var body: some Scene {
        WindowGroup { /* ... */ }

        WindowGroup { /* ... */ }
        .handlesExternalEvents(matching: [
            OpenLandmarkIntent.persistentIdentifier
        ])
    }
}
```

### View activation condition — [23:33]

```swift
struct LandmarksNavigationStack: View {
    var body: some View {
        NavigationStack(path: $path) { /* ... */ }
        .handlesExternalEvents(
            preferring: [],
            allowing: !isEditing ? [OpenLandmarkIntent.persistentIdentifier] : []
        )
    }
}
```

### Computed property — [24:23]

```swift
struct SettingsEntity: UniqueAppEntity {

    @ComputedProperty
    var defaultPlace: PlaceDescriptor {
        UserDefaults.standard.defaultPlace
    }

    init() {
    }
}
```

### Deferred property — [24:48]

```swift
struct LandmarkEntity: IndexedEntity {
    // ...

    @DeferredProperty
    var crowdStatus: Int {
        get async throws {
            await modelData.getCrowdStatus(self)
        }
    }

    // ...
}
```

### AppIntentsPackage — [25:50]

```swift
// Framework or dynamic library
public struct LandmarksKitPackage: AppIntentsPackage { }

// App target
struct LandmarksPackage: AppIntentsPackage {
    static var includedPackages: [any AppIntentsPackage.Type] {
        [LandmarksKitPackage.self]
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/275/5/354f4cf3-69e7-40de-b8ac-a7a5ce248c11/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/275/5/354f4cf3-69e7-40de-b8ac-a7a5ce248c11/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/275) — developer.apple.com. Indexed for agent consumption._
