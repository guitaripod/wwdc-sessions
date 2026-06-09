---
id: "wwdc2020-10026"
event: "wwdc2020"
year: 2020
title: "Lists in UICollectionView"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10026"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Lists in UICollectionView

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10026](https://developer.apple.com/videos/play/wwdc2020/10026)

Learn how to build lists and sidebars in your app with UICollectionView. Replace table view appearance while taking advantage of the full flexibility of compositional layout. Explore modular layout options and find out how they can unlock more design options for your apps than ever before. Find out how to combine table view-like lists with custom compositional layouts inside of a single UICollectionView. Discover how to work with lists, create richer cells, and customize your layout to create a well-designed presentation of information within your app.

To get the most out of this session, you should have a basic understanding of compositional layouts. Watch “Advances in Collection View Layout” from WWDC19 for more information.

**Keywords:** `outline`, `sidebar`, `table`, `uitableview`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,647 words)

## Documentation & Resources

- [Implementing modern collection views](https://developer.apple.com/documentation/UIKit/implementing-modern-collection-views) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/implementing-modern-collection-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/implementing-modern-collection-views.json

## Code Snippets

### Simple Setup — [3:47]

```swift
// Simple setup

let configuration = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
let layout = UICollectionViewCompositionalLayout.list(using: configuration)
```

### Per-Section Setup — [4:25]

```swift
// Per section setup

let configuration = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
let section = NSCollectionLayoutSection.list(using: configuration, layoutEnvironment: layoutEnvironment)
```

### Per-Section Setup full — [4:40]

```swift
// Per section setup

let layout = UICollectionViewCompositionalLayout() {
    [weak self] sectionIndex, layoutEnvironment in
    guard let self = self else { return nil }

    // @todo: add custom layout sections for various sections

    let configuration = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
    let section = NSCollectionLayoutSection.list(using: configuration, layoutEnvironment: layoutEnvironment)
    return section
}
```

### Header Mode Supplementary — [5:49]

```swift
var configuration = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
configuration.headerMode = .supplementary
let layout = UICollectionViewCompositionalLayout.list(using: configuration)

dataSource.supplementaryViewProvider = { (collectionView, elementKind, indexPath) in
    if elementKind == UICollectionView.elementKindSectionHeader {
        return collectionView.dequeueConfiguredReusableSupplementary(using: header, for: indexPath)
    }
    else {
        return nil
    }
}
```

### Header Mode Supplementary Optional Header — [6:51]

```swift
let layout = UICollectionViewCompositionalLayout() {
    [weak self] sectionIndex, layoutEnvironment in
    guard let self = self else { return nil }

    // check if this section should show a header, e.g. by implementing a shouldShowHeader(for:) method.
    let sectionHasHeader = self.shouldShowHeader(for: sectionIndex)

    let configuration = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
    configuration.headerMode = sectionHasHeader ? .supplementary : .none
    let section = NSCollectionLayoutSection.list(using: configuration, layoutEnvironment: layoutEnvironment)
    return section
}
```

### Header Mode First Item In Section — [7:07]

```swift
var configuration = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
configuration.headerMode = .firstItemInSection
let layout = UICollectionViewCompositionalLayout.list(using: configuration)
```

### Swipe Actions — [11:40]

```swift
let cellRegistration = UICollectionView.CellRegistration<UICollectionViewListCell, Model> { (cell, indexPath, item) in
    // @todo configure the cell's content

    let markFavorite = UIContextualAction(style: .normal, title: "Mark as Favorite") {
        [weak self] (_, _, completion) in
        guard let self = self else { return }
        // trigger the action with a reference to the model
        self.markItemAsFavorite(with: item.identifier)
        completion(true)
    }
    cell.leadingSwipeActionsConfiguration = UISwipeActionsConfiguration(actions: [markFavorite])
}
```

### Accessories — [14:55]

```swift
let cellRegistration = UICollectionView.CellRegistration<UICollectionViewListCell, String> { (cell, indexPath, item) in
    // @todo configure the cell's content

    cell.accessories = [
        .disclosureIndicator(),
        .delete()
    ]
}
```

### Accessories w/ Parameters — [15:51]

```swift
let cellRegistration = UICollectionView.CellRegistration<UICollectionViewListCell, String> { (cell, indexPath, item) in
    // @todo configure the cell's content

    cell.accessories = [
        .disclosureIndicator(displayed: .whenNotEditing),
        .delete()
    ]
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10026/6/9DBF6E96-B0C9-4104-B03E-F016434855BD/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10026) — developer.apple.com. Indexed for agent consumption._