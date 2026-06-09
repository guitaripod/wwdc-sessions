---
id: "wwdc2025-204"
event: "wwdc2025"
year: 2025
title: "Go further with MapKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/204"
topics: ["Maps & Location"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Go further with MapKit

**Event:** WWDC25 · **Topic:** Maps & Location · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-204](https://developer.apple.com/videos/play/wwdc2025/204)

Discover the latest updates to MapKit and MapKit JS. We’ll introduce a new type of directions — cycling — and show you how to enable 3D Look Around imagery on the web. Learn how the new Geocoding API supports conversion between coordinates and addresses, and how to use the Address Representations API to get the most appropriate address for a region. Then we’ll wrap it up with a new way of referencing places that ensures your app will work seamlessly with App Intents.

**Keywords:** `javascript`, `place`, `route`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,579 words)

## Documentation & Resources

- [Searching, displaying, and navigating to places](https://developer.apple.com/documentation/MapKit/searching-displaying-and-navigating-to-places) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MapKit/searching-displaying-and-navigating-to-places
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MapKit/searching-displaying-and-navigating-to-places.json
- [Adopting unified Maps URLs](https://developer.apple.com/documentation/MapKit/Unified-Map-URLs) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MapKit/Unified-Map-URLs
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MapKit/Unified-Map-URLs.json
- [Place ID Lookup](https://developer.apple.com/maps/place-id-lookup/) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/maps/place-id-lookup/

## Code Snippets

### Putting Marker on the Map with a coordinate — [4:49]

```swift
// Putting Marker on the Map with a coordinate

let annaLiviaCoordinates = CLLocationCoordinate2D(
    latitude: 53.347673,
    longitude: -6.290198
)
var body: some View {
    Map {
       Marker(
            "Anna Livia Fountain",
            coordinate: annaLiviaCoordinates
        )
    }
}
```

### Creating and resolving a PlaceDescriptor with coordinate PlaceRepresentation — [5:07]

```swift
// Creating and resolving a PlaceDescriptor with coordinate PlaceRepresentation

import GeoToolbox
import MapKit

let annaLiviaCoordinates = CLLocationCoordinate2D(
    latitude: 53.347673,
    longitude: -6.290198
)
let annaLiviaDescriptor =  PlaceDescriptor(
    representations: [.coordinate(annaLiviaCoordinates)],
    commonName: "Anna Livia Fountain"
)

let request = MKMapItemRequest(placeDescriptor: annaLiviaDescriptor)
do {
    annaLiviaMapItem = try await request.mapItem
} catch {
    print("Error resolving placeDescriptor: \(error)")
}
```

### Creating and resolving a PlaceDescriptor with address PlaceRepresentation — [5:56]

```swift
// Creating and resolving a PlaceDescriptor with address PlaceRepresentation

import GeoToolbox
import MapKit

let address = "121-122 James's St, Dublin 8"
let descriptor =  PlaceDescriptor(
    representations: [.address(address)],
    commonName: "Obelisk Fountain"
)

let request = MKMapItemRequest(placeDescriptor: descriptor)
do {
    obeliskFountain = try await request.mapItem
} catch {
    print("Error resolving placeDescriptor: \(error)")
}
```

### Creating a PlaceDescriptor with identifiers — [6:45]

```swift
// Creating a PlaceDescriptor with identifiers

import GeoToolbox

let annaLiviaCoordinates = CLLocationCoordinate2D(
    latitude: 53.347673,
    longitude: -6.290198
)
let identifiers = ["com.apple.MapKit" : "ICBB5FD7684CE949"]
let annaLiviaDescriptor =  PlaceDescriptor(
    representations: [.coordinate(annaLiviaCoordinates)],
    commonName: "Anna Livia Fountain",
    supportingRepresentations: [.serviceIdentifiers(identifiers)]
)
```

### Fetching a MapItem from a PlaceDescriptor — [7:28]

```swift
// Fetching a MapItem from a PlaceDescriptor

let request = MKMapItemRequest(placeDescriptor: descriptor)
let mapitem = try await request.mapItem
```

### Getting a PlaceDescriptor from a MapItem — [7:43]

```swift
// Getting a PlaceDescriptor from a MapItem

let descriptor = PlaceDescriptor(mapItem: mapitem)
```

### Place Card — [8:10]

```swift
// Place Card

var body: some View {
    Map {
        ForEach(fountains, id:\.name) { fountain in
            Marker(item: fountain)
                .mapItemDetailSelectionAccessory(.callout)
        }
    }
}
```

### Reverse geocode with MapKit — [10:45]

```swift
// Reverse geocode with MapKit

import MapKit

let millCreekCoordinates = CLLocation(latitude: 39.042617, longitude: -94.587526)
if let request = MKReverseGeocodingRequest(location: millCreekCoordinates) {
    do {
        let mapItems = try await request.mapItems
        millCreekMapItem = mapItems.first
    } catch {
        print("Error reverse geocoding location: \(error)")
    }
}
```

### Forward geocoding with MapKit — [13:50]

```swift
// Forward geocoding with MapKit

var body: some View {
    Map {
        if let mapItem {
            Marker(item: mapItem)
        }
    }
    .task {
        let request = MKGeocodingRequest(
            addressString: "1 Ferry Building, San Francisco"
        )
        do {
            mapItem = try await request?.mapItems.first
        } catch {
            print("Error geocoding location: \(error)")
        }
    }
}
```

### Allowing Map Selection — [14:38]

```swift
// Allowing Map Selection

@State var selectedItem: MKMapItem?

var body: some View {
    Map(selection: $selectedItem) {
       UserAnnotation()
       ForEach(fountains, id: \.self) { item in
          Marker(item: item)
       }
    }
    .onChange(of: selectedItem) {
       // Compute Route
    }
}
```

### Fetch a route — [15:00]

```swift
// Fetch a route

let request = MKDirections.Request()
request.source = MKMapItem.forCurrentLocation()
request.destination = selectedItem
let directions = MKDirections(request: request)
do {
    let response = try await directions.calculate()
    returnedRoutes = response.routes
} catch {
    print("Error calculating directions: \(error)")
}
```

### Fetch a cycling route — [16:06]

```swift
// Fetch a cycling route

let request = MKDirections.Request()
request.source = MKMapItem.forCurrentLocation()
request.destination = selectedItem
request.transportType = .cycling
let directions = MKDirections(request: request)
do {
    let response = try await directions.calculate()
    returnedRoutes = response.routes
} catch {
    print("Error calculating directions: \(error)")
}
```

### Display a route on the Map — [16:25]

```swift
// Display a route on the Map

Map {
    if let mapRoute {
        UserAnnotation()
        MapPolyline(mapRoute)
            .stroke(Color.blue, lineWidth: 5)
    }
}
```

### Cycling directions in MapKit JS — [16:40]

```javascript
// Cycling directions in MapKit JS

let directions = new mapkit.Directions();
directions.route ({
    origin: safariPlayground,
    destination: cherryHillFountain,
    transportType: mapkit.Directions.Transport.Cycling
}, (error, { routes: [{ polyline }] }) => {
    polyline.style.lineWidth = 5;
    map.showItems([
        new mapkit.PlaceAnnotation(place),
        new mapkit.PlaceAnnotation(
          place2,
          { selected: true }
        ),
        polyline
    ]);
});
```

### Look Around — [17:26]

```swift
// Look Around

var body: some View {
    Map {
        ForEach(fountains, id:\.name) { fountain in
            Marker(item: fountain)
       }
    }
    .overlay(alignment: .bottomLeading) {
        if (lookAroundScene != nil) {
            LookAroundPreview(scene: $lookAroundScene)
                .frame(width: 230, height: 140)
                .cornerRadius(10)
                .padding(8)
        }
    }
}
```

### Look Around View in MapKit JS — [18:10]

```javascript
// Look Around View in MapKit JS

const placeLookup = new mapkit.PlaceLookup();
const place = await new Promise(
    resolve => placeLookup.getPlace(
        "IBE1F65094A7A13B1",
        (error, result) => resolve(result)
    )
);

// Create an interactive look around view.
const lookAround = new mapkit.LookAround(
    document.getElementById("container"),
    place,
    options
);
```

### Look Around Options — [18:35]

```javascript
// Look Around Options for MapKit JS

const options = {
    // Enters a full window experience
    // immediately on load
    openDialog: true,

    // Provides a button to enter and
    // exit full window.
    showsDialogControl: true,

    // Provides a button to destroy
    // the look around view.
    showsCloseControl: true,
};
```

### Handle MapKit JS Look Around events — [19:10]

```javascript
// Handle MapKit JS Look Around events

lookAround.addEventListener(
    "close",
    event => {
        app.closeView();
        event.preventDefault();
    }
);

lookAround.addEventListener(
    "load",
    event => app.fadeInView()
);

lookAround.addEventListener(
    "error",
    event => app.fadeOutView()
);

lookAround.addEventListener(
    "readystatechange",
    event => console.log(lookAround.readyState)
);
```

### MapKit JS Look Around Preview — [20:01]

```javascript
// MapKit JS Look Around Preview

const lookAround = new mapkit.LookAroundPreview(
    document.getElementById("container"),
    place
);
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/204/5/38ed2a79-6f38-4c36-8d25-933f80d3b8ce/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/204/5/38ed2a79-6f38-4c36-8d25-933f80d3b8ce/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/204) — developer.apple.com. Indexed for agent consumption._
