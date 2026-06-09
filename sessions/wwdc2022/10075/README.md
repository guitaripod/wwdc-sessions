---
id: "wwdc2022-10075"
event: "wwdc2022"
year: 2022
title: "Use SwiftUI with AppKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10075"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Use SwiftUI with AppKit

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10075](https://developer.apple.com/videos/play/wwdc2022/10075)

Discover how the Shortcuts app uses both SwiftUI and AppKit to create a top-tier experience on macOS. Follow along with the Shortcuts team as we explore how you can host SwiftUI views in AppKit code, handle layout and sizing, participate in the responder chain, enable navigational focus, and more. We’ll also show you how to host AppKit views, helping you migrate existing code into a SwiftUI layout within your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,603 words)

## Documentation & Resources

- [UIKit integration](https://developer.apple.com/documentation/SwiftUI/UIKit-integration) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/UIKit-integration
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/UIKit-integration.json

## Code Snippets

### SidebarView and SidebarItem — [1:29]

```swift
struct SidebarView: View {
    @State private var selectedItem: SidebarItem

    var body: some View {
        List(selection: $selectedItem) {
            ...
            Section("Shortcuts") { ... }
            Section("Folders") { ... }
        }
    }
}

enum SidebarItem: Hashable {
    case gallery
    case allShortcuts
    ...
    case folder(Folder)
}
```

### Hosting SwiftUI sidebar — [1:53]

```swift
let splitViewController = NSSplitViewController()

let sidebar = NSHostingController(rootView: SidebarView(...))
let splitViewItem = NSSplitViewItem(viewController: sidebar)
splitViewController.addSplitViewItem(splitViewItem)
```

### Sidebar selection model — [3:06]

```swift
class SelectionModel: ObservableObject {

    @Published var selectedItem: SidebarItem = .allShortcuts

}

// AppKit Window Controller
cancellable = selectionModel.$selectedItem.sink { newItem in
    // update the NSSplitViewController detail
}
```

### Collection view item hosting SwiftUI — [4:37]

```swift
class ShortcutItemView: NSCollectionViewItem {
    private var hostingView: NSHostingView<ShortcutView>?

    func displayShortcut(_ shortcut: Shortcut) {
        let shortcutView = ShortcutView(shortcut: shortcut)

        if let hostingView = hostingView {
            hostingView.rootView = shortcutView
        } else {
            let newHostingView = NSHostingView(rootView: shortcutView)
            view.addSubview(newHostingView)
            setupConstraints(for: newHostingView)
            self.hostingView = newHostingView
        }
    }
}
```

### Popover presentation — [7:55]

```swift
viewController.present(NSHostingController(rootView: ...), 
asPopoverRelativeTo: rect, of: view, 
preferredEdge: .maxY, behavior: .transient)
```

### Sheet presentation — [8:15]

```swift
viewController.presentAsSheet(NSHostingController(rootView: ...))
```

### Modal window presentation — [8:22]

```swift
let hostingController = NSHostingController(rootView: ModalView())
hostingController.title = "Window Title"
viewController.presentAsModalWindow(hostingController)
```

### Sizing options — [8:45]

```swift
hostingController.sizingOptions = [.minSize, .intrinsicContentSize, .maxSize]
```

### Copy, Cut, and Paste commands — [10:47]

```swift
Image(...)
.focusable()
.copyable { ... }
.cuttable { ... }
.pasteDestination(payloadType: Image.self) { ... }
```

### Respond to standard commands — [11:02]

```swift
struct ShortcutsEditorView: View {
    var body: some View {
        ScrollView { ... }
            .onMoveCommand { moveSelection(direction: $0) }
            .onExitCommand { cancelOperations() }
            .onCommand(#selector(NSResponder.selectAll(_:)) { selectAllActions() }
            .onCommand(#selector(moveActionUp(_:)) { moveSelectedAction(.up) }
            .onCommand(#selector(moveActionDown(_:)) { moveSelectedAction(.down) }
    }
}
```

### Script editor — [15:18]

```swift
class ScriptEditorView: NSView {
    var sourceCode: String
    var isEditable: Bool
    weak var delegate: ScriptEditorViewDelegate?
}

protocol ScriptEditorViewDelegate: AnyObject {
    func sourceCodeDidChange(in view: ScriptEditorView) -> Void
}
```

### Script editor container — [15:40]

```swift
struct ScriptEditorContainerView: View {
    @State var sourceCode: String = ""

    var body: some View {
        VStack {
            CompileButton { compile(code: sourceCode) }
            Divider()
            ScriptEditorRepresentable(sourceCode: $sourceCode)
        }
    }
}
```

### Script editor representable — [16:13]

```swift
struct ScriptEditorRepresentable: NSViewRepresentable {
    @Binding var sourceCode: String

    func makeNSView(context: Context) -> ScriptEditorView {
        let scriptEditor = ScriptEditorView(frame: .zero)
        scriptEditor.delegate = context.coordinator
        return scriptEditor
    }

    func updateNSView(_ nsView: ScriptEditorView, context: Context) {
        if sourceCode != scriptEditor.sourceCode {
            scriptEditor.sourceCode = sourceCode
        }
        scriptEditor.isEditable = context.environment.isEnabled
        // Make sure coordinator has a reference to the current value 
        // of the binding:
        context.coordinator.representable = self
    }

    func makeCoordinator() -> Coordinator {
        Coordinator(representable: self)
    }
}

class Coordinator: NSObject, ScriptEditorViewDelegate {
    var representable: ScriptEditorRepresentable

    init(representable: ScriptEditorRepresentable) { ... }

    func sourceCodeDidChange(in view: ScriptEditorView) {
        representable.sourceCode = view.sourceCode
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10075/5/041C40B8-2F14-4B08-8406-CFCE8E85A1B0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10075/5/041C40B8-2F14-4B08-8406-CFCE8E85A1B0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10075) — developer.apple.com. Indexed for agent consumption._