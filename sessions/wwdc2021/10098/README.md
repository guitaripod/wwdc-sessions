---
id: "wwdc2021-10098"
event: "wwdc2021"
year: 2021
title: "Showcase app data in Spotlight"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10098"
topics: ["SwiftUI & UI Frameworks", "System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Showcase app data in Spotlight

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10098](https://developer.apple.com/videos/play/wwdc2021/10098)

Discover how Core Data can surface data from your app in Spotlight with as little as two lines of code. Learn how to make that data discoverable in Spotlight search and to customize how it is presented to people on device. Lastly, we’ll show you how to implement full-text search within your app, driven completely with the data indexed by Spotlight.

**Keywords:** `app data in spotlight`, `attributeset`, `coredata`, `core data`, `cssearchableitemattributeset`, `cssearchqueryobject`, `define attribute set`, `forstorewith:coordinator`, `indexing event loop`, `index update notifications`, `nscoredata`, `nscoredatacorespotlightdelegate`, `nscoredatacorespotlightdelegate.indexdidupdatenotification`, `nsexpression`, `query string`, `search my app in spotlight`, `search query`, `spotlight`, `spotlight display name`, `spotlightindexer`, `spotlight search`, `startspotlightindexing`, `stopspotlightindexing`, `tag`, `tags app`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,198 words)

## Documentation & Resources

- [Showcase App Data in Spotlight](https://developer.apple.com/documentation/CoreData/showcase-app-data-in-spotlight) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreData/showcase-app-data-in-spotlight
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreData/showcase-app-data-in-spotlight.json

## Code Snippets

### Creating a NSCoreDataCoreSpotlightDelegate — [2:40]

```swift
let spotlightDelegate = NSCoreDataCoreSpotlightDelegate(forStoreWith: description,
                                                        coordinator: coordinator)
spotlightDelegate.startSpotlightIndexing()
```

### Adding a NSCoreDataCoreSpotlightDelegate to a CoreDataStack — [5:24]

```swift
import Foundation
import CoreData

class CoreDataStack {
    private (set) var spotlightIndexer: TagsSpotlightDelegate?

    lazy var persistentContainer: NSPersistentContainer = {
        let container = NSPersistentContainer(name: "Tags")

        guard let description = container.persistentStoreDescriptions.first else {
            fatalError("###\(#function): Failed to retrieve a persistent store description.")
        }

        description.type = NSSQLiteStoreType
        description.setOption(true as NSNumber, forKey: NSPersistentStoreRemoteChangeNotificationPostOptionKey)
        description.setOption(true as NSNumber, forKey: NSPersistentHistoryTrackingKey)

        container.loadPersistentStores(completionHandler: { (_, error) in
            guard let error = error as NSError? else { return }
            fatalError("###\(#function): Failed to load persistent stores:\(error)")
        })

        spotlightIndexer = TagsSpotlightDelegate(forStoreWith: description,
                                                 coordinator: container.persistentStoreCoordinator)

        container.viewContext.mergePolicy = NSMergeByPropertyObjectTrumpMergePolicy

        container.viewContext.automaticallyMergesChangesFromParent = true
        do {
            try container.viewContext.setQueryGenerationFrom(.current)
        } catch {
            fatalError("###\(#function): Failed to pin viewContext to the current generation:\(error)")
        }

        return container
    }()
}
```

### Creating TagsSpotlightDelegate — [6:24]

```swift
class TagsSpotlightDelegate: NSCoreDataCoreSpotlightDelegate {
    override func domainIdentifier() -> String {
        return "com.example.apple-samplecode.tags"
    }

    override func indexName() -> String? {
        return "tags-index"
    }

    override func attributeSet(for object: NSManagedObject) -> CSSearchableItemAttributeSet? {
        if let photo = object as? Photo {
            let attributeSet = CSSearchableItemAttributeSet(contentType: .image)
            attributeSet.identifier = photo.uniqueName
            attributeSet.displayName = photo.userSpecifiedName
            attributeSet.thumbnailData = photo.thumbnail?.data
            for case let tag as Tag in photo.tags ?? [] {
                if let name = tag.name {
                    if attributeSet.keywords != nil {
                        attributeSet.keywords?.append(name)
                    } else {
                        attributeSet.keywords = [name]
                    }
                }
            }
            return attributeSet
        } else if let object as? Tag {
            let attributeSet = CSSearchableItemAttributeSet(contentType: .text)
            attributeSet.displayName = tag.name
            return attributeSet
        }
        return nil
    }
}
```

### Customizing PhotosViewController with Spotlight delegate functionality — [9:51]

```swift
class PhotosViewController: UICollectionViewController {
    @IBOutlet var generateDefaultPhotosItem: UIBarButtonItem!
    @IBOutlet var deleteSpotlightIndexItem: UIBarButtonItem!
    @IBOutlet var startStopIndexingItem: UIBarButtonItem!

    private var isTagging = false
    private var spotlightFoundItems = [CSSearchableItem]()
    private static let defaultSectionNumber = 0
    private var searchQuery: CSSearchQuery?
    var spotlightUpdateObserver: NSObjectProtocol?

    private lazy var spotlightIndexer: TagsSpotlightDelegate = {
        let appDelegate = UIApplication.shared.delegate as? AppDelegate
        return appDelegate!.coreDataStack.spotlightIndexer!
    }()

    override func viewDidLoad() {
        super.viewDidLoad()

        // ...

        toggleSpotlightIndexing(enabled: true)
    }

    @IBAction func deleteSpotlightIndex(_ sender: Any) {
        toggleSpotlightIndexing(enabled: false)

        spotlightIndexer.deleteSpotlightIndex(completionHandler: { (error) in
            if let err = error {
                print("Encountered error while deleting Spotlight index data, \(err.localizedDescription)")
            } else {
                print("Finished deleting Spotlight index data.")
            }
        })
    }

    @IBAction func toggleSpotlightIndexingEnabled(_ sender: Any) {
        if spotlightIndexer.isIndexingEnabled == true {
            toggleSpotlightIndexing(enabled: false)
        } else {
            toggleSpotlightIndexing(enabled: true)
        }
    }

    private func toggleSpotlightIndexing(enabled: Bool) {
        if enabled {
            spotlightIndexer.startSpotlightIndexing()
            startStopIndexingItem.image = UIImage(systemName: "pause")
        } else {
            spotlightIndexer.stopSpotlightIndexing()
            startStopIndexingItem.image = UIImage(systemName: "play")
        }

        let center = NotificationCenter.default
        if spotlightIndexer.isIndexingEnabled && spotlightUpdateObserver == nil {
            let queue = OperationQueue.main
            spotlightUpdateObserver = center.addObserver(forName: NSCoreDataCoreSpotlightDelegate.indexDidUpdateNotification,
                                                         object: nil,
                                                         queue: queue) { (notification) in
                let userInfo = notification.userInfo
                let storeID = userInfo?[NSStoreUUIDKey] as? String
                let token = userInfo?[NSPersistentHistoryTokenKey] as? NSPersistentHistoryToken
                if let storeID = storeID, let token = token {
                    print("Store with identifier \(storeID) has completed ",
                          "indexing and has processed history token up through \(String(describing: token)).")
                }
            }
        } else {
            if spotlightUpdateObserver == nil {
                return
            }
            center.removeObserver(spotlightUpdateObserver as Any)
        }
    }
}
```

### Adding full-text search to PhotosViewController — [13:13]

```swift
extension PhotosViewController: UISearchResultsUpdating {
    func updateSearchResults(for searchController: UISearchController) {
        guard let userInput = searchController.searchBar.text, !userInput.isEmpty else {
            dataProvider.performFetch(predicate: nil)
            reloadCollectionView()
            return
        }

        let escapedString = userInput.replacingOccurrences(of: "\\", with: "\\\\").replacingOccurrences(of: "\"", with: "\\\"")
        let queryString = "(keywords == \"" + escapedString + "*\"cwdt)"

        searchQuery = CSSearchQuery(queryString: queryString, attributes: ["displayName", "keywords"])

        // Set a handler for results. This will be a called 0 or more times.
        searchQuery?.foundItemsHandler = { items in
            DispatchQueue.main.async {
                self.spotlightFoundItems += items
            }
        }

        // Set a completion handler. This will be called once.
        searchQuery?.completionHandler = { error in
            guard error == nil else {
                print("CSSearchQuery completed with error: \(error!).")
                return
            }

            DispatchQueue.main.async {
                self.dataProvider.performFetch(searchableItems: self.spotlightFoundItems)
                self.reloadCollectionView()
                self.spotlightFoundItems.removeAll()
            }
        }

        // Start the query.
        searchQuery?.start()
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10098/5/E1444CD9-0588-4D3B-8AFA-EB590BA9CD23/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10098/5/E1444CD9-0588-4D3B-8AFA-EB590BA9CD23/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10098) — developer.apple.com. Indexed for agent consumption._