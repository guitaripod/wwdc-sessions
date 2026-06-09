---
id: "wwdc2023-10192"
event: "wwdc2023"
year: 2023
title: "Explore enhancements to RoomPlan"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10192"
topics: ["Spatial Computing"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Explore enhancements to RoomPlan

**Event:** WWDC23 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10192](https://developer.apple.com/videos/play/wwdc2023/10192)

Join us for an exciting update to RoomPlan as we explore MultiRoom support and enhancements to room representations. Learn how you can scan areas with more detail, capture multiple rooms, and merge individual scans into one larger structure. We’ll also share workflows and best practices when working with RoomPlan results that you want to combine into your existing 3D model library.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,880 words)

## Code Snippets

### RoomPlan with custom ARSession — [3:00]

```swift
// RoomCaptureSession

public class RoomCaptureSession {
    // Init: ARSession is an optional input for RoomCaptureSession
    public init(arSession: ARSession? = nil) {
       ...
  }

    // Stop: pauseARSession is used for whether to continue ARSession experience
    public func stop(pauseARSession: Bool = true) {
       ...
  }
}
```

### MultiRoom support with Continuous ARSession — [5:50]

```swift
// Continuous ARSession

// start 1st scan
roomCaptureSession.run(configuration: captureSessionConfig)

// stop 1st scan with continuing ARSession
roomCaptureSession.stop(pauseARSession: false)

// start 2nd scan
roomCaptureSession.run(configuration: captureSessionConfig)

// stop 2nd scan (pauseARSession = true by default)
roomCaptureSession.stop()
```

### MultiRoom capture with loading ARWorldMap — [7:30]

```swift
// Capture with loading ARWorldMap

// load ARWorldMap
let arWorldMap = try NSKeyedUnarchiver.unarchivedObject(ofClass: ARWorldMap.self, from: data)

// run ARKit relocalization
let arWorldTrackingConfig = ARWorldTrackingConfiguration()
arWorldTrackingConfig.initialWorldMap = arWorldMap
roomCaptureSession.init()
roomCaptureSession.arSession.run(arWorldTrackingConfig, options: [])

// Wait for relocalization to complete
// start 2nd scan
roomCaptureSession.run(configuration: captureSessionConfig)

// stop 2nd scan
roomCaptureSession.stop()
```

### StructureBuilder — [9:40]

```swift
// StructureBuilder

// create structureBuilder instance
let structureBuilder = StructureBuilder(option: [.beautifyObjects])

// load multiple capturedRoom results to capturedRoomArray
var capturedRoomArray: [CapturedRoom] = []

// run structureBuilder API to get capturedStructure
let capturedStructure = try await structureBuilder.capturedStructure(from: capturedRoomArray)

// export capturedStructure to usdz
try capturedStructure.export(to: destinationURL)
```

### CapturedStructure — [10:11]

```swift
// CapturedStructure

public struct CapturedStructure: Codable, Sendable {
    public var rooms: [CapturedRoom]

    public var walls: [Surface]
    public var doors: [Surface]
    public var windows: [Surface]
    public var openings: [Surface]
    public var objects: [Object]
    public var floors: [Surface]
    public var sections: [Section]

    public func export(to url: URL, metadataURL: URL? = nil, modelProvider: ModelProvider? = nil, exportOptions: USDExportOptions = .mesh) throws
}
```

### Parse attributes and categories to create folder hierarchy — [19:20]

```swift
// Parse attributes and categories to create folder hierarchy

for category in CapturedRoom.Object.Category.allCases {

    let url = generateFolderURL(category: category, attributes: [])
    FileManager.default.createDirectory(at: url, withIntermediateDirectories: true)

    for attributes in category.supportedCombinations {
        let url = generateFolderURL(category: category, attributes: attributes)
        FileManager.default.createDirectory(at: url, withIntermediateDirectories: true)
    }
}
```

### Create a Catalog index — [20:00]

```swift
// Create a Catalog index

struct RoomPlanCatalog: Codable {
    let categoryAttributes: [RoomPlanCatalogCategoryAttribute]
}

struct RoomPlanCatalogCategoryAttribute: Codable {
    enum CodingKeys: String, CodingKey {
        case folderRelativePath
        case category
        case attributes
        case modelFilename
    }
    let category: CapturedRoom.Object.Category
    let attributes: [any CapturedRoomAttribute]
    let folderRelativePath: String
    private(set) var modelFilename: String? = nil

    func encode(to encoder: Encoder) throws {
       …
    }
}
```

### Create a Catalog bundle — [20:15]

```swift
//  Create a Catalog bundle

let catalog = RoomPlanCatalog(categoryAttributes: categoryAttributes)
let plistEncoder = PropertyListEncoder()
let data = try plistEncoder.encode(catalog)
let catalogURL = inputURL.appending(path: "catalog.plist")
try data.write(to: catalogURL)
let fileWrapper = try FileWrapper(url: inputURL)
try fileWrapper.write(to: outputURL, options: [.atomic, .withNameUpdating],
                      originalContentsURL: nil)
```

### Instantiate a Model Provider from a Catalog — [20:22]

```swift
// Instantiate a Model Provider from a Catalog

for categoryAttribute in catalog.categoryAttributes {
    guard let modelFilename = categoryAttribute.modelFilename else {
        continue 
    }
    let folderRelativePath = categoryAttribute.folderRelativePath
    let modelURL = url.appending(path: folderRelativePath).appending(path: modelFilename)
    if categoryAttribute.attributes.isEmpty {
       try modelProvider.setModelFileURL(modelURL, for: categoryAttribute.category)
    } else {
       try modelProvider.setModelFileURL(modelURL, for: categoryAttribute.attributes)
    }
}
```

### Exporting a captured room to usdz with models — [20:47]

```swift
// Exporting a captured room to usdz with models

try capturedRoom.export(to: outputURL, modelProvider: modelProvider, 
                        exportOptions: .model)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10192/4/0D847FCD-B40B-4324-A284-F22B79E78F4D/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10192/4/0D847FCD-B40B-4324-A284-F22B79E78F4D/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10192) — developer.apple.com. Indexed for agent consumption._