---
id: "wwdc2022-10120"
event: "wwdc2022"
year: 2022
title: "Evolve your Core Data schema"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10120"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Evolve your Core Data schema

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10120](https://developer.apple.com/videos/play/wwdc2022/10120)

Learn how you can cleanly migrate Core Data schemas after updating your app, and breeze through data model changes. We’ll show you how you can take advantage of built-in migration tools to keep your data storage up to date, and let Core Data analyze your schema to infer data model migrations. We’ll also provide best practices, help you tackle tough migration challenges, and discover how Core Data schemas can interact with CloudKit to support easy migrations in the cloud.

To get the most out of this session, we recommend being familiar with Core Data schemas and data types, and have a basic understanding around syncing Core Data databases with CloudKit.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,727 words)

## Documentation & Resources

- [Migrating your data model automatically](https://developer.apple.com/documentation/CoreData/migrating-your-data-model-automatically) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData/migrating-your-data-model-automatically
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData/migrating-your-data-model-automatically.json

## Code Snippets

### Migrate your Core Data schema — [6:16]

```swift
import CoreData

let storeURL = NSURL.fileURL(withPath: "/path/to/store")
let momURL = NSURL.fileURL(withPath: "/path/to/model")
guard let mom = NSManagedObjectModel(contentsOf: momURL) else { 
    fatalError("Error initializing managed object model for URL: \(momURL)")
}
let coordinator = NSPersistentStoreCoordinator(managedObjectModel: mom)
do {
    let opts = [NSMigratePersistentStoresAutomaticallyOption: true,
                      NSInferMappingModelAutomaticallyOption: true]

    try coordinator.addPersistentStore(ofType: NSSQLiteStoreType,
                                       configurationName: Optional<String>.none,
                                       at: storeURL,
                                       options: opts)
} catch {
    fatalError("Error configuring persistent store: \(error)")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10120/5/7685DE64-40AC-4C35-9865-8CDA798501E4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10120/5/7685DE64-40AC-4C35-9865-8CDA798501E4/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10120) — developer.apple.com. Indexed for agent consumption._