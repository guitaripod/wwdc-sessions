---
id: "wwdc2021-10109"
event: "wwdc2021"
year: 2021
title: "What's new in Foundation"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10109"
topics: ["Essentials", "System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# What's new in Foundation

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10109](https://developer.apple.com/videos/play/wwdc2021/10109)

Discover how the latest updates to Foundation can help you improve your app's localization and internationalization support. Find out about the new AttributedString, designed specifically for Swift, and learn how you can use Markdown to apply style to your localized strings. Explore the grammar agreement engine, which automatically fixes up localized strings so they match grammatical gender and pluralization. And we’ll take you through improvements to date and number formatting that simplify complex requirements while also improving performance.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,747 words)

## Documentation & Resources

- [Foundation](https://developer.apple.com/documentation/Foundation) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Foundation
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Foundation.json

## Code Snippets

### Attributed String Basics — [2:50]

```swift
func attributedStringBasics(important: Bool) {
    var thanks = AttributedString("Thank you!")
    thanks.font = .body.bold()

    var website = AttributedString("Please visit our website.")
    website.font = .body.italic()
    website.link = URL(string: "http://www.example.com")

    var container = AttributeContainer()
    if important {
        container.foregroundColor = .red
        container.underlineColor = .primary
    } else {
        container.foregroundColor = .primary
    }

    thanks.mergeAttributes(container)
    website.mergeAttributes(container)

    print(thanks)
    print(website)
}
```

### Attributed String Characters — [4:24]

```swift
func attributedStringCharacters() {
    var message = AttributedString(localized: "Thank you! _Please visit our [website](http://www.example.com)._")
    let characterView = message.characters
    for i in characterView.indices where characterView[i].isPunctuation {
        message[i..<characterView.index(after: i)].foregroundColor = .orange
    }

    print(message)
}
```

### Attributed String Runs (Part 1) — [5:12]

```swift
func attributedStringRuns() {
    let message = AttributedString(localized: "Thank you! _Please visit our [website](http://www.example.com)._")
    let runCount = message.runs.count
    // runCount is 4
    print(runCount)

    let firstRun = message.runs.first!
    let firstString = String(message.characters[firstRun.range])
    // firstString is "Thank you!"
    print(firstString)
}
```

### Attributed String Runs (Part 2) — [5:49]

```swift
func attributedStringRuns2() {
    let message = AttributedString(localized: "Thank you! _Please visit our [website](http://www.example.com)._")

    let linkRunCount = message.runs[\.link].count
    // linkRunCount is 3
    print(linkRunCount)

    var insecureLinks: [URL] = []
    for (value, range) in message.runs[\.link] {
        if let v = value, v.scheme != "https" {
            insecureLinks.append(v)
        }
    }
    // insecureLinks is [http://www.example.com]
    print(insecureLinks)
}
```

### Attributed String Mutation — [6:36]

```swift
func attributedStringMutation() {
    var message = AttributedString(localized: "Thank you! _Please visit our [website](http://www.example.com)._")

    if let range = message.range(of: "visit") {
        message[range].font = .body.italic().bold()
        message.characters.replaceSubrange(range, with: "surf")
    }

    print(message)
}
```

### Localized Strings — [7:29]

```swift
func prompt(for document: String) -> String {
    String(localized: "Would you like to save the document “\(document)”?")
}

func attributedPrompt(for document: String) -> AttributedString {
    AttributedString(localized: "Would you like to save the document “\(document)”?")
}
```

### Codable Attributed Strings — [9:34]

```swift
struct FoodItem: Codable {
    // Placeholder type to demonstrate concept
    var name: String
}

struct Receipt: Codable {
    var items: [FoodItem]
    var thankYouMessage: AttributedString
}

func codableBasics() {
    let message = AttributedString(localized: "Thank you! _Please visit our [website](http://www.example.com)._")
    let receipt = Receipt(items: [FoodItem(name: "Juice")], thankYouMessage: message)

    let encoded = try! JSONEncoder().encode(receipt)
    let decodedReceipt = try! JSONDecoder().decode(Receipt.self, from: encoded)

    print("\(decodedReceipt.thankYouMessage)")
}
```

### Markdown Decodable Attribute — [10:42]

```swift
enum RainbowAttribute : CodableAttributedStringKey, MarkdownDecodableAttributedStringKey {
    enum Value : String, Codable {
        case plain
        case fun
        case extreme
    }

    public static var name = "rainbow"
}
```

### Custom Markdown Syntax — [11:30]

```markdown
This text contains [a link](http://www.example.com).

This text contains ![an image](http://www.example.com/my_image.gif).

This text contains ^[an attribute](rainbow: 'extreme').
```

### Custom Markdown Attributes — [12:27]

```markdown
This text contains ^[an attribute](rainbow: 'extreme').

This text contains ^[two attributes](rainbow: 'extreme', otherValue: 42).

This text contains ^[an attribute with 2 properties](someStuff: {key: true, key2: false}).
```

### Attribute Scopes — [13:15]

```swift
extension AttributeScopes {
    struct CaffeAppAttributes : AttributeScope {
        let rainbow: RainbowAttribute

        let swiftUI: SwiftUIAttributes
    }

    var caffeApp: CaffeAppAttributes.Type { CaffeAppAttributes.self }
}

func customAttributesFromMarkdown() {
    let header = AttributedString(localized: "^[Fast & Delicious](rainbow: 'extreme') Food", including: \.caffeApp)

    print(header)
}
```

### Formatting Dates — [17:28]

```swift
func formattingDates() {
    // Note: This will use your current date & time plus current locale. Example output is for en_US locale.
    let date = Date.now

    let formatted = date.formatted()
    // example: "6/7/2021, 9:42 AM"
    print(formatted)

    let onlyDate = date.formatted(date: .numeric, time: .omitted)
    // example: "6/7/2021"
    print(onlyDate)

    let onlyTime = date.formatted(date: .omitted, time: .shortened)
    // example: "9:42 AM"
    print(onlyTime)
}
```

### Formatting Dates With Styles — [18:16]

```swift
func formattingDatesWithStyles() {
    // Note: This will use your current date & time plus current locale. Example output is for en_US locale.
    let date = Date.now

    let formatted = date.formatted(.dateTime)
    // example: "6/7/2021, 9:42 AM"
    print(formatted)
}
```

### Formatting Dates - More Examples — [18:36]

```swift
func formattingDatesMoreExamples() {
    // Note: This will use your current date & time plus current locale. Example output is for en_US locale.
    let date = Date.now

    let formatted = date.formatted(.dateTime.year().day().month())
    // example: "Jun 7, 2021"
    print(formatted)

    let formattedWide = date.formatted(.dateTime.year().day().month(.wide))
    // example: "June 7, 2021"
    print(formattedWide)

    let formattedWeekday = date.formatted(.dateTime.weekday(.wide))
    // example: "Monday"
    print(formattedWeekday)

    let logFormat = date.formatted(.iso8601)
    // example: "20210607T164200Z"
    print(logFormat)

    let fileNameFormat = date.formatted(.iso8601.year().month().day().dateSeparator(.dash))
    // example: "2021-06-07"
    print(fileNameFormat)
}
```

### Formatting Intervals — [20:30]

```swift
func formattingIntervals() {
    // Note: This will use your current date & time plus current locale. Example output is for en_US locale.
    let now = Date.now
    // Note on time calculations: This represents the absolute point in time 5000 seconds from now. For calculations that are in terms of hours, days, etc., please use Calendar API.
    let later = now + TimeInterval(5000)

    let range = (now..<later).formatted()
    // example: "6/7/21, 9:42 – 11:05 AM"
    print(range)

    let noDate = (now..<later).formatted(date: .omitted, time: .complete)
    // example: "9:42:00 AM PDT – 11:05:20 AM PDT"
    print(noDate)

    let timeDuration = (now..<later).formatted(.timeDuration)
    // example: "1:23:20"
    print(timeDuration)

    let components = (now..<later).formatted(.components(style: .wide))
    // example: "1 hour, 23 minutes, 20 seconds"
    print(components)

    let relative = later.formatted(.relative(presentation: .named, unitsStyle: .wide))
    // example: "in 1 hour"
    print(relative)
}
```

### Demo - SwiftUI and AttributedString — [21:39]

```swift
import SwiftUI

struct ContentView: View {
    @State var date = Date.now
    @Environment(\.locale) var locale

    var dateString : AttributedString {
        var str = date.formatted(.dateTime
                                    .minute()
                                    .hour()
                                    .weekday()
                                    .locale(locale)
                                    .attributed)

        let weekday = AttributeContainer
            .dateField(.weekday)

        let color = AttributeContainer
            .foregroundColor(.orange)

        str.replaceAttributes(weekday, with: color)

        return str
    }


    var body: some View {
        VStack {
            Text("Next free coffee")
            Text(dateString).font(.title2)
        }
        .multilineTextAlignment(.center)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .environment(\.locale, Locale(identifier: "en_US"))
        ContentView()
            .environment(\.locale, Locale(identifier: "he_IL"))
        ContentView()
            .environment(\.locale, Locale(identifier: "es_ES"))
    }
}
```

### Parsing Dates — [23:53]

```swift
func parsingDates() {
    let date = Date.now

    let format = Date.FormatStyle().year().day().month()
    let formatted = date.formatted(format)
    // example: "Jun 7, 2021"
    print(formatted)

    if let date = try? Date(formatted, strategy: format) {
        // example: 2021-06-07 07:00:00 +0000
        print(date)
    }
}
```

### Parsing Dates - Strategies — [24:23]

```swift
func parsingDatesStrategies() {
    let strategy = Date.ParseStrategy(
        format: "\(year: .defaultDigits)-\(month: .twoDigits)-\(day: .twoDigits)",
        timeZone: TimeZone.current)

    if let date = try? Date("2021-06-07", strategy: strategy) {
        // date is 2021-06-07 07:00:00 +0000
        print(date)
    }
}
```

### Formatting Numbers — [25:30]

```swift
func formattingNumbers() {
    // Note: This will use your current locale. Example output is for en_US locale.
    let value = 12345

    let formatted = value.formatted()
    // formatted is "12,345"
    print(formatted)
}
```

### Formatting Numbers With Styles — [25:36]

```swift
func formattingNumbersWithStyles() {
    // Note: This will use your current locale. Example output is for en_US locale.
    let percent = 25
    let percentFormatted = percent.formatted(.percent)
    // percentFormatted is "25%"
    print(percentFormatted)

    let scientific = 42e9
    let scientificFormatted = scientific.formatted(.number.notation(.scientific))
    // scientificFormatted is "4.2E10"
    print(scientificFormatted)

    let price = 29
    let priceFormatted = price.formatted(.currency(code: "usd"))
    // priceFormatted is "$29.00"
    print(priceFormatted)
}
```

### Formatting Lists — [25:47]

```swift
func formattingLists() {
    // Note: This will use your current locale. Example output is for en_US locale.
    let list = [25, 50, 75].formatted(.list(memberStyle: .percent, type: .or))
    // list is "25%, 50%, or 75%"
    print(list)
}
```

### Receipt Tip View — [26:05]

```swift
struct ReceiptTipView: View {
    @State var tip = 0.15

    var body: some View {
        HStack {
            Text("Tip")
            Spacer()
            TextField("Amount",
                      value: $tip,
                      format: .percent)
        }
    }
}
```

### Automatic Grammar Agreement — [29:41]

```swift
func addToOrderEnglish() {
    // Note: This will use your current locale. Example output is for en_US locale.
    let quantity = 2
    let size = "large"
    let food = "salad"

    let message = AttributedString(localized: "Add ^[\(quantity) \(size) \(food)](inflect: true) to your order")
    print(message)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10109/5/31B61A71-9D39-4F29-97DF-66309DBA320E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10109/5/31B61A71-9D39-4F29-97DF-66309DBA320E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10109) — developer.apple.com. Indexed for agent consumption._