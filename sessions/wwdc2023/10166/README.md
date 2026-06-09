---
id: "wwdc2023-10166"
event: "wwdc2023"
year: 2023
title: "Write Swift macros"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10166"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Write Swift macros

**Event:** WWDC23 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10166](https://developer.apple.com/videos/play/wwdc2023/10166)

Discover how you can use Swift macros to make your codebase more expressive and easier to read. Code along as we explore how macros can help you avoid writing repetitive code and find out how to use them in your app. We’ll share the building blocks of a macro, show you how to test it, and take you through how you can emit compilation errors from macros.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,103 words)

## Code Snippets

### Invocation of the stringify macro — [5:55]

```swift
import WWDC

let a = 17
let b = 25

let (result, code) = #stringify(a + b)

print("The value \(result) was produced by the code \"\(code)\"")
```

### Declaration of the stringify macro — [6:31]

```swift
@freestanding(expression)
public macro stringify<T>(_ value: T) -> (T, String) = #externalMacro(module: "WWDCMacros", type: "StringifyMacro")
```

### Implementation of the stringify macro — [7:10]

```swift
public struct StringifyMacro: ExpressionMacro {
    public static func expansion(
        of node: some FreestandingMacroExpansionSyntax,
        in context: some MacroExpansionContext
    ) -> ExprSyntax {
        guard let argument = node.argumentList.first?.expression else {
            fatalError("compiler bug: the macro does not have any arguments")
        }

        return "(\(argument), \(literal: argument.description))"
    }
}
```

### Tests for the stringify Macro — [9:12]

```swift
final class WWDCTests: XCTestCase {
    func testMacro() {
        assertMacroExpansion(
            """
            #stringify(a + b)
            """,
            expandedSource: """
            (a + b, "a + b")
            """,
            macros: testMacros
        )
    }
}

let testMacros: [String: Macro.Type] = [
    "stringify": StringifyMacro.self
]
```

### Slope and EasySlope — [12:05]

```swift
/// Slopes in my favorite ski resort.
enum Slope {
    case beginnersParadise
    case practiceRun
    case livingRoom
    case olympicRun
    case blackBeauty
}

/// Slopes suitable for beginners. Subset of `Slopes`.
enum EasySlope {
    case beginnersParadise
    case practiceRun

    init?(_ slope: Slope) {
        switch slope {
        case .beginnersParadise: self = .beginnersParadise
        case .practiceRun: self = .practiceRun
        default: return nil
        }
    }

    var slope: Slope {
        switch self {
        case .beginnersParadise: return .beginnersParadise
        case .practiceRun: return .practiceRun
        }
    }
}
```

### Declare SlopeSubset — [14:16]

```swift
/// Defines a subset of the `Slope` enum
///
/// Generates two members:
///  - An initializer that converts a `Slope` to this type if the slope is
///    declared in this subset, otherwise returns `nil`
///  - A computed property `slope` to convert this type to a `Slope`
///
/// - Important: All enum cases declared in this macro must also exist in the
///              `Slope` enum.
@attached(member, names: named(init))
public macro SlopeSubset() = #externalMacro(module: "WWDCMacros", type: "SlopeSubsetMacro")
```

### Write empty implementation for SlopeSubset — [15:24]

```swift
/// Implementation of the `SlopeSubset` macro.
public struct SlopeSubsetMacro: MemberMacro {
    public static func expansion(
        of attribute: AttributeSyntax,
        providingMembersOf declaration: some DeclGroupSyntax,
        in context: some MacroExpansionContext
    ) throws -> [DeclSyntax] {
        return []
    }
}
```

### Register SlopeSubsetMacro in the compiler plugin — [16:23]

```swift
@main
struct WWDCPlugin: CompilerPlugin {
    let providingMacros: [Macro.Type] = [
        SlopeSubsetMacro.self
    ]
}
```

### Test SlopeSubset — [18:41]

```swift
let testMacros: [String: Macro.Type] = [
    "SlopeSubset" : SlopeSubsetMacro.self,
]

final class WWDCTests: XCTestCase {
    func testSlopeSubset() {
        assertMacroExpansion(
            """
            @SlopeSubset
            enum EasySlope {
                case beginnersParadise
                case practiceRun
            }
            """, 
            expandedSource: """

            enum EasySlope {
                case beginnersParadise
                case practiceRun
                init?(_ slope: Slope) {
                    switch slope {
                    case .beginnersParadise:
                        self = .beginnersParadise
                    case .practiceRun:
                        self = .practiceRun
                    default:
                        return nil
                    }
                }
            }
            """, 
            macros: testMacros
        )
    }
}
```

### Cast declaration to an enum declaration — [19:25]

```swift
guard let enumDecl = declaration.as(EnumDeclSyntax.self) else {
    // TODO: Emit an error here
    return []
}
```

### Extract enum members — [21:14]

```swift
let members = enumDecl.memberBlock.members
```

### Load enum cases — [21:32]

```swift
let caseDecls = members.compactMap { $0.decl.as(EnumCaseDeclSyntax.self) }
```

### Retrieve enum elements — [21:58]

```swift
let elements = caseDecls.flatMap { $0.elements }
```

### Generate initializer — [24:11]

```swift
let initializer = try InitializerDeclSyntax("init?(_ slope: Slope)") {
    try SwitchExprSyntax("switch slope") {
        for element in elements {
            SwitchCaseSyntax(
                """
                case .\(element.identifier):
                    self = .\(element.identifier)
                """
            )
        }
        SwitchCaseSyntax("default: return nil")
    }
}
```

### Return generated initializer — [24:19]

```swift
return [DeclSyntax(initializer)]
```

### Apply SlopeSubset to EasySlope — [25:51]

```swift
/// Slopes suitable for beginners. Subset of `Slopes`.
@SlopeSubset
enum EasySlope {
    case beginnersParadise
    case practiceRun

    var slope: Slope {
        switch self {
        case .beginnersParadise: return .beginnersParadise
        case .practiceRun: return .practiceRun
        }
    }
}
```

### Test that we generate an error when applying SlopeSubset to a struct — [28:00]

```swift
func testSlopeSubsetOnStruct() throws {
    assertMacroExpansion(
        """
        @SlopeSubset
        struct Skier {
        }
        """,
        expandedSource: """

        struct Skier {
        }
        """,
        diagnostics: [
            DiagnosticSpec(message: "@SlopeSubset can only be applied to an enum", line: 1, column: 1)
        ],
        macros: testMacros
    )
}
```

### Define error to emit when SlopeSubset is applied to a non-enum type — [28:48]

```swift
enum SlopeSubsetError: CustomStringConvertible, Error {
    case onlyApplicableToEnum

    var description: String {
        switch self {
        case .onlyApplicableToEnum: return "@SlopeSubset can only be applied to an enum"
        }
    }
}
```

### Throw error if SlopeSubset is applied to a non-enum type — [29:09]

```swift
throw SlopeSubsetError.onlyApplicableToEnum
```

### Generalize SlopeSubset declaration to EnumSubset — [31:03]

```swift
@attached(member, names: named(init))
public macro EnumSubset<Superset>() = #externalMacro(module: "WWDCMacros", type: "SlopeSubsetMacro")
```

### Retrieve the generic parameter of EnumSubset — [31:33]

```swift
guard let supersetType = attribute
    .attributeName.as(SimpleTypeIdentifierSyntax.self)?
    .genericArgumentClause?
    .arguments.first?
    .argumentType else {
    // TODO: Handle error
    return []
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10166/5/58425163-99DA-4506-A86E-A2D794244136/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10166/5/58425163-99DA-4506-A86E-A2D794244136/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10166) — developer.apple.com. Indexed for agent consumption._