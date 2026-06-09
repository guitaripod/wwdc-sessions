---
id: "wwdc2020-10105"
event: "wwdc2020"
year: 2020
title: "Build for iPad"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10105"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Build for iPad

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10105](https://developer.apple.com/videos/play/wwdc2020/10105)

Learn how to improve iPad apps to leverage the increased screen size and additional features of iPadOS, and help people accomplish more with their devices. Discover how you can build detailed multi-column layouts and integrate lists into your app with little adjustment to your existing code. We’ll also explore reducing modality within your views to make it easier to navigate your interface with fewer taps and touches.

To get the most out of this session, you should have a general understanding of iPad app layouts and UIKit. For more information, watch “Making Apps Adaptive, Part 1.” And while not necessary, familiarity with UICollectionView may also be helpful. Watch “Advances in Collection View Layout” for an overview. 

Want to learn more about list creation for your apps? Watch “Lists in UICollectionView”.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,882 words)

## Documentation & Resources

- [Human Interface Guidelines: Sidebars](https://developer.apple.com/design/human-interface-guidelines/ios/bars/sidebars) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/ios/bars/sidebars
- [Human Interface Guidelines: Split views](https://developer.apple.com/design/human-interface-guidelines/ios/views/split-views/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/ios/views/split-views/
- [UISplitViewController](https://developer.apple.com/documentation/UIKit/UISplitViewController) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UISplitViewController
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UISplitViewController.json

## Code Snippets

### Create two column UISplitViewController — [1:57]

```swift
let splitViewController = UISplitViewController(style: .doubleColumn)
```

### Set view controllers for primary and secondary columns — [2:13]

```swift
splitViewController.setViewController(sidebarViewController, for: .primary)
splitViewController.setViewController(myHomeViewController, for: .secondary)
```

### Create three column UISplitViewController — [2:28]

```swift
let splitViewController = UISplitViewController(style: .tripleColumn)
```

### Set view controller for supplementary column — [2:29]

```swift
splitViewController.setViewController(inboxViewController, for: .supplementary)
```

### Set view controller for compact column — [4:02]

```swift
splitViewController.setViewController(tabBarController, for: .compact)
```

### Set preferredSplitBehavior to .tile — [5:29]

```swift
splitViewController.preferredSplitBehavior = .tile
```

### Set preferredSplitBehavior to .displace — [5:44]

```swift
splitViewController.preferredSplitBehavior = .displace
```

### Set preferredSplitBehavior to .overlay — [5:51]

```swift
splitViewController.preferredSplitBehavior = .overlay
```

### Hide and show columns — [5:56]

```swift
splitViewController.hideColumn(.primary)

splitViewController.showColumn(.supplementary)
```

### Set preferredDisplayMode — [6:08]

```swift
splitViewController.preferredDisplayMode = .oneBesideSecondary
```

### Collection view setup for sidebar list — [8:06]

```swift
let configuration = UICollectionLayoutListConfiguration(appearance: .sidebar)
let layout = UICollectionViewCompositionalLayout.list(using: configuration)
let collectionView = UICollectionView(frame: frame, collectionViewLayout: layout)
```

### Define a type for an example data structure — [8:38]

```swift
struct MyItem: Hashable {
    let title: String
    let image: UIImage
}
```

### Create cell registration — [9:36]

```swift
let cellRegistration = UICollectionView.CellRegistration<UICollectionViewListCell, MyItem> 
{ cell, indexPath, item in

    var content = cell.defaultContentConfiguration()

    content.text = item.title
    content.image = item.image

    cell.contentConfiguration = content
}
```

### Create diffable data source — [10:31]

```swift
let dataSource = UICollectionViewDiffableDataSource<Section, MyItem>
   (collectionView: collectionView)
{ collectionView, indexPath, item in
   return collectionView.dequeueConfiguredReusableCell(using: cellRegistration, 
                                                       for: indexPath,
                                                       item: item)
}
```

### Collection view setup for sidebar plain list — [11:29]

```swift
let configuration = UICollectionLayoutListConfiguration(appearance: .sidebarPlain)
let layout = UICollectionViewCompositionalLayout.list(using: configuration)
let collectionView = UICollectionView(frame: frame, collectionViewLayout: layout)
```

### Example: Initializing UISplitViewController — [15:35]

```swift
let splitViewController = UISplitViewController(style: .doubleColumn)

// Primary column

let sidebar = SidebarViewController()
splitViewController.setViewController(sidebar, for: .primary)


// Secondary column

func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
    splitViewController.showDetailViewController(DetailViewController(), sender: self)
}
```

### Example: Setting a view controller for compact width — [17:50]

```swift
let tabBarController = createTabBarController()

splitViewController.setViewController(tabBarController, for: .compact)
```

### Example: Sidebar Collection View setup — [20:39]

```swift
let layout = UICollectionViewCompositionalLayout(sectionProvider: sectionProvider,
         configuration: UICollectionViewCompositionalLayoutConfiguration())

func sectionProvider(_ section: Int, environment: NSCollectionLayoutEnvironment)
-> NSCollectionLayoutSection {
    var configuration = UICollectionLayoutListConfiguration(appearance: .sidebar)

    if (environment.traitCollection.horizontalSizeClass == .compact) {
        configuration.headerMode = .firstItemInSection
    } else {
        configuration.headerMode = .none
    }

    return NSCollectionLayoutSection.list(using: configuration, layoutEnvironment: environment)
}
```

### Example: Cell Registration — [21:13]

```swift
struct Section: Hashable { … }

struct Item: Hashable { … }


let cellRegistration = UICollectionView.CellRegistration<UICollectionViewListCell, Item> { cell, indexPath, item in
    // Configure the cell
}


let dataSource = UICollectionViewDiffableDataSource<Section, Item>(collectionView: collectionView) { collectionView, indexPath, item in
    return collectionView.dequeueConfiguredReusableCell(using: cellRegistration, for: indexPath, item: item)
}
```

### Example: Cell registration — [21:48]

```swift
let cellRegistration = UICollectionView.CellRegistration<UICollectionViewListCell, Item> { cell, indexPath, item in

    var content = cell.defaultContentConfiguration()

    content.text = item.title
    content.image = item.image

    cell.contentConfiguration = content
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10105/2/8B0CF78F-98E7-440E-B226-565F58288462/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10105) — developer.apple.com. Indexed for agent consumption._