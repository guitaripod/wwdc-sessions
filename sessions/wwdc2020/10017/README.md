---
id: "wwdc2020-10017"
event: "wwdc2020"
year: 2020
title: "Core Data: Sundries and maxims"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10017"
topics: ["Developer Tools", "SwiftUI & UI Frameworks", "System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Core Data: Sundries and maxims

**Event:** WWDC20 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10017](https://developer.apple.com/videos/play/wwdc2020/10017)

Core Data is the central way to durably and persistently store information from your app — and we’re going to show you how to refine that implementation for even faster data ingest and fetching. Discover how you can improve data capture with batch insert, tailor fetch requests to your data needs, and react to notifications about changes in the persistent store.

To get the most out of this session, you should know and have interacted with Core Data in the past. For more information on the framework, watch “Making Apps with Core Data.”

**Keywords:** `batch delete`, `batch ingestion`, `batch insert`, `batch insert with dictionary block`, `batch operations`, `block ingestion`, `dictionary block`, `fetch request`, `history request`, `nsbatchdeleterequest`, `nsbatchinsertrequest`, `nsmanagedobjectcontext`, `persistent history`, `persistent store`, `remote change notification`, `remote change notifications`, `upsert`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,935 words)

## Documentation & Resources

- [Loading and displaying a large data feed](https://developer.apple.com/documentation/SwiftUI/loading-and-displaying-a-large-data-feed) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/loading-and-displaying-a-large-data-feed
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/loading-and-displaying-a-large-data-feed.json

## Code Snippets

### Batch Operations - Enable Persistent History — [1:48]

```swift
storeDesc.setOption(true as NSNumber, forKey: NSPersistentHistoryTrackingKey)
```

### NSBatchInsertRequest.h — [2:32]

```swift
//NSBatchInsertRequest.h

@available(iOS 13.0, *)
open class NSBatchInsertRequest : NSPersistentStoreRequest {
    open var resultType: NSBatchInsertRequestResultType

    public convenience init(entityName: String, objects dictionaries: [[String : Any]])
    public convenience init(entity: NSEntityDescription, objects dictionaries: [[String : Any]])

    @available(iOS 14.0, *)
    open var dictionaryHandler: ((inout Dictionary<String, Any>) -> Void)?
    open var managedObjectHandler: ((inout NSManagedObject) -> Void)?

    public convenience init(entity: NSEntityDescription, dictionaryHandler handler: @escaping (inout Dictionary<String, Any>) -> Void)
    public convenience init(entity: NSEntityDescription, managedObjectHandler handler: @escaping (inout NSManagedObject) -> Void)
}
```

### Earthquakes Sample - Regular Save — [3:01]

```swift
//Earthquakes Sample - Regular Save

for quakeData in quakesBatch {
     guard let quake = NSEntityDescription.insertNewObject(forEntityName: "Quake", into: taskContext) as? Quake else { ... }
     do {
         try quake.update(with: quakeData)
     } catch QuakeError.missingData {
         ...
         taskContext.delete(quake)
     }
     ...
 }
 do {
     try taskContext.save()
 } catch { ... }
```

### Earthquakes Sample - Batch Insert with Array of Dictionaries — [3:16]

```swift
//Earthquakes Sample - Batch Insert

var quakePropertiesArray = [[String:Any]]()
for quake in quakesBatch {
    quakePropertiesArray.append(quake.dictionary)
}

let batchInsert = NSBatchInsertRequest(entityName: "Quake", objects: quakePropertiesArray)

var insertResult : NSBatchInsertResult
do {
    insertResult = try taskContext.execute(batchInsert) as! NSBatchInsertResult
    ... 
}
```

### Earthquakes Sample - Batch Insert with a block — [3:28]

```swift
//Earthquakes Sample - Batch Insert with a block

var batchInsert = NSBatchInsertRequest(entityName: "Quake", dictionaryHandler: { 
    (dictionary) in
        if (blockCount == batchSize) {
            return true
        } else {
            dictionary = quakesBatch[blockCount]
            blockCount += 1
        }
    })
    var insertResult : NSBatchInsertResult
    do {
        insertResult = try taskContext.execute(batchInsert) as! NSBatchInsertResult
        ...
    }
```

### NSBatchInsertRequest - UPSERT — [5:42]

```swift
let moc = NSManagedObjectContext(concurrencyType:
                           NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType)

moc.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy

insertResult = try moc.execute(insertRequest)
```

### Batch Update Example — [6:30]

```swift
//Earthquakes Sample - Batch Update

let updateRequest = NSBatchUpdateRequest(entityName: "Quake")
updateRequest.propertiesToUpdate = ["validated" : true]
updateRequest.predicate = NSPredicate("%K > 2.5", "magnitude")

var updateResult : NSBatchUpdateResult
do {
    updateResult = try taskContext.execute(updateRequest) as! NSBatchUpdateResult
    ... 
}
```

### Batch Delete without and with a Fetch Limit — [7:33]

```swift
// Batch Delete without and with a Fetch Limit

DispatchQueue.global(qos: .background).async {
    moc.performAndWait { () -> Void in
       do {
           let expirationDate = Date.init().addingTimeInterval(-30*24*3600)

           let request = NSFetchRequest<Quake>(entityName: "Quake")
           request.predicate = NSPredicate(format:"creationDate < %@", expirationDate)

           let batchDelete = NSBatchDeleteRequest(fetchRequest: request)
           batchDelete.fetchLimit = 1000
           moc.execute(batchDelete)
        }
    }
}
```

### Fetch average magnitude of each place — [12:18]

```swift
//Fetch average magnitude of each place

let magnitudeExp = NSExpression(forKeyPath: "magnitude")
let avgExp = NSExpression(forFunction: "avg:", arguments: [magnitudeExp])

let avgDesc = NSExpressionDescription()
avgDesc.expression = avgExp
avgDesc.name = "average magnitude"
avgDesc.expressionResultType = .floatAttributeType

let fetch = NSFetchRequest<NSFetchRequestResult>(entityName: "Quake")
fetch.propertiesToFetch = [avgDesc, "place"]
fetch.propertiesToGroupBy = ["place"]
fetch.resultType = .dictionaryResultType
```

### NSManagedObjectContext.h - Modernized Notifications — [13:36]

```swift
//NSManagedObjectContext.h

@available(iOS 14.0, *)
extension NSManagedObjectContext {
    public static let willSaveObjectsNotification: Notification.Name
    public static let didSaveObjectsNotification: Notification.Name
    public static let didChangeObjectsNotification: Notification.Name

    public static let didSaveObjectIDsNotification: Notification.Name
    public static let didMergeChangesObjectIDsNotification: Notification.Name
}
```

### NSManagedObjectContext.h - Modernized Keys — [13:54]

```swift
//NSManagedObjectContext.h

@available(iOS 14.0, *)
extension NSManagedObjectContext {
    public enum NotificationKey : String {  
        case sourceContext
        case queryGeneration
        case invalidatedAllObjects
        case insertedObjects
        case updatedObjects
        case deletedObjects
        case refreshedObjects
        case invalidatedObjects
        case insertedObjectIDs
        case updatedObjectIDs
        case deletedObjectIDs
        case refreshedObjectIDs
        case invalidatedObjectIDs
    }
}
```

### Enable Remote Change Notifications with Persistent History — [14:08]

```swift
storeDesc.setOption(true as NSNumber, forKey: NSPersistentStoreRemoteChangeNotificationPostOptionKey)
storeDesc.setOption(true as NSNumber, forKey: NSPersistentHistoryTrackingKey)
```

### History Pointers — [16:19]

```swift
let changeDesc = NSPersistentHistoryChange.entityDescription(with: moc)
let request = NSFetchRequest<NSFetchRequestResult>()

//Set fetch request entity and predicate
request.entity = changeDesc
request.predicate = 
    NSPredicate(format: "%K = %@",changeDesc?.attributesByName["changedObjectID"], objectID)

//Set up history request with distantPast and set fetch request              
let historyReq = NSPersistentHistoryChangeRequest.fetchHistory(after: Date.distantPast)
historyReq.fetchRequest = request

let results = try moc.execute(historyReq)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10017/5/F2FB4653-3146-4087-A264-6EFCE0C197D5/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10017) — developer.apple.com. Indexed for agent consumption._