---
id: "wwdc2022-10069"
event: "wwdc2022"
year: 2022
title: "Meet desktop-class iPad"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10069"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Meet desktop-class iPad

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10069](https://developer.apple.com/videos/play/wwdc2022/10069)

Learn how you can bring desktop-class features to your iPad app. Explore updates to UINavigationBar that bring more discoverability and customizability to your app’s features. Find out how the latest updates to UIKit can help make it easier and faster for people to explore content in your app. Lastly, we’ll share a few updates on how it’s easier than ever to bring your iPad app to the desktop with Mac Catalyst.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,867 words)

## Documentation & Resources

- [titleMenuProvider](https://developer.apple.com/documentation/UIKit/UINavigationItem/titleMenuProvider) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UINavigationItem/titleMenuProvider
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UINavigationItem/titleMenuProvider.json
- [UINavigationItem.ItemStyle](https://developer.apple.com/documentation/UIKit/UINavigationItem/ItemStyle) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UINavigationItem/ItemStyle
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UINavigationItem/ItemStyle.json
- [searchSuggestions](https://developer.apple.com/documentation/UIKit/UISearchController/searchSuggestions) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UISearchController/searchSuggestions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UISearchController/searchSuggestions.json
- [centerItemGroups](https://developer.apple.com/documentation/UIKit/UINavigationItem/centerItemGroups) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UINavigationItem/centerItemGroups
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UINavigationItem/centerItemGroups.json
- [UINavigationItemRenameDelegate](https://developer.apple.com/documentation/UIKit/UINavigationItemRenameDelegate-5j4ws) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UINavigationItemRenameDelegate-5j4ws
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UINavigationItemRenameDelegate-5j4ws.json
- [UIDocumentProperties](https://developer.apple.com/documentation/UIKit/UIDocumentProperties) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIDocumentProperties
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIDocumentProperties.json
- [Building a desktop-class iPad app](https://developer.apple.com/documentation/UIKit/building-a-desktop-class-ipad-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/building-a-desktop-class-ipad-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/building-a-desktop-class-ipad-app.json
- [Supporting desktop-class features in your iPad app](https://developer.apple.com/documentation/UIKit/supporting-desktop-class-features-in-your-ipad-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/supporting-desktop-class-features-in-your-ipad-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/supporting-desktop-class-features-in-your-ipad-app.json

## Code Snippets

### Creating a fixed UIBarButtonItemGroup from a single UIBarButtonItem — [4:27]

```swift
let insertGroup = UIBarButtonItem(title: "Insert", image: UIImage(systemName: "photo"), primaryAction: UIAction { _ in }).creatingFixedGroup()
```

### Convenient form — [4:55]

```swift
// Creating the 'Draw' group

// Convenient form of
// UIBarButtonItemGroup.movableGroup(customizationIdentifier:representativeItem:items:)
let drawGroup = UIBarButtonItem(title: "Draw", …)
    .creatingMovableGroup(customizationIdentifier: "Draw")
```

### Creating an optional group with multiple UIBarButtonItems using UIBarButtonItemGroup — [5:30]

```swift
let shapeGroup = UIBarButtonItemGroup.optionalGroup(
customizationIdentifier: "Shapes",
representativeItem: UIBarButtonItem(title: "Shapes", image: UIImage(systemName: "square.on.circle")),
items: [
    UIBarButtonItem(title: "Square", image: UIImage(systemName: "square"), primaryAction: UIAction { _ in }),
    UIBarButtonItem(title: "Circle", image: UIImage(systemName: "circle"), primaryAction: UIAction { _ in }),
    UIBarButtonItem(title: "Rectangle", image: UIImage(systemName: "rectangle"), primaryAction: UIAction { _ in }),
    UIBarButtonItem(title: "Diamond", image: UIImage(systemName: "diamond"), primaryAction: UIAction { _ in }),
])
```

### Setting up customizable centerItemGroups on a UINavigationItem — [6:56]

```swift
navigationItem.customizationIdentifier = "com.jetpack.blueprints.maineditor"
navigationItem.centerItemGroups = [
    // groups in the default customization
    UIBarButtonItem(title: "Insert", image: UIImage(systemName: "photo"), primaryAction: UIAction { _ in }).creatingFixedGroup(),
    UIBarButtonItem(title: "Draw", image: UIImage(systemName: "scribble"), primaryAction: UIAction { _ in }).creatingMovableGroup(customizationIdentifier: "Draw"),
    .optionalGroup(customizationIdentifier: "Shapes",
                   representativeItem: UIBarButtonItem(title: "Shapes", image: UIImage(systemName: "square.on.circle")),
                   items: [
                    UIBarButtonItem(title: "Square", image: UIImage(systemName: "square"), primaryAction: UIAction { _ in }),
                    UIBarButtonItem(title: "Circle", image: UIImage(systemName: "circle"), primaryAction: UIAction { _ in }),
                    UIBarButtonItem(title: "Rectangle", image: UIImage(systemName: "rectangle"), primaryAction: UIAction { _ in }),
                    UIBarButtonItem(title: "Diamond", image: UIImage(systemName: "diamond"), primaryAction: UIAction { _ in }),
                   ]),
    .optionalGroup(customizationIdentifier: "Text",
                   items: [
                    UIBarButtonItem(title: "Label", image: UIImage(systemName: "character.textbox"), primaryAction: UIAction { _ in }),
                    UIBarButtonItem(title: "Text", image: UIImage(systemName: "text.bubble"), primaryAction: UIAction { _ in }),
                   ]),

    // additional group not in the default customization
    .optionalGroup(customizationIdentifier: "Format",
                   isInDefaultCustomization: false,
                   representativeItem: UIBarButtonItem(title: "BIU", image: UIImage(systemName: "bold.italic.underline")),
                   items:[
                    UIBarButtonItem(title: "Bold", image: UIImage(systemName: "bold"), primaryAction: UIAction { _ in }),
                    UIBarButtonItem(title: "Italic", image: UIImage(systemName: "italic"), primaryAction: UIAction { _ in }),
                    UIBarButtonItem(title: "Underline", image: UIImage(systemName: "underline"), primaryAction: UIAction { _ in }),
                   ])
]
```

### Adding a "Comments" item to the default title menu — [9:30]

```swift
navigationItem.titleMenuProvider = { suggestedActions in
    var children = suggestedActions
    children += [
        UIAction(title: "Comments", image: UIImage(systemName: "text.bubble")) { _ in }
    ]
    return UIMenu(children: children)
}
```

### Supporting Drag & Drop and Sharing from the title menu — [10:15]

```swift
let url = <#T##URL#>
let documentProperties = UIDocumentProperties(url: url)

if let itemProvider = NSItemProvider(contentsOf: url) {
    documentProperties.dragItemsProvider = { _ in
        [UIDragItem(itemProvider: itemProvider)]
    }

    documentProperties.activityViewControllerProvider = {
        UIActivityViewController(activityItems: [itemProvider], applicationActivities: nil)
    }
}

navigationItem.documentProperties = documentProperties
```

### Implementing inline rename — [12:45]

```swift
class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        navigationItem.renameDelegate = self
    }
}

extension ViewController: UINavigationItemRenameDelegate {
    func navigationItem(_ navigationItem: UINavigationItem, didEndRenamingWith title: String) {
        // Try renaming our document, the completion handler will have the updated URL or return an error.
        documentBrowserViewController.renameDocument(at: <#T##URL#>, proposedName: title, completionHandler: <#T##(URL?, Error?) -> Void#>)
    }
}
```

### Implementing Search Suggestions — [14:05]

```swift
class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        searchController.searchResultsUpdater = self
    }
}

extension ViewController: UISearchResultsUpdating {
    func fetchQuerySuggestions(for searchController: UISearchController) -> [(String, UIImage?)] {
        let queryText = searchController.searchBar.text
        // Here you would decide how to transform the queryText into search results. This example just returns something fixed.
        return [("Sample Suggestion", UIImage(systemName: "rectangle.and.text.magnifyingglass"))]
    }

    func updateSearch(_ searchController: UISearchController, query: String) {
        // This method is used to update the search UI from our query text change
        // You should also update internal state related to when the query changes, as you might for when the user changes the query by typing.
        searchController.searchBar.text = query
    }

    func updateSearchResults(for searchController: UISearchController) {
        let querySuggestions = self.fetchQuerySuggestions(for: searchController)
        searchController.searchSuggestions = querySuggestions.map { name, icon in
            UISearchSuggestionItem(localizedSuggestion: name, localizedDescription: nil, iconImage: icon)
        }
    }

    func updateSearchResults(for searchController: UISearchController, selecting searchSuggestion: UISearchSuggestion) {
        if let suggestion = searchSuggestion.localizedSuggestion {
            updateSearch(searchController, query: suggestion)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10069/4/1646A8BA-EEFA-4533-A631-3BCDF704A4EB/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10069/4/1646A8BA-EEFA-4533-A631-3BCDF704A4EB/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10069) — developer.apple.com. Indexed for agent consumption._