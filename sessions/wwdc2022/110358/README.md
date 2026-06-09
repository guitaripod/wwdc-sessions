---
id: "wwdc2022-110358"
event: "wwdc2022"
year: 2022
title: "Swift Regex: Beyond the basics"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110358"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Swift Regex: Beyond the basics

**Event:** WWDC22 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-110358](https://developer.apple.com/videos/play/wwdc2022/110358)

Go beyond the basics of string processing with Swift Regex. We'll share an overview of Regex and how it works, explore Foundation’s rich data parsers and discover how to integrate your own, and delve into captures. We’ll also provide best practices for matching strings and wielding Regex-powered algorithms with ease.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,833 words)

## Documentation & Resources

- [SE-0357: Regex-powered algorithms](https://github.com/apple/swift-evolution/blob/main/proposals/0357-regex-string-processing-algorithms.md) _guide_
- [SE-0355: Regex syntax](https://github.com/apple/swift-evolution/blob/main/proposals/0355-regex-syntax-run-time-construction.md) _guide_
- [SE-0354: Regex literals](https://github.com/apple/swift-evolution/blob/main/proposals/0354-regex-literals.md) _guide_
- [SE-0351: Regex builder DSL](https://github.com/apple/swift-evolution/blob/main/proposals/0351-regex-builder.md) _guide_
- [SE-0350: Regex type and overview](https://github.com/apple/swift-evolution/blob/main/proposals/0350-regex-type-overview.md) _guide_

## Code Snippets

### Regex matching "Hi, WWDC22!" — [0:39]

```swift
Regex {
    "Hi, WWDC"
    Repeat(.digit, count: 2)
    "!"
}
```

### Simple Regex from a string — [1:06]

```swift
let input = "name:  John Appleseed,  user_id:  100"

let regex = try Regex(#"user_id:\s*(\d+)"#)

if let match = input.firstMatch(of: regex) {
    print("Matched: \(match[0])")
    print("User ID: \(match[1])")
}
```

### Simple Regex from a literal — [1:56]

```swift
let input = "name:  John Appleseed,  user_id:  100"

let regex = /user_id:\s*(\d+)/

if let match = input.firstMatch(of: regex) {
    print("Matched: \(match.0)")
    print("User ID: \(match.1)")
}
```

### Simple regex builder — [2:08]

```swift
import RegexBuilder

let input = "name:  John Appleseed,  user_id:  100"

let regex = Regex {
    "user_id:"
    OneOrMore(.whitespace)
    Capture(.localizedInteger)
}

if let match = input.firstMatch(of: regex) {
    print("Matched: \(match.0)")
    print("User ID: \(match.1)")
}
```

### A trivial Regex interpreted by the Regex engine — [2:38]

```swift
let regex = Regex {
    OneOrMore("a")
    OneOrMore(.digit)
}

let match = "aaa12".wholeMatch(of: regex)
```

### Regex-powered algorithms — [3:49]

```swift
let input = "name:  John Appleseed,  user_id:  100"

let regex = /user_id:\s*(\d+)/

input.firstMatch(of: regex)           // Regex.Match<(Substring, Substring)>
input.wholeMatch(of: regex)           // nil
input.prefixMatch(of: regex)          // nil

input.starts(with: regex)             // false
input.replacing(regex, with: "456")   // "name:  John Appleseed,  456"
input.trimmingPrefix(regex)           // "name:  John Appleseed,  user_id:  100"
input.split(separator: /\s*,\s*/)     // ["name:  John Appleseed", "user_id:  100"]

switch "abc" {
case /\w+/:
    print("It's a word!")
}
```

### Use Foundation parsers in regex builder — [5:14]

```swift
let statement = """
    DSLIP    04/06/20 Paypal  $3,020.85
    CREDIT   04/03/20 Payroll $69.73
    DEBIT    04/02/20 Rent    ($38.25)
    DEBIT    03/31/20 Grocery ($27.44)
    DEBIT    03/24/20 IRS     ($52,249.98)
    """

let regex = Regex {
    Capture(.date(format: "\(month: .twoDigits)/\(day: .twoDigits)/\(year: .twoDigits)"))
    OneOrMore(.whitespace)
    OneOrMore(.word)
    OneOrMore(.whitespace)
    Capture(.currency(code: "USD").sign(strategy: .accounting))
}
```

### XCTest log regex (version 1) — [6:24]

```swift
import RegexBuilder

let regex = Regex {
    "Test Suite '"
    /[a-zA-Z][a-zA-Z0-9]*/
    "' "
    ChoiceOf {
        "started"
        "passed"
        "failed"
    }
    " at "
    OneOrMore(.any)
    Optionally(".")
}
```

### Test our Regex against some inputs — [6:25]

```swift
let testSuiteTestInputs = [
    "Test Suite 'RegexDSLTests' started at 2022-06-06 09:41:00.001",
    "Test Suite 'RegexDSLTests' failed at 2022-06-06 09:41:00.001.",
    "Test Suite 'RegexDSLTests' passed at 2022-06-06 09:41:00.001."
]

for line in testSuiteTestInputs {
    if let match = line.wholeMatch(of: regex) {
        print("Matched: \(match.output)")
    }
}
```

### Example of capture — [10:28]

```swift
let regex = Regex {
   "a"
   Capture("b")
   "c"
   /d(e)f/
}

if let match = "abcdef".wholeMatch(of: regex) {
    let (wholeMatch, b, e) = match.output
}
```

### XCTest log regex (version 2, with captures) — [11:10]

```swift
import RegexBuilder

let regex = Regex {
    "Test Suite '"
    Capture(/[a-zA-Z][a-zA-Z0-9]*/)
    "' "
    Capture {
        ChoiceOf {
            "started"
            "passed"
            "failed"
        }
    }
    " at "
    Capture(OneOrMore(.any))
    Optionally(".")
}
```

### Test our Regex (version 2) against some inputs — [11:21]

```swift
let testSuiteTestInputs = [
    "Test Suite 'RegexDSLTests' started at 2022-06-06 09:41:00.001",
    "Test Suite 'RegexDSLTests' failed at 2022-06-06 09:41:00.001.",
    "Test Suite 'RegexDSLTests' passed at 2022-06-06 09:41:00.001."
]

for line in testSuiteTestInputs {
    if let (whole, name, status, dateTime) = line.wholeMatch(of: regex)?.output {
        print("Matched: \"\(name)\", \"\(status)\", \"\(dateTime)\"")
    }
}
```

### XCTest log regex (version 3, with reluctant repetition) — [11:51]

```swift
import RegexBuilder

let regex = Regex {
    "Test Suite '"
    Capture(/[a-zA-Z][a-zA-Z0-9]*/)
    "' "
    Capture {
        ChoiceOf {
            "started"
            "passed"
            "failed"
        }
    }
    " at "
    Capture(OneOrMore(.any, .reluctant))
    Optionally(".")
}
```

### Example of transforming capture — [15:20]

```swift
Regex {
    Capture {
        OneOrMore(.digit)
    } transform: {
        Int($0)     // Int.init?(_: some StringProtocol)
    }
} // Regex<(Substring, Int?)>
```

### Example of transforming capture and removing optionality — [15:55]

```swift
Regex {
    TryCapture {
        OneOrMore(.digit)
    } transform: {
        Int($0)     // Int.init?(_: some StringProtocol)
    }
} // Regex<(Substring, Int)>
```

### XCTest log regex (version 4, with transforming capture) — [16:21]

```swift
enum TestStatus: String {
    case started = "started"
    case passed = "passed"
    case failed = "failed"
}

let regex = Regex {
    "Test Suite '"
    Capture(/[a-zA-Z][a-zA-Z0-9]*/)
    "' "
    TryCapture {
        ChoiceOf {
            "started"
            "passed"
            "failed"
        }
    } transform: {
        TestStatus(rawValue: String($0))
    }
    " at "
    Capture(OneOrMore(.any, .reluctant))
    Optionally(".")
} // Regex<(Substring, Substring, TestStatus, Substring)>
```

### XCTest log regex (version 5, with Foundation ISO 8601 date parser) — [17:23]

```swift
let regex = Regex {
    "Test Suite '"
    Capture(/[a-zA-Z][a-zA-Z0-9]*/)
    "' "
    TryCapture {
        ChoiceOf {
            "started"
            "passed"
            "failed"
        }
    } transform: {
        TestStatus(rawValue: String($0))
    }
    " at "
    Capture(.iso8601(
        timeZone: .current, includingFractionalSeconds: true, dateTimeSeparator: .space))
    Optionally(".")
} // Regex<(Substring, Substring, TestStatus, Date)>
```

### XCTest log duration parser — [18:19]

```swift
let input = "Test Case '-[RegexDSLTests testCharacterClass]' passed (0.001 seconds)."

let regex = Regex {
    "Test Case "
    OneOrMore(.any, .reluctant)
    "("
    Capture {
        .localizedDouble
    }
    " seconds)."
}

if let match = input.wholeMatch(of: regex) {
    print("Time: \(match.output)")
}
```

### CDoubleParser definition — [19:16]

```swift
import Darwin

struct CDoubleParser: CustomConsumingRegexComponent {
    typealias RegexOutput = Double

    func consuming(
        _ input: String, startingAt index: String.Index, in bounds: Range<String.Index>
    ) throws -> (upperBound: String.Index, output: Double)? {
        input[index...].withCString { startAddress in
            var endAddress: UnsafeMutablePointer<CChar>!
            let output = strtod(startAddress, &endAddress)
            guard endAddress > startAddress else { return nil }
            let parsedLength = startAddress.distance(to: endAddress)
            let upperBound = input.utf8.index(index, offsetBy: parsedLength)
            return (upperBound, output)
        }
    }
}
```

### Use CDoubleParser in regex builder — [20:13]

```swift
let input = "Test Case '-[RegexDSLTests testCharacterClass]' passed (0.001 seconds)."

let regex = Regex {
    "Test Case "
    OneOrMore(.any, .reluctant)
    "("
    Capture {
        CDoubleParser()
    }
    " seconds)."
} // Regex<(Substring, Double)>

if let match = input.wholeMatch(of: regex) {
    print("Time: \(match.1)")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110358/6/CCCFE7E0-48F7-4D00-A8C1-6DB5E768F833/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110358/6/CCCFE7E0-48F7-4D00-A8C1-6DB5E768F833/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110358) — developer.apple.com. Indexed for agent consumption._