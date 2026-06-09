---
id: "wwdc2022-10119"
event: "wwdc2022"
year: 2022
title: "Optimize your use of Core Data and CloudKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10119"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Optimize your use of Core Data and CloudKit

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10119](https://developer.apple.com/videos/play/wwdc2022/10119)

Join us as we explore the three parts of the development cycle that can help you optimize your Core Data and CloudKit implementation. We'll show you how you can analyze your app's architecture and feature set to verify assumptions, explore changes in behavior after ingesting large data sets, and get actionable feedback to make improvements to your workflow. To get the most out of this session, we recommend familiarity with syncing your data model to CloudKit.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,664 words)

## Documentation & Resources

- [Synchronizing a local store to the cloud](https://developer.apple.com/documentation/CoreData/synchronizing-a-local-store-to-the-cloud) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData/synchronizing-a-local-store-to-the-cloud
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData/synchronizing-a-local-store-to-the-cloud.json
- [Mirroring a Core Data store with CloudKit](https://developer.apple.com/documentation/CoreData/mirroring-a-core-data-store-with-cloudkit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData/mirroring-a-core-data-store-with-cloudkit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData/mirroring-a-core-data-store-with-cloudkit.json
- [Core Data](https://developer.apple.com/documentation/CoreData) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData.json

## Code Snippets

### Define a large data generator — [4:35]

```swift
class LargeDataGenerator {
    func generateData(context: NSManagedObjectContext) throws {
        try context.performAndWait {
            for postCount in 1...60 {
                //add a post               
                for attachmentCount in 1...11 {
                    //add an attachment with an image
                    let imageFileData = NSData(contentsOf: url!)!
               }
            }
        }
    }
}
```

### Testing a large data generator — [5:07]

```swift
class TestLargeDataGenerator: CoreDataCloudKitDemoUnitTestCase {
    func testGenerateData() throws {
        let context = self.coreDataStack.persistentContainer.newBackgroundContext()
        try self.generator.generateData(context: context)
        try context.performAndWait {                     
            let posts = try context.fetch(Post.fetchRequest())
            for post in posts {
                self.verify(post: post, has: 11, matching: imageDatas)
            }
        }
    }
}
```

### Sync generated data in test — [5:33]

```swift
func testExportThenImport() throws {
    let exportContainer = newContainer(role: "export", postLoadEventType: .setup)
    try self.generator.generateData(context: exportContainer.newBackgroundContext())
    self.expectation(for: .export, from: exportContainer)
    self.waitForExpectations(timeout: 1200)
}
```

### Expectation helper method — [6:35]

```swift
func expectation(for eventType: NSPersistentCloudKitContainer.EventType,
                 from container: NSPersistentCloudKitContainer) -> [XCTestExpectation] {
    var expectations = [XCTestExpectation]()
    for store in container.persistentStoreCoordinator.persistentStores {
        let expectation = self.expectation(
            forNotification: NSPersistentCloudKitContainer.eventChangedNotification,
            object: container
        ) { notification in
            let userInfoKey = NSPersistentCloudKitContainer.eventNotificationUserInfoKey
            let event = notification.userInfo![userInfoKey]               
            return (event.type == eventType) &&
                (event.storeIdentifier == store.identifier) &&
                (event.endDate != nil)
        }
        expectations.append(expectation)
    }
    return expectations
}
```

### Import data model in test — [7:18]

```swift
func testExportThenImport() throws {
    let exportContainer = newContainer(role: "export", postLoadEventType: .setup)
    try self.generator.generateData(context: exportContainer.newBackgroundContext())
    self.expectation(for: .export, from: exportContainer)
    self.waitForExpectations(timeout: 1200)

    let importContainer = newContainer(role: "import", postLoadEventType: .import)
    self.waitForExpectations(timeout: 1200)
}
```

### Data generator alert action — [8:23]

```swift
UIAlertAction(title: "Generator: Large Data", 
              style: .default) {_ in
    let generator = LargeDataGenerator()
    try generator.generateData(context: context)
    self.dismiss(animated: true)
}
```

### Eagerly generating thumbnail in data generator — [10:50]

```swift
func generateData(context: NSManagedObjectContext) throws {
    try context.performAndWait {
        for postCount in 1...60 {
            for attachmentCount in 1...11 {
                let attachment = Attachment(context: context)
                let imageData = ImageData(context: context)
                imageData.attachment = attachment
                imageData.data = autoreleasepool {
                    let imageFileData = NSData(contentsOf: url!)!
                    attachment.thumbnail = Attachment.thumbnail(from: imageFileData,        
                                                                thumbnailPixelSize: 80)
                    return imageFileData
                }
            }
        }
    }
}
```

### Lazily generating thumbnail in data generator — [11:13]

```swift
func generateData(context: NSManagedObjectContext) throws {
    try context.performAndWait {
        for postCount in 1...60 {
            for attachmentCount in 1...11 {
                let attachment = Attachment(context: context)
                let imageData = ImageData(context: context)
                imageData.attachment = attachment
                imageData.data = autoreleasepool {
                    return NSData(contentsOf: url!)!
                }
            }
        }
    }
}
```

### Problematic verifyPosts implementation — [14:14]

```swift
func verifyPosts(in context: NSManagedObjectContext) throws {
    try context.performAndWait {
        let fetchRequest = Post.fetchRequest()
        let posts = try context.fetch(fetchRequest)

        for post in posts {
            // verify post

            let attachments = post.attachments as! Set<Attachment>
            for attachment in attachments {

                XCTAssertNotNil(attachment.imageData)
                //verify image
            }
        }
    }
}
```

### Efficient verifyPosts implementation — [14:49]

```swift
func verifyPosts(in context: NSManagedObjectContext) throws {
    try context.performAndWait {
        let fetchRequest = Attachment.fetchRequest()
        fetchRequest.resultType = .managedObjectIDResultType
        let attachments = try context.fetch(fetchRequest) as! [NSManagedObjectID]

        for index in 0...attachments.count - 1 {
            let attachment = context.object(with: attachments[index]) as! Attachment

            //verify attachment
            let post = attachment.post!
            //verify post

            if 0 == (index % 10) {
                context.reset()
            }
        }
    }
}
```

### Display logs using `log stream` — [20:41]

```bash
# Application
log stream --predicate 'process = "CoreDataCloudKitDemo" AND 
                        (sender = "CoreData" OR sender = "CloudKit")'

# CloudKit 
log stream --predicate 'process = "cloudd" AND
                        message contains[cd] "iCloud.com.example.CloudKitCoreDataDemo"'

# Push
log stream --predicate 'process = "apsd" AND message contains[cd] "CoreDataCloudKitDemo"'

# Scheduling
log stream --predicate 'process = "dasd" AND 
                        message contains[cd] "com.apple.coredata.cloudkit.activity" AND
                        message contains[cd] "CEF8F02F-81DC-48E6-B293-6FCD357EF80F"'
```

### Display logs with `log show` — [24:36]

```bash
log show --info --debug
    --predicate 'process = "apsd" AND
                 message contains[cd] "iCloud.com.example.CloudKitCoreDataDemo"'
    system_logs.logarchive

log show --info --debug
    --start "2022-06-04 09:40:00"
    --end "2022-06-04 09:42:00"
    --predicate 'process = "apsd" AND 
                 message contains[cd] "iCloud.com.example.CloudKitCoreDataDemo"'
    system_logs.logarchive
```

### Provide a predicate to `log show` — [25:17]

```bash
log show --info --debug
    --start "2022-06-04 09:40:00" --end "2022-06-04 09:42:00"
    --predicate '(process = "CoreDataCloudKitDemo" AND
                      (sender = "CoreData" or sender = "CloudKit")) OR
                 (process = "cloudd" AND
                      message contains[cd] "iCloud.com.example.CloudKitCoreDataDemo") OR
                 (process = "apsd" AND message contains[cd] "CoreDataCloudKitDemo") OR 
                 (process = "dasd" AND
                     message contains[cd] "com.apple.coredata.cloudkit.activity" AND
                     message contains[cd] "CEF8F02F-81DC-48E6-B293-6FCD357EF80F")'
    system_logs.logarchive
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10119/4/8D4ACDA6-A3CE-4294-8DFE-B4CF5DE26D86/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10119/4/8D4ACDA6-A3CE-4294-8DFE-B4CF5DE26D86/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10119) — developer.apple.com. Indexed for agent consumption._
