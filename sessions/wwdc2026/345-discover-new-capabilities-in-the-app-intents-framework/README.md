---
id: "wwdc2026-345"
event: "wwdc2026"
year: 2026
title: "Discover new capabilities in the App Intents framework"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/345"
topics: ["App Services", "AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "visionOS"]
hasTranscript: true
---

# Discover new capabilities in the App Intents framework

**Event:** WWDC26 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-345](https://developer.apple.com/videos/play/wwdc2026/345)

Level up your App Intents adoption with advanced features to make it faster, more flexible, and more relevant. Find out how ValueRepresentation and RelevantEntities make your content more discoverable and allow it to travel across apps, EntityCollection improves performance, and SyncableEntity let you scale across devices. Explore richer parameter types including union values and long-running intents that handle cancellation gracefully.

**Keywords:** `ai`, `app intents`, `machine learning`, `siri`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,786 words)

## Documentation & Resources

- [Adopting App Intents to support system experiences](https://developer.apple.com/documentation/AppIntents/adopting-app-intents-to-support-system-experiences) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/adopting-app-intents-to-support-system-experiences
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/adopting-app-intents-to-support-system-experiences.json
- [App Intents](https://developer.apple.com/documentation/AppIntents) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents.json

## Code Snippets

### Share structured entities with ValueRepresentation — [0:01]

```swift
struct LandmarkEntity: AppEntity, Transferable {
      var id: Int
      var landmark: Landmark  // contains CLLocationCoordinate2D

      static var transferRepresentation: some TransferRepresentation {
          ValueRepresentation(
              exporting: { entity in
                  PlaceDescriptor(
                      representations: [.coordinate(entity.landmark.locationCoordinate)],
                      commonName: entity.landmark.name
                  )
              }
          )
      }
  }

  // If the entity already has a PlaceDescriptor property, use a key-path — much less code:
  struct LandmarkEntity: AppEntity, Transferable {
      var id: Int
      @Property var placeDescriptor: PlaceDescriptor

      static var transferRepresentation: some TransferRepresentation {
          ValueRepresentation(exporting: \.placeDescriptor)
      }
  }
```

### Register relevant entities with RelevantEntities — [5:18]

```swift
// Suggest playlists for the workout session
  let playlistEntities = [dailyRun, runningMix]
  let workoutContext = AppEntityContext.audio(.workout(activityType: .running))

  try await RelevantEntities.shared.updateEntities(
      playlistEntities, for: workoutContext
  )

  // Clear all entities for a context
  try await RelevantEntities.shared.removeAllEntities(for: workoutContext)

  // Remove specific entities from a context
  try await RelevantEntities.shared.removeEntities(playlistEntities, from: workoutContext)

  // Or remove all entities across all contexts
  try await RelevantEntities.shared.removeAllEntities()
```

### Handle large entity sets with EntityCollection — [7:15]

```swift
struct TagPhotosIntent: AppIntent {
      static let title: LocalizedStringResource = "Tag Travel Photos"

      @Parameter var photos: EntityCollection<PhotoEntity>   // was: [PhotoEntity]
      @Parameter var tag: String

      func perform() async throws -> some IntentResult {
          modelData.tagPhotos(ids: photos.identifiers, tag: tag)   // was: tagPhotos(photos, tag: tag)
          return .result()
      }
  }
```

### Make entity IDs stable with SyncableEntity — [10:14]

```swift
// If your ID is already stable across devices (server UUID, CloudKit record ID):
  struct PhotoEntity: AppEntity, SyncableEntity {
      var id: Int  // Already stable across devices — that's it
  }

  // If you use local IDs, pair a local and a stable ID:
  struct PhotoEntity: AppEntity, SyncableEntity {
      var id: SyncableEntityIdentifier<String, String>

      init(localID: String, stableID: String) {
          self.id = SyncableEntityIdentifier(local: localID, stable: stableID)
      }
  }
```

### Accept multiple types with @UnionValue — [11:58]

```swift
@UnionValue
  enum TravelGalleryContent {
      case landmarkCollection(LandmarkCollectionEntity)
      case photoAlbum(PhotoAlbumEntity)

      static let typeDisplayRepresentation: TypeDisplayRepresentation = "Travel Gallery"
      static let caseDisplayRepresentations: [Cases: DisplayRepresentation] = [
          .landmarkCollection: "Landmark Collection",
          .photoAlbum: "Photo Album"
      ]
  }
```

### Run beyond 30 s with LongRunningIntent + CancellableIntent — [13:41]

```swift
struct UploadPhotoIntent: LongRunningIntent, CancellableIntent {
      static let title: LocalizedStringResource = "Upload Photo"

      @Parameter var photo: IntentFile

      func perform() async throws -> some IntentResult & ProvidesDialog {
          let result = try await performBackgroundTask {
              let chunks = calculateChunks(for: photo)
              progress.totalUnitCount = Int64(chunks)

              for chunk in 1...chunks {
                  try Task.checkCancellation()
                  try await uploadChunk(chunk)
                  progress.completedUnitCount = Int64(chunk)
              }
              return "Upload complete!"
          } onCancel: { reason in
              cleanup(for: reason)
          }
          return .result(dialog: "\(result)")
      }
  }
```

### Control which process runs your intent with ExecutionTargets — [16:54]

```swift
// Write operation — needs the main app
  struct UpdateFavoriteIntent: AppIntent {
      static var allowedExecutionTargets: ExecutionTargets { .main }
  }

  // Standalone download — runs in the extension
  struct DownloadPhotoIntent: AppIntent {
      static var allowedExecutionTargets: ExecutionTargets { .appIntentsExtension }
  }

  // Display-only — runs in the widget extension
  struct GetLandmarkStatusIntent: AppIntent {
      static var allowedExecutionTargets: ExecutionTargets { .widgetKitExtension }
  }

  // Works in either — lets the system choose
  struct TagPhotosIntent: AppIntent {
      static var allowedExecutionTargets: ExecutionTargets { [.main, .appIntentsExtension] }
  }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/345/4/bc719e14-772a-4737-aceb-6e54cda6b511/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/345/4/bc719e14-772a-4737-aceb-6e54cda6b511/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/345) — developer.apple.com. Indexed for agent consumption._
