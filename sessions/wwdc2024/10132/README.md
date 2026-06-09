---
id: "wwdc2024-10132"
event: "wwdc2024"
year: 2024
title: "Evolve your document launch experience"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10132"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iPadOS"]
hasTranscript: true
---

# Evolve your document launch experience

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iPadOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10132](https://developer.apple.com/videos/play/wwdc2024/10132)

Make your document-based app stand out, and bring its unique identity into focus with the new document launch experience. Learn how to leverage the new API to customize the first screen people see when they launch your app. Utilize the new system-provided design, and amend it with custom actions, delightful decorative views, and impressive animations.

**Keywords:** `alien flower`, `document-based`, `fashion shirt`, `julia`, `yael`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,266 words)

## Documentation & Resources

- [Building a document-based app with SwiftUI](https://developer.apple.com/documentation/SwiftUI/Building-a-document-based-app-with-SwiftUI) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Building-a-document-based-app-with-SwiftUI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Building-a-document-based-app-with-SwiftUI.json
- [Customizing a document-based app’s launch experience](https://developer.apple.com/documentation/UIKit/customizing-a-document-based-app-s-launch-experience) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/customizing-a-document-based-app-s-launch-experience
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/customizing-a-document-based-app-s-launch-experience.json
- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010

## Code Snippets

### Document-based application — [2:38]

```swift
@main
struct WritingApp: App {
    var body: some Scene {
        DocumentGroup(newDocument: { StoryDocument() }) { file in
            StoryView(document: $file.document)
        }
    }
}
```

### Presenting a document from the browser in iOS 17 — [3:26]

```swift
class DocumentViewController: UIDocumentViewController { ... }

let documentViewController = DocumentViewController()
let browserViewController = UIDocumentBrowserViewController(
    forOpening: [.plainText]
)
window.rootViewController = browserViewController
```

### Presenting a document from the browser in iOS 17 — [3:38]

```swift
class DocumentViewController: UIDocumentViewController { ... }

let documentViewController = DocumentViewController()
let browserViewController = UIDocumentBrowserViewController(
    forOpening: [.plainText]
)
window.rootViewController = browserViewController
browserViewController.delegate = self
```

### Presenting a document from the browser in iOS 17 — [3:43]

```swift
class DocumentViewController: UIDocumentViewController { ... }

let documentViewController = DocumentViewController()
let browserViewController = UIDocumentBrowserViewController(
    forOpening: [.plainText]
)
window.rootViewController = browserViewController
browserViewController.delegate = self

// MARK: UIDocumentBrowserViewControllerDelegate

func documentBrowser(
    _ browser: UIDocumentBrowserViewController, 
    didPickDocumentsAt documentURLs: [URL]
) {
    guard let url = documentURLs.first else { return }
    documentViewController.document = StoryDocument(fileURL: url)
    browser.present(documentViewController, animated: true)
}
```

### Presenting a document from the browser in iOS 18 — [3:56]

```swift
class DocumentViewController: UIDocumentViewController { ... }

let documentViewController = DocumentViewController()
window.rootViewController = documentViewController
```

### Customize the document launch experience: background — [4:38]

```swift
DocumentGroup(
    newDocument: { StoryDocument() }
) { file in
    StoryView(document: $file.document)
}

DocumentGroupLaunchScene {
...
} background: {
    Image(.pinkJungle)
        .resizable()
        .aspectRatio(contentMode: .fill)
}
```

### Customize the document launch experience: new document button title — [4:49]

```swift
DocumentGroup(
    newDocument: { StoryDocument() }
) { file in
    StoryView(document: $file.document)
}
DocumentGroupLaunchScene {
    NewDocumentButton("Start Writing")
} background: {
    Image(.pinkJungle)
        .resizable()
        .aspectRatio(contentMode: .fill)
}
```

### Customize the document launch experience: accessory views — [5:29]

```swift
DocumentGroupLaunchScene {
    NewDocumentButton("Start Writing")
} background: {
    Image(.pinkJungle)
        .resizable()
        .aspectRatio(contentMode: .fill)
} overlayAccessoryView: {

}
```

### Position accessory views — [5:44]

```swift
DocumentGroupLaunchScene {
    NewDocumentButton("Start Writing")
} background: {
    Image(.pinkJungle)
        .resizable()
        .aspectRatio(contentMode: .fill)
} overlayAccessoryView: { geometry in

}
```

### Position accessory views — [5:53]

```swift
DocumentGroupLaunchScene {
    NewDocumentButton("Start Writing")
} background: {
...
} overlayAccessoryView: { geometry in
    ZStack {
        Image(.robot)
            .position(
                x: geometry.titleViewFrame.minX, 
                y: geometry.titleViewFrame.minY
            )
        Image(.plant)
            .position(
                x: geometry.titleViewFrame.maxX, 
                y: geometry.titleViewFrame.maxY
            )
    }
}
```

### Customize the document launch experience in a UIKit app — [6:11]

```swift
class DocumentViewController: UIDocumentViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Update the background
        launchOptions.background.image = UIImage(resource: .pinkJungle)

        // Add foreground accessories
        launchOptions.foregroundAccessoryView = ForegroundAccessoryView()
    }
}
```

### Create a document from a template: add a button — [7:31]

```swift
DocumentGroupLaunchScene {
    NewDocumentButton("Start Writing")
    NewDocumentButton("Choose a Template", for: StoryDocument.self) {

    }
}
```

### Create a document from a template: return document later — [7:45]

```swift
@State private var creationContinuation: CheckedContinuation<StoryDocument?, any Error>?

DocumentGroupLaunchScene {
    NewDocumentButton("Start Writing")
    NewDocumentButton("Choose a Template", for: StoryDocument.self) {
        try await withCheckedThrowingContinuation { continuation in
            self.creationContinuation = continuation
       }
    }
}
```

### Create a document from a template: present a template picker — [7:56]

```swift
@State private var creationContinuation: CheckedContinuation<StoryDocument?, any Error>?
@State private var isTemplatePickerPresented = false

DocumentGroupLaunchScene {
    NewDocumentButton("Start Writing")
    NewDocumentButton("Choose a Template", for: StoryDocument.self) {
        try await withCheckedThrowingContinuation { continuation in
            self.creationContinuation = continuation
            self.isTemplatePickerPresented = true
        }
    }
    .sheet(isPresented: $isTemplatePickerPresented) {
        TemplatePicker(continuation: $creationContinuation
    }
}
```

### Create a document from a template: template picker view — [8:07]

```swift
struct TemplatePicker: View {
    @Binding var creationContinuation: CheckedContinuation<StoryDocument?, any Error>?

    var body: some View {
        Button("Three Act Structure") {
            creationContinuation?.resume(returning: StoryDocument.threeActStructure())
            creationContinuation = nil
        }
    }
}

extension StoryDocument {
    static func threeActStructure() -> Self {
        Self.init(...)
    }
}
```

### Create a document from a template in UIKit — [8:20]

```swift
extension UIDocument.CreationIntent {
    static let template = UIDocument.CreationIntent("template")
}
```

### Create a document from a template in UIKit — [8:29]

```swift
launchOptions.secondaryAction = LaunchOptions.createDocumentAction(with: .template) 
launchOptions.browserViewController.delegate = self

// MARK: UIDocumentBrowserViewControllerDelegate

func documentBrowser(
    _ browser: UIDocumentBrowserViewController, 
    didRequestDocumentCreationWithHandler importHandler: @escaping (URL?, ImportMode) -> Void) 
{
    switch browser.activeDocumentCreationIntent {
    case .template: 
        presentTemplatePicker(with: importHandler)
    default:
        let newDocumentURL = // ...
        importHandler(newDocumentURL, .copy)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10132/4/F41D2CAF-097E-4793-B867-78798357CBBC/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10132/4/F41D2CAF-097E-4793-B867-78798357CBBC/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10132) — developer.apple.com. Indexed for agent consumption._