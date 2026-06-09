---
id: "wwdc2025-301"
event: "wwdc2025"
year: 2025
title: "Deep dive into the Foundation Models framework"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/301"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Deep dive into the Foundation Models framework

**Event:** WWDC25 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-301](https://developer.apple.com/videos/play/wwdc2025/301)

Level up with the Foundation Models framework. Learn how guided generation works under the hood, and use guides, regexes, and generation schemas to get custom structured responses. We’ll show you how to use tool calling to let the model autonomously access external information and perform actions, for a personalized experience. To get the most out of this video, we recommend first watching “Meet the Foundation Models framework”.

**Keywords:** `ai`, `machine learning`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,027 words)

## Documentation & Resources

- [Generate dynamic game content with guided generation and tools](https://developer.apple.com/documentation/FoundationModels/generate-dynamic-game-content-with-guided-generation-and-tools) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FoundationModels/generate-dynamic-game-content-with-guided-generation-and-tools
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FoundationModels/generate-dynamic-game-content-with-guided-generation-and-tools.json
- [Human Interface Guidelines: Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/generative-ai

## Code Snippets

### Prompting a session — [1:05]

```swift
import FoundationModels

func respond(userInput: String) async throws -> String {
  let session = LanguageModelSession(instructions: """
    You are a friendly barista in a world full of pixels.
    Respond to the player’s question.
    """
  )
  let response = try await session.respond(to: userInput)
  return response.content
}
```

### Handle context size errors — [3:37]

```swift
var session = LanguageModelSession()

do {
  let answer = try await session.respond(to: prompt)
  print(answer.content)
} catch LanguageModelSession.GenerationError.exceededContextWindowSize {
  // New session, without any history from the previous session.
  session = LanguageModelSession()
}
```

### Handling context size errors with a new session — [3:55]

```swift
var session = LanguageModelSession()

do {
  let answer = try await session.respond(to: prompt)
  print(answer.content)
} catch LanguageModelSession.GenerationError.exceededContextWindowSize {
  // New session, with some history from the previous session.
  session = newSession(previousSession: session)
}

private func newSession(previousSession: LanguageModelSession) -> LanguageModelSession {
  let allEntries = previousSession.transcript.entries
  var condensedEntries = [Transcript.Entry]()
  if let firstEntry = allEntries.first {
    condensedEntries.append(firstEntry)
    if allEntries.count > 1, let lastEntry = allEntries.last {
      condensedEntries.append(lastEntry)
    }
  }
  let condensedTranscript = Transcript(entries: condensedEntries)
  // Note: transcript includes instructions.
  return LanguageModelSession(transcript: condensedTranscript)
}
```

### Sampling — [6:14]

```swift
// Deterministic output
let response = try await session.respond(
  to: prompt,
  options: GenerationOptions(sampling: .greedy)
)

// Low-variance output
let response = try await session.respond(
  to: prompt,
  options: GenerationOptions(temperature: 0.5)
)

// High-variance output
let response = try await session.respond(
  to: prompt,
  options: GenerationOptions(temperature: 2.0)
)
```

### Handling languages — [7:06]

```swift
var session = LanguageModelSession()

do {
  let answer = try await session.respond(to: userInput)
  print(answer.content)
} catch LanguageModelSession.GenerationError.unsupportedLanguageOrLocale {
  // Unsupported language in prompt.
}

let supportedLanguages = SystemLanguageModel.default.supportedLanguages
guard supportedLanguages.contains(Locale.current.language) else {
  // Show message
  return
}
```

### Generable — [8:14]

```swift
@Generable
struct NPC {
  let name: String
  let coffeeOrder: String
}

func makeNPC() async throws -> NPC {
  let session = LanguageModelSession(instructions: ...)
  let response = try await session.respond(generating: NPC.self) {
    "Generate a character that orders a coffee."
  }
  return response.content
}
```

### NPC — [9:22]

```swift
@Generable
struct NPC {
  let name: String
  let coffeeOrder: String
}
```

### Generable with enum — [10:49]

```swift
@Generable
struct NPC {
  let name: String
  let encounter: Encounter

  @Generable
  enum Encounter {
    case orderCoffee(String)
    case wantToTalkToManager(complaint: String)
  }
}
```

### Generable with guides — [11:20]

```swift
@Generable
struct NPC {
  @Guide(description: "A full name")
  let name: String
  @Guide(.range(1...10))
  let level: Int
  @Guide(.count(3))
  let attributes: [Attribute]
  let encounter: Encounter

  @Generable
  enum Attribute {
    case sassy
    case tired
    case hungry
  }
  @Generable
  enum Encounter {
    case orderCoffee(String)
    case wantToTalkToManager(complaint: String)
  }
}
```

### Regex guide — [13:40]

```swift
@Generable
struct NPC {
  @Guide(Regex {
    Capture {
      ChoiceOf {
        "Mr"
        "Mrs"
      }
    }
    ". "
    OneOrMore(.word)
  })
  let name: String
}

session.respond(to: "Generate a fun NPC", generating: NPC.self)
// > {name: "Mrs. Brewster"}
```

### Generable riddle — [14:50]

```swift
@Generable
struct Riddle {
  let question: String
  let answers: [Answer]

  @Generable
  struct Answer {
    let text: String
    let isCorrect: Bool
  }
}
```

### Dynamic schema — [15:10]

```swift
struct LevelObjectCreator {
  var properties: [DynamicGenerationSchema.Property] = []

  mutating func addStringProperty(name: String) {
    let property = DynamicGenerationSchema.Property(
      name: name,
      schema: DynamicGenerationSchema(type: String.self)
    )
    properties.append(property)
  }

  mutating func addArrayProperty(name: String, customType: String) {
    let property = DynamicGenerationSchema.Property(
      name: name,
      schema: DynamicGenerationSchema(
        arrayOf: DynamicGenerationSchema(referenceTo: customType)
      )
    )
    properties.append(property)
  }

  var root: DynamicGenerationSchema {
    DynamicGenerationSchema(
      name: name,
      properties: properties
    )
  }
}

var riddleBuilder = LevelObjectCreator(name: "Riddle")
riddleBuilder.addStringProperty(name: "question")
riddleBuilder.addArrayProperty(name: "answers", customType: "Answer")

var answerBuilder = LevelObjectCreator(name: "Answer")
answerBuilder.addStringProperty(name: "text")
answerBuilder.addBoolProperty(name: "isCorrect")

let riddleDynamicSchema = riddleBuilder.root
let answerDynamicSchema = answerBuilder.root

let schema = try GenerationSchema(
  root: riddleDynamicSchema,
  dependencies: [answerDynamicSchema]
)

let session = LanguageModelSession()
let response = try await session.respond(
  to: "Generate a fun riddle about coffee",
  schema: schema
)
let generatedContent = response.content
let question = try generatedContent.value(String.self, forProperty: "question")
let answers = try generatedContent.value([GeneratedContent].self, forProperty: "answers")
```

### FindContactTool — [18:47]

```swift
import FoundationModels
import Contacts

struct FindContactTool: Tool {
  let name = "findContact"
  let description = "Finds a contact from a specified age generation."

  @Generable
  struct Arguments {
    let generation: Generation

    @Generable
    enum Generation {
      case babyBoomers
      case genX
      case millennial
      case genZ            
    }
  }

  func call(arguments: Arguments) async throws -> ToolOutput {
    let store = CNContactStore()

    let keysToFetch = [CNContactGivenNameKey, CNContactBirthdayKey] as [CNKeyDescriptor]
    let request = CNContactFetchRequest(keysToFetch: keysToFetch)

    var contacts: [CNContact] = []
    try store.enumerateContacts(with: request) { contact, stop in
      if let year = contact.birthday?.year {
        if arguments.generation.yearRange.contains(year) {
          contacts.append(contact)
        }
      }
    }
    guard let pickedContact = contacts.randomElement() else {
      return ToolOutput("Could not find a contact.")
    }
    return ToolOutput(pickedContact.givenName)
  }
}
```

### Call FindContactTool — [20:26]

```swift
import FoundationModels

let session = LanguageModelSession(
  tools: [FindContactTool()],
  instructions: "Generate fun NPCs"
)
```

### FindContactTool with state — [21:55]

```swift
import FoundationModels
import Contacts

class FindContactTool: Tool {
  let name = "findContact"
  let description = "Finds a contact from a specified age generation."

  var pickedContacts = Set<String>()

  ...

  func call(arguments: Arguments) async throws -> ToolOutput {
    contacts.removeAll(where: { pickedContacts.contains($0.givenName) })
    guard let pickedContact = contacts.randomElement() else {
      return ToolOutput("Could not find a contact.")
    }
    return ToolOutput(pickedContact.givenName)
  }
}
```

### GetContactEventTool — [22:27]

```swift
import FoundationModels
import EventKit

struct GetContactEventTool: Tool {
  let name = "getContactEvent"
  let description = "Get an event with a contact."

  let contactName: String

  @Generable
  struct Arguments {
    let day: Int
    let month: Int
    let year: Int
  }

  func call(arguments: Arguments) async throws -> ToolOutput { ... }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/301/4/955589c1-ae33-47db-9e86-2b87311dedb5/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/301/4/955589c1-ae33-47db-9e86-2b87311dedb5/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/301) — developer.apple.com. Indexed for agent consumption._
