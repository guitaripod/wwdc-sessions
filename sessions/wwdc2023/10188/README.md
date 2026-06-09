---
id: "wwdc2023-10188"
event: "wwdc2023"
year: 2023
title: "Sync to iCloud with CKSyncEngine"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10188"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Sync to iCloud with CKSyncEngine

**Event:** WWDC23 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10188](https://developer.apple.com/videos/play/wwdc2023/10188)

Discover how CKSyncEngine can help you sync people’s CloudKit data to iCloud. Learn how you can reduce the amount of code in your app when you let the system handle scheduling for your sync operations. We’ll share how you can automatically benefit from enhanced performance as CloudKit evolves, explore testing for your sync implementation, and more.

To get the most out of this session, you should be familiar with CloudKit and CKRecord types.

**Keywords:** `app`, `backend`, `cksyncengine`, `cloud`, `cloudkit`, `database`, `engine`, `icloud`, `model`, `object`, `orm`, `persistence`, `relational`, `share`, `sharing`, `storage`, `sync`, `sync engine`, `syncing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,446 words)

## Documentation & Resources

- [CloudKit Samples: CKSyncEngine](https://github.com/apple/sample-cloudkit-sync-engine) _samplecode_
- [CKSyncEngine](https://developer.apple.com/documentation/CloudKit/CKSyncEngine-5sie5) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CloudKit/CKSyncEngine-5sie5
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CloudKit/CKSyncEngine-5sie5.json

## Code Snippets

### Initializing CKSyncEngine — [12:14]

```swift
actor MySyncManager : CKSyncEngineDelegate {

    init(container: CKContainer, localPersistence: MyLocalPersistence) {
        let configuration = CKSyncEngine.Configuration(
            database: container.privateCloudDatabase,
            stateSerialization: localPersistence.lastKnownSyncEngineState,
            delegate: self
        )
        self.syncEngine = CKSyncEngine(configuration)
    }

    func handleEvent(_ event: CKSyncEngine.Event, syncEngine: CKSyncEngine) async {
        switch event {
        case .stateUpdate(let stateUpdate):
            self.localPersistence.lastKnownSyncEngineState = stateUpdate.stateSerialization
        }
    }
}
```

### Sending changes to the server — [14:13]

```swift
func userDidEditData(recordID: CKRecord.ID) {
    // Tell the sync engine we need to send this data to the server.
    self.syncEngine.state.add(pendingRecordZoneChanges: [ .save(recordID) ])
}

func nextRecordZoneChangeBatch(
    _ context: CKSyncEngine.SendChangesContext, 
    syncEngine: CKSyncEngine
) async -> CKSyncEngine.RecordZoneChangeBatch? {

    let changes = syncEngine.state.pendingRecordZoneChanges.filter { 
        context.options.zoneIDs.contains($0.recordID.zoneID) 
    }

    return await CKSyncEngine.RecordZoneChangeBatch(pendingChanges: changes) { recordID in
        self.recordToSave(for: recordID)
    }
}
```

### Fetching changes from the server — [15:40]

```swift
func handleEvent(_ event: CKSyncEngine.Event, syncEngine: CKSyncEngine) async {
    switch event {

    case .fetchedRecordZoneChanges(let recordZoneChanges):
        for modifications in recordZoneChanges.modifications {
            // Persist the fetched modification locally
        }

        for deletions in recordZoneChanges.deletions {
            // Remove the deleted data locally
        }

    case .fetchedDatabaseChanges(let databaseChanges):      
        for modifications in databaseChanges.modifications {
            // Persist the fetched modification locally
        }

        for deletions in databaseChanges.deletions { 
            // Remove the deleted data locally
        }

    // Perform any setup/cleanup necessary
    case .willFetchChanges, .didFetchChanges:
        break

    case .sentRecordZoneChanges(let sentChanges):

        for failedSave in sentChanges.failedRecordSaves {
            let recordID = failedSave.record.recordID

            switch failedSave.error.code {

            case .serverRecordChanged:
                if let serverRecord = failedSave.error.serverRecord {
                    // Merge server record into local data
                    syncEngine.state.add(pendingRecordZoneChanges: [ .save(recordID) ])
                }

            case .zoneNotFound: 
                // Tried to save a record, but the zone doesn't exist yet.
                syncEngine.state.add(pendingDatabaseChanges: [ .save(recordID.zoneID) ])
                syncEngine.state.add(pendingRecordZoneChanges: [ .save(recordID) ])

            // CKSyncEngine will automatically handle these errors
            case .networkFailure, .networkUnavailable, .serviceUnavailable, .requestRateLimited:
                break

            // An unknown error occurred
            default:
                break
            }
        }

    case .accountChange(let event):
        switch event.changeType {

        // Prepare for new user
        case .signIn:
            break

        // Delete local data
        case .signOut:
            break

        // Delete local data and prepare for new user
        case .switchAccounts: 
            break
        }
    }
}
```

### Using CKSyncEngine with private and shared databases — [18:49]

```swift
let databases = [ container.privateCloudDatabase, container.sharedCloudDatabase ]

let syncEngines = databases.map {
    var configuration = CKSyncEngine.Configuration(
        database: $0,
        stateSerialization: lastKnownSyncEngineState($0.databaseScope),
        delegate: self
    )
    return CKSyncEngine(configuration)
}
```

### Testing CKSyncEngine integration — [20:00]

```swift
func testSyncConflict() async throws {

    // Create two local databases to simulate two devices.
    let deviceA = MySyncManager()
    let deviceB = MySyncManager()

    // Save a value from the first device to the server.
    deviceA.value = "A"
    try await deviceA.syncEngine.sendChanges()

    // Try to save the value from the second device before it fetches changes.
    // The record save should fail with a conflict that includes the current server record.
    // In this example, we expect the value from the server to win.
    deviceB.value = "B"
    XCTAssertThrows(try await deviceB.syncEngine.sendChanges())
    XCTAssertEqual(deviceB.value, "A")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10188/3/F63E6FC7-4329-401C-9D80-CD4E7C8A478A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10188/3/F63E6FC7-4329-401C-9D80-CD4E7C8A478A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10188) — developer.apple.com. Indexed for agent consumption._