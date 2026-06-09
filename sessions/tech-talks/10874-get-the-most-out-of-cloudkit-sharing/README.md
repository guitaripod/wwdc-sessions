---
id: "tech-talks-10874"
event: "tech-talks"
year: 2021
title: "Get the most out of CloudKit Sharing"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/10874"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Get the most out of CloudKit Sharing

**Event:** Tech Talks · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-12-07 · **Session:** [tech-talks-10874](https://developer.apple.com/videos/play/tech-talks/10874)

Discover how apps can use CloudKit to share records with others. We'll show you how to encourage collaboration between people using your app and support those interactions with Apple frameworks. Learn how to create and manage shares, explore sharing options like public permissions, and find out how you can use zone sharing in iOS 15 and macOS Monterey to share entire record zones of data. To get the most out of this session, we recommend being familiar with CloudKit and a basic understanding of record and data types.

**Keywords:** `ckshare`, `cloudkit sharing`, `hierarchical`, `sharing`, `sharing sample app`, `zone`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,754 words)

## Documentation & Resources

- [CloudKit Samples: Sharing](https://github.com/apple/cloudkit-sample-sharing) _samplecode_

## Code Snippets

### Create a new Contact record — [1:58]

```swift
// Create a new Contact record

func addContact(name: String, phoneNumber: String) async throws {
    let id = CKRecord.ID(zoneID: recordZone.zoneID)
    let contactRecord = CKRecord(recordType: "Contact", recordID: id)
    contactRecord["name"] = name
    contactRecord["phoneNumber"] = phoneNumber
    try await privateCloudDatabase.save(contactRecord)
}
```

### Preparing a CKShare — [4:09]

```swift
// Preparing a CKShare

func createShare(contactRecord: CKRecord) async throws -> CKShare {
    let share = CKShare(rootRecord: contactRecord)

    try await privateCloudDatabase.modifyRecords(
        saving: [contactRecord, share], 
        deleting: []
    )

    return share
}
```

### UICloudSharingControllerDelegate — [5:25]

```swift
// UICloudSharingControllerDelegate

public protocol UICloudSharingControllerDelegate {

    // ...

    // Called after the CloudKit sharing controller failed to save the share record.
    func cloudSharingController(UICloudSharingController, failedToSaveShareWithError: Error)

    // Called after the CloudKit sharing controller saves the share record.
    func cloudSharingControllerDidSaveShare(UICloudSharingController)

    // Called after the user decided to stop sharing the record.
    func cloudSharingControllerDidStopSharing(UICloudSharingController)

}
```

### Processing an accepted share invitation — [6:27]

```swift
// Processing a user’s acceptance of a share invitation

func application(
    _ application: UIApplication,
    userDidAcceptCloudKitShareWith shareMetadata: CKShare.Metadata
) {
    let container = CKContainer(identifier: shareMetadata.containerIdentifier)

    Task {
        do {
            try await container.accept(shareMetadata)
        } catch {
            // Handle errors that may occur
        }
    }
}
```

### Fetching shared records — [7:24]

```swift
// Fetching records shared with the current iCloud user

func fetchSharedContacts(in zone: CKRecordZone) async throws {
    var changeToken: CKServerChangeToken? = nil
    var moreChangesComing = true

    while moreChangesComing {
        let changes = try await sharedCloudDatabase.recordZoneChanges(
            inZoneWith: zone.zoneID, 
            since: changeToken
        )

        // Process changes as needed (modifications and deletions)
        processChanges(changes)

        moreChangesComing = changes.moreComing
        changeToken = changes.changeToken
    }
}
```

### Search: Phone Number — [9:16]

```swift
// Search by phone number

let phoneNumber = "417-555-9311"
let participant = try await container.shareParticipant(forPhoneNumber: phoneNumber)
```

### Search: Email Address — [9:16]

```swift
// Search by email address

let emailAddress = "dave_knox@icloud.com"
let participant = try await container.shareParticipant(forEmailAddress: emailAddress)
```

### Search: Record ID — [9:16]

```swift
// Search by user record ID

let participant = try await container.shareParticipant(forUserRecordID: recordID)
```

### Add participant to a share — [9:32]

```swift
// Add participant to existing CKShare record

func addParticipant(_ participant: CKShare.Participant, to share: CKShare) async throws {
    participant.permission = .readWrite
    share.addParticipant(participant)
    try await privateCloudDatabase.save(share)
}
```

### Confirm invitation acceptance — [9:47]

```swift
// Fetch CKShare.Metadata and confirm accepting share from a given URL

func confirmShareParticipation(from url: URL) async throws {
    let shareMetadata = try await container.shareMetadata(for: url)
    try await container.accept(shareMetadata)
}
```

### Share an entire record zone — [11:14]

```swift
// Create a CKShare sharing an entire record zone

func createAndSaveShare(for zone: CKRecordZone) async throws -> CKShare {
    let share = CKShare(recordZoneID: zone.zoneID)
    try await privateCloudDatabase.save(share)

    if share.recordID.recordName == CKRecordNameZoneWideShare {
        // This is managing a shared record zone
    }

    return share
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/10874/3/E774EFC4-2BA1-475F-A66D-CACB5A60FDCE/cmaf.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/10874) — developer.apple.com. Indexed for agent consumption._
