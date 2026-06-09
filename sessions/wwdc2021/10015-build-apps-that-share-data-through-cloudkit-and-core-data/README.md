---
id: "wwdc2021-10015"
event: "wwdc2021"
year: 2021
title: "Build apps that share data through CloudKit and Core Data"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10015"
topics: ["SwiftUI & UI Frameworks", "System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Build apps that share data through CloudKit and Core Data

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10015](https://developer.apple.com/videos/play/wwdc2021/10015)

Learn how to easily build apps that share data between multiple iCloud users with NSPersistentCloudKitContainer. Discover how to create informative experiences around shared data and learn about the CloudKit technologies that support these features in Core Data. To get the most out of this session, check out our previous videos on NSPersistentCloudKitContainer: "Using Core Data With CloudKit" from WWDC19 and "Sync a Core Data store with the CloudKit public database" from WWDC20.

**Keywords:** `allowscloudencryption`, `allows cloud encryption`, `candeleterecord`, `canmodifymanagedobjects`, `canupdaterecord`, `ckdatabase`, `ckrecord`, `ckshare`, `cksharedrecord`, `ckshare.metadata`, `cloud encryption`, `cloudkit`, `coredata`, `core data`, `decorate shared objects`, `encrypted record values`, `encryptedvalues`, `encryption`, `encrypt sensitive data`, `fetchshares`, `initializeschema`, `isshared`, `nspersistentcloudkitcontainer`, `owners and participants`, `persistent cloudkit container`, `persistent store`, `.private`, `private database`, `record`, `record sharing`, `.share`, `.shared`, `shared database`, `shared objects`, `sharing architecture`, `sharing data`, `sharing information`, `sharingprovider`, `testing`, `user keychain`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,393 words)

## Documentation & Resources

- [Synchronizing a local store to the cloud](https://developer.apple.com/documentation/CoreData/synchronizing-a-local-store-to-the-cloud) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData/synchronizing-a-local-store-to-the-cloud
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData/synchronizing-a-local-store-to-the-cloud.json

## Code Snippets

### Add shared store description — [5:20]

```swift
let privateStoreDescription = container.persistentStoreDescriptions.first!
let storesURL = privateStoreDescription.url!.deletingLastPathComponent()
privateStoreDescription.url = storesURL.appendingPathComponent("private.sqlite")
privateStoreDescription.setOption(true as NSNumber, forKey: NSPersistentHistoryTrackingKey)
privateStoreDescription.setOption(true as NSNumber, forKey: NSPersistentStoreRemoteChangeNotificationPostOptionKey)

let sharedStoreURL = storesURL.appendingPathComponent("shared.sqlite")
let sharedStoreDescription = privateStoreDescription.copy()
sharedStoreDescription.url = sharedStoreURL

let containerIdentifier = privateStoreDescription.cloudKitContainerOptions!.containerIdentifier
let sharedStoreOptions = NSPersistentCloudKitContainerOptions(containerIdentifier: containerIdentifier)
sharedStoreOptions.databaseScope = .shared
sharedStoreDescription.cloudKitContainerOptions = sharedStoreOptions
container.persistentStoreDescriptions.append(sharedStoreDescription)
```

### shareNoteAction, DetailViewController.swift — [6:00]

```swift
@IBAction func shareNoteAction(_ sender: Any) {
  guard let barButtonItem = sender as? UIBarButtonItem else {
    fatalError("Not a UI Bar Button item??")
  }

  guard let post = self.post else {
    fatalError("Can't share without a post")
  }

  let container = AppDelegate.sharedAppDelegate.coreDataStack.persistentContainer
  let cloudSharingController = UICloudSharingController {
    (controller, completion: @escaping (CKShare?, CKContainer?, Error?) -> Void) in
    container.share([post], to: nil) { objectIDs, share, container, error in
			if let actualShare = share {
				post.managedObjectContext?.performAndWait {
					actualShare[CKShare.SystemFieldKey.title] = post.title
				}
			}
			completion(share, container, error)
		}
  }
  cloudSharingController.delegate = self

  if let popover = cloudSharingController.popoverPresentationController {
    popover.barButtonItem = barButtonItem
  }
  present(cloudSharingController, animated: true) {}
}
```

### SharingProvider — [17:06]

```swift
protocol SharingProvider {
  func isShared(object: NSManagedObject) -> Bool
  func isShared(objectID: NSManagedObjectID) -> Bool
  func participants(for object: NSManagedObject) -> [RenderableShareParticipant]
  func shares(matching objectIDs: [NSManagedObjectID]) throws -> [NSManagedObjectID: RenderableShare]
  func canEdit(object: NSManagedObject) -> Bool
  func canDelete(object: NSManagedObject) -> Bool
}
```

### Decorate table cells for shared posts, MainViewController.swift — [17:58]

```swift
override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    guard let cell = tableView.dequeueReusableCell(withIdentifier: "PostCell", for: indexPath) as? PostCell else {
        fatalError("###\(#function): Failed to dequeue a PostCell. Check the cell reusable identifier in Main.storyboard.")
    }
    let post = dataProvider.fetchedResultsController.object(at: indexPath)
    cell.title.text = post.title
    cell.post = post
    cell.collectionView.reloadData()
    cell.collectionView.invalidateIntrinsicContentSize()

    if let attachments = post.attachments, attachments.allObjects.isEmpty {
        cell.hasAttachmentLabel.isHidden = true
    } else {
        cell.hasAttachmentLabel.isHidden = false
    }

    if sharingProvider.isShared(object: post) {
        let attachment = NSTextAttachment(image: UIImage(systemName: "person.circle")!)
        let attributedString = NSMutableAttributedString(attachment: attachment)
        attributedString.append(NSAttributedString(string: " " + (post.title ?? "")))
        cell.title.text = nil
        cell.title.attributedText = attributedString
    }
    return cell
}
```

### Testing the MainViewController's table view, TestMainViewController.swift — [18:44]

```swift
func testSharedPostsGetDisclosure() {
    var sharedObjectIDs: Set<NSManagedObjectID> = Set()
    let context = coreDataStack.persistentContainer.viewContext
    self.generatePosts(in: context, postSaveBlock: { posts in
        for (index, post) in posts.enumerated() where (index % 4) == 0 {
            sharedObjectIDs.insert(post.objectID)
        }
    })

    let provider = BlockBasedShareProvider(stack: coreDataStack)
    provider.isSharedBlock = sharedObjectIDs.contains
    mainViewController.sharingProvider = provider

    do {
        try mainViewController.dataProvider.fetchedResultsController.performFetch()
    } catch let error {
        XCTFail("Error while fetching \(error)")
    }

    reloadTableView()
    let rowCount = mainViewController.tableView(mainViewController.tableView,
                                                    numberOfRowsInSection: 0)
    XCTAssertEqual(100, rowCount)
    guard let expectedSharedImage = UIImage(systemName: "person.circle") else {
        XCTFail("Failed to get the person system image.")
        return
    }

    for index in 0..<rowCount {
        let indexPath = IndexPath(row: index, section: 0)
        let post = mainViewController.dataProvider.fetchedResultsController.object(at: indexPath)
        guard let title = post.title else {
            XCTFail("All posts should have been given a title.")
            return
        }

        guard let cell = mainViewController.tableView(mainViewController.tableView,
                                                           cellForRowAt: indexPath) as? PostCell else {
            XCTFail("Encountered an unexpected cell type in the main view controller's table view.")
            return
        }

        if sharedObjectIDs.contains(post.objectID) {
            guard let attributedText = cell.title.attributedText else {
                XCTFail("Failed to get the attributed text of \(cell). Was it not set?")
                return
            }

            guard let attachment = attributedText.attributes(at: 0, effectiveRange: nil)[.attachment] as? NSTextAttachment else {
                XCTFail("Expected an image attachment at the first character.")
                return
            }

            XCTAssertEqual(expectedSharedImage, attachment.image)
        } else {
            XCTAssertEqual(cell.title.text, title)
        }
    }
}

class BlockBasedShareProvider: SharingProvider {
    var coreDataStack: CoreDataStack
    init(stack: CoreDataStack) {
        coreDataStack = stack
    }

    func isShared(object: NSManagedObject) -> Bool {
        return isShared(objectID: object.objectID)
    }

    public var isSharedBlock: ((_ object: NSManagedObjectID) -> Bool)? = nil
    func isShared(objectID: NSManagedObjectID) -> Bool {
        guard let block = isSharedBlock else {
            return coreDataStack.isShared(objectID: objectID)
        }
        return block(objectID)
    }

    public var participantsBlock: ((_ object: NSManagedObject) -> [RenderableShareParticipant])? = nil
    func participants(for object: NSManagedObject) -> [RenderableShareParticipant] {
        guard let block = participantsBlock else {
            return coreDataStack.participants(for: object)
        }
        return block(object)
    }

    public var sharesBlock: ((_ objectIDs: [NSManagedObjectID]) -> [NSManagedObjectID: RenderableShare])? = nil
    func shares(matching objectIDs: [NSManagedObjectID]) throws -> [NSManagedObjectID: RenderableShare] {
        guard let block = sharesBlock else {
            return try coreDataStack.shares(matching: objectIDs)
        }
        return block(objectIDs)
    }

    public var canEditBlock: ((_ object: NSManagedObject) -> Bool)? = nil
    func canEdit(object: NSManagedObject) -> Bool {
        guard let block = canEditBlock else {
            return coreDataStack.canEdit(object: object)
        }
        return block(object)
    }

    public var canDeleteBlock: ((_ object: NSManagedObject) -> Bool)? = nil
    func canDelete(object: NSManagedObject) -> Bool {
        guard let block = canDeleteBlock else {
            return coreDataStack.canDelete(object: object)
        }
        return block(object)
    }
}
```

### CoreDataStack + Sharing, CoreDataStack.swift — [20:01]

```swift
extension CoreDataStack: SharingProvider {
    func isShared(object: NSManagedObject) -> Bool {
        return isShared(objectID: object.objectID)
    }

    func isShared(objectID: NSManagedObjectID) -> Bool {
        var isShared = false
        if let persistentStore = objectID.persistentStore {
            if persistentStore == sharedPersistentStore {
                isShared = true
            } else {
                let container = persistentContainer
                do {
                    let shares = try container.fetchShares(matching: [objectID])
                    if nil != shares.first {
                        isShared = true
                    }
                } catch let error {
                    print("Failed to fetch share for \(objectID): \(error)")
                }
            }
        }
        return isShared
    }

    func participants(for object: NSManagedObject) -> [RenderableShareParticipant] {
        var participants = [CKShare.Participant]()
        do {
            let container = persistentContainer
            let shares = try container.fetchShares(matching: [object.objectID])
            if let share = shares[object.objectID] {
                participants = share.participants
            }
        } catch let error {
            print("Failed to fetch share for \(object): \(error)")
        }
        return participants
    }

    func shares(matching objectIDs: [NSManagedObjectID]) throws -> [NSManagedObjectID: RenderableShare] {
        return try persistentContainer.fetchShares(matching: objectIDs)
    }

    func canEdit(object: NSManagedObject) -> Bool {
        return persistentContainer.canUpdateRecord(forManagedObjectWith: object.objectID)
    }

    func canDelete(object: NSManagedObject) -> Bool {
        return persistentContainer.canDeleteRecord(forManagedObjectWith: object.objectID)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10015/4/7C4C52B4-3B54-4FCE-8300-BEA17FC4A7AE/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10015/4/7C4C52B4-3B54-4FCE-8300-BEA17FC4A7AE/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10015) — developer.apple.com. Indexed for agent consumption._
