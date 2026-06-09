---
id: "wwdc2024-10075"
event: "wwdc2024"
year: 2024
title: "Track model changes with SwiftData history"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10075"
topics: ["App Services", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Track model changes with SwiftData history

**Event:** WWDC24 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-13 · **Session:** [wwdc2024-10075](https://developer.apple.com/videos/play/wwdc2024/10075)

Reveal the history of your model’s changes with SwiftData! Use the history API to understand when data store changes occurred, and learn how to use this information to build features like remote server sync and out-of-process change handing in your app. We’ll also cover how you can build support for the history API into a custom data store.

**Keywords:** `historydescriptor`, `historyproviding`, `history tracking`, `model changes`, `nspersistenthistorytrackingkey`, `persistent history`, `transactions`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,229 words)

## Documentation & Resources

- [Fetching and filtering time-based model changes](https://developer.apple.com/documentation/SwiftData/Fetching-and-filtering-time-based-model-changes) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftData/Fetching-and-filtering-time-based-model-changes
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftData/Fetching-and-filtering-time-based-model-changes.json
- [Forum: Programming Languages](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/programming-languages-topic?cid=vf-a-0010
- [SwiftData](https://developer.apple.com/documentation/SwiftData) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftData
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftData.json

## Code Snippets

### Preserve values in history on deletion — [4:57]

```swift
// Add .preserveValueOnDeletion to capture unique columns
import SwiftData

@Model 
class Trip {
    #Unique<Trip>([\.name, \.startDate, \.endDate])

    @Attribute(.preserveValueOnDeletion)
    var name: String
    var destination: String

    @Attribute(.preserveValueOnDeletion)
    var startDate: Date

    @Attribute(.preserveValueOnDeletion)
    var endDate: Date

    var bucketList: [BucketListItem] = [BucketListItem]()
    var livingAccommodation: LivingAccommodation?
}
```

### Fetch transactions from history — [6:26]

```swift
private func findTransactions(after token: DefaultHistoryToken?, author: String) -> [DefaultHistoryTransaction] {
    var historyDescriptor = HistoryDescriptor<DefaultHistoryTransaction>() 
    if let token {
        historyDescriptor.predicate = #Predicate { transaction in
            (transaction.token > token) && (transaction.author == author)
        }
    }

    var transactions: [DefaultHistoryTransaction] = []
    let taskContext = ModelContext(modelContainer)
    do {
        transactions = try taskContext.fetchHistory(historyDescriptor)
    } catch let error {
        print(error)
    }

    return transactions
}
```

### Process history changes — [7:34]

```swift
private func findTrips(in transactions: [DefaultHistoryTransaction]) -> (Set<Trip>, DefaultHistoryToken?) {
    let taskContext = ModelContext(modelContainer)
    var resultTrips: Set<Trip> = []
    for transaction in transactions {
        for change in transaction.changes {
            let modelID = change.changedPersistentIdentifier
            let fetchDescriptor = FetchDescriptor<Trip>(predicate: #Predicate { trip in
                trip.livingAccommodation?.persistentModelID == modelID
            })
            let fetchResults = try? taskContext.fetch(fetchDescriptor)
            guard let matchedTrip = fetchResults?.first else {
                continue
            }
            switch change {
            case .insert(_ as DefaultHistoryInsert<LivingAccommodation>):
                resultTrips.insert(matchedTrip)
            case .update(_ as DefaultHistoryUpdate<LivingAccommodation>):
                resultTrips.update(with: matchedTrip)
            case .delete(_ as DefaultHistoryDelete<LivingAccommodation>):
                resultTrips.remove(matchedTrip)
            default: break
            }
        }
    }
    return (resultTrips, transactions.last?.token)
}
```

### Save and use a history token — [10:19]

```swift
private func findUnreadTrips() -> Set<Trip> {
    let tokenData = UserDefaults.standard.data(forKey: UserDefaultsKey.historyToken)

    var historyToken: DefaultHistoryToken? = nil
    if let tokenData {
        historyToken = try? JSONDecoder().decode(DefaultHistoryToken.self, from: tokenData)
    }
    let transactions = findTransactions(after: historyToken, author: TransactionAuthor.widget)
    let (unreadTrips, newToken) = findTrips(in: transactions)

    if let newToken {
        let newTokenData = try? JSONEncoder().encode(newToken)
        UserDefaults.standard.set(newTokenData, forKey: UserDefaultsKey.historyToken)
    }
    return unreadTrips
}
```

### Update the user interface — [11:30]

```swift
struct ContentView: View {
    @Environment(\.scenePhase) private var scenePhase
    @State private var showAddTrip = false
    @State private var selection: Trip?
    @State private var searchText: String = ""
    @State private var tripCount = 0
    @State private var unreadTripIdentifiers: [PersistentIdentifier] = []

    var body: some View {
        NavigationSplitView {
            TripListView(selection: $selection, tripCount: $tripCount,
                         unreadTripIdentifiers: $unreadTripIdentifiers,
                         searchText: searchText)
            .toolbar {
                ToolbarItem(placement: .topBarLeading) {
                    EditButton()
                        .disabled(tripCount == 0)
                }
                ToolbarItemGroup(placement: .topBarTrailing) {
                    Spacer()
                    Button {
                        showAddTrip = true
                    } label: {
                        Label("Add trip", systemImage: "plus")
                    }
                }
            }
        } detail: {
            if let selection = selection {
                NavigationStack {
                    TripDetailView(trip: selection)
                }
            }
        }
        .task {
            unreadTripIdentifiers = await DataModel.shared.unreadTripIdentifiersInUserDefaults
        }
        .searchable(text: $searchText, placement: .sidebar)
        .sheet(isPresented: $showAddTrip) {
            NavigationStack {
                AddTripView()
            }
            .presentationDetents([.medium, .large])
        }
        .onChange(of: selection) { _, newValue in
            if let newSelection = newValue {
                if let index = unreadTripIdentifiers.firstIndex(where: {
                    $0 == newSelection.persistentModelID
                }) {
                    unreadTripIdentifiers.remove(at: index)
                }
            }
        }
        .onChange(of: scenePhase) { _, newValue in
            Task {
                if newValue == .active {
                    unreadTripIdentifiers += await DataModel.shared.findUnreadTripIdentifiers()
                } else {
                    // Persist the unread trip names for the next launch session.
                    await DataModel.shared.setUnreadTripIdentifiersInUserDefaults(unreadTripIdentifiers)
                }
            }
        }
        #if os(macOS)
        .onReceive(NotificationCenter.default.publisher(for: NSApplication.didBecomeActiveNotification)) { _ in
            Task {
                unreadTripIdentifiers += await DataModel.shared.findUnreadTripIdentifiers()
            }
        }
        .onReceive(NotificationCenter.default.publisher(for: NSApplication.willTerminateNotification)) { _ in
            Task {
                await DataModel.shared.setUnreadTripIdentifiersInUserDefaults(unreadTripIdentifiers)
            }
        }
        #endif
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10075/4/0F3D64B6-B594-42E8-8B59-2088D1B251F8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10075/4/0F3D64B6-B594-42E8-8B59-2088D1B251F8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10075) — developer.apple.com. Indexed for agent consumption._