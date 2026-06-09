---
id: "wwdc2021-10086"
event: "wwdc2021"
year: 2021
title: "What's new in CloudKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10086"
topics: ["Essentials", "Privacy & Security", "System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# What's new in CloudKit

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10086](https://developer.apple.com/videos/play/wwdc2021/10086)

CloudKit provides a secure, convenient, and reliable cloud database for your apps — and it’s only getting better. Discover how you can unravel your threads with support for async/await and convenience API additions. We’ll also show you how to encourage collaboration between people using your app through sharing entire record zones of data, and explore how to adopt CloudKit features like encrypted values and help protect sensitive data within your app.

To get the most out of this session, we recommend being familiar with CloudKit and its operations on containers, as well as a basic understanding of record and data types.

**Keywords:** `cloud`, `database`, `encrypted`, `encryption`, `fields`, `hierarchical`, `privacy`, `record`, `security`, `share`, `sharing`, `storage`, `zone`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,749 words)

## Documentation & Resources

- [CloudKit Samples: Encryption](https://github.com/apple/cloudkit-sample-encryption) _samplecode_
- [CloudKit Samples: Private Database](https://github.com/apple/cloudkit-sample-privatedb) _samplecode_
- [CloudKit](https://developer.apple.com/documentation/CloudKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CloudKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CloudKit.json

## Code Snippets

### CloudKit: Existing convenience API — [3:34]

```swift
// Sample code using existing Convenience API

/// Delete the last person record.
/// - Parameter completionHandler: An optional handler to process completion `success` or `failure`.
func deleteLastPerson(completionHandler: ((Result<Void, Error>) -> Void)? = nil) {
    database.delete(withRecordID: lastPersonRecordId) { recordId, error in
        if let recordId = recordId {
            os_log("Record with ID \(recordId.recordName) was deleted.")
        }
        if let error = error {
            self.reportError(error)
            // If there is a completion handler, pass along the error here.
            completionHandler?(.failure(error))
        } else {
            // If there is a completion handler, like during tests, call it back now.
            completionHandler?(.success(()))
        }
    }
}
```

### CloudKit: Async convenience API — [4:04]

```swift
// Sample code updated to CloudKit Async API

/// Delete the last person record.
func deleteLastPerson() async throws {
    do {
        let recordId = try await database.deleteRecord(with: lastPersonRecordId)
        os_log("Record with ID \(recordId.recordName) was deleted.")
    } catch {
        self.reportError(error)
        throw error
    }
}
```

### CloudKit: Existing completion blocks — [5:39]

```swift
// Error reporting in CKFetchRecordsOperation

extension CKFetchRecordsOperation {
    var perRecordCompletionBlock: ((CKRecord?, CKRecord.ID?, Error?) -> Void)?

    var fetchRecordsCompletionBlock: (([CKRecord.ID : CKRecord]?, Error?) -> Void)?
}


fetchRecordsOp.perRecordCompletionBlock = { record, recordID, error in
    // error is CKError.unknownItem. 
}

fetchRecordsOp.fetchRecordsCompletionBlock = { recordsByRecordID, operationError in
    // operationError is CKError.partialFailure.
    // operationError.partialErrorsByItemID[missingRecordID] is CKError.unknownItem.
}
```

### CloudKit: Result type completion blocks — [6:35]

```swift
// Error reporting in CKFetchRecordsOperation

extension CKFetchRecordsOperation {
    var perRecordResultBlock: ((CKRecord.ID, Result<CKRecord, Error>) -> Void)?

    var fetchRecordsResultBlock: ((Result<Void, Error>) -> Void)?
}


fetchRecordsOp.perRecordResultBlock = { recordID, result in
    // result is .failure(CKError.unknownItem) or .success(record).
}

fetchRecordsOp.fetchRecordsResultBlock = { result in
    // result is .success.
}
```

### CloudKit: Delete single item — [9:14]

```swift
// Single item delete

func deleteLastPerson() async throws {
    do {
        let recordId = try await database.deleteRecord(with: lastPersonRecordId)
        os_log("Record with ID \(recordId.recordName) was deleted.")
    } catch {
        self.reportError(error)
        throw error
    }
}
```

### CloudKit: Delete batch — [9:37]

```swift
// Batched modifications

func deleteLastPeople() async throws {
    do {
        let recordIds = [lastPersonRecordId, penultimatePersonRecordId]
        let (_, deleteResults) = try await database.modifyRecords(deleting: recordIds)
        for (recordId, deleteResult) in deleteResults {
            switch deleteResult {
            case .failure(let error):
                self.reportError(error, itemId: recordId)
            case .success:
                os_log("Record with ID \(recordId.recordName) was deleted.")
            }
        }
    } catch let operationError {
        self.reportError(operationError)
        throw operationError
    }
}
```

### CloudKit: Encrypted values — [13:43]

```swift
extension CKRecord {
    @NSCopying open var encryptedValues: CKRecordKeyValueSetting { get }
}
```

### CloudKit: Using encrypted values — [14:29]

```swift
// Device 1: Encrypt data before calling CKModifyRecordsOperation.

myRecord.encryptedValues["encryptedStringField"] = "Sensitive value"

// Device 2: Decrypt data after calling CKFetchRecordsOperation.

let decryptedString = myRecord.encryptedValues["encryptedStringField"] as? String
```

### CloudKit: Account status — [16:35]

```swift
open func accountStatus(completionHandler: @escaping (CKAccountStatus, Error?) -> Void)
```

### CloudKit: CKAccountStatus — [16:46]

```swift
public enum CKAccountStatus : Int {
    case couldNotDetermine
    case available
    case restricted
    case noAccount
    case temporarilyUnavailable
}
```

### CloudKit: Setup a record hierarchy — [21:10]

```swift
// Share a record hierarchy


let zone = CKRecordZone(zoneName: "MyZone")

// Save zone...

let fileRecordA = CKRecord(recordType: "File", recordID: CKRecord.ID(zoneID: zone.zoneID))
let fileRecordB = CKRecord(recordType: "File", recordID: CKRecord.ID(zoneID: zone.zoneID))
let folderRecord = CKRecord(recordType: "Folder", recordID: CKRecord.ID(zoneID: zone.zoneID))

fileRecordA.setParent(folderRecord)
fileRecordB.setParent(folderRecord)

// Save records...
```

### CloudKit: Record Hierarchy, Share — [21:41]

```swift
// Share a record hierarchy


let share = CKShare(rootRecord: folderRecord)

do {
    let (saveResults, _) = try await database.modifyRecords(saving: [folderRecord, share])
    for (recordID, saveResult) in saveResults { 
        // Handle per-record result.
    }
} catch let operationError { 
    // Handle operation error.
}
```

### CloudKit: Share a Record Zone — [22:51]

```swift
// Share a record zone


let zone = CKRecordZone(zoneName: "MyZone")

// Save zone... 

let share = CKShare(recordZoneID: zone.zoneID)

do {
    let (saveResults, _) = try await database.modifyRecords(saving: [share])
    for (recordID, saveResult) in saveResults { 
        // Handle per-record result.
    }
} catch let operationError { 
    // Handle operation error.
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10086/3/0126BD48-6C5E-4D8C-9464-DA85CFDF193B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10086/3/0126BD48-6C5E-4D8C-9464-DA85CFDF193B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10086) — developer.apple.com. Indexed for agent consumption._