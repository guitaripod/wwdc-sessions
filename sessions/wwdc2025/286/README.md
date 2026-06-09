---
id: "wwdc2025-286"
event: "wwdc2025"
year: 2025
title: "Meet the Foundation Models framework"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/286"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Meet the Foundation Models framework

**Event:** WWDC25 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-286](https://developer.apple.com/videos/play/wwdc2025/286)

Learn how to tap into the on-device large language model behind Apple Intelligence! This high-level overview covers everything from guided generation for generating Swift data structures and streaming for responsive experiences, to tool calling for integrating data sources and sessions for context management. This session has no prerequisites.

**Keywords:** `ai`, `machine learning`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,289 words)

## Documentation & Resources

- [Human Interface Guidelines: Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/generative-ai

## Code Snippets

### Playground - Trip to Japan — [2:28]

```swift
import FoundationModels
import Playgrounds

#Playground {
    let session = LanguageModelSession()
    let response = try await session.respond(to: "What's a good name for a trip to Japan? Respond only with a title")
}
```

### Playground - Loop over landmarks — [2:43]

```swift
import FoundationModels
import Playgrounds

#Playground {
    let session = LanguageModelSession()
    for landmark in ModelData.shared.landmarks {
        let response = try await session.respond(to: "What's a good name for a trip to \(landmark.name)? Respond only with a title")
    }
}
```

### Creating a Generable struct — [5:32]

```swift
// Creating a Generable struct

@Generable
struct SearchSuggestions {
    @Guide(description: "A list of suggested search terms", .count(4))
    var searchTerms: [String]
}
```

### Responding with a Generable type — [5:51]

```swift
// Responding with a Generable type

let prompt = """
    Generate a list of suggested search terms for an app about visiting famous landmarks.
    """

let response = try await session.respond(
    to: prompt,
    generating: SearchSuggestions.self
)

print(response.content)
```

### Composing Generable types — [6:18]

```swift
// Composing Generable types

@Generable struct Itinerary {
    var destination: String
    var days: Int
    var budget: Float
    var rating: Double
    var requiresVisa: Bool
    var activities: [String]
    var emergencyContact: Person
    var relatedItineraries: [Itinerary]
}
```

### PartiallyGenerated types — [9:20]

```swift
// PartiallyGenerated types

@Generable struct Itinerary {
    var name: String
    var days: [Day]
}
```

### Streaming partial generations — [9:40]

```swift
// Streaming partial generations

let stream = session.streamResponse(
    to: "Craft a 3-day itinerary to Mt. Fuji.",
    generating: Itinerary.self
)

for try await partial in stream {
    print(partial)
}
```

### Streaming itinerary view — [10:05]

```swift
struct ItineraryView: View {
    let session: LanguageModelSession
    let dayCount: Int
    let landmarkName: String

    @State
    private var itinerary: Itinerary.PartiallyGenerated?

    var body: some View {
        //...
        Button("Start") {
            Task {
                do {
                    let prompt = """
                        Generate a \(dayCount) itinerary \
                        to \(landmarkName).
                        """

                    let stream = session.streamResponse(
                        to: prompt,
                        generating: Itinerary.self
                    )

                    for try await partial in stream {
                        self.itinerary = partial
                    }
                } catch {
                    print(error)  
                }
            }
        }
    }
}
```

### Property order matters — [11:00]

```swift
@Generable struct Itinerary {

  @Guide(description: "Plans for each day")
  var days: [DayPlan]

  @Guide(description: "A brief summary of plans")
  var summary: String
}
```

### Defining a tool — [13:42]

```swift
// Defining a tool
import WeatherKit
import CoreLocation
import FoundationModels

struct GetWeatherTool: Tool {
    let name = "getWeather"
    let description = "Retrieve the latest weather information for a city"

    @Generable
    struct Arguments {
        @Guide(description: "The city to fetch the weather for")
        var city: String
    }

    func call(arguments: Arguments) async throws -> ToolOutput {
        let places = try await CLGeocoder().geocodeAddressString(arguments.city)
        let weather = try await WeatherService.shared.weather(for: places.first!.location!)
        let temperature = weather.currentWeather.temperature.value

        let content = GeneratedContent(properties: ["temperature": temperature])
        let output = ToolOutput(content)

        // Or if your tool’s output is natural language:
        // let output = ToolOutput("\(arguments.city)'s temperature is \(temperature) degrees.")

        return output
    }
}
```

### Attaching tools to a session — [15:03]

```swift
// Attaching tools to a session

let session = LanguageModelSession(
    tools: [GetWeatherTool()],
    instructions: "Help the user with weather forecasts."
)

let response = try await session.respond(
    to: "What is the temperature in Cupertino?"
)

print(response.content)
// It’s 71˚F in Cupertino!
```

### Supplying custom instructions — [16:30]

```swift
// Supplying custom instructions

let session = LanguageModelSession(
    instructions: """
        You are a helpful assistant who always \
        responds in rhyme.
        """
)
```

### Multi-turn interactions — [17:46]

```swift
// Multi-turn interactions

let session = LanguageModelSession()

let firstHaiku = try await session.respond(to: "Write a haiku about fishing")
print(firstHaiku.content)
// Silent waters gleam,
// Casting lines in morning mist—
// Hope in every cast.

let secondHaiku = try await session.respond(to: "Do another one about golf")
print(secondHaiku.content)
// Silent morning dew,
// Caddies guide with gentle words—
// Paths of patience tread.

print(session.transcript) // (Prompt) Write a haiku about fishing
// (Response) Silent waters gleam...
// (Prompt) Do another one about golf
// (Response) Silent morning dew...
```

### Gate on isResponding — [18:22]

```swift
import SwiftUI
import FoundationModels

struct HaikuView: View {

    @State
    private var session = LanguageModelSession()

    @State
    private var haiku: String?

    var body: some View {
        if let haiku {
            Text(haiku)
        }
        Button("Go!") {
            Task {
                haiku = try await session.respond(
                    to: "Write a haiku about something you haven't yet"
                ).content
            }
        }
        // Gate on `isResponding`
        .disabled(session.isResponding)
    }
}
```

### Using a built-in use case — [18:39]

```swift
// Using a built-in use case

let session = LanguageModelSession(
    model: SystemLanguageModel(useCase: .contentTagging)
)
```

### Content tagging use case - 1 — [19:19]

```swift
// Content tagging use case

@Generable
struct Result {
    let topics: [String]
}

let session = LanguageModelSession(model: SystemLanguageModel(useCase: .contentTagging))
let response = try await session.respond(to: ..., generating: Result.self)
```

### Content tagging use case - 2 — [19:35]

```swift
// Content tagging use case

@Generable
struct Top3ActionEmotionResult {
    @Guide(.maximumCount(3))
    let actions: [String]
    @Guide(.maximumCount(3))
    let emotions: [String]
}

let session = LanguageModelSession(
    model: SystemLanguageModel(useCase: .contentTagging),
    instructions: "Tag the 3 most important actions and emotions in the given input text."
)
let response = try await session.respond(to: ..., generating: Top3ActionEmotionResult.self)
```

### Availability checking — [19:56]

```swift
// Availability checking

struct AvailabilityExample: View {
    private let model = SystemLanguageModel.default

    var body: some View {
        switch model.availability {
        case .available:
            Text("Model is available").foregroundStyle(.green)
        case .unavailable(let reason):
            Text("Model is unavailable").foregroundStyle(.red)
            Text("Reason: \(reason)")
        }
    }
}
```

### Encodable feedback attachment data structure — [22:13]

```swift
let feedback = LanguageModelFeedbackAttachment(
  input: [
    // ...
  ],
  output: [
    // ...
  ],
  sentiment: .negative,
  issues: [
    LanguageModelFeedbackAttachment.Issue(
      category: .incorrect,
      explanation: "..."
    )
  ],
  desiredOutputExamples: [
    [
      // ...
    ]
  ]
)
let data = try JSONEncoder().encode(feedback)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/286/4/6f221dca-f35f-4dad-bfec-0ec0970849bb/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/286/4/6f221dca-f35f-4dad-bfec-0ec0970849bb/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/286) — developer.apple.com. Indexed for agent consumption._