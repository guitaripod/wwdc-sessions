---
id: "wwdc2024-10121"
event: "wwdc2024"
year: 2024
title: "Meet the Contact Access Button"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10121"
topics: ["SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Meet the Contact Access Button

**Event:** WWDC24 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2024-06-13 · **Session:** [wwdc2024-10121](https://developer.apple.com/videos/play/wwdc2024/10121)

Learn about the new Contacts authorization modes and how to improve Contacts access in your app. Discover how to integrate the Contact Access Button into your app to share additional contacts on demand and provide an easier path to Contacts authorization. We’ll also cover Contacts security features and an alternative API to be used if the button isn’t appropriate for your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,088 words)

## Documentation & Resources

- [Accessing a person’s contact data using Contacts and ContactsUI](https://developer.apple.com/documentation/Contacts/accessing-a-person-s-contact-data-using-contacts-and-contactsui) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Contacts/accessing-a-person-s-contact-data-using-contacts-and-contactsui
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Contacts/accessing-a-person-s-contact-data-using-contacts-and-contactsui.json
- [Forum: App & System Services](https://developer.apple.com/forums/topics/app-and-system-services?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/app-and-system-services?cid=vf-a-0010

## Code Snippets

### Using ContactAccessButton — [5:15]

```swift
// Using ContactAccessButton

@Binding var searchText: String
@State var authorizationStatus: CNAuthorizationStatus = .notDetermined

var body: some View {
    List {
        ForEach(searchResults(for: searchText)) { person in
            ResultRow(person)
        }
        if authorizationStatus == .limited || authorizationStatus == .notDetermined {
            ContactAccessButton(queryString: searchText) { identifiers in
                let contacts = await fetchContacts(withIdentifiers: identifiers)
                dismissSearch(withResult: contacts)
            }
        }
    }
}
```

### Appearance options — [6:10]

```swift
ContactAccessButton(queryString: searchText)
  .font(.system(weight: .bold))
  .foregroundStyle(.gray)
  .tint(.green)
  .contactAccessButtonCaption(.phone)
  .contactAccessButtonStyle(ContactAccessButton.Style(imageWidth: 30))
```

### Fetching contacts with CNContactStore — [10:11]

```swift
// Fetching contacts with CNContactStore

func fetchContacts(withIdentifiers identifiers: [String]) async -> [CNContact] {
    return await Task {
        let keys = [CNContactFormatter.descriptorForRequiredKeys(for: .fullName)]
        let fetchRequest = CNContactFetchRequest(keysToFetch: keys)
        fetchRequest.predicate = CNContact.predicateForContacts(withIdentifiers: identifiers)
        var contacts: [CNContact] = []
        do {
            try CNContactStore().enumerateContacts(with: fetchRequest) { contact, _ in
                contacts.append(contact)
            }
        } catch {
            // ...
        }
        return contacts
    }.value
}
```

### Using contactAccessPicker — [12:47]

```swift
// Using contactAccessPicker

@State private var isPresented = false

var body: some View {
    Button("Show picker") {
        isPresented.toggle()
    }.contactAccessPicker(isPresented: $isPresented) { identifiers in
        let contacts = await fetchContacts(withIdentifiers: identifiers)
        // use the new contacts!
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10121/4/A4253FF7-546D-4248-9DFA-DACBFB567A90/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10121/4/A4253FF7-546D-4248-9DFA-DACBFB567A90/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10121) — developer.apple.com. Indexed for agent consumption._
