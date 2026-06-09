---
id: "wwdc2024-10124"
event: "wwdc2024"
year: 2024
title: "What’s new in AppKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10124"
topics: ["App Services", "SwiftUI & UI Frameworks"]
platforms: ["macOS"]
hasTranscript: true
---

# What’s new in AppKit

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** macOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10124](https://developer.apple.com/videos/play/wwdc2024/10124)

Discover the latest advances in Mac app development. Get an overview of the new features in macOS Sequoia, and how to adopt them in your app. Explore new ways to integrate your existing code with SwiftUI. Learn about the improvements made to numerous AppKit controls, like toolbars, menus, text input, and more.

**Keywords:** `breathe`, `genmoji`, `image playground`, `symbols`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,790 words)

## Documentation & Resources

- [AppKit updates](https://developer.apple.com/documentation/Updates/AppKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Updates/AppKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Updates/AppKit.json
- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010

## Code Snippets

### Adding the Image Playground experience — [2:09]

```swift
extension DocumentCanvasViewController {

    @IBAction
    func importFromImagePlayground(_ sender: Any?) {
        // Initialize the playground, get set up to be notified of lifecycle events.
        let playground = ImagePlaygroundViewController()
        playground.delegate = self

        // Seed the playground with concepts and source imagery. (Optional)
        playground.concepts = [.text("birthday card")]
        playground.sourceImage = NSImage(named: "balloons")

        presentAsSheet(playground)
    }

}

extension DocumentCanvasViewController: ImagePlaygroundViewController.Delegate {

    func imagePlaygroundViewController(
        _ imagePlaygroundViewController: ImagePlaygroundViewController,
        didCreateImageAt resultingImageURL: URL
    ) {
        if let image = NSImage(contentsOf: resultingImageURL) {
            imageView.image = image
        } else {
            logger.error("Could not read image at \(resultingImageURL)")
        }
        dismiss(imagePlaygroundViewController)
    }

}
```

### Using window resize increments — [5:50]

```swift
window.resizeIncrements = NSSize(width: characterWidth, height: characterHeight)
```

### Build menus with SwiftUI — [7:05]

```swift
struct ActionMenu: View {

    var body: some View {
        Toggle("Use Groups", isOn: $useGroups)
        Picker("Sort By", selection: $sortOrder) {
            ForEach(SortOrder.allCases) { Text($0.title) }
        }.pickerStyle(.inline)
        Button("Customize View…") { <#Action#> }
    }

}

let menu = NSHostingMenu(rootView: ActionMenu())

let pullDown = NSPopUpButton(image: image, pullDownMenu: menu)
```

### Get animated with SwiftUI — [7:43]

```swift
NSAnimationContext.animate(with: .spring(duration: 0.3)) {
    drawer.isExpanded.toggle()
}
```

### Get animated with SwiftUI — [7:55]

```swift
class PaletteView: NSView {

    @Invalidating(.layout)    
    var isExpanded: Bool = false

    private func onHover(_ isHovered: Bool) {
        NSAnimationContext.animate(with: .spring) {
            isExpanded = isHovered
            layoutSubtreeIfNeeded()
        }
    }

}
```

### Text highlighting — [10:31]

```swift
let attributes: [NSAttributedString.Key: Any] = [
    .textHighlight: NSAttributedString.TextHighlightStyle.systemDefault,
    .textHighlightColorScheme: NSAttributedString.TextHighlightColorScheme.pink,
]
```

### SF Symbols effects — [11:11]

```swift
imageView.addSymbolEffect(.wiggle)
imageView.addSymbolEffect(.rotate)
imageView.addSymbolEffect(.breathe)
```

### SF Symbols playback (periodic) — [11:24]

```swift
imageView.addSymbolEffect(.wiggle, options: .repeat(.periodic(3, delay: 0.5)))
```

### SF Symbols playback (continuous) — [11:30]

```swift
imageView.addSymbolEffect(.wiggle, options: .repeat(.continuous))
```

### SF Symbols magic replace — [11:37]

```swift
imageView.setSymbolImage(badgedSymbolImage, contentTransition: .replace)
```

### Save panel content types — [12:19]

```swift
extension ImageViewController: NSOpenSavePanelDelegate {

    @MainActor
    @IBAction
    internal func saveDocument(_ sender: Any?) {
        Task {
            let savePanel = NSSavePanel()
            savePanel.delegate = self
            savePanel.identifier = NSUserInterfaceItemIdentifier("ImageExport")
            savePanel.showsContentTypes = true
            savePanel.allowedContentTypes = [.png, .jpeg]
            let result = await savePanel.beginSheetModal(for: window)
            switch result {
                case .OK:
                    let url = savePanel.url
                    // Save the document to 'url'. It already has the appropriate extension.
                case .cancel: break
                default: break
            }
        }
    }

    func panel(_ panel: Any, displayNameFor type: UTType) -> String? {
        switch type {
            case .png:
                NSLocalizedString("PNG (Greater Quality)", comment: <#Comment#>)
            case .jpeg:
                NSLocalizedString("JPG (Smaller File Size)", comment: <#Comment#>)
            default:
                nil
        }
    }

}
```

### Frame-resize cursors — [13:34]

```swift
let cursor = NSCursor.frameResize(position: .bottomRight, directions: .all)
```

### Column and row resize cursors — [14:20]

```swift
let cursor = NSCursor.columnResize(directions: .left)
let cursor = NSCursor.rowResize(directions: .up)
```

### Zoom in and out cursors — [14:29]

```swift
let cursor = NSCusor.zoomIn
let cursor = NSCusor.zoomOut
```

### Display mode customizable toolbar — [15:57]

```swift
let toolbar = NSToolbar(identifier: NSToolbar.Identifier("ViewerWindow"))
toolbar.allowsDisplayModeCustomization // Defaults to `true`.
```

### Hidden toolbar items — [16:57]

```swift
let downloadsToolbarItem: NSToolbarItem
downloadsToolbarItem.isHidden = downloadsManager.downloads.isEmpty
```

### Text entry suggestions — [17:49]

```swift
class MYViewController: NSViewController {

    let museumTextField = NSTextField(string: "")

    let museumTextSuggestionsController = MuseumTextSuggestionsController()

    override func viewDidLoad() {
        super.viewDidLoad()

        self.museumTextField.suggestionsDelegate = self.museumTextSuggestionsController
    }

}

class MuseumTextSuggestionsController: NSTextSuggestionsDelegate {

    typealias SuggestionItemType = Museum

    func textField(
        _ textField: NSTextField,
        provideUpdatedSuggestions responseHandler: @escaping ((ItemResponse) -> Void)
    ) {
        let searchString = textField.stringValue

        func museumItem(_ museum: Museum) -> Item {
            var item = NSSuggestionItem(representedValue: museum, title: museum.name)
            item.secondaryTitle = museum.address
            return item
        }

        let favoriteMuseums = Museum.favorites.filter({
            $0.matches(searchString)
        })

        let favorites = NSSuggestionItemSection(
            title: NSLocalizedString("Favorites", comment: "The title of suggestion results section containing favorite museums."),
            items: favoriteMuseums.map(museumItem(_:))
        )
        var response = NSSuggestionItemResponse(itemSections: [favorites])
        response.phase = .intermediate
        responseHandler(response)

        Task {
            let otherMuseums = await Museum.allMatching(searchString)
            let nonFavorites = NSSuggestionItemSection(items: otherMuseums.map(museumItem(_:)))

            var response = NSSuggestionItemResponse(itemSections: [
                favorites,
                nonFavorites,
            ])
            response.phase = .final
            responseHandler(response)
        }
    }

}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10124/6/75BDBA0D-71A3-435A-8E9E-AE18B78981B0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10124/6/75BDBA0D-71A3-435A-8E9E-AE18B78981B0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10124) — developer.apple.com. Indexed for agent consumption._
