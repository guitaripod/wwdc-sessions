---
id: "wwdc2023-10155"
event: "wwdc2023"
year: 2023
title: "Discover String Catalogs"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10155"
topics: ["Essentials", "SwiftUI & UI Frameworks", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Discover String Catalogs

**Event:** WWDC23 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10155](https://developer.apple.com/videos/play/wwdc2023/10155)

Discover how Xcode 15 makes it easy to localize your app by managing all of your strings in one place. We’ll show you how to extract, edit, export, and build strings in your project using String Catalogs. We’ll also share how you can adopt String Catalogs in existing projects at your own pace by choosing which files to migrate.

**Keywords:** `i10n`, `internationalization`, `l18n`, `localization`, `localizedstringresource`, `nslocalizedstring`, `stringsdict`, `xcstring`, `xliff`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,173 words)

## Documentation & Resources

- [Localization](https://developer.apple.com/documentation/Xcode/localization) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/localization
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/localization.json
- [Expanding Your App to New Markets](https://developer.apple.com/localization/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/localization/

## Code Snippets

### Localizable string — [4:30]

```swift
String(localized: "Welcome to WWDC!")
```

### Localizable string with default value — [4:42]

```swift
String(localized: "WWDC_NOTIFICATION_TITLE",
       defaultValue: "Welcome to WWDC!")
```

### Localizable string with comment — [5:05]

```swift
String(localized: "Welcome to WWDC!",
       comment: "Notification banner title")
```

### Localizable string with table and comment — [5:22]

```swift
String(localized: "Welcome to WWDC!",
       table: "WWDCNotifications",
       comment: "Notification banner title")
```

### Localizable strings in SwiftUI — [7:36]

```swift
// Localizable strings in SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Label("Thanks for shopping with us!", systemImage: "bag")
                .font(.title)

            HStack {
                Button("Clear Cart") { }

                Button("Checkout") { }
            }
        }
    }
}
```

### Localizable strings in SwiftUI with LocalizedStringKey — [8:01]

```swift
// Localizable strings in SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            // init(_ titleKey: LocalizedStringKey, systemImage name: String)
            Label("Thanks for shopping with us!", systemImage: "bag")
                .font(.title)

            HStack {
                Button("Clear Cart") { }

                Button("Checkout") { }
            }
        }
    }
}
```

### Localizable strings in SwiftUI text view — [8:08]

```swift
// Localizable strings in SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Label {
                Text("Thanks for shopping with us!", comment: "Label above checkout button")
            } icon: {
                Image(systemName: "bag")
            }
            .font(.title)

            HStack {
                Button("Clear Cart") { }
                Button("Checkout") { }
            }
        }
    }
}
```

### Localizable strings in SwiftUI custom view — [8:16]

```swift
// Localizable strings in SwiftUI

struct CardView: View {
    let title: LocalizedStringResource
    let subtitle: LocalizedStringResource

    var body: some View {
        ZStack {
            RoundedRectangle(cornerRadius: 10.0)
            VStack {
                Text(title)
                Text(subtitle)
            }
            .padding()
        }
    }
}

CardView(title: "Recent Purchases", subtitle: "Items you’ve ordered in the past week.")
```

### Localizable strings in Swift displayed at runtime — [9:03]

```swift
// Localizable strings in Swift

import Foundation

func stringsToPresent() -> (String, AttributedString) {
    let deferredString = LocalizedStringResource("Title")

    …

    return (
        String(localized: deferredString),
        AttributedString(localized: "**Attributed** _Subtitle_")
    )
}
```

### Localizable strings in Objective-C — [9:44]

```objectivec
// Localizable strings in Objective-C

#import <Foundation/Foundation.h>

- (NSString *)stringForDisplay {
    return NSLocalizedString(@"Recent Purchases", @"Button Title");
}

#define MyLocalizedString(key, comment) \
    [myBundle localizedStringForKey:key value:nil table:nil]
```

### Localizable strings in C — [10:04]

```cpp
// Localizable strings in C

#include <CoreFoundation/CoreFoundation.h>

CFStringRef stringForDisplay(void) {
    return CFCopyLocalizedString(CFSTR("Recent Purchases"), CFSTR("Button Title"));
}

#define MyLocalizedString(key, comment) \
    CFBundleCopyLocalizedString(myBundle, key, NULL, NULL)
```

### App Shortcut phrases — [11:23]

```swift
// App Shortcut phrases

struct FoodTruckShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: ShowTopDonutsIntent(),
            phrases: [
                "\(.applicationName) Trends for \(\.$timeframe)",
                "Show trending donuts for \(\.$timeframe) in \(.applicationName)",
                "Give me trends for \(\.$timeframe) in \(.applicationName)"
            ]
        )
    }
}
```

### Stringsdict in XLIFF — [23:53]

```xml
// Stringsdict in XLIFF

<trans-unit id="/%lld Recent Visitors:dict/NSStringLocalizedFormatKey:dict/:string">
    <source>%#@recentVisitors@</source>
    <target>%#@recentVisitors@</target>
</trans-unit>

<trans-unit id="/%lld Recent Visitors:dict/recentVisitors:dict/one:dict/:string">
    <source>%lld Recent Visitor</source>
    <target>%lld Visitante Recente</target>
</trans-unit>

<trans-unit id="/%lld Recent Visitors:dict/recentVisitors:dict/other:dict/:string">
    <source>%lld Recent Visitors</source>
    <target>%lld Visitantes Recentes</target>
</trans-unit>
```

### String Catalog in XLIFF — [24:08]

```xml
// String Catalog in XLIFF

<trans-unit id="%lld Recent Visitors|==|plural.one">
    <source>%lld Recent Visitor</source>
    <target>%lld Visitante Recente</target>
</trans-unit>

<trans-unit id="%lld Recent Visitors|==|plural.other">
    <source>%lld Recent Visitors</source>
    <target>%lld Visitantes Recentes</target>
</trans-unit>
```

### String Catalog variations in XLIFF — [24:58]

```xml
// Overriding variation in XLIFF

<trans-unit id="Bird Food Shop|==|device.applewatch">
    <source>Bird Food Shop</source>
    <target>Loja de Comida</target>
</trans-unit>

<trans-unit id="Bird Food Shop|==|device.other">
    <source>Bird Food Shop</source>
    <target>Loja de Comida de Passarinho</target>
</trans-unit>
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10155/4/0A18D858-81AA-4A3C-B77E-EF67C956908B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10155/4/0A18D858-81AA-4A3C-B77E-EF67C956908B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10155) — developer.apple.com. Indexed for agent consumption._
