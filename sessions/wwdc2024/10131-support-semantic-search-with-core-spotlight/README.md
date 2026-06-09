---
id: "wwdc2024-10131"
event: "wwdc2024"
year: 2024
title: "Support semantic search with Core Spotlight"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10131"
topics: ["AI & Machine Learning", "App Services", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Support semantic search with Core Spotlight

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10131](https://developer.apple.com/videos/play/wwdc2024/10131)

Learn how to provide semantic search results in your app using Core Spotlight. Understand how to make your app’s content available in the user’s private, on-device index so people can search for items using natural language. We’ll also share how to optimize your app’s performance by scheduling indexing activities. To get the most out of this session, we recommend first checking out Core Spotlight documentation on the Apple Developer website.

**Keywords:** `🔍`, `cssearchableindex`, `cssearchableitem`, `cssearchableitemattributeset`, `csuserquery`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,932 words)

## Documentation & Resources

- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010
- [Core Spotlight](https://developer.apple.com/documentation/CoreSpotlight) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreSpotlight
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreSpotlight.json

## Code Snippets

### Creating CSSearchableItem — [2:14]

```swift
// Creating searchable items for donation


let item = CSSearchableItem(uniqueIdentifier: uniqueIdentifier, domainIdentifier: domainIdentifier, attributeSet: attributeSet)
```

### Creating CSSearchableAttributeSet — [2:28]

```swift
// Creating searchable content for donation


let attributeSet = CSSearchableItemAttributeSet(contentType: UTType.text)
attributeSet.contentType = UTType.text.identifier
```

### Searchable items with type — [2:40]

```swift
// Searchable items with text


attributeSet.title
attributeSet.textContent


// Searchable items with media


attributeSet.contentType
attributeSet.contentURL


// Searchable items with links


attributeSet.contentURL
attributeSet.relatedUniqueIdentifier
```

### Batch indexing with client state — [3:31]

```swift
// Batch indexing with client state


let index = CSSearchableIndex(name: "SpotlightSearchSample")        
index.fetchLastClientState { state, error in         
    if state == nil {
        index.beginBatch()
        index.indexSearchableItems(items)
        index.endIndexBatch(expectedClientState: state, newClientState: newState) { error in
        }
    }
}
```

### Avoid overwriting existing attributes — [3:56]

```swift
// Make it an update to avoid overwriting existing attributes


item.isUpdate = true
```

### Configure a query — [7:19]

```swift
// Configure a query


let queryContext = CSUserQueryContext()
queryContext.fetchAttributes = ["title", "contentDescription"]
```

### Ranked results — [7:33]

```swift
// Ranked results


queryContext.enableRankedResults = true
queryContext.maxRankedResultCount = 2
```

### Suggestions — [7:47]

```swift
// Suggestions


queryContext.maxSuggestionCount = 4
```

### Filter queries — [7:55]

```swift
// Filter queries


queryContext.filterQueries = ["contentTypeTree=\"public.image\""]
```

### Query for searchable items and suggestions — [8:23]

```swift
// Query for searchable items and suggestions


let query = CSUserQuery(userQueryString: "windsurfing carmel", userQueryContext: queryContext)
for try await element in query.responses {
    switch(element) {
        case .item(let item):
            self.items.append(item)
            break
        case .suggestion(let suggestion):
            self.suggestions.append(suggestion)
            break
    }
}
```

### Suggestions — [8:40]

```swift
// Suggestions


suggestion.localizedAttributedSuggestion
```

### Preparing for queries — [8:56]

```swift
// Preparing for queries


CSUserQuery.prepare
CSUserQuery.prepareWithProtectionClasses
```

### Set the lastUsedDate — [9:50]

```swift
// Set the lastUsedDate when the user interacts with the item


item.attributeSet.lastUsedDate = Date.now
item.isUpdate = true
```

### Interactions with items and suggestions from a query — [10:00]

```swift
// Interactions with items and suggestions from a query


query.userEngaged(item, visibleItems: visibleItems, interaction: CSUserQuery.UserInteractionKind.select)

query.userEngaged(suggestion, visibleSuggestions: visibleSuggestions, interaction: CSUserQuery.UserInteractionKind.select)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10131/5/537550D3-98A7-4C5B-B4BC-CD55CDAD3547/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10131/5/537550D3-98A7-4C5B-B4BC-CD55CDAD3547/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10131) — developer.apple.com. Indexed for agent consumption._
