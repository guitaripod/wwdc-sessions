---
id: "wwdc2025-306"
event: "wwdc2025"
year: 2025
title: "Optimize SwiftUI performance with Instruments"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/306"
topics: ["Swift", "SwiftUI & UI Frameworks", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Optimize SwiftUI performance with Instruments

**Event:** WWDC25 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-306](https://developer.apple.com/videos/play/wwdc2025/306)

Discover the new SwiftUI instrument. We’ll cover how SwiftUI updates views, how changes in your app’s data affect those updates, and how the new instrument helps you visualize those causes and effects. 

To get the most out of this session, we recommend being familiar with writing apps in SwiftUI.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,679 words)

## Documentation & Resources

- [Performance and metrics](https://developer.apple.com/documentation/Xcode/performance-and-metrics) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/performance-and-metrics
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/performance-and-metrics.json
- [Measuring your app’s power use with Power Profiler](https://developer.apple.com/documentation/Xcode/measuring-your-app-s-power-use-with-power-profiler) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/measuring-your-app-s-power-use-with-power-profiler
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/measuring-your-app-s-power-use-with-power-profiler.json
- [Understanding and improving SwiftUI performance](https://developer.apple.com/documentation/Xcode/understanding-and-improving-swiftui-performance) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/understanding-and-improving-swiftui-performance
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/understanding-and-improving-swiftui-performance.json
- [Analyzing the performance of your visionOS app](https://developer.apple.com/documentation/visionOS/analyzing-the-performance-of-your-visionOS-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/analyzing-the-performance-of-your-visionOS-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/analyzing-the-performance-of-your-visionOS-app.json
- [Improving app responsiveness](https://developer.apple.com/documentation/Xcode/improving-app-responsiveness) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/improving-app-responsiveness
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/improving-app-responsiveness.json

## Code Snippets

### LandmarkListItemView — [8:47]

```swift
import SwiftUI
import CoreLocation

/// A view that shows a single landmark in a list.
struct LandmarkListItemView: View {
    @Environment(ModelData.self) private var modelData

    let landmark: Landmark

    var body: some View {
        Image(landmark.thumbnailImageName)
            .resizable()
            .aspectRatio(contentMode: .fill)
            .frame(minWidth: 0, maxWidth: .infinity, minHeight: 0, maxHeight: .infinity)
            .overlay { ... }
            .clipped()
            .cornerRadius(Constants.cornerRadius)
            .overlay(alignment: .bottom) {
                VStack(spacing: 6) {
                    Text(landmark.name)
                        .font(.title3).fontWeight(.semibold)
                        .multilineTextAlignment(.center)
                        .foregroundColor(.white)

                    if let distance {
                        Text(distance)
                            .font(.callout)
                            .foregroundStyle(.white.opacity(0.9))
                            .padding(.bottom)
                    }
                }
            }
            .contextMenu { ... }
    }

    private var distance: String? {
        guard let currentLocation = modelData.locationFinder.currentLocation else { return nil }
        let distance = currentLocation.distance(from: landmark.clLocation)

        let numberFormatter = NumberFormatter()
        numberFormatter.numberStyle = .decimal
        numberFormatter.maximumFractionDigits = 0

        let formatter = MeasurementFormatter()
        formatter.locale = Locale.current
        formatter.unitStyle = .medium
        formatter.unitOptions = .naturalScale
        formatter.numberFormatter = numberFormatter
        return formatter.string(from: Measurement(value: distance, unit: UnitLength.meters))
    }
}
```

### LocationFinder Class with Cached Distance Strings — [12:13]

```swift
import CoreLocation

/// A class the app uses to find the current location.
@Observable
class LocationFinder: NSObject {
    var currentLocation: CLLocation?
    private let currentLocationManager: CLLocationManager = CLLocationManager()

    private let formatter: MeasurementFormatter

    override init() {
        // Format the numeric distance
        let numberFormatter = NumberFormatter()
        numberFormatter.numberStyle = .decimal
        numberFormatter.maximumFractionDigits = 0

        // Format the measurement based on the current locale
        let formatter = MeasurementFormatter()
        formatter.locale = Locale.current
        formatter.unitStyle = .medium
        formatter.unitOptions = .naturalScale
        formatter.numberFormatter = numberFormatter
        self.formatter = formatter

        super.init()

        currentLocationManager.desiredAccuracy = kCLLocationAccuracyKilometer
        currentLocationManager.delegate = self
    }

    // MARK: - Landmark Distance

    var landmarks: [Landmark] = [] {
        didSet {
            updateDistances()
        }
    }

    private var distanceCache: [Landmark.ID: String] = [:]

    private func updateDistances() {
        guard let currentLocation else { return }

        // Populate the cache with each formatted distance string
        self.distanceCache = landmarks.reduce(into: [:]) { result, landmark in
            let distance = self.formatter.string(
                from: Measurement(
                    value: currentLocation.distance(from: landmark.clLocation),
                    unit: UnitLength.meters
                )
            )
            result[landmark.id] = distance
        }
    }

    // Call this function from the view to access the cached value
    func distance(from landmark: Landmark) -> String? {
        distanceCache[landmark.id]
    }
}

extension LocationFinder: CLLocationManagerDelegate {
    func locationManagerDidChangeAuthorization(_ manager: CLLocationManager) {
        switch currentLocationManager.authorizationStatus {
        case .authorizedWhenInUse, .authorizedAlways:
            currentLocationManager.requestLocation()
        case .notDetermined:
            currentLocationManager.requestWhenInUseAuthorization()
        default:
            currentLocationManager.stopUpdatingLocation()
        }
    }

    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        print("Found a location.")
        currentLocation = locations.last
        // Update the distance strings when the location changes
        updateDistances() 
    }

    func locationManager(_ manager: CLLocationManager, didFailWithError error: any Error) {
        print("Received an error while trying to find a location: \(error.localizedDescription).")
        currentLocationManager.stopUpdatingLocation()
    }
}
```

### LandmarkListItemView with Favorite Button — [16:51]

```swift
import SwiftUI
import CoreLocation

/// A view that shows a single landmark in a list.
struct LandmarkListItemView: View {
    @Environment(ModelData.self) private var modelData

    let landmark: Landmark

    var body: some View {
        Image(landmark.thumbnailImageName)
            .resizable()
            .aspectRatio(contentMode: .fill)
            .frame(minWidth: 0, maxWidth: .infinity, minHeight: 0, maxHeight: .infinity)
            .overlay { ... }
            .clipped()
            .cornerRadius(Constants.cornerRadius)
            .overlay(alignment: .bottom) { ... }
            .contextMenu { ... }
            .overlay(alignment: .topTrailing) {
                let isFavorite = modelData.isFavorite(landmark)
                Button {
                    modelData.toggleFavorite(landmark)
                } label: {
                    Label {
                        Text(isFavorite ? "Remove Favorite" : "Add Favorite")
                    } icon: {
                        Image(systemName: "heart")
                            .symbolVariant(isFavorite ? .fill : .none)
                            .contentTransition(.symbolEffect)
                            .font(.title)
                            .foregroundStyle(.background)
                            .shadow(color: .primary.opacity(0.25), radius: 2, x: 0, y: 0)
                    }
                }
                .labelStyle(.iconOnly)
                .padding()
            }
    }
}
```

### ModelData Class — [17:20]

```swift
/// A structure that defines a collection of landmarks.
@Observable
class LandmarkCollection: Identifiable {
    // ...
    var landmarks: [Landmark] = []
    // ...
}

/// A class the app uses to store and manage model data.
@Observable @MainActor
class ModelData {
    // ...
    var favoritesCollection: LandmarkCollection!
    // ...

    func isFavorite(_ landmark: Landmark) -> Bool {
        var isFavorite: Bool = false

        if favoritesCollection.landmarks.firstIndex(of: landmark) != nil {
            isFavorite = true
        }

        return isFavorite
    }

    func toggleFavorite(_ landmark: Landmark) {
        if isFavorite(landmark) {
            removeFavorite(landmark)
        } else {
            addFavorite(landmark)
        }
    }

    func addFavorite(_ landmark: Landmark) {
        favoritesCollection.landmarks.append(landmark)
    }

    func removeFavorite(_ landmark: Landmark) {
        if let landmarkIndex = favoritesCollection.landmarks.firstIndex(of: landmark) {
            favoritesCollection.landmarks.remove(at: landmarkIndex)
        }
    }
    // ...
}
```

### OnOffView — [20:50]

```swift
struct OnOffView: View {
    @State private var isOn = true
    var body: some View {
        Text(isOn ? "On" : "Off")
    }
}
```

### Favorites View Model Class — [29:21]

```swift
@Observable class ViewModel {
    var isFavorite: Bool

    init(isFavorite: Bool = false) {
        self.isFavorite = isFavorite
    }
}
```

### ModelData Class with New ViewModel — [29:21]

```swift
@Observable @MainActor
class ModelData {
    // ...
    var favoritesCollection: LandmarkCollection!
    // ...

    @Observable class ViewModel {
        var isFavorite: Bool
        init(isFavorite: Bool = false) {
            self.isFavorite = isFavorite
        }
    }

    // Don't observe this property because we only need to react to changes
    // to each view model individually, rather than the whole dictionary
    @ObservationIgnored private var viewModels: [Landmark.ID: ViewModel] = [:]

    private func viewModel(for landmark: Landmark) -> ViewModel {
        // Create a new view model for a landmark on first access
        if viewModels[landmark.id] == nil {
            viewModels[landmark.id] = ViewModel()
        }
        return viewModels[landmark.id]!
    }

    func isFavorite(_ landmark: Landmark) -> Bool {
        // When a SwiftUI view, such as LandmarkListItemView, calls
        // `isFavorite` from its body, accessing `isFavorite` on the 
        // view model here establishes a direct dependency between
        // the view and the view model
        viewModel(for: landmark).isFavorite
    }

    func toggleFavorite(_ landmark: Landmark) {
        if isFavorite(landmark) {
            removeFavorite(landmark)
        } else {
            addFavorite(landmark)
        }
    }

    func addFavorite(_ landmark: Landmark) {
        favoritesCollection.landmarks.append(landmark)
        viewModel(for: landmark).isFavorite = true
    }

    func removeFavorite(_ landmark: Landmark) {
        if let landmarkIndex = favoritesCollection.landmarks.firstIndex(of: landmark) {
            favoritesCollection.landmarks.remove(at: landmarkIndex)
        }
        viewModel(for: landmark).isFavorite = false
    }
    // ...
}
```

### Cause and effect: EnvironmentValues — [31:34]

```swift
struct View1: View {
    @Environment(\.colorScheme)
    private var colorScheme

    var body: some View {
        Text(colorScheme == .dark
                ? "Dark Mode"
                : "Light Mode")
    }
}

struct View2: View {
    @Environment(\.counter) private var counter

    var body: some View {
        Text("\(counter)")
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/306/4/cc55ba18-71e2-4481-8491-3473e650fdcc/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/306/4/cc55ba18-71e2-4481-8491-3473e650fdcc/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/306) — developer.apple.com. Indexed for agent consumption._