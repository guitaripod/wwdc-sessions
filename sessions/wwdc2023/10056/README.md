---
id: "wwdc2023-10056"
event: "wwdc2023"
year: 2023
title: "Build better document-based apps"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10056"
topics: ["App Services", "System Services", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# Build better document-based apps

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10056](https://developer.apple.com/videos/play/wwdc2023/10056)

Discover how you can use the latest features in iPadOS to improve your document-based apps. We’ll show you how to take advantage of UIDocument as well as existing desktop-class iPad and document-based APIs to add new features in your app. Find out how to convert data models to UIDocument, present documents with UIDocumentViewController, learn how to migrate your apps to the latest APIs, and explore best practices.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,921 words)

## Documentation & Resources

- [UIDocument](https://developer.apple.com/documentation/UIKit/UIDocument) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIDocument
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIDocument.json
- [UIDocumentViewController](https://developer.apple.com/documentation/UIKit/UIDocumentViewController) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIDocumentViewController
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIDocumentViewController.json

## Code Snippets

### Loading a document — [3:54]

```swift
override func load(fromContents contents: Any, ofType typeName: String?) throws {
    // Load your document from contents
    guard let data = contents as? Data,
          let text = String(data: data, encoding: .utf8) else {
        throw DocumentError.readError
    }
    self.text = text
}
```

### Saving a document — [4:08]

```swift
override func contents(forType typeName: String) throws -> Any {
    // Encode your document with an instance of NSData or NSFileWrapper
    guard let data = self.text?.data(using: .utf8) else {
        throw DocumentError.writeError
    }
    return data
}
```

### Manually saving and loading a document — [4:34]

```swift
override func save(to url: URL,
                   for saveOperation: UIDocument.SaveOperation,
                   completionHandler: ((Bool) -> Void)? = nil) {
    self.performAsynchronousFileAccess {
        // Set up file coordination and write file to URL
   }
}

override func read(from url: URL) throws {
    // Set up file coordination and read file from URL
}
```

### Defining document that require saving — [5:08]

```swift
class Document: UIDocument {
    var text: String? {
        didSet {
            if oldValue != nil && oldValue != text {
                self.updateChangeCount(.done)
            }
        }
    }
}
```

### Updating the view hierarchy for a document — [6:30]

```swift
override func documentDidOpen() {
    configureViewForCurrentDocument()
}

override func viewDidLoad() {
    super.viewDidLoad()
    configureViewForCurrentDocument()
}

func configureViewForCurrentDocument() {
    guard let document = markdownDocument,
          !document.documentState.contains(.closed)
            && isViewLoaded else { return }
    // Configure views for document
}
```

### Updating navigation items for a document — [7:17]

```swift
override func navigationItemDidUpdate() {
    // Customize navigation item
}
```

### Manually opening a document — [8:01]

```swift
documentController.openDocument { success in
    if success {
        self.present(documentController, animated: true)
    }
}
```

### Renaming a UIDocument without UIDocumentViewController — [9:20]

```swift
navigationItem.renameDelegate = document
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10056/4/288B8B11-EFDD-4A1E-8F4E-B5C863A03ADC/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10056/4/288B8B11-EFDD-4A1E-8F4E-B5C863A03ADC/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10056) — developer.apple.com. Indexed for agent consumption._