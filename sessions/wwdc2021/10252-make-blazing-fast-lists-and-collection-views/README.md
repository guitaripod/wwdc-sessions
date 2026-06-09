---
id: "wwdc2021-10252"
event: "wwdc2021"
year: 2021
title: "Make blazing fast lists and collection views"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10252"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["macOS"]
hasTranscript: true
---

# Make blazing fast lists and collection views

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10252](https://developer.apple.com/videos/play/wwdc2021/10252)

Build consistently smooth scrolling list and collection views: Explore the lifecycle of a cell and learn how to apply that knowledge to eliminate rough scrolling and missed frames. We’ll also show you how to improve your overall scrolling experience and avoid costly hitches, with optimized image loading and automatic cell prefetching. To get the most out of this video, we recommend a basic familiarity with diffable data sources and compositional layout.

**Keywords:** `glitch`, `hitch`, `performance`, `rendering`, `tableview`, `table view`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,408 words)

## Documentation & Resources

- [Building high-performance lists and collection views](https://developer.apple.com/documentation/UIKit/building-high-performance-lists-and-collection-views) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/building-high-performance-lists-and-collection-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/building-high-performance-lists-and-collection-views.json
- [UIKit](https://developer.apple.com/documentation/UIKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit.json

## Code Snippets

### Structuring data — [1:25]

```swift
// Structuring data

struct DestinationPost: Identifiable {
    // Each post has a unique identifier
    var id: String

    var title: String
    var numberOfLikes: Int
    var assetID: Asset.ID
}
```

### Setting up diffable data source — [2:01]

```swift
// Setting up diffable data source

class DestinationGridViewController: UIViewController {
    // Use DestinationPost.ID as the item identifier
    var dataSource: UICollectionViewDiffableDataSource<Section, DestinationPost.ID>

    private func setInitialData() {
        var snapshot = NSDiffableDataSourceSnapshot<Section, DestinationPost.ID>()

        // Only one section in this collection view, identified by Section.main
        snapshot.appendSections([.main])

        // Get identifiers of all destination posts in our model and add to initial snapshot
        let itemIdentifiers = postStore.allPosts.map { $0.id }
        snapshot.appendItems(itemIdentifiers)

        dataSource.apply(snapshot, animatingDifferences: false)
    }
}
```

### Creating cell registrations — [3:47]

```swift
// Cell registrations

let cellRegistration = UICollectionView.CellRegistration<DestinationPostCell,
                                                         DestinationPost.ID> {
    (cell, indexPath, postID) in

    let post = self.postsStore.fetchByID(postID)
    let asset = self.assetsStore.fetchByID(post.assetID)

    cell.titleView.text = post.region
    cell.imageView.image = asset.image
}
```

### Using cell registrations — [4:03]

```swift
// Cell registrations

let cellRegistration = UICollectionView.CellRegistration<DestinationPostCell,
                                                         DestinationPost.ID> {
    (cell, indexPath, postID) in
    ...
}

let dataSource = UICollectionViewDiffableDataSource<Section.ID,
                                                    DestinationPost.ID>(collectionView: cv){
    (collectionView, indexPath, postID) in

     return collectionView.dequeueConfiguredReusableCell(using: cellRegistration,
                                                           for: indexPath,
                                                          item: postID)
}
```

### Existing cell registration — [13:58]

```swift
// Existing cell registration

let cellRegistration = UICollectionView.CellRegistration<DestinationPostCell,
                                                         DestinationPost.ID> {
    (cell, indexPath, postID) in

    let post = self.postsStore.fetchByID(postID)
    let asset = self.assetsStore.fetchByID(post.assetID)

    cell.titleView.text = post.region
    cell.imageView.image = asset.image
}
```

### Updating cells asynchronously (wrong) — [14:17]

```swift
// Updating cells asynchronously 

let cellRegistration = UICollectionView.CellRegistration<DestinationPostCell,
                                                         DestinationPost.ID> {
    (cell, indexPath, postID) in

    let post = self.postsStore.fetchByID(postID)
    let asset = self.assetsStore.fetchByID(post.assetID)

    if asset.isPlaceholder {
        self.assetsStore.downloadAsset(post.assetID) { asset in
            cell.imageView.image = asset.image
        }
    }

    cell.titleView.text = post.region
    cell.imageView.image = asset.image
}
```

### Reconfiguring items — [15:15]

```swift
private func setPostNeedsUpdate(id: DestinationPost.ID) {
    var snapshot = dataSource.snapshot()
    snapshot.reconfigureItems([id])
    dataSource.apply(snapshot, animatingDifferences: true)
}
```

### Updating cells asynchronously (correct) — [15:23]

```swift
// Updating cells asynchronously

let cellRegistration = UICollectionView.CellRegistration<DestinationPostCell,
                                                         DestinationPost.ID> {
    (cell, indexPath, postID) in

    let post = self.postsStore.fetchByID(postID)
    let asset = self.assetsStore.fetchByID(post.assetID)

    if asset.isPlaceholder {
        self.assetsStore.downloadAsset(post.assetID) { _ in
            self.setPostNeedsUpdate(id: post.id)
        }
    }

    cell.titleView.text = post.region
    cell.imageView.image = asset.image
}
```

### Data source prefetching — [15:52]

```swift
// Data source prefetching

var prefetchingIndexPaths: [IndexPath: Cancellable]

func collectionView(_ collectionView: UICollectionView,
                    prefetchItemsAt indexPaths [IndexPath]) {
   // Begin download work
    for indexPath in indexPaths {
        guard let post = fetchPost(at: indexPath) else { continue }
        prefetchingIndexPaths[indexPath] = assetsStore.loadAssetByID(post.assetID)
    }
}

func collectionView(_ collectionView: UICollectionView,
                    cancelPrefetchingForItemsAt indexPaths: [IndexPath]) {
    // Stop fetching
    for indexPath in indexPaths {
        prefetchingIndexPaths[indexPath]?.cancel()
    }
}
```

### Using prepareForDisplay — [18:43]

```swift
// Using prepareForDisplay

// Initialize the full image
let fullImage = UIImage()

// Set a placeholder before preparation
imageView.image = placeholderImage

// Prepare the full image
fullImage.prepareForDisplay { preparedImage in
    DispatchQueue.main.async {
       self.imageView.image = preparedImage
    }
}
```

### Asset downloading without image preparation — [19:51]

```swift
// Asset downloading – before image preparation

func downloadAsset(_ id: Asset.ID,
                   completionHandler: @escaping (Asset) -> Void) -> Cancellable {

    return fetchAssetFromServer(assetID: id) { asset in
        DispatchQueue.main.async {
            completionHandler(asset)
        }
    }
}
```

### Asset downloading with image preparation — [19:58]

```swift
// Asset downloading – with image preparation

func downloadAsset(_ id: Asset.ID,
                   completionHandler: @escaping (Asset) -> Void) -> Cancellable {
    // Check for an already prepared image
    if let preparedAsset = imageCache.fetchByID(id) {
        completionHandler(preparedAsset)
        return AnyCancellable {}
    }
    return fetchAssetFromServer(assetID: id) { asset in
        asset.image.prepareForDisplay { preparedImage in
            // Store the image in the cache.
            self.imageCache.add(asset: asset.withImage(preparedImage!))
            DispatchQueue.main.async {
                completionHandler(asset)
            }
        }
    }
}
```

### Using prepareThumbnail — [20:50]

```swift
// Using prepareThumbnail

// Initialize the full image
let profileImage = UIImage(...)

// Set a placeholder before preparation
posterAvatarView.image = placeholderImage

// Prepare the image
profileImage.prepareThumbnail(of: posterAvatarView.bounds.size) { thumbnailImage in
    DispatchQueue.main.async {
        self.posterAvatarView.image = thumbnailImage
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10252/5/B37B6913-C7C8-49EA-982E-9D10AC147454/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10252/5/B37B6913-C7C8-49EA-982E-9D10AC147454/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10252) — developer.apple.com. Indexed for agent consumption._
