---
id: "wwdc2022-110343"
event: "wwdc2022"
year: 2022
title: "SwiftUI on iPad: Add toolbars, titles, and more"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110343"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# SwiftUI on iPad: Add toolbars, titles, and more

**Event:** WWDC22 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-110343](https://developer.apple.com/videos/play/wwdc2022/110343)

Get ready to tune up your iPad app’s toolbars with SwiftUI. We’ll show you how you can structure toolbars to take advantage of the space available on iPad and help people maximize their productivity. We’ll also take you through customization, explore the latest ways you can represent documents, and more. This is the second session in a two-part series. To get the most out of this video, we recommend starting with “SwiftUI on iPad: Organize your interface.”

**Keywords:** `area`, `center`, `controlgroup`, `control group`, `customizable toolbars`, `customization`, `customization popover`, `document`, `editable titles`, `id`, `label`, `leading`, `leading aligned navigation`, `menu`, `more menu`, `navigation titles`, `overflow menu`, `placement`, `.primaryaction`, `primary action`, `primary action placement`, `renamebutton()`, `.secondaryaction`, `secondary action`, `title menu`, `title menu header`, `toolbar`, `toolbar customization`, `toolbar item`, `trailing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,077 words)

## Documentation & Resources

- [Configure your apps navigation titles](https://developer.apple.com/documentation/SwiftUI/Configure-Your-Apps-Navigation-Titles) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Configure-Your-Apps-Navigation-Titles
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Configure-Your-Apps-Navigation-Titles.json
- [ControlGroup](https://developer.apple.com/documentation/SwiftUI/ControlGroup) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/ControlGroup
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/ControlGroup.json
- [ShareLink](https://developer.apple.com/documentation/SwiftUI/ShareLink) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/ShareLink
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/ShareLink.json
- [ToolbarItem](https://developer.apple.com/documentation/SwiftUI/ToolbarItem) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/ToolbarItem
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/ToolbarItem.json
- [ToolbarRole](https://developer.apple.com/documentation/SwiftUI/ToolbarRole) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/ToolbarRole
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/ToolbarRole.json

## Code Snippets

### Explicit More Menu — [0:01]

```swift
PlaceDetailContent(place: $place)
    .toolbar {
        ToolbarItem(placement: .primaryAction) {
            Menu {
                FavoriteToggle(place: $place)
                AdjustImageButton(place: $place)
                AdjustMapButton(place: $place)
            } label: {
                Label(
                    "More", 
                    systemImage: "ellipsis.circle")
            }
        }
    }
```

### Menu in ToolbarItemGroup — [0:02]

```swift
PlaceDetailContent(place: $place)
    .toolbar {
        ToolbarItemGroup(placement: .primaryAction) {
            Menu {
                FavoriteToggle(place: $place)
                AdjustImageButton(place: $place)
                AdjustMapButton(place: $place)
            } label: {
                Label("More", systemImage: "ellipsis.circle")
            }
        }
    }
```

### ToolbarItemGroup with Menu Content — [0:03]

```swift
PlaceDetailContent(place: $place)
    .toolbar {
        ToolbarItemGroup(placement: .primaryAction) {
            FavoriteToggle(place: $place)
            AdjustImageButton(place: $place)
            AdjustMapButton(place: $place)
        }
    }
```

### Secondary Action ToolbarItemGroup — [0:04]

```swift
PlaceDetailContent(place: $place)
    .toolbar {
        ToolbarItemGroup(placement: .secondaryAction) {
            FavoriteToggle(place: $place)
            AdjustImageButton(place: $place)
            AdjustMapButton(place: $place)
        }
    }
```

### Toolbar Role — [0:05]

```swift
PlaceDetailContent(place: $place)
    .toolbar {
        ToolbarItemGroup(placement: .secondaryAction) {
            FavoriteToggle(place: $place)
            AdjustImageButton(place: $place)
            AdjustMapButton(place: $place)
        }
    }
    .toolbarRole(.editor)
```

### Individual ToolbarItems — [0:06]

```swift
PlaceDetailContent(place: $place)
    .toolbar {
        ToolbarItem(placement: .secondaryAction) {
            FavoriteToggle(place: $place)
        }
        ToolbarItem(placement: .secondaryAction) {
            AdjustImageButton(place: $place)
        }
        ToolbarItem(placement: .secondaryAction) {
            AdjustMapButton(place: $place)
        }
    }
    .toolbarRole(.editor)
```

### Customizable ToolbarItems — [0:07]

```swift
PlaceDetailContent(place: $place)
    .toolbar(id: "place") {
        ToolbarItem(id: "favorite", placement: .secondaryAction) {
            FavoriteToggle(place: $place)
        }
        ToolbarItem(id: "image", placement: .secondaryAction) {
            AdjustImageButton(place: $place)
        }
        ToolbarItem(id: "map", placement: .secondaryAction) {
            AdjustMapButton(place: $place)
        }
    }
    .toolbarRole(.editor)
```

### ShareLink ToolbarItem — [0:08]

```swift
PlaceDetailContent(place: $place)
    .toolbar(id: "place") {
        ToolbarItem(id: "favorite", placement: .secondaryAction) {
            FavoriteToggle(place: $place)
        }
        ToolbarItem(id: "image", placement: .secondaryAction) {
            AdjustImageButton(place: $place)
        }
        ToolbarItem(id: "map", placement: .secondaryAction) {
            AdjustMapButton(place: $place)
        }
        ToolbarItem(id: "share", placement: .secondaryAction) {
            ShareLink(item: place)
        }
    }
    .toolbarRole(.editor)
```

### Non-default ShareLink ToolbarItem — [0:09]

```swift
PlaceDetailContent(place: $place)
    .toolbar(id: "place") {
        ToolbarItem(id: "favorite", placement: .secondaryAction) {
            FavoriteToggle(place: $place)
        }
        ToolbarItem(id: "image", placement: .secondaryAction) {
            AdjustImageButton(place: $place)
        }
        ToolbarItem(id: "map", placement: .secondaryAction) {
            AdjustMapButton(place: $place)
        }
        ToolbarItem(id: "share", placement: .secondaryAction, showsByDefault: false) {
            ShareLink(item: place)
        }
    }
    .toolbarRole(.editor)
```

### ControlGroup in ToolbarItem — [0:10]

```swift
PlaceDetailContent(place: $place)
    .toolbar(id: "place") {
        ToolbarItem(id: "favorite", placement: .secondaryAction) {
            FavoriteToggle(place: $place)
        }
        ToolbarItem(id: "image", placement: .secondaryAction) {
            ControlGroup {
                AdjustImageButton(place: $place)
                AdjustMapButton(place: $place)
            }
        }
        ToolbarItem(id: "share", placement: .secondaryAction, showsByDefault: false) {
            ShareLink(item: place)
        }
    }
    .toolbarRole(.editor)
```

### ControlGroup in ToolbarItem with Label — [0:11]

```swift
PlaceDetailContent(place: $place)
    .toolbar(id: "place") {
        ToolbarItem(id: "favorite", placement: .secondaryAction) {
            FavoriteToggle(place: $place)
        }
        ToolbarItem(id: "image", placement: .secondaryAction) {
            ControlGroup {
                AdjustImageButton(place: $place)
                AdjustMapButton(place: $place)
            } label: {
                Label("Edits", systemImage: "wand.and.stars")
            }
        }
    }
    .toolbarRole(.editor)
```

### NewButton ToolbarItem — [0:12]

```swift
PlaceDetailContent(place: $place)
    .toolbar(id: "place") {
        ToolbarItem(id: "new", placement: .primaryAction) {
            NewButton()
        }
        ToolbarItem(id: "favorite", placement: .secondaryAction) {
            FavoriteToggle(place: $place)
        }
        ToolbarItem(id: "image", placement: .secondaryAction) {
            ControlGroup {
                AdjustImageButton(place: $place)
                AdjustMapButton(place: $place)
            } label: {
                Label("Edits", systemImage: "wand.and.stars")
            }
        }
        ToolbarItem(id: "share", placement: .secondaryAction, showsByDefault: false) {
            ShareLink(item: place)
        }
    }
    .toolbarRole(.editor)
```

### Navigation Title — [0:13]

```swift
PlaceDetailContent(place: $place)
    // toolbar customizations ...
    .navigationTitle(place.name)
```

### Navigation Title with Menu — [0:14]

```swift
PlaceDetailContent(place: $place)
    // toolbar customizations ...
    .navigationTitle(place.name) {
        MyPrintButton()
    }
```

### Editable Navigation Title with Menu — [0:15]

```swift
PlaceDetailContent(place: $place)
    // toolbar customizations ...
    .navigationTitle($place.name) {
        MyPrintButton()
    }
```

### Editable Navigation Title with RenameButton — [0:16]

```swift
PlaceDetailContent(place: $place)
    // toolbar customizations ...
    .navigationTitle($place.name) {
        MyPrintButton()
        RenameButton()
    }
```

### Navigation Document — [0:17]

```swift
PlaceDetailContent(place: $place)
    // toolbar customizations ...
    .navigationTitle($place.name) {
        MyPrintButton()
        RenameButton()
    }
    .navigationDocument(place.url)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110343/4/61E55FAE-4837-4DAF-912C-8D101B7DF820/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110343/4/61E55FAE-4837-4DAF-912C-8D101B7DF820/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110343) — developer.apple.com. Indexed for agent consumption._
