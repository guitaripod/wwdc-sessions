---
id: "wwdc2022-10074"
event: "wwdc2022"
year: 2022
title: "What's new in AppKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10074"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What's new in AppKit

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10074](https://developer.apple.com/videos/play/wwdc2022/10074)

Discover the latest advances in Mac app development using AppKit. We’ll take you through the latest updates to SF Symbols, show you how you can elevate your interface with enhanced controls, and help you learn to coordinate your windows with Stage Manager. We’ll also explore the latest sharing and collaboration features for macOS.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,271 words)

## Code Snippets

### Using the grouped form style in SwiftUI — [4:54]

```swift
enum AirDropVisbility: String, CaseIterable, Identifiable {
    case nobody = "No One"
    case contactsOnly = "Contacts Only"
    case everyone = "Everyone"

    var id: String { rawValue }
    var label: String { rawValue }
    var symbolName: String {
        switch self {
        case .nobody: return "person.crop.circle.badge.xmark"
        case .contactsOnly: return "person.2.circle"
        case .everyone: return "person.crop.circle.badge.checkmark"
        }
    }
}

struct ExampleFormView: View {
    @State private var name: String = "Mac Studio"
    @State private var screenSharingEnabled: Bool = true
    @State private var fileSharingEnabled: Bool = false
    @State private var airdropVisibility = AirDropVisbility.contactsOnly

    var body: some View {
        Form {
            TextField("Computer Name", text: $name)
            Toggle("Screen Sharing", isOn: $screenSharingEnabled)
            Toggle("File Sharing", isOn: $fileSharingEnabled)
            Picker("AirDrop", selection: $airdropVisibility) {
                ForEach(AirDropVisbility.allCases) {
                    Label($0.label, systemImage: $0.symbolName)
                        .labelStyle(.titleAndIcon)
                        .tag($0)
                }
            }
        }
        .formStyle(.grouped)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10074/3/1BF7E42D-BA6E-467E-9A03-1973DCC5E9A5/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10074/3/1BF7E42D-BA6E-467E-9A03-1973DCC5E9A5/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10074) — developer.apple.com. Indexed for agent consumption._