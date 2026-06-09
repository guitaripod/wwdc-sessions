---
id: "wwdc2023-10052"
event: "wwdc2023"
year: 2023
title: "Discover Calendar and EventKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10052"
topics: ["App Services", "System Services"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# Discover Calendar and EventKit

**Event:** WWDC23 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10052](https://developer.apple.com/videos/play/wwdc2023/10052)

Discover how you can bring Calendar into your app and help people better manage their time. Find out how to create new events from your app, fetch events, and implement a virtual conference extension. We’ll also take you through some of the changes to calendar access levels that help your app stay connected without compromising the privacy of someone’s calendar data. 

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,862 words)

## Documentation & Resources

- [Accessing Calendar using EventKit and EventKitUI](https://developer.apple.com/documentation/EventKit/accessing-calendar-using-eventkit-and-eventkitui) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/EventKit/accessing-calendar-using-eventkit-and-eventkitui
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/EventKit/accessing-calendar-using-eventkit-and-eventkitui.json
- [Explore the Human Interface Guidelines for privacy](https://developer.apple.com/design/human-interface-guidelines/privacy) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/privacy
- [EventKit](https://developer.apple.com/documentation/EventKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/EventKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/EventKit.json
- [Universal Links for Developers](https://developer.apple.com/ios/universal-links/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/ios/universal-links/

## Code Snippets

### Adding an event with EventKitUI — [5:49]

```swift
// Create an event store
let store = EKEventStore()

// Create an event
let event = EKEvent(eventStore: store)
event.title = "WWDC23 Keynote"
let startDateComponents = DateComponents(year: 2023, month: 6, day: 5, hour: 10)
let startDate = Calendar.current.date(from: startDateComponents)!
event.startDate = startDate
event.endDate = Calendar.current.date(byAdding: .hour, value: 2, to: startDate)!
event.timeZone = TimeZone(identifier: "America/Los_Angeles")
event.location = "1 Apple Park Way, Cupertino, CA, United States"
event.notes = "Kick off an exhilarating week of technology and community."

// Create a view controller
let eventEditViewController = EKEventEditViewController()
eventEditViewController.event = event
eventEditViewController.eventStore = store
eventEditViewController.editViewDelegate = self

// Present the view controller
present(eventEditViewController, animated: true)
```

### Siri Event Suggestions — [9:17]

```swift
// Create an INReservation
let spokenPhrase = “Lunch at Caffè Macs”
let reservationReference = INSpeakableString(vocabularyIdentifier: "df9bc3f5",
                                             spokenPhrase: spokenPhrase,
                                             pronunciationHint: nil)
let duration = INDateComponentsRange(start: myEventStart, end: myEventEnd)
let location = CLPlacemark(location: myCLLocation,
                           name: "Caffè Macs",
                           postalAddress: myAddress)
let reservation = INRestaurantReservation(itemReference: reservationReference,
                                          reservationStatus: .confirmed,
                                          reservationHolderName: "Jane Appleseed",
                                          reservationDuration: duration,
                                          restaurantLocation: location)

// Create an intent and response
let intent = INGetReservationDetailsIntent(reservationContainerReference:
    reservationReference)
let intentResponse = INGetReservationDetailsIntentResponse(code: .success, userActivity: nil)
intentResponse.reservations = [reservation]

// Create an INInteraction
let interaction = INInteraction(intent: intent, response: intentResponse)

// Donate the interaction to the system
interaction.donate()
```

### Adding an event with write-only access — [12:41]

```swift
// Create an event store
let store = EKEventStore()

// Request write-only access
guard try await store.requestWriteOnlyAccessToEvents() else { return }

// Create an event
let event = EKEvent(eventStore: store)
event.calendar = store.defaultCalendarForNewEvents
event.title = "WWDC23 Keynote"
event.startDate = myEventStartDate
event.endDate = myEventEndDate
event.timeZone = TimeZone(identifier: "America/Los_Angeles")
event.location = "1 Apple Park Way, Cupertino, CA, United States"
event.notes = "Kick off an exhilarating week of technology and community."

// Save the event
guard try eventStore.save(event, span: .thisEvent) else { return }
```

### Fetch events — [15:51]

```swift
// Create an event store
let store = EKEventStore()

// Request full access
guard try await store.requestFullAccessToEvents() else { return }

// Create a predicate
guard let interval = Calendar.current.dateInterval(of: .month, for: Date()) else { return }
let predicate = store.predicateForEvents(withStart: interval.start,
                                         end: interval.end,
                                         calendars: nil)

// Fetch the events
let events = store.events(matching: predicate)

let sortedEvents = events.sorted { $0.compareStartDate(with: $1) == .orderedAscending }
```

### Virtual conference extension — [19:18]

```swift
// Create the extension target
class VirtualConferenceProvider: EKVirtualConferenceProvider {

    // Provide the room types
    override func fetchAvailableRoomTypes() async throws ->
        [EKVirtualConferenceRoomTypeDescriptor] {
        let title = "My Room"
        let identifier = "my_room"
        let roomType = EKVirtualConferenceRoomTypeDescriptor(title: title, identifier: identifier)
        return [roomType]
    }

    // Provide the virtual conference
    override func fetchVirtualConference(identifier: EKVirtualConferenceRoomTypeIdentifier)
        async throws -> EKVirtualConferenceDescriptor {
        let urlDescriptor = EKVirtualConferenceURLDescriptor(title: nil, url: myURL)
        let details = "Enter the meeting code 12345 to enter the meeting."
        return EKVirtualConferenceDescriptor(title: nil,
                                             urlDescriptors: [urlDescriptor],
                                             conferenceDetails: details)
    }

}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10052/5/B5C95345-FDF4-40FF-AFFB-350DD26BED61/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10052/5/B5C95345-FDF4-40FF-AFFB-350DD26BED61/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10052) — developer.apple.com. Indexed for agent consumption._