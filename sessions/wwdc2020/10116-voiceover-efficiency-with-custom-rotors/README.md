---
id: "wwdc2020-10116"
event: "wwdc2020"
year: 2020
title: "VoiceOver efficiency with custom rotors"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10116"
topics: ["Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# VoiceOver efficiency with custom rotors

**Event:** WWDC20 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10116](https://developer.apple.com/videos/play/wwdc2020/10116)

Discover how you can integrate custom rotors and help people who use VoiceOver navigate complex situations within your app. Learn how custom rotors can help people explore even the most intricate interfaces, explore how to implement a custom rotor, and find out how rotors can improve navigation for someone who relies on VoiceOver. To get the most out of this session, you should be familiar with general accessibility principles and VoiceOver accessibility APIs on iOS and iPadOS. For an overview, watch “Making Apps More Accessible with Custom Actions.”

**Keywords:** `accessibility`, `custom rotors`, `related elements`, `rotors`, `text accessibility`, `uiaccessibilitycustomrotor`, `voiceover`, `voice over`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,796 words)

## Documentation & Resources

- [Accessibility for UIKit](https://developer.apple.com/documentation/UIKit/accessibility-for-uikit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/accessibility-for-uikit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/accessibility-for-uikit.json

## Code Snippets

### mapView.accessibilityCustomRotors = [customRotor(for: .stores), customRotor(for: .parks)] — [4:04]

```swift
mapView.accessibilityCustomRotors = [customRotor(for: .stores), customRotor(for: .parks)]
```

### map rotor 1 — [4:31]

```swift
// Custom map rotors

func customRotor(for poiType: POI) -> UIAccessibilityCustomRotor {
    UIAccessibilityCustomRotor(name: poiType.rotorName) { [unowned self] predicate in

        return UIAccessibilityCustomRotorItemResult(    )
    }
}
```

### map rotor 2 — [4:56]

```swift
// Custom map rotors

func customRotor(for poiType: POI) -> UIAccessibilityCustomRotor {
    UIAccessibilityCustomRotor(name: poiType.rotorName) { [unowned self] predicate in
        let currentElement = predicate.currentItem.targetElement as? MKAnnotationView
        let annotations = self.annotationViews(for: poiType)
        let currentIndex = annotations.firstIndex { $0 == currentElement }
        return UIAccessibilityCustomRotorItemResult(    )

    }
}
```

### map rotor 3 — [5:04]

```swift
// Custom map rotors

func customRotor(for poiType: POI) -> UIAccessibilityCustomRotor {
    UIAccessibilityCustomRotor(name: poiType.rotorName) { [unowned self] predicate in
        let currentElement = predicate.currentItem.targetElement as? MKAnnotationView
        let annotations = self.annotationViews(for: poiType)
        let currentIndex = annotations.firstIndex { $0 == currentElement }
        let targetIndex: Int
        switch predicate.searchDirection {
        case .previous:
            targetIndex = (currentIndex ?? 1) - 1
        case .next:
            targetIndex = (currentIndex ?? -1) + 1
        }
        return UIAccessibilityCustomRotorItemResult(    )

    }
}
```

### Maps rotor 4 — [5:17]

```swift
// Custom map rotors

func customRotor(for poiType: POI) -> UIAccessibilityCustomRotor {
    UIAccessibilityCustomRotor(name: poiType.rotorName) { [unowned self] predicate in
        let currentElement = predicate.currentItem.targetElement as? MKAnnotationView
        let annotations = self.annotationViews(for: poiType)
        let currentIndex = annotations.firstIndex { $0 == currentElement }
        let targetIndex: Int
        switch predicate.searchDirection {
        case .previous:
            targetIndex = (currentIndex ?? 1) - 1
        case .next:
            targetIndex = (currentIndex ?? -1) + 1
        }
        guard 0..<annotations.count ~= targetIndex else { return nil } // Reached boundary
        return UIAccessibilityCustomRotorItemResult(targetElement: annotations[targetIndex],
                                                    targetRange: nil)
    }
}
```

### Text rotor 1 — [8:07]

```swift
// Custom text rotor

func customRotor(for attribute: NSAttributedString.Key) -> UIAccessibilityCustomRotor {
    UIAccessibilityCustomRotor(name: attribute.rotorName) { [unowned self] predicate in
        var targetRange: UITextRange? // Goal: find the range of following `attribute`
        let beginningRange = 
        guard let currentRange =    else { return nil }

        switch predicate.searchDirection {   }

        return UIAccessibilityCustomRotorItemResult(targetElement: self,
                                                    targetRange: targetRange)
    }
}
```

### Text rotor 2 — [8:20]

```swift
// Custom text rotor

func customRotor(for attribute: NSAttributedString.Key) -> UIAccessibilityCustomRotor {
    UIAccessibilityCustomRotor(name: attribute.rotorName) { [unowned self] predicate in
        var targetRange: UITextRange? // Goal: find the range of following `attribute`
        let beginningRange = self.textRange(from: self.beginningOfDocument,
                                            to: self.beginningOfDocument)
        guard let currentRange = predicate.currentItem.targetRange ?? beginningRange else {
            return nil
        }
        let searchRange: NSRange, searchOptions: NSAttributedString.EnumerationOptions
        switch predicate.searchDirection {   }

        return UIAccessibilityCustomRotorItemResult(targetElement: self,
                                                    targetRange: targetRange)
    }
}
```

### Text rotor 3 — [8:37]

```swift
// Custom text rotor

func customRotor(for attribute: NSAttributedString.Key) -> UIAccessibilityCustomRotor {
    UIAccessibilityCustomRotor(name: attribute.rotorName) { [unowned self] predicate in
        var targetRange: UITextRange? // Goal: find the range of following `attribute`
        let beginningRange = 
        guard let currentRange =    else { return nil }
        let searchRange: NSRange, searchOptions: NSAttributedString.EnumerationOptions
        switch predicate.searchDirection {
        case .previous:
            searchRange = self.rangeOfAttributedTextBefore(currentRange)
            searchOptions = [.reverse]
        case .next:
            searchRange = self.rangeOfAttributedTextAfter(currentRange)
            searchOptions = []
        }

        return UIAccessibilityCustomRotorItemResult(targetElement: self,
                                                    targetRange: targetRange)
    }
}
```

### Text rotor 4 (end) — [9:06]

```swift
// Custom text rotor

func customRotor(for attribute: NSAttributedString.Key) -> UIAccessibilityCustomRotor {
    UIAccessibilityCustomRotor(name: attribute.rotorName) { [unowned self] predicate in
        var targetRange: UITextRange? // Goal: find the range of following `attribute`
        let beginningRange =
        guard let currentRange =    else { return nil }
        let searchRange: NSRange, searchOptions: NSAttributedString.EnumerationOptions
        switch predicate.searchDirection {   }
        self.attributedText.enumerateAttribute(
            attribute, in: searchRange, options: searchOptions) { value, range, stop in
            guard value != nil else { return }
            targetRange = self.textRange(from: range)
            stop.pointee = true
        }
        return UIAccessibilityCustomRotorItemResult(targetElement: self,
                                                    targetRange: targetRange)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10116/5/80EA07DE-B3B6-4DA6-80FE-BC03C5F0CB43/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10116) — developer.apple.com. Indexed for agent consumption._
