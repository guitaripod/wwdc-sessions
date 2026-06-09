---
id: "wwdc2023-10167"
event: "wwdc2023"
year: 2023
title: "Expand on Swift macros"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10167"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Expand on Swift macros

**Event:** WWDC23 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10167](https://developer.apple.com/videos/play/wwdc2023/10167)

Discover how Swift macros can help you reduce boilerplate in your codebase and adopt complex features more easily. Learn how macros can analyze code, emit rich compiler errors to guide developers towards correct usage, and generate new code that is automatically incorporated back into your project. We’ll also take you through important concepts like macro roles, compiler plugins, and syntax trees.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(6,782 words)

## Code Snippets

### The #unwrap expression macro, with a more complicated argument — [0:44]

```swift
let image = #unwrap(request.downloadedImage, message: "was already checked")

            // Begin expansion for "#unwrap"
            { [wrappedValue = request.downloadedImage] in
                guard let wrappedValue else {
                    preconditionFailure(
                        "Unexpectedly found nil: ‘request.downloadedImage’ " + 
                            "was already checked",
                        file: "main/ImageLoader.swift",
                        line: 42
                    )
                }
                return wrappedValue
            }()
            // End expansion for "#unwrap"
```

### Existing features using expansions (1) — [0:50]

```swift
struct Smoothie: Codable {
    var id, title, description: String
    var measuredIngredients: [MeasuredIngredient]

    static let berryBlue =
        Smoothie(id: "berry-blue", title: "Berry Blue") {
            """
            Filling and refreshing, this smoothie \
            will fill you with joy!
            """

            Ingredient.orange
                .measured(with: .cups).scaled(by: 1.5)
            Ingredient.blueberry
                .measured(with: .cups)
            Ingredient.avocado
                .measured(with: .cups).scaled(by: 0.2)
        }
}
```

### Existing features using expansions (2) — [1:11]

```swift
struct Smoothie: Codable {
    var id, title, description: String
    var measuredIngredients: [MeasuredIngredient]

        // Begin expansion for Codable
        private enum CodingKeys: String, CodingKey {
            case id, title, description,
                 measuredIngredients
        }

        init(from decoder: Decoder) throws { … }

        func encode(to encoder Encoder) throws { … }
        // End expansion for Codable

    static let berryBlue =
        Smoothie(id: "berry-blue", title: "Berry Blue") {
            """
            Filling and refreshing, this smoothie \
            will fill you with joy!
            """

            Ingredient.orange
                .measured(with: .cups).scaled(by: 1.5)
            Ingredient.blueberry
                .measured(with: .cups)
            Ingredient.avocado
                .measured(with: .cups).scaled(by: 0.2)
        }
}
```

### Macros inputs are complete, type-checked, and validated — [3:16]

```swift
#unwrap(1 + )    // error: expected expression after operator




@AddCompletionHandler(parameterName: 42)    // error: cannot convert argument of type 'Int' to expected type 'String'
func sendRequest() async throws -> Response




@DictionaryStorage class Options { … }    // error: '@DictionaryStorage' can only be applied to a 'struct'
```

### Macro expansions are inserted in predictable ways — [3:45]

```swift
func doThingy() {
    startDoingThingy()

    #someUnknownMacro()

    finishDoingThingy()
}
```

### How macros work, featuring #stringify — [4:51]

```swift
func printAdd(_ a: Int, _ b: Int) {
    let (result, str) = #stringify(a + b)

        // Begin expansion for "#stringify"
        (a + b, "a + b")
        // End expansion for "#stringify"

    print("\(str) = \(result)")
}

printAdd(1, 2)    // prints "a + b = 3"
```

### Macro declaration for #stringify — [5:43]

```swift
/// Creates a tuple containing both the result of `expr` and its source code represented as a
/// `String`.
@freestanding(expression)
macro stringify<T>(_ expr: T) -> (T, String)
```

### What’s an expression? — [7:11]

```swift
let numPixels = (x + width) * (y + height)
//              ^~~~~~~~~~~~~~~~~~~~~~~~~~ This is an expression
//               ^~~~~~~~~                 But so is this
//                   ^~~~~                 And this
```

### The #unwrap expression macro: motivation — [7:34]

```swift
// Some teams are nervous about this:
let image = downloadedImage!

// Alternatives are super wordy:
guard let image = downloadedImage else {
    preconditionFailure("Unexpectedly found nil: downloadedImage was already checked")
}
```

### The #unwrap expression macro: macro declaration — [8:03]

```swift
/// Force-unwraps the optional value passed to `expr`.
/// - Parameter message: Failure message, followed by `expr` in single quotes
@freestanding(expression)
macro unwrap<Wrapped>(_ expr: Wrapped?, message: String) -> Wrapped
```

### The #unwrap expression macro: usage — [8:21]

```swift
let image = #unwrap(downloadedImage, message: "was already checked")

            // Begin expansion for "#unwrap"
            { [downloadedImage] in
                guard let downloadedImage else {
                    preconditionFailure(
                        "Unexpectedly found nil: ‘downloadedImage’ " + "was already checked",
                        file: "main/ImageLoader.swift",
                        line: 42
                    )
                }
                return downloadedImage
            }()
            // End expansion for "#unwrap"
```

### The #makeArrayND declaration macro: motivation — [9:09]

```swift
public struct Array2D<Element>: Collection {
    public struct Index: Hashable, Comparable { var storageIndex: Int }

    var storage: [Element]
    var width1: Int

    public func makeIndex(_ i0: Int, _ i1: Int) -> Index {
        Index(storageIndex: i0 * width1 + i1)
    }

    public subscript (_ i0: Int, _ i1: Int) -> Element {
        get { self[makeIndex(i0, i1)] }
        set { self[makeIndex(i0, i1)] = newValue }
    }

    public subscript (_ i: Index) -> Element {
        get { storage[i.storageIndex] }
        set { storage[i.storageIndex] = newValue }
    }

    // Note: Omitted additional members needed for 'Collection' conformance
}

public struct Array3D<Element>: Collection {
    public struct Index: Hashable, Comparable { var storageIndex: Int }

    var storage: [Element]
    var width1, width2: Int

    public func makeIndex(_ i0: Int, _ i1: Int, _ i2: Int) -> Index {
        Index(storageIndex: (i0 * width1 + i1) * width2 + i2)
    }

    public subscript (_ i0: Int, _ i1: Int, _ i2: Int) -> Element {
        get { self[makeIndex(i0, i1, i2)] }
        set { self[makeIndex(i0, i1, i2)] = newValue }
    }

    public subscript (_ i: Index) -> Element {
        get { storage[i.storageIndex] }
        set { storage[i.storageIndex] = newValue }
    }

    // Note: Omitted additional members needed for 'Collection' conformance
}
```

### The #makeArrayND declaration macro: macro declaration — [10:03]

```swift
/// Declares an `n`-dimensional array type named `Array<n>D`.
/// - Parameter n: The number of dimensions in the array.
@freestanding(declaration, names: arbitrary)
macro makeArrayND(n: Int)
```

### The #makeArrayND declaration macro: usage — [10:15]

```swift
#makeArrayND(n: 2)

// Begin expansion for "#makeArrayND"
public struct Array2D<Element>: Collection {
    public struct Index: Hashable, Comparable { var storageIndex: Int }
    var storage: [Element]
    var width1: Int
    public func makeIndex(_ i0: Int, _ i1: Int) -> Index {
        Index(storageIndex: i0 * width1 + i1)
    }
    public subscript (_ i0: Int, _ i1: Int) -> Element {
        get { self[makeIndex(i0, i1)] }
        set { self[makeIndex(i0, i1)] = newValue }
    }
    public subscript (_ i: Index) -> Element {
        get { storage[i.storageIndex] }
        set { storage[i.storageIndex] = newValue }
    }
}
// End expansion for "#makeArrayND"

#makeArrayND(n: 3)
#makeArrayND(n: 4)
#makeArrayND(n: 5)
```

### The @AddCompletionHandler peer macro: motivation — [11:23]

```swift
/// Fetch the avatar for the user with `username`.
func fetchAvatar(_ username: String) async -> Image? {
    ...
}

func fetchAvatar(_ username: String, onCompletion: @escaping (Image?) -> Void) {
    Task.detached { onCompletion(await fetchAvatar(username)) }
}
```

### The @AddCompletionHandler peer macro: macro declaration — [11:51]

```swift
/// Overload an `async` function to add a variant that takes a completion handler closure as
/// a parameter.
@attached(peer, names: overloaded)
macro AddCompletionHandler(parameterName: String = "completionHandler")
```

### The @AddCompletionHandler peer macro: usage — [11:59]

```swift
/// Fetch the avatar for the user with `username`.
@AddCompletionHandler(parameterName: "onCompletion")
func fetchAvatar(_ username: String) async -> Image? {
    ...
}

    // Begin expansion for "@AddCompletionHandler"

    /// Fetch the avatar for the user with `username`.
    /// Equivalent to ``fetchAvatar(username:)`` with
    /// a completion handler.
    func fetchAvatar(
        _ username: String,
        onCompletion: @escaping (Image?) -> Void
    ) {
        Task.detached {
            onCompletion(await fetchAvatar(username))
        }
    }

    // End expansion for "@AddCompletionHandler"
```

### The @DictionaryStorage accessor macro: motivation — [12:36]

```swift
struct Person: DictionaryRepresentable {
    init(dictionary: [String: Any]) { self.dictionary = dictionary }
    var dictionary: [String: Any]

    var name: String {
        get { dictionary["name"]! as! String }
        set { dictionary["name"] = newValue }
    }
    var height: Measurement<UnitLength> {
        get { dictionary["height"]! as! Measurement<UnitLength> }
        set { dictionary["height"] = newValue }
    }
    var birthDate: Date? {
        get { dictionary["birth_date"] as! Date? }
        set { dictionary["birth_date"] = newValue as Any? }
    }
}
```

### The @DictionaryStorage accessor macro: declaration — [13:04]

```swift
/// Adds accessors to get and set the value of the specified property in a dictionary
/// property called `storage`.
@attached(accessor)
macro DictionaryStorage(key: String? = nil)
```

### The @DictionaryStorage accessor macro: usage — [13:20]

```swift
struct Person: DictionaryRepresentable {
    init(dictionary: [String: Any]) { self.dictionary = dictionary }
    var dictionary: [String: Any]

    @DictionaryStorage var name: String
        // Begin expansion for "@DictionaryStorage"
        {
            get { dictionary["name"]! as! String }
            set { dictionary["name"] = newValue }
        }
        // End expansion for "@DictionaryStorage"

    @DictionaryStorage var height: Measurement<UnitLength>
        // Begin expansion for "@DictionaryStorage"
        {
            get { dictionary["height"]! as! Measurement<UnitLength> }
            set { dictionary["height"] = newValue }
        }
        // End expansion for "@DictionaryStorage"

    @DictionaryStorage(key: "birth_date") var birthDate: Date?
        // Begin expansion for "@DictionaryStorage"
        {
            get { dictionary["birth_date"] as! Date? }
            set { dictionary["birth_date"] = newValue as Any? }
        }
        // End expansion for "@DictionaryStorage"
}
```

### The @DictionaryStorage member attribute macro: macro declaration — [13:56]

```swift
/// Adds accessors to get and set the value of the specified property in a dictionary
/// property called `storage`.
@attached(memberAttribute)
@attached(accessor)
macro DictionaryStorage(key: String? = nil)
```

### The @DictionaryStorage member attribute macro: usage — [14:46]

```swift
@DictionaryStorage
struct Person: DictionaryRepresentable {
    init(dictionary: [String: Any]) { self.dictionary = dictionary }
    var dictionary: [String: Any]

        // Begin expansion for "@DictionaryStorage"
        @DictionaryStorage
        // End expansion for "@DictionaryStorage"
    var name: String

        // Begin expansion for "@DictionaryStorage"
        @DictionaryStorage
        // End expansion for "@DictionaryStorage"
    var height: Measurement<UnitLength>

    @DictionaryStorage(key: "birth_date") var birthDate: Date?
}
```

### The @DictionaryStorage member macro: macro definition — [15:52]

```swift
/// Adds accessors to get and set the value of the specified property in a dictionary
/// property called `storage`.
@attached(member, names: named(dictionary), named(init(dictionary:)))
@attached(memberAttribute)
@attached(accessor)
macro DictionaryStorage(key: String? = nil)
```

### The @DictionaryStorage member macro: usage — [16:26]

```swift
// The @DictionaryStorage member macro

@DictionaryStorage struct Person: DictionaryRepresentable {
        // Begin expansion for "@DictionaryStorage"
        init(dictionary: [String: Any]) {
            self.dictionary = dictionary
        }
        var dictionary: [String: Any]
        // End expansion for "@DictionaryStorage"

    var name: String
    var height: Measurement<UnitLength>
    @DictionaryStorage(key: "birth_date") var birthDate: Date?
}
```

### The @DictionaryStorage conformance macro: macro definition — [16:59]

```swift
/// Adds accessors to get and set the value of the specified property in a dictionary
/// property called `storage`.
@attached(conformance)
@attached(member, names: named(dictionary), named(init(dictionary:)))
@attached(memberAttribute)
@attached(accessor)
macro DictionaryStorage(key: String? = nil)
```

### The @DictionaryStorage conformance macro: usage — [17:09]

```swift
struct Person
        // Begin expansion for "@DictionaryStorage"
        : DictionaryRepresentable
        // End expansion for "@DictionaryStorage"
{
    var name: String
    var height: Measurement<UnitLength>
    @DictionaryStorage(key: "birth_date") var birthDate: Date?
}
```

### @DictionaryStorage starting point — [17:28]

```swift
struct Person: DictionaryRepresentable {
    init(dictionary: [String: Any]) { self.dictionary = dictionary }
    var dictionary: [String: Any]

    var name: String {
        get { dictionary["name"]! as! String }
        set { dictionary["name"] = newValue }
    }
    var height: Measurement<UnitLength> {
        get { dictionary["height"]! as! Measurement<UnitLength> }
        set { dictionary["height"] = newValue }
    }
    var birthDate: Date? {
        get { dictionary["birth_date"] as! Date? }
        set { dictionary["birth_date"] = newValue as Any? }
    }
}
```

### @DictionaryStorage ending point — [17:32]

```swift
@DictionaryStorage
struct Person
        // Begin expansion for "@DictionaryStorage"
        : DictionaryRepresentable
        // End expansion for "@DictionaryStorage"
{
        // Begin expansion for "@DictionaryStorage"
        init(dictionary: [String: Any]) { self.dictionary = dictionary }
        var dictionary: [String: Any]
        // End expansion for "@DictionaryStorage"

        // Begin expansion for "@DictionaryStorage"
        @DictionaryStorage
        // End expansion for "@DictionaryStorage"
    var name: String
        // Begin expansion for "@DictionaryStorage"
        {
            get { dictionary["name"]! as! String }
            set { dictionary["name"] = newValue }
        }
        // End expansion for "@DictionaryStorage"

        // Begin expansion for "@DictionaryStorage"
        @DictionaryStorage
        // End expansion for "@DictionaryStorage"
    var height: Measurement<UnitLength>
        // Begin expansion for "@DictionaryStorage"
        {
            get { dictionary["height"]! as! Measurement<UnitLength> }
            set { dictionary["height"] = newValue }
        }
        // End expansion for "@DictionaryStorage"

    @DictionaryStorage(key: "birth_date")
    var birthDate: Date?
        // Begin expansion for "@DictionaryStorage"
        {
            get { dictionary["birth_date"] as! Date? }
            set { dictionary["birth_date"] = newValue as Any? }
        }
        // End expansion for "@DictionaryStorage"
}
```

### @DictionaryStorage ending point (without expansions) — [17:35]

```swift
@DictionaryStorage
struct Person {
    var name: String
    var height: Measurement<UnitLength>

    @DictionaryStorage(key: "birth_date")
    var birthDate: Date?
}
```

### Macro implementations — [18:01]

```swift
/// Creates a tuple containing both the result of `expr` and its source code represented as a
/// `String`.
@freestanding(expression)
macro stringify<T>(_ expr: T) -> (T, String) = #externalMacro(
                                                   module: "MyLibMacros",
                                                   type: "StringifyMacro"
                                               )
```

### Implementing @DictionaryStorage’s @attached(member) role (1) — [19:18]

```swift
import SwiftSyntax
import SwiftSyntaxMacros
import SwiftSyntaxBuilder

struct DictionaryStorageMacro: MemberMacro {
    static func expansion(
        of attribute: AttributeSyntax,
        providingMembersOf declaration: some DeclGroupSyntax,
        in context: some MacroExpansionContext
    ) throws -> [DeclSyntax] {
        return [
           "init(dictionary: [String: Any]) { self.dictionary = dictionary }",
           "var dictionary: [String: Any]"
        ]
    }
}
```

### Code used to demonstrate SwiftSyntax trees — [19:52]

```swift
@DictionaryStorage
struct Person {
    var name: String
    var height: Measurement<UnitLength>
    @DictionaryStorage(key: "birth_date")
    var birthDate: Date?
}
```

### Implementing @DictionaryStorage’s @attached(member) role (2) — [22:00]

```swift
import SwiftSyntax
import SwiftSyntaxMacros
import SwiftSyntaxBuilder

struct DictionaryStorageMacro: MemberMacro {
    static func expansion(
        of attribute: AttributeSyntax,
        providingMembersOf declaration: some DeclGroupSyntax,
        in context: some MacroExpansionContext
    ) throws -> [DeclSyntax] {
        return [
           "init(dictionary: [String: Any]) { self.dictionary = dictionary }",
           "var dictionary: [String: Any]"
        ]
    }
}
```

### A type that @DictionaryStorage isn’t compatible with — [24:29]

```swift
@DictionaryStorage
enum Gender {
    case other(String)
    case female
    case male

        // Begin expansion for "@DictionaryStorage"
        init(dictionary: [String: Any]) { self.dictionary = dictionary }
        var dictionary: [String: Any]
        // End expansion for "@DictionaryStorage"
}
```

### Expansion method with error checking — [25:17]

```swift
import SwiftSyntax
import SwiftSyntaxMacros
import SwiftSyntaxBuilder

struct DictionaryStorageMacro: MemberMacro {
    static func expansion(
        of attribute: AttributeSyntax,
        providingMembersOf declaration: some DeclGroupSyntax,
        in context: some MacroExpansionContext
    ) throws -> [DeclSyntax] {
        guard declaration.is(StructDeclSyntax.self) else {
            let structError = Diagnostic(
                node: attribute,
                message: MyLibDiagnostic.notAStruct
            )
            context.diagnose(structError)
            return []
        }
        return [
            "init(dictionary: [String: Any]) { self.dictionary = dictionary }",
            "var dictionary: [String: Any]"
        ]
    }
}

enum MyLibDiagnostic: String, DiagnosticMessage {
    case notAStruct

    var severity: DiagnosticSeverity { return .error }

    var message: String {
        switch self {
        case .notAStruct:
            return "'@DictionaryStorage' can only be applied to a 'struct'"
        }
    }

    var diagnosticID: MessageID {
        MessageID(domain: "MyLibMacros", id: rawValue)
    }
}
```

### Parameter list for `ArrayND.makeIndex` — [29:32]

```swift
FunctionParameterListSyntax {
    for dimension in 0 ..< numDimensions {
        FunctionParameterSyntax(
            firstName: .wildcardToken(),
            secondName: .identifier("i\(dimension)"),
            type: TypeSyntax("Int")
        )
    }
}
```

### The #unwrap expression macro: revisited — [30:17]

```swift
let image = #unwrap(downloadedImage, message: "was already checked")

            // Begin expansion for "#unwrap"
            { [downloadedImage] in
                guard let downloadedImage else {
                    preconditionFailure(
                        "Unexpectedly found nil: ‘downloadedImage’ " + "was already checked",
                        file: "main/ImageLoader.swift",
                        line: 42
                    )
                }
                return downloadedImage
            }()
            // End expansion for "#unwrap"
```

### Implementing the #unwrap expression macro: start — [30:38]

```swift
static func makeGuardStmt() -> StmtSyntax {
    return """
        guard let downloadedImage else {
            preconditionFailure(
                "Unexpectedly found nil: ‘downloadedImage’ " + "was already checked",
                file: "main/ImageLoader.swift",
                line: 42
            )
        }
    """
}
```

### Implementing the #unwrap expression macro: the message string — [30:57]

```swift
static func makeGuardStmt(message: ExprSyntax) -> StmtSyntax {
    return """
        guard let downloadedImage else {
            preconditionFailure(
                "Unexpectedly found nil: ‘downloadedImage’ " + \(message),
                file: "main/ImageLoader.swift",
                line: 42
            )
        }
    """
}
```

### Implementing the #unwrap expression macro: the variable name — [31:21]

```swift
static func makeGuardStmt(wrapped: TokenSyntax, message: ExprSyntax) -> StmtSyntax {
    return """
        guard let \(wrapped) else {
            preconditionFailure(
                "Unexpectedly found nil: ‘downloadedImage’ " + \(message),
                file: "main/ImageLoader.swift",
                line: 42
            )
        }
    """
}
```

### Implementing the #unwrap expression macro: interpolating a string as a literal — [31:44]

```swift
static func makeGuardStmt(wrapped: TokenSyntax, message: ExprSyntax) -> StmtSyntax {
    let messagePrefix = "Unexpectedly found nil: ‘downloadedImage’ "

    return """
        guard let \(wrapped) else {
            preconditionFailure(
                \(literal: messagePrefix) + \(message),
                file: "main/ImageLoader.swift",
                line: 42
            )
        }
    """
}
```

### Implementing the #unwrap expression macro: adding an expression as a string — [32:11]

```swift
static func makeGuardStmt(wrapped: TokenSyntax,
                           originalWrapped: ExprSyntax,
                           message: ExprSyntax) -> StmtSyntax {
    let messagePrefix = "Unexpectedly found nil: ‘\(originalWrapped.description)’ "

    return """
        guard let \(wrapped) else {
            preconditionFailure(
                \(literal: messagePrefix) + \(message),
                file: "main/ImageLoader.swift",
                line: 42
            )
        }
    """
}
```

### Implementing the #unwrap expression macro: inserting the file and line numbers — [33:00]

```swift
static func makeGuardStmt(wrapped: TokenSyntax,
                           originalWrapped: ExprSyntax,
                           message: ExprSyntax,
                           in context: some MacroExpansionContext) -> StmtSyntax {
    let messagePrefix = "Unexpectedly found nil: ‘\(originalWrapped.description)’ "
    let originalLoc = context.location(of: originalWrapped)!

    return """
        guard let \(wrapped) else {
            preconditionFailure(
                \(literal: messagePrefix) + \(message),
                file: \(originalLoc.file),
                line: \(originalLoc.line)
            )
        }
    """
}
```

### The #unwrap expression macro, with a name conflict — [34:05]

```swift
let wrappedValue = "🎁"
let image = #unwrap(request.downloadedImage, message: "was \(wrappedValue)")

            // Begin expansion for "#unwrap"
            { [wrappedValue = request.downloadedImage] in
                guard let wrappedValue else {
                    preconditionFailure(
                        "Unexpectedly found nil: ‘request.downloadedImage’ " +
                            "was \(wrappedValue)",
                        file: "main/ImageLoader.swift",
                        line: 42
                    )
                }
                return wrappedValue
            }()
            // End expansion for "#unwrap"
```

### The MacroExpansion.makeUniqueName() method — [34:30]

```swift
let captureVar = context.makeUniqueName()

return  """
        { [\(captureVar) = \(originalWrapped)] in
            \(makeGuardStmt(wrapped: captureVar, …))
            \(makeReturnStmt(wrapped: captureVar))
        }
        """
```

### Declaring a macro’s names — [35:44]

```swift
@attached(conformance)
@attached(member, names: named(dictionary), named(init(dictionary:)))
@attached(memberAttribute)
@attached(accessor)
macro DictionaryStorage(key: String? = nil)



@attached(peer, names: overloaded)
macro AddCompletionHandler(parameterName: String = "completionHandler")



@freestanding(declaration, names: arbitrary)
macro makeArrayND(n: Int)
```

### Macros are testable — [38:28]

```swift
import MyLibMacros
import XCTest
import SwiftSyntaxMacrosTestSupport

final class MyLibTests: XCTestCase {
    func testMacro() {
        assertMacroExpansion(
            """
            @DictionaryStorage var name: String
            """,
            expandedSource: """
            var name: String {
                get { dictionary["name"]! as! String }
                set { dictionary["name"] = newValue }
            }
            """,
            macros: ["DictionaryStorage": DictionaryStorageMacro.self])
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10167/4/EAAEDDF4-5E7C-4AE9-A20C-CCD2E061E331/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10167/4/EAAEDDF4-5E7C-4AE9-A20C-CCD2E061E331/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10167) — developer.apple.com. Indexed for agent consumption._
