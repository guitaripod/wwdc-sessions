---
id: "wwdc2020-10634"
event: "wwdc2020"
year: 2020
title: "Discover search suggestions for Apple TV"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10634"
topics: ["SwiftUI & UI Frameworks", "Audio & Video"]
platforms: ["tvOS"]
hasTranscript: true
---

# Discover search suggestions for Apple TV

**Event:** WWDC20 · **Topic:** Audio & Video · **Platforms:** tvOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10634](https://developer.apple.com/videos/play/wwdc2020/10634)

Searching your tvOS app just got even better. Get ready to explore the new simplified search interface and learn how to integrate it into your app with UISearchController. Support your global audience with the addition of new international keyboards and languages. Discover how to add search suggestions to your interface and update results with suggestions on the fly. And we’ll share some of our favorite tips for adding a great search experience to Apple TV.

**Keywords:** `appletv`, `apple tv`, `apple tv 4k`, `apple tv app`, `apple tv design`, `apple tv dev`, `apple tv developer`, `apple tv search`, `search`, `search suggestions`, `suggestions`, `tv`, `tv app dev`, `tv app developer`, `tv dev`, `tv developer`, `tvos`, `tv search`, `uisearchcontroller`, `video`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,316 words)

## Documentation & Resources

- [UISearchController](https://developer.apple.com/documentation/UIKit/UISearchController) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UISearchController
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UISearchController.json
- [Human Interface Guidelines: Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/designing-for-tvos

## Code Snippets

### SearchViewController init — [1:40]

```swift
private let appData: AppData

init(appData: AppData) {
    self.appData = appData

    super.init(nibName: nil, bundle: nil)
}

required init?(coder: NSCoder) {
    fatalError("init(coder:) has not been implemented")
}
```

### Search Tab Bar Item — [1:51]

```swift
// use the system standard search tab bar item
tabBarItem = UITabBarItem(tabBarSystemItem: UITabBarItem.SystemItem.search, tag: 0)
```

### SearchController and SearchContainerViewController Definition — [2:05]

```swift
private let searchController: UISearchController
private let searchContainerViewController: UISearchContainerViewController
```

### SearchController and SearchContainerViewController Initialization — [2:11]

```swift
self.searchController = UISearchController(searchResultsController: self.searchResultsController)
self.searchContainerViewController = UISearchContainerViewController(searchController: searchController)
```

### viewDidLoad - Add Child View Controller — [2:16]

```swift
override func viewDidLoad() {
    addChild(searchContainerViewController)

    searchContainerViewController.view.frame = view.bounds
    view.addSubview(searchContainerViewController.view)
    searchContainerViewController.didMove(toParent: self)
}
```

### Set searchControllerObservedScrollView — [3:17]

```swift
// scroll search controller allong with results collection view
searchController.searchControllerObservedScrollView = searchResultsController.collectionView
```

### Assign searchResultsUpdater — [3:43]

```swift
searchController.searchResultsUpdater = self
```

### Implement updateSearchResults — [4:00]

```swift
func updateSearchResults(for searchController: UISearchController) {
    if let searchText = searchController.searchBar.text {
        // get search results for 'searchText' from data source
        let (results, _) = appData.searchResults(seachTerm: searchText, includePhotos: true, includeVideos: true)

        searchResultsController.items = results
    } else {
        // no search text, show unfiltered results
        searchResultsController.items = appData.allEntries
    }
}
```

### Create Instance of SearchViewController — [4:16]

```swift
let searchViewController =  SearchViewController(appData: appData)
```

### UISearchSuggestionItem Example — [5:30]

```swift
let suggestion1 = UISearchSuggestionItem(localizedSuggestion: "Result1", localizedDescription: "Result1", iconImage: nil)
let suggestion2 = UISearchSuggestionItem(localizedSuggestion: "Result2", localizedDescription: "Result2", iconImage: nil)

searchController.searchSuggestions = [suggestion1, suggestion 2]
```

### Implement UISearchSuggestion Properties — [7:05]

```swift
var localizedSuggestion: String? {
    return self.name
}

var iconImage: UIImage? {
    return self.isVideo ? UIImage(systemName: "video") : UIImage(systemName: "photo")
}
```

### Implement Accessibility Description — [7:20]

```swift
var localizedDescription: String? {
    if (self.isVideo) {
        return String.localizedStringWithFormat(NSLocalizedString("%@ - Video", comment: ""), self.name)
    }
    return String.localizedStringWithFormat(NSLocalizedString("%@ - Photo", comment: ""), self.name)
}
```

### Add new UISearchResultsUpdating — [9:01]

```swift
func updateSearchResults(for searchController: UISearchController, selecting searchSuggestion: UISearchSuggestion) {
    if let searchText = searchController.searchBar.text {
        var includePhotos = true;
        var includeVideos = true;


    }
}
```

### Inspect Suggestion — [9:13]

```swift
// check if the suggestion is for a photo or video
if let suggestedEntry = searchSuggestion as? SuggestedEntry {
    includeVideos = suggestedEntry.isVideo
    includePhotos = !includeVideos
}
```

### Filter Results — [9:21]

```swift
// filter the results by to include photos, videos, or both
let (results, _) = appData.searchResults(seachTerm: searchText, includePhotos: includePhotos, includeVideos: includeVideos)

searchResultsController.items = results
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10634/4/F7B5D94B-69EE-4ABC-86AF-2354D9C93060/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10634) — developer.apple.com. Indexed for agent consumption._