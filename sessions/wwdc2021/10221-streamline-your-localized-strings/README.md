---
id: "wwdc2021-10221"
event: "wwdc2021"
year: 2021
title: "Streamline your localized strings"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10221"
topics: ["Essentials", "SwiftUI & UI Frameworks", "System Services", "Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Streamline your localized strings

**Event:** WWDC21 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10221](https://developer.apple.com/videos/play/wwdc2021/10221)

When you localize the text within your app, you can help make your app more accessible to a worldwide audience. Discover best practices for building your localization workflow, including how to write and format strings accurately, and learn how to prepare strings for localization in different languages using Xcode.

**Keywords:** `🌍`, `🌎`, `🌏`, `formatter`, `i18n`, `internationalization`, `stringsdict`, `swiftui`, `translation`, `xcloc`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,592 words)

## Documentation & Resources

- [Localization](https://developer.apple.com/documentation/Xcode/localization) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/localization
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/localization.json
- [Expanding Your App to New Markets](https://developer.apple.com/localization/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/localization/

## Code Snippets

### Declaring a string — [3:30]

```swift
Button("Order")
```

### Declaring a string anywhere else — [3:44]

```swift
button.title = NSLocalizedString("Order", comment: "…")
button.title = String(localized: "Order")
```

### Declaring a string in a SwiftUI view 2 — [4:20]

```swift
Text("Your order is ready.")
Button("Order") {
  // Action…
}
```

### Declare a string in SwiftUI view with verbatim — [4:33]

```swift
Text(verbatim: "Sample data")
```

### Button to place an order — [4:54]

```swift
// SwiftUI
Button("Order") { … }


// Swift
button.title = String(localized: "Order")
```

### Button to place an order with a variable — [5:15]

```swift
let count = 3


// SwiftUI
Button("Order \(count) Tickets") { … }


// Swift
button.title = String(localized: "Order \(count) Tickets")
```

### Button to place an order with a variable 2 — [5:36]

```swift
let count = 3

// Supports user’s preferred numbers,
// pluralization, RTL variables isolation…
// Previously: .localizedStringWithFormat()
String(localized: "Order \(count) Tickets")
```

### Use 2 separate strings — [6:21]

```swift
// Recommended for all languages
String(localized: "Order Now")
String(localized: "Order Later")
```

### Button to place an order 2 — [6:57]

```swift
// SwiftUI
Text("Order")


// Swift
String(localized: "Order")
```

### Button to place an order with comment — [7:09]

```swift
// SwiftUI
Text("Order", comment: "Button: confirms concert tickets booking”)


// Swift
String(localized: "Order", comment: "Button: confirms concert tickets booking")
```

### What makes a good comment — [7:36]

```swift
Text("Order", comment: "Button: confirms concert tickets booking")
Text("Order", comment: "Button: confirms concert tickets booking")
Text("\(ticketCount) Ordered", comment: "Order summary: total number of tickets ordered")
```

### Request server strings in the user's language — [10:52]

```swift
Bundle.preferredLocalizations(from: allServerLanguages).first
```

### Declare a string with a variable, customized table name, and a comment — [11:37]

```swift
Text("\(ticketCount) Ordered",
     tableName: "UserProfile",
     comment: "Profile subtitle: total number of tickets ordered")
```

### Using a framework — [13:49]

```swift
/* —-----------—------------—-—---- In TicketKit Framework —---------—------------—-—---- */

// TicketKit/OrderStatus.swift
public enum OrderStatus {
    case pending, processing, complete, canceled, invalid(Error)

    var displayName: String {
        switch self {
        case .complete: return String(localized: "Complete",
                                      bundle: Bundle(for: AnyClassInTicketKit.self),
                                      comment: "Standalone ticket status: order finalized")

/* —-----------—-----------—---—---       In Host App      —---------—------------—-—---- */

import TicketKit
Text(OrderStatus.complete.displayName)
```

### Import translated strings catalogs — [17:43]

```bash
xcodebuild -exportLocalizations -workspace VacationPlanet.xcworkspace -localizationPath ~/Documents
xcodebuild -importLocalizations -workspace VacationPlanet.xcworkspace -localizationPath ~/Documents/de.xcloc
```

### Localized attributed strings — [18:28]

```swift
AttributedString(localized: "Your order is **complete**!",
                 comment: "Ticket order confirmation title")
```

### Plural with stringsdict — [19:22]

```swift
String(localized: "Order \(ticketCount) Ticket(s)")
```

### Plural for strings without a number — [22:46]

```swift
if ticketCount == 1 {
    button.text = String(localized: "Order This Ticket")
} else if ticketCount == 2 { // If needed
    button.text = String(localized: "Order Both Tickets")
} else {
    button.text = String(localized: "Order All Tickets")
}
```

### Automatic grammar agreement — [23:31]

```swift
AttributedString(localized: "Order ^[\(ticketsCount) Ticket](inflect: true)")
```

### Format data in strings — [25:45]

```swift
["pop", "rock", "electronic"].formatted(.list(type: .or)) // pop, rock, or electronic

Text("Total: \(price, format: .currency(code: "USD"))", // Total: $9.41
     comment: "Order subtitle: total price of all tickets")
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10221/4/E712C2D5-BD11-435B-8F19-C4ACFD79160A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10221/4/E712C2D5-BD11-435B-8F19-C4ACFD79160A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10221) — developer.apple.com. Indexed for agent consumption._
