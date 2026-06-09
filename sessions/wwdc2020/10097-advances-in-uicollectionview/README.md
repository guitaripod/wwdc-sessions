---
id: "wwdc2020-10097"
event: "wwdc2020"
year: 2020
title: "Advances in UICollectionView"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10097"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Advances in UICollectionView

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10097](https://developer.apple.com/videos/play/wwdc2020/10097)

Learn about new features of UICollectionView that make it easier to use and unlock powerful new functionality. We'll show you how to use section snapshots with your diffable data source to create outlines that can expand and collapse, and introduce you to building lists with compositional layout to create UITableView-like interfaces with a collection view. And discover modern techniques for dequeuing cells and configuring their content and styling. To get the most out of this session, you should have a basic understanding of compositional layouts. Watch “Advances in Collection View Layout” from WWDC19 for more information.

**Keywords:** `cell`, `collection`, `layout`, `table`, `tableview`, `uicollectionview`, `uitableview`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,382 words)

## Documentation & Resources

- [Implementing modern collection views](https://developer.apple.com/documentation/UIKit/implementing-modern-collection-views) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/implementing-modern-collection-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/implementing-modern-collection-views.json

## Code Snippets

### UICollectionViewCompositionalLayout Lists — [6:15]

```swift
let configuration = UICollectionLayoutListConfiguration(appearance: .insetGrouped)
let layout = UICollectionViewCompositionalLayout.list(using: configuration)
```

### Cell Registration — [7:33]

```swift
// Example of using new iOS 14 cell registration

let reg = UICollectionView.CellRegistration<MyCell, ViewModel> { cell, indexPath, model in
   // configure cell content 
}

let dataSource = UICollectionViewDiffableDataSource<S,I>(collectionView: collectionView) {
                     collectionView, indexPath, item -> UICollectionViewCell in
   return collectionView.dequeueConfiguredReusableCell(using: reg, for: indexPath, item: item)
}
```

### .cell Content Configuration — [8:32]

```swift
var contentConfiguration = UIListContentConfiguration.cell()
contentConfiguration.image = UIImage(systemName:"hammer")
contentConfiguration.text = "Ready. Set. Code"
cell.contentConfiguration = contentConfiguration
```

### .valueCell Content Configuration — [8:38]

```swift
var contentConfiguration = UIListContentConfiguration.valueCell()
contentConfiguration.image = UIImage(systemName:"hammer")
contentConfiguration.text = "Ready. Set. Code."
contentConfiguration.secondaryText = "#WWDC20"
cell.contentConfiguration = contentConfiguration
```

### .subtitleCell Content Configuration — [8:44]

```swift
var contentConfiguration = UIListContentConfiguration.subtitleCell()
contentConfiguration.image = UIImage(systemName:"hammer")
contentConfiguration.text = "Ready. Set. Code."
contentConfiguration.secondaryText = "#WWDC20"
cell.contentConfiguration = contentConfiguration
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10097/3/CE693EFF-2BF8-4B42-B483-04F69015A601/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10097) — developer.apple.com. Indexed for agent consumption._
