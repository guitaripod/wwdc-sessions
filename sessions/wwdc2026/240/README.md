---
id: "wwdc2026-240"
event: "wwdc2026"
year: 2026
title: "Build intelligent Siri experiences with App Schemas"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/240"
topics: ["App Services", "AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Build intelligent Siri experiences with App Schemas

**Event:** WWDC26 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-240](https://developer.apple.com/videos/play/wwdc2026/240)

Bring your app’s content and actions to Siri with App Intents. Model your data using App Entities, adopt App Schemas to enable powerful system actions, and support natural language interactions powered by Apple Intelligence. Explore how to enable semantic search, perform actions across apps, and create contextual experiences using onscreen awareness and content transfer. Find out best practices and testing tools to build fast, reliable Siri experiences.

**Keywords:** `ai`, `app intents`, `machine learning`, `siri`, `spotlight`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,439 words)

## Documentation & Resources

- [Integrating your messaging app with Apple Intelligence](https://developer.apple.com/documentation/AppIntents/integrating-your-messaging-app-with-apple-intelligence) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/integrating-your-messaging-app-with-apple-intelligence
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/integrating-your-messaging-app-with-apple-intelligence.json
- [Donating your app’s data and actions to the system](https://developer.apple.com/documentation/AppIntents/donating-your-apps-data-and-actions-to-the-system) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/donating-your-apps-data-and-actions-to-the-system
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/donating-your-apps-data-and-actions-to-the-system.json
- [Making app entities available in Spotlight](https://developer.apple.com/documentation/AppIntents/making-app-entities-available-in-spotlight) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/making-app-entities-available-in-spotlight
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/making-app-entities-available-in-spotlight.json
- [Making actions and content discoverable by Apple Intelligence](https://developer.apple.com/documentation/AppIntents/making-actions-and-content-discoverable-by-apple-intelligence) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/making-actions-and-content-discoverable-by-apple-intelligence
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/making-actions-and-content-discoverable-by-apple-intelligence.json
- [Providing contextual cues to Apple Intelligence and Siri](https://developer.apple.com/documentation/AppIntents/providing-contextual-cues-to-apple-intelligence-and-siri) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/providing-contextual-cues-to-apple-intelligence-and-siri
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/providing-contextual-cues-to-apple-intelligence-and-siri.json
- [Apple Intelligence and Siri AI](https://developer.apple.com/documentation/AppIntents/apple-intelligence-and-siri-ai) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/apple-intelligence-and-siri-ai
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/apple-intelligence-and-siri-ai.json
- [Messages](https://developer.apple.com/documentation/AppIntents/app-schema-domain-messages) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/app-schema-domain-messages
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/app-schema-domain-messages.json
- [App schema domains](https://developer.apple.com/documentation/AppIntents/app-schema-domains) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppIntents/app-schema-domains
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppIntents/app-schema-domains.json

## Code Snippets

### Contributing message content to Apple Intelligence — [7:59]

```swift
// Contributing message content to Apple Intelligence

@AppEntity(schema: .messages.message)
struct MessageEntity: IndexedEntity {

    // The text content of the message
    @Property(indexingKey: \.textContent)
    var body: AttributedString?
}
```

### An interface that locates entities using arbitrary string input — [8:36]

```swift
// An interface that locates entities using arbitrary string input

struct ContactQuery: EntityStringQuery {
    func entities(matching string: String) async throws -> [ContactEntity] {
        let predicate = #Predicate<Person> { person in
            person.name.localizedStandardContains(string)
        }
        let descriptor = FetchDescriptor<Person>(predicate: predicate)
        let matches = try modelContext.fetch(descriptor)
        return matches.map(\.entity)
    }
}
```

### Working across apps - View annotations — [17:19]

```swift
// Working across apps - View annotations

List {
    ForEach(messages) { message in
        MessageRow(message: message)
            .appEntityIdentifier(
                EntityIdentifier(
                    for: MessageEntity.self,
                    identifier: message.id
                )
            )
    }
}
```

### Working across apps - Exporting content to another app — [18:18]

```swift
// Working across apps - Exporting content to another app

extension ContactEntity: Transferable {

    static var transferRepresentation: some TransferRepresentation {
        IntentValueRepresentation(
            exporting: \.person
        )
    }
}
```

### Working across apps - IntentValueQuery — [19:21]

```swift
// Working across apps - IntentValueQuery

struct ContactEntityQuery: IntentValueQuery {

    func values(for input: [IntentPerson]) async throws -> [ContactEntity] {
        let names = input.map(\.displayName)
        let descriptor = FetchDescriptor<Contact>()
        let contacts = try model.mainContext.fetch(descriptor)
        let matches = contacts.filter { contact in
            names.contains(where: { name in
                contact.name.localizedStandardContains(name)
            })
        }
        return matches.map(\.entity)
    }
}
```

### Working across apps - IntentValueRepresentation — [20:00]

```swift
// Working across apps - IntentValueRepresentation

extension ContactEntity: Transferable {

    static var transferRepresentation: some TransferRepresentation {
        IntentValueRepresentation(exporting: \.person, importing: { intentPerson in                    
            let contact = Contact(importing: intentPerson)
            ContactManager.shared.contacts.append(contact)
            return contact.entity
        })
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/240/4/d46aac11-3990-42cd-bb33-4ce5e958b902/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/240/4/d46aac11-3990-42cd-bb33-4ce5e958b902/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/240) — developer.apple.com. Indexed for agent consumption._