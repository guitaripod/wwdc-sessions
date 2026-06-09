---
id: "wwdc2021-10121"
event: "wwdc2021"
year: 2021
title: "Tailor the VoiceOver experience in your data-rich apps"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10121"
topics: ["Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Tailor the VoiceOver experience in your data-rich apps

**Event:** WWDC21 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10121](https://developer.apple.com/videos/play/wwdc2021/10121)

Learn how to present complex data through VoiceOver with the Accessibility Custom Content API. Discover how you can deliver accessibility information in a concise form, and only when someone wants it. We’ll show you how you can integrate AXCustomContent and help people who want VoiceOver enabled to navigate your data-rich apps in an efficient manner.

To get the most out of this session, you should be familiar with general accessibility principles and VoiceOver accessibility APIs available in Swift and SwiftUI.

**Keywords:** `accessibility`, `accessibilitycustomcontent`, `accessibility custom content`, `accessibilitycustomcontentkey`, `axcustomcontent`, `axcustomcontentprovider`, `custom content api`, `importance property`, `more content available`, `more content rotor`, `screen reader`, `verbosity`, `voiceover`, `voice over`, `voiceover rotor`, `woof woof`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,412 words)

## Documentation & Resources

- [Accessibility for Developers](https://developer.apple.com/accessibility/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/accessibility/

## Code Snippets

### Accessibility Custom Content API Sample — [5:03]

```swift
import UIKit
import Accessibility

class DogTableViewCell: UITableViewCell, AXCustomContentProvider {

    var coverImage: UIImageView!
    var name: UILabel!
    var type: UILabel!
    var desc: UILabel!
    var popularity: UILabel!
    var age: UILabel!
    var weight: UILabel!
    var height: UILabel!

    override var accessibilityLabel: String? {
        get {
            guard let nameLabel = name.text else { return nil }
            guard let typeLabel = type.text else { return nil }
            return nameLabel + ", " + typeLabel
        }
        set { }
    }

    var accessibilityCustomContent: [AXCustomContent]! {
        get {
            let notes = AXCustomContent(label: "Description", value: desc.text!)
            let popularity = AXCustomContent(label: "Popularity", value: popularity.text!)
            let age = AXCustomContent(label: "Age", value: age.text!)
            let weight = AXCustomContent(label: "Weight", value: weight.text!)
            let height = AXCustomContent(label: "Height" , value: height.text!)
            return [age, popularity, weight, height, notes]
        }
        set { }
    }
}
```

### Accessibility Custom Content API Sample with importance property — [6:49]

```swift
import UIKit
import Accessibility

class DogTableViewCell: UITableViewCell, AXCustomContentProvider {

    var coverImage: UIImageView!
    var name: UILabel!
    var type: UILabel!
    var desc: UILabel!
    var popularity: UILabel!
    var age: UILabel!
    var weight: UILabel!
    var height: UILabel!

    override var accessibilityLabel: String? {
        get {
            guard let nameLabel = name.text else { return nil }
            guard let typeLabel = type.text else { return nil }
            return nameLabel + ", " + typeLabel
        }
        set { }
    }

    var accessibilityCustomContent: [AXCustomContent]! {
        get {
            let notes = AXCustomContent(label: "Description", value: desc.text!)
            let popularity = AXCustomContent(label: "Popularity", value: popularity.text!)
            let age = AXCustomContent(label: "Age", value: age.text!)
            age.importance = .high
            let weight = AXCustomContent(label: "Weight", value: weight.text!)
            let height = AXCustomContent(label: "Height" , value: height.text!)
            return [popularity, age, weight, height, notes]
        }
        set { }
    }
}
```

### Accessibility Custom Content API Basic Sample in SwiftUI — [7:47]

```swift
struct SampleView: View {
    var body: some View {
        VStack {
            Text(name)
            Text(description)
        }
        .accessibilityElement(children: .combine)
        .accessibilityCustomContent("Description", description, importance: .high)
    }
}
```

### Accessibility Custom Content API Sample in Swift UI — [8:10]

```swift
import SwiftUI
import Accessibility

struct DogCell: View {
    var dog: Dog
    var body: some View {
        VStack {
            HStack {
                dog.image
                    .resizable()
                VStack(alignment: .leading) {
                    Text(dog.name)
                        .font(.title)
                    Spacer()
                    Text(dog.type)
                        .font(.body)
                    Spacer()
                    Text(dog.description)
                        .fixedSize(horizontal: false, vertical: true)
                        .font(.subheadline)
                        .foregroundColor(Color(uiColor: UIColor.brown))
                        .accessibilityHidden(true)
                }
                Spacer()
            }
            .padding(.horizontal)
            HStack(alignment: .top) {
                VStack(alignment: .leading) {
                    HStack {
                        Text(dog.popularity)
                        Spacer()
                        Text(dog.age)
                        Spacer()
                        Text(dog.weight)
                        Spacer()
                        Text(dog.height)
                    }
                    .foregroundColor(Color(uiColor: UIColor.darkGray))
                    .accessibilityHidden(true)
                }
                Spacer()
            }
            .padding(.horizontal)
            Divider()
        }
        .accessibilityElement(children: .combine)
        .accessibilityCustomContent("Age", dog.age, importance: .high)
        .accessibilityCustomContent("Popularity", dog.popularity)
        .accessibilityCustomContent("Weight", dog.weight)
        .accessibilityCustomContent("Height", dog.height)
        .accessibilityCustomContent("Description", dog.description)
    }
}
```

### Accessibility Custom Content API Sample with AccessibilityCustomContentKey in SwiftUI — [8:57]

```swift
import SwiftUI
import Accessibility

extension AccessibilityCustomContentKey {
    static var age: AccessibilityCustomContentKey {
        AccessibilityCustomContentKey("Age")
    }
}

struct DogCell: View {
    var dog: Dog
    var body: some View {
        VStack {
            HStack {
                dog.image
                    .resizable()
                VStack(alignment: .leading) {
                    Text(dog.name)
                        .font(.title)
                    Spacer()
                    Text(dog.type)
                        .font(.body)
                    Spacer()
                    Text(dog.description)
                        .fixedSize(horizontal: false, vertical: true)
                        .font(.subheadline)
                        .foregroundColor(Color(uiColor: UIColor.brown))
                        .accessibilityHidden(true)
                }
                Spacer()
            }
            .padding(.horizontal)
            HStack(alignment: .top) {
                VStack(alignment: .leading) {
                    HStack {
                        Text(dog.popularity)
                        Spacer()
                        Text(dog.age)
                        Spacer()
                        Text(dog.weight)
                        Spacer()
                        Text(dog.height)
                    }
                    .foregroundColor(Color(uiColor: UIColor.darkGray))
                    .accessibilityHidden(true)
                }
                Spacer()
            }
            .padding(.horizontal)
            Divider()
        }
        .accessibilityElement(children: .combine)
        .accessibilityCustomContent(.age, dog.age, importance: .high)
        .accessibilityCustomContent("Popularity", dog.popularity)
        .accessibilityCustomContent("Weight", dog.weight)
        .accessibilityCustomContent("Height", dog.height)
        .accessibilityCustomContent("Description", dog.description)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10121/6/9DFDD9FF-82AF-48DC-A0C1-C2CB8A518D93/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10121/6/9DFDD9FF-82AF-48DC-A0C1-C2CB8A518D93/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10121) — developer.apple.com. Indexed for agent consumption._