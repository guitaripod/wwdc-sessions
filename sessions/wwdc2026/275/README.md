---
id: "wwdc2026-275"
event: "wwdc2026"
year: 2026
title: "Code-along: Add persistence with SwiftData"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/275"
topics: ["Swift", "SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Code-along: Add persistence with SwiftData

**Event:** WWDC26 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-275](https://developer.apple.com/videos/play/wwdc2026/275)

Experience SwiftData in action as we add persistence to an existing app. We’ll show you how to define your data models and seamlessly integrate persistent data with SwiftUI. You’ll also learn foundational skills for managing your app’s state using this expressive, declarative API.

**Keywords:** `screenshots`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,133 words)

## Documentation & Resources

- [Wishlist: Planning travel in a SwiftUI app](https://developer.apple.com/documentation/SwiftUI/wishlist-planning-travel-in-a-swiftui-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/wishlist-planning-travel-in-a-swiftui-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/wishlist-planning-travel-in-a-swiftui-app.json
- [SwiftData](https://developer.apple.com/documentation/SwiftData) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftData
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftData.json

## Code Snippets

### Convert Activity to a persistent model with @Model — [3:39]

```swift
import Foundation
import SwiftData

// SwiftData automatically generates Observable conformance
@Model
class Activity {
    var name: String
    var isComplete: Bool = false
    var dateCreated = Date.now
    var dateEdited = Date.now
}
```

### Add Codable conformance to TripCollection — [6:06]

```swift
enum TripCollection: String, CaseIterable, RawRepresentable, Codable {
    case springEscapes
    case summerVibes
    case fallGetaways
    case winterRetreats
}
```

### Set up model relationships between Trip, TripImage, and Activity — [10:32]

```swift
import Foundation
import SwiftData

@Model
class Trip {
    var name: String
    var collection: TripCollection

    var photo: TripImage
    var thumbnailData: Data?

    @Relationship(deleteRule: .cascade, inverse: \Activity.trip)
    var activities: [Activity] = []

    private(set) var creationDate = Date.now
    var subtitle: String?
    var isComplete: Bool = false
}
```

### Enable interoperability between your schema and SwiftUI views — [13:21]

```swift
import SwiftUI
import SwiftData

@main
struct WishlistApp: App {
    let container: ModelContainer = {
        do {
            let modelContainer = try ModelContainer(for: Trip.self, Activity.self, TripImage.self, Goal.self, TripGoal.self, ActivityGoal.self)
            try SampleData.seedIfNeeded(in: modelContainer.mainContext)
            return modelContainer
        } catch {
            fatalError("Could not create model container: \(error)")
        }
    }()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .preferredColorScheme(.dark)
        }
        .modelContainer(container)
    }
}
```

### Fetch achieved and upcoming goals — [16:27]

```swift
@Query(filter: #Predicate<Goal> { $0.isAchieved }, sort: \Goal.dateAchieved, order: .reverse)
private var achievedGoals: [Goal]

@Query(filter: #Predicate<Goal> { !$0.isAchieved }, sort: \Goal.sortOrder)
private var upcomingGoals: [Goal]
```

### Fetch recent trips — [16:49]

```swift
import SwiftUI
import SwiftData

struct RecentTripsPageView: View {
    // Fetch most recent trips in reverse chronological order
    @Query(FetchDescriptor<Trip>(sortBy: [SortDescriptor(\Trip.creationDate, order: .reverse)], fetchLimit: 5))
    private var trips: [Trip]

    @Namespace private var namespace

    var body: some View {
        TabView {
            ForEach(trips) { trip in
                NavigationLink {
                    TripDetailView(trip: trip)
                        .navigationTransition(
                            .zoom(sourceID: trip.id, in: namespace))
                } label: {
                    TripImageView(trip: trip)
                        .overlay(alignment: .bottomLeading) {
                            VStack(alignment: .leading) {
                                Text("RECENTLY ADDED")
                                    .font(.subheadline)
                                    .fontWeight(.bold)
                                    .foregroundStyle(.limeGreen)

                                Text(trip.name)
                                    .font(.title)
                                    .fontWidth(.expanded)
                                    .fontWeight(.medium)
                                    .foregroundStyle(.primary)
                            }
                            .padding(.horizontal)
                            .padding(.bottom, 54)
                        }
                        .matchedTransitionSource(id: trip.id, in: namespace)
                }
                .buttonStyle(.plain)
            }
        }
        .tabViewStyle(.page)
        .containerRelativeFrame([.horizontal, .vertical]) { length, axis in
            if axis == .vertical {
                return length / 1.3
            } else {
                return length
            }
        }
    }
}
```

### Dynamically construct a query in the initializer of TripCollectionView — [17:26]

```swift
init(tripCollection: TripCollection, cardSize: TripCard.Size, namespace: Namespace.ID) {
    _trips = Query(filter: #Predicate<Trip> { $0.collection == tripCollection }, sort: \Trip.name)
    self.tripCollection = tripCollection
    self.cardSize = cardSize
    self.namespace = namespace
}
```

### Search for trips and activities by name — [18:13]

```swift
import SwiftUI
import SwiftData

private struct SearchResultsListView: View {
    @Query(sort: \Trip.name) private var trips: [Trip]
    @Query(sort: \Activity.name) private var activities: [Activity]

    var searchText: String
    var namespace: Namespace.ID

    init(searchText: String, namespace: Namespace.ID) {
        self.searchText = searchText
        self.namespace = namespace

        if searchText.isEmpty {
            _trips = Query(FetchDescriptor(sortBy: [SortDescriptor(\Trip.creationDate, order: .reverse)], fetchLimit: 3))
            _activities = Query(filter: #Predicate<Activity> { _ in false })
        } else {
            // All trips whose name matches searchText, sorted lexicographically
            let tripSearchPredicate = #Predicate<Trip> { $0.name.localizedStandardContains(searchText) }
            _trips = Query(filter: tripSearchPredicate, sort: \Trip.name)
            // All matching activities that belong to a trip
            let activitySearchPredicate = #Predicate<Activity> { $0.trip != nil && $0.name.localizedStandardContains(searchText) }
            _activities = Query(filter: activitySearchPredicate, sort: \Activity.name)
        }
    }

    var body: some View {
        List {
            if !trips.isEmpty {
                TripSearchSectionView(trips: trips, namespace: namespace, title: searchText.isEmpty ? "Recent Trips" : "Trips")
            }

            if !activities.isEmpty {
                ActivitySearchSectionView(activities: activities)
            }
        }
        .overlay {
            if trips.isEmpty && activities.isEmpty {
                ContentUnavailableView(
                    "No results for “\(searchText)”",
                    systemImage: "magnifyingglass",
                    description: Text("Check spelling or try a new search.")
                )
            }
        }
        .listStyle(.plain)
    }
}
```

### Capture and report errors from ActivityItemView — [19:42]

```swift
var body: some View {
    HStack(alignment: .firstTextBaseline, spacing: 17) {
        Group {
            if isEditing {
                rowContentWhenEditing
            } else {
                rowContentWhenNotEditing
            }
        }
        .transition(.opacity.animation(.snappy))
        .animation(.snappy, value: isEditing)
    }
    .onDisappear {
        do {
            try updateGoalAchievements()
        } catch {
            updateError = error
            reportError(error)
        }
    }
    .alert(error: $updateError) {
        // Customize the presentation of the error
    }
}
```

### Update dateEdited and propagate side effects on property changes — [21:04]

```swift
init(activity: Activity, isLast: Bool, isEditing: Bool) {
    activity.token = withContinuousObservation(options: .didSet) { event in
        _ = activity.name
        _ = activity.isComplete

        if event.matches(\Activity.name) {
            activity.dateEdited = .now
        }

        if event.matches(\Activity.isComplete) {
            activity.dateEdited = .now
            activity.trip?.isComplete = activity.trip?.activities.isEmpty == false
            && activity.trip?.activities.allSatisfy { $0.isComplete } == true
        }
    }
    self.activity = activity
    self.isLast = isLast
    self.isEditing = isEditing
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/275/4/7c64f887-3c3c-4bdf-8472-72d6b96f8e3d/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/275/4/7c64f887-3c3c-4bdf-8472-72d6b96f8e3d/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/275) — developer.apple.com. Indexed for agent consumption._