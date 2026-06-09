---
id: "wwdc2020-10045"
event: "wwdc2020"
year: 2020
title: "Advances in diffable data sources"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10045"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Advances in diffable data sources

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10045](https://developer.apple.com/videos/play/wwdc2020/10045)

Diffable data sources dramatically simplify the work involved in managing and updating collection and table views to create dynamic and responsive experiences in your apps. Discover how you can use section snapshots to efficiently build lists and outline collection views for iOS and iPadOS and provide support for implementing the sidebar in an iPad app. We’ll also show you how to simplify cell reordering using UICollectionViewDiffableDataSource to help you streamline your code and build app interfaces more quickly.

This session builds on 2019’s “Advances in UI Data Sources,” which you may want to check out first.

**Keywords:** `uicollectionview`, `uitableview`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,742 words)

## Documentation & Resources

- [Implementing modern collection views](https://developer.apple.com/documentation/UIKit/implementing-modern-collection-views) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/implementing-modern-collection-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/implementing-modern-collection-views.json

## Code Snippets

### NSDiffableDataSourceSectionSnapshot — [3:24]

```swift
// NSDiffableDataSourceSectionSnapshot

public struct NSDiffableDataSourceSectionSnapshot<ItemIdentifierType> where ItemIdentifierType : Hashable {

    public init()

    public init(_ snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)

    public mutating func append(_ items: [ItemIdentifierType], to parent: ItemIdentifierType? = nil)

    public mutating func insert(_ items: [ItemIdentifierType], before item: ItemIdentifierType)

    public mutating func insert(_ items: [ItemIdentifierType], after item: ItemIdentifierType)

    public mutating func delete(_ items: [ItemIdentifierType])

    public mutating func deleteAll()

    public mutating func expand(_ items: [ItemIdentifierType])

    public mutating func collapse(_ items: [ItemIdentifierType])

    public mutating func replace(childrenOf parent: ItemIdentifierType, using snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>)

    public mutating func insert(_ snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, before item: (ItemIdentifierType))

    public mutating func insert(_ snapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>, after item: (ItemIdentifierType))

    public func isExpanded(_ item: ItemIdentifierType) -> Bool

    public func isVisible(_ item: ItemIdentifierType) -> Bool

    public func contains(_ item: ItemIdentifierType) -> Bool

    public func level(of item: ItemIdentifierType) -> Int

    public func index(of item: ItemIdentifierType) -> Int?

    public func parent(of child: ItemIdentifierType) -> ItemIdentifierType?

    public func snapshot(of parent: ItemIdentifierType, includingParent: Bool = false) -> NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>

    public var items: [ItemIdentifierType] { get }

    public var rootItems: [ItemIdentifierType] { get }

    public var visibleItems: [ItemIdentifierType] { get }
}
```

### UICollectionViewDiffableDataSource Additions for Section Snapshots — [4:20]

```swift
// UICollectionViewDiffableDataSource additions for iOS 14

extension UICollectionViewDiffableDataSource<Item, Section> {

    func apply(_ snapshot: NSDiffableDataSourceSectionSnapshot<Item>, 
               to section: Section, 
               animatingDifferences: Bool = true, 
               completion: (() -> Void)? = nil)

    func snapshot(for section: Section) ->   
                  NSDiffableDataSourceSectionSnapshot<Item>
}
```

### Using Snapshots and Section Snapshots together — [4:43]

```swift
// Example of using snapshots and section snapshots together

func update(animated: Bool=true) {

   // Add our sections in a specific order
   let sections: [Section] = [.recent, .top, .suggested]
   var snapshot = NSDiffableDataSourceSnapshot<Section, Item>()
   snapshot.appendSections(sections)
   dataSource.apply(snapshot, animatingDifferences: animated)

   // update each section's data via section snapshots in the existing position
   for section in sections {
      let sectionItems = items(for: section)
      var sectionSnapshot = NSDiffableDataSourceSectionSnapshot<Item>()
      sectionSnapshot.append(sectionItems)
      dataSource.apply(sectionSnapshot, to: section, animatingDifferences:animated)
   }
}
```

### Creating hierarchical data with NSDiffableDataSourceSectionSnapshot — [5:18]

```swift
// Create hierarchical data for our Outline

var sectionSnapshot = ...

sectionSnapshot.append(["Smileys", "Nature", 
                        "Food", "Activities",
                        "Travel", "Objects", "Symbols"])

sectionSnapshot.append(["🥃", "🍎", "🍑"], to: "Food")
```

### Child Section Snapshots — [6:01]

```swift
let childSnapshot = sectionSnapshot.snapshot(for: parent, includingParent: false)
```

### Section Snapshot Expand / Collapse API — [6:11]

```swift
struct NSDiffableDataSourceSectionSnapshot<Item: Hashable> {
   func expand(_ items: [Item])
   func collapse(_ items: [Item])
   func isExpanded(_ item: Item) -> Bool
}
```

### Section Snapshot Handlers — [7:21]

```swift
// Section Snapshot Handlers: handling user interactions for expand / collapse state changes

extension UICollectionViewDiffableDataSource {

  struct SectionSnapshotHandlers<Item> {
    var shouldExpandItem: ((Item) -> Bool)?
    var willExpandItem: ((Item) -> Void)?

    var shouldCollapseItem: ((Item) -> Bool)?
    var willCollapseItem: ((Item) -> Void)?

    var snapshotForExpandingParent: ((Item, NSDiffableDataSourceSectionSnapshot<Item>) -> NSDiffableDataSourceSectionSnapshot<Item>)?
  }

  var sectionSnapshotHandlers: SectionSnapshotHandlers<Item>

}
```

### Reordering Handlers — [8:52]

```swift
// Diffable Data Source Reordering Handlers

extension UICollectionViewDiffableDataSource {

  struct ReorderingHandlers {
    var canReorderItem: ((Item) -> Bool)?
    var willReorder: ((NSDiffableDataSourceTransaction<Section, Item>) -> Void)?
    var didReorder: ((NSDiffableDataSourceTransaction<Section, Item>) -> Void)?
  }

  var reorderingHandlers: ReorderingHandlers
}
```

### Diffable Data Source Transactions — [9:45]

```swift
// NSDiffableDataSourceTransaction

struct NSDiffableDataSourceTransaction<Section, Item> {
   var initialSnapshot: NSDiffableDataSourceSnapshot<Section, Item> { get }
   var finalSnapshot: NSDiffableDataSourceSnapshot<Section, Item> { get }
   var difference: CollectionDifference<Item> { get }
   var sectionTransactions: [NSDiffableDataSourceSectionTransaction<Section, Item>] { get }
}

struct NSDiffableDataSourceSectionTransaction<Section, Item> {
   var sectionIdentifier: Section { get }
   var initialSnapshot: NSDiffableDataSourceSectionSnapshot<Item> { get }
   var finalSnapshot: NSDiffableDataSourceSectionSnapshot<Item> { get }
   var difference: CollectionDifference<Item> { get }
}
```

### Diffable Data Source Reordering Example — [11:07]

```swift
dataSource.reorderingHandlers.didReorder = { [weak self] transaction in 
   guard let self = self else { return }

   if let updateBackingStore = self.backingStore.applying(transaction.difference) {
      self.backingStore = updatedBackingStore
   }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10045/2/7473959D-7A47-4AC5-ACC1-1FFD5712F680/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10045) — developer.apple.com. Indexed for agent consumption._