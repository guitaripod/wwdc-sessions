---
id: "wwdc2026-219"
event: "wwdc2026"
year: 2026
title: "Enhance the accessibility of your reading app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/219"
topics: ["SwiftUI & UI Frameworks", "Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Enhance the accessibility of your reading app

**Event:** WWDC26 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-219](https://developer.apple.com/videos/play/wwdc2026/219)

Learn how to create robust reading experiences for VoiceOver, Speak Screen, and more. Find out how to provide intuitive text selection, clear navigation between lines and paragraphs, and continuous reading across individual elements and multiple pages.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,752 words)

## Documentation & Resources

- [accessibilityNextTextNavigationElement](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/accessibilityNextTextNavigationElement) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ObjectiveC/NSObject-swift.class/accessibilityNextTextNavigationElement
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ObjectiveC/NSObject-swift.class/accessibilityNextTextNavigationElement.json
- [editCategory](https://developer.apple.com/documentation/UIKit/UIAccessibilityCustomAction/editCategory) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIAccessibilityCustomAction/editCategory
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIAccessibilityCustomAction/editCategory.json
- [accessibilityLinkedGroup(id:in:)](https://developer.apple.com/documentation/SwiftUI/View/accessibilityLinkedGroup(id:in:)) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/View/accessibilityLinkedGroup(id:in:)
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/View/accessibilityLinkedGroup(id:in:).json
- [causesPageTurn](https://developer.apple.com/documentation/SwiftUI/AccessibilityTraits/causesPageTurn) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/AccessibilityTraits/causesPageTurn
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/AccessibilityTraits/causesPageTurn.json
- [UITextInput](https://developer.apple.com/documentation/UIKit/UITextInput) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UITextInput
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UITextInput.json
- [Accessibility for UIKit](https://developer.apple.com/documentation/UIKit/accessibility-for-uikit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/accessibility-for-uikit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/accessibility-for-uikit.json

## Code Snippets

### Link text elements together with navigation APIs — [7:29]

```swift
// Link text elements together with navigation APIs

import UIKit

class TravelGuidePageController: UIViewController {

    var paragraphs: [TravelGuideParagraph]

    func configureNavigationElements() {
        for (index, paragraph) in paragraphs.enumerated() {
            if index + 1 < paragraphs.count {
                paragraph.accessibilityNextTextNavigationElement = paragraphs[index + 1]
            }
            if index - 1 >= 0 {
                paragraph.accessibilityPreviousTextNavigationElement = paragraphs[index - 1]
            }
        }
    }
}
```

### Link text elements together with a linked group — [7:59]

```swift
// Link text elements together with a linked group

import SwiftUI

struct PageView : View {
    @Namespace private var pageNamespace
    var paragraphs: [String
    var pageNumber: Int

    var body: some View {
        Text(paragraphs[0])
            .textSelection(.enabled)
            .accessibilityLinkedGroup(id: pageNumber, in: pageNamespace)

        Text(paragraphs[1])
            .textSelection(.enabled)
            .accessibilityLinkedGroup(id: pageNumber, in: pageNamespace)
    }
}
```

### Turn pages automatically after reading — [9:50]

```swift
// Turn pages automatically after reading

import UIKit

class TravelGuidePageController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        self.lastParagraphView.accessibilityTraits.insert(.causesPageTurn)
    }

    override func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool {
        moveToPage(direction)
        var scrollString = "Page \(currentPage) of \(pages.count)"
        UIAccessibility.post(notification: .pageScrolled, argument: scrollString)
        return true
    }
}
```

### Add actions to the editor rotor — [11:45]

```swift
// Add actions to the editor rotor

import UIKit

class TravelGuideParagraph: UITextView {

    override var accessibilityCustomActions: [UIAccessibilityCustomAction]? {
        get {
            let saveAction = UIAccessibilityCustomAction(name: "Save Recommendation") { _ in
                self.saveRecommendation()
            }
            saveAction.category = UIAccessibilityCustomAction.editCategory
            return (super.accessibilityCustomActions ?? []) + [saveAction]
        }
        set { }
    }

    private func saveRecommendation() -> Bool {
        ...
        return true
    }
}
```

### Adopt UITextInput — [16:10]

```swift
// Adopt UITextInput

import UIKit

class ScannedPage: UIView, UITextInput {

    override init(frame: CGRect) {
        super.init(frame: frame)
        let interaction = UITextInteraction(for: .nonEditable)
        interaction.textInput = self
        addInteraction(interaction)
    }

    func selectionRects(for range: UITextRange) -> [UITextSelectionRect] {
        var rects: [UITextSelectionRect] = []

        let startLine = lineIndex(for: range.start)
        let endLine = lineIndex(for: range.end)

        for line in startLine...endLine {
            let rect = selectionRectFromImage(for: range, in: line)
            rects.append(rect)
        }

        return rects
    }

    func text(in range: UITextRange) -> String? {
        let nsRange = nsRange(from: range)
        guard let range = Range(nsRange, in: scannedText) else {
            return nil
        }
        return String(scannedText[range])
    }

    var tokenizer: any UITextInputTokenizer { CustomHandwritingTokenizer(textInput: self) }

    weak var inputDelegate: UITextInputDelegate?

      var selectedTextRange: UITextRange? {
        // Update visuals when assistive technologies change selection
        willSet { inputDelegate?.selectionWillChange(self) }
        didSet { inputDelegate?.selectionDidChange(self) }
    }

}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/219/4/da70a3a7-e193-4513-904f-991788c1fa81/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/219/4/da70a3a7-e193-4513-904f-991788c1fa81/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/219) — developer.apple.com. Indexed for agent consumption._