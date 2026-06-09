---
id: "wwdc2022-110357"
event: "wwdc2022"
year: 2022
title: "Meet Swift Regex"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110357"
topics: ["Essentials", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet Swift Regex

**Event:** WWDC22 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-110357](https://developer.apple.com/videos/play/wwdc2022/110357)

Learn how you can process strings more effectively when you take advantage of Swift Regex. Come for concise literals but stay for Regex builders — a new, declarative approach to string processing. We'll also explore the Unicode models in String and share how Swift Regex can make Unicode-correct processing easy.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,090 words)

## Code Snippets

### Processing collections — [1:35]

```swift
let transaction = "DEBIT     03/05/2022    Doug's Dugout Dogs         $33.27"

let fragments = transaction.split(whereSeparator: \.isWhitespace)
// ["DEBIT", "03/05/2022", "Doug\'s", "Dugout", "Dogs", "$33.27"]
```

### Low-level index manipulation — [1:49]

```swift
var slice = transaction[...]

// Extract a field, advancing `slice` to the start of the next field
func extractField() -> Substring {
  let endIdx = {
    var start = slice.startIndex
    while true {
      // Position of next whitespace (including tabs)
      guard let spaceIdx = slice[start...].firstIndex(where: \.isWhitespace) else {
        return slice.endIndex
      }

      // Tab suffices
      if slice[spaceIdx] == "\t" {
        return spaceIdx
      }

      // Otherwise check for a second whitespace character
      let afterSpaceIdx = slice.index(after: spaceIdx)
      if afterSpaceIdx == slice.endIndex || slice[afterSpaceIdx].isWhitespace {
        return spaceIdx
      }

      // Skip over the single space and try again
      start = afterSpaceIdx
    }
  }()
  defer { slice = slice[endIdx...].drop(while: \.isWhitespace) }
  return slice[..<endIdx]
}

let kind = extractField()
let date = try Date(String(extractField()), strategy:  Date.FormatStyle(date: .numeric))
let account = extractField()
let amount = try Decimal(String(extractField()), format: .currency(code: "USD"))
```

### Regex literals — [2:47]

```swift
// Regex literals
let digits = /\d+/
// digits: Regex<Substring>
```

### Regex created at run-time — [3:20]

```swift
// Run-time construction
let runtimeString = #"\d+"#
let digits = try Regex(runtimeString)
// digits: Regex<AnyRegexOutput>
```

### Regex builder — [3:44]

```swift
// Regex builders
let digits = OneOrMore(.digit)
// digits: Regex<Substring>
```

### Split approach with a regex literal — [3:56]

```swift
let transaction = "DEBIT     03/05/2022    Doug's Dugout Dogs         $33.27"

let fragments = transaction.split(separator: /\s{2,}|\t/)
// ["DEBIT", "03/05/2022", "Doug's Dugout Dogs", "$33.27"]
```

### Normalize field separators — [4:36]

```swift
let transaction = "DEBIT     03/05/2022    Doug's Dugout Dogs         $33.27"

let normalized = transaction.replacing(/\s{2,}|\t/, with: "\t")
// DEBIT»03/05/2022»Doug's Dugout Dogs»$33.27
```

### Create a Regex builder — [6:55]

```swift
// CREDIT    03/02/2022    Payroll from employer         $200.23
// CREDIT    03/03/2022    Suspect A                     $2,000,000.00
// DEBIT     03/03/2022    Ted's Pet Rock Sanctuary      $2,000,000.00
// DEBIT     03/05/2022    Doug's Dugout Dogs            $33.27

import RegexBuilder
let fieldSeparator = /\s{2,}|\t/
let transactionMatcher = Regex {
  /CREDIT|DEBIT/
  fieldSeparator
  One(.date(.numeric, locale: Locale(identifier: "en_US"), timeZone: .gmt))
  fieldSeparator
  OneOrMore {
    NegativeLookahead { fieldSeparator }
    CharacterClass.any
  }
  fieldSeparator
  One(.localizedCurrency(code: "USD").locale(Locale(identifier: "en_US")))
}
```

### Use Captures to extract portions of input — [9:04]

```swift
let fieldSeparator = /\s{2,}|\t/
let transactionMatcher = Regex {
  Capture { /CREDIT|DEBIT/ }
  fieldSeparator

  Capture { One(.date(.numeric, locale: Locale(identifier: "en_US"), timeZone: .gmt)) }
  fieldSeparator

  Capture {
    OneOrMore {
      NegativeLookahead { fieldSeparator }
      CharacterClass.any
    }
  }
  fieldSeparator
  Capture { One(.localizedCurrency(code: "USD").locale(Locale(identifier: "en_US"))) }
}
// transactionMatcher: Regex<(Substring, Substring, Date, Substring, Decimal)>
```

### Plot twist! — [10:31]

```swift
private let ledger = """
KIND      DATE          INSTITUTION                AMOUNT
----------------------------------------------------------------
CREDIT    03/01/2022    Payroll from employer      $200.23
CREDIT    03/03/2022    Suspect A                  $2,000,000.00
DEBIT     03/03/2022    Ted's Pet Rock Sanctuary   $2,000,000.00
DEBIT     03/05/2022    Doug's Dugout Dogs         $33.27
DEBIT     06/03/2022    Oxford Comma Supply Ltd.   £57.33
"""
// 😱
```

### Use named captures — [10:53]

```swift
let regex = #/
  (?<date>     \d{2} / \d{2} / \d{4})
  (?<middle>   \P{currencySymbol}+)
  (?<currency> \p{currencySymbol})
/#
// Regex<(Substring, date: Substring, middle: Substring, currency: Substring)>
```

### Use Foundation's date parser — [11:33]

```swift
let regex = #/
  (?<date>     \d{2} / \d{2} / \d{4})
  (?<middle>   \P{currencySymbol}+)
  (?<currency> \p{currencySymbol})
/#
// Regex<(Substring, date: Substring, middle: Substring, currency: Substring)>

func pickStrategy(_ currency: Substring) -> Date.ParseStrategy {
  switch currency {
  case "$": return .date(.numeric, locale: Locale(identifier: "en_US"), timeZone: .gmt)
  case "£": return .date(.numeric, locale: Locale(identifier: "en_GB"), timeZone: .gmt)
  default: fatalError("We found another one!")
  }
}
```

### Find and replace — [11:48]

```swift
let regex = #/
  (?<date>     \d{2} / \d{2} / \d{4})
  (?<middle>   \P{currencySymbol}+)
  (?<currency> \p{currencySymbol})
/#
// Regex<(Substring, date: Substring, middle: Substring, currency: Substring)>

func pickStrategy(_ currency: Substring) -> Date.ParseStrategy { … }

ledger.replace(regex) { match -> String in
  let date = try! Date(String(match.date), strategy: pickStrategy(match.currency))

  // ISO 8601, it's the only way to be sure
  let newDate = date.formatted(.iso8601.year().month().day())

  return newDate + match.middle + match.currency
}
```

### A zombie love story — [12:45]

```swift
let aZombieLoveStory = "🧟‍♀️💖🧠"
// Characters: 🧟‍♀️, 💖, 🧠
```

### A zombie love story in unicode scalars — [13:01]

```swift
aZombieLoveStory.unicodeScalars
// Unicode scalar values: U+1F9DF, U+200D, U+2640, U+FE0F, U+1F496, U+1F9E0
```

### A zombie love story in UTF8 — [13:44]

```swift
aZombieLoveStory.utf8
// UTF-8 code units: F0 9F A7 9F E2 80 8D E2 99 80 EF B8 8F F0 9F 92 96 F0 9F A7 A0
```

### Unicode canonical equivalence — [14:12]

```swift
"café".elementsEqual("cafe\u{301}")
// true
```

### String's views are compared at binary level — [14:49]

```swift
"café".elementsEqual("cafe\u{301}")
// true

"café".unicodeScalars.elementsEqual("cafe\u{301}".unicodeScalars)
// false

"café".utf8.elementsEqual("cafe\u{301}".utf8)
// false
```

### Unicode processing — [15:14]

```swift
switch ("🧟‍♀️💖🧠", "The Brain Cafe\u{301}") {
case (/.\N{SPARKLING HEART}./, /.*café/.ignoresCase()):
  print("Oh no! 🧟‍♀️💖🧠, but 🧠💖☕️!")
default:
  print("No conflicts found")
}
```

### Complex scalar processing — [15:54]

```swift
let input = "Oh no! 🧟‍♀️💖🧠, but 🧠💖☕️!"

input.firstMatch(of: /.\N{SPARKLING HEART}./)
// 🧟‍♀️💖🧠

input.firstMatch(of: /.\N{SPARKLING HEART}./.matchingSemantics(.unicodeScalar))
// ️💖🧠
```

### Live transaction matcher — [17:56]

```swift
let timestamp = Regex { ... } // proprietary
let details = try Regex(inputString)
let amountMatcher = /[\d.]+/

// CREDIT    <proprietary>      <redacted>        200.23        A1B34EFF     ...
let fieldSeparator = /\s{2,}|\t/
let transactionMatcher = Regex {
  Capture { /CREDIT|DEBIT/ }
  fieldSeparator

  Capture { timestamp }
  fieldSeparator

  Capture { details }
  fieldSeparator

  // ...
}
```

### Replace field separator — [18:26]

```swift
let field = OneOrMore {
  NegativeLookahead { fieldSeparator }
  CharacterClass.any
}
```

### Use TryCapture — [18:55]

```swift
// CREDIT    <proprietary>      <redacted>        200.23        A1B34EFF     ...
let fieldSeparator = /\s{2,}|\t/
let field = OneOrMore {
  NegativeLookahead { fieldSeparator }
  CharacterClass.any
}
let transactionMatcher = Regex {
  Capture { /CREDIT|DEBIT/ }
  fieldSeparator

  TryCapture(field) { timestamp ~= $0 ? $0 : nil }
  fieldSeparator

  TryCapture(field) { details ~= $0 ? $0 : nil }
  fieldSeparator

  // ...
}
```

### Fixing the scaling issues — [21:45]

```swift
// CREDIT    <proprietary>      <redacted>        200.23        A1B34EFF     ...
let fieldSeparator = Local { /\s{2,}|\t/ } 
let field = OneOrMore {
  NegativeLookahead { fieldSeparator }
  CharacterClass.any
}
let transactionMatcher = Regex {
  Capture { /CREDIT|DEBIT/ }
  fieldSeparator

  TryCapture(field) { timestamp ~= $0 ? $0 : nil }
  fieldSeparator

  TryCapture(field) { details ~= $0 ? $0 : nil }
  fieldSeparator

  // ...
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110357/3/8FEA2DD3-43EE-44FB-A856-53169F90D683/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110357/3/8FEA2DD3-43EE-44FB-A856-53169F90D683/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110357) — developer.apple.com. Indexed for agent consumption._
