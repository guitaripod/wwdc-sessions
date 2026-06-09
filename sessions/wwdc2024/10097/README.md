---
id: "wwdc2024-10097"
event: "wwdc2024"
year: 2024
title: "Unlock the power of places with MapKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10097"
topics: ["App Services", "Safari & Web", "Maps & Location"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Unlock the power of places with MapKit

**Event:** WWDC24 · **Topic:** Maps & Location · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10097](https://developer.apple.com/videos/play/wwdc2024/10097)

Discover powerful new ways to integrate maps into your apps and websites with MapKit and MapKit JS.  Learn how to save and reference unique places using Place ID. Check out improvements to search that make it more efficient to find relevant places.  Get introduced to the new Place Card API that lets you display rich information about places so customers can explore destinations right in your app. And, we’ll show you quick ways to embed maps in your website with our simplified token provisioning and Web Embed API.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,942 words)

## Documentation & Resources

- [Displaying place information using the Maps Embed API](https://developer.apple.com/documentation/MapKitJS/displaying-place-information-using-the-maps-embed-api) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MapKitJS/displaying-place-information-using-the-maps-embed-api
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MapKitJS/displaying-place-information-using-the-maps-embed-api.json
- [Identifying unique locations with Place IDs](https://developer.apple.com/documentation/MapKit/identifying-unique-locations-with-place-ids) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MapKit/identifying-unique-locations-with-place-ids
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MapKit/identifying-unique-locations-with-place-ids.json
- [Resources - Apple Maps - Apple Developer](https://developer.apple.com/maps/resources/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/maps/resources/
- [Forum: Maps & Location](https://developer.apple.com/forums/topics/maps-and-location?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/maps-and-location?cid=vf-a-0010
- [Interacting with nearby points of interest](https://developer.apple.com/documentation/MapKit/interacting-with-nearby-points-of-interest) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MapKit/interacting-with-nearby-points-of-interest
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MapKit/interacting-with-nearby-points-of-interest.json

## Code Snippets

### Display a visitor center annotation — [3:06]

```swift
// Display a visitor center annotation

struct PlaceMapView: View {
    var placeID: String // "I63802885C8189B2B"

    @State private var item: MKMapItem?

    var body: some View {
        Map {
            if let item {
                Marker(item: item)
            }
        }
        .task {
            guard let identifier = MKMapItem.Identifier(
                rawValue: placeID
            ) else {
                return
            }
            let request = MKMapItemRequest(
                mapItemIdentifier: identifier
            )
            item = try? await request.mapItem
        }
    }
}
```

### Display an annotation for the center — [3:44]

```javascript
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    #map {
      margin: 0 auto;
    }
  </style>
</head>
<body>

<script
  crossorigin async
  src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.js"
  data-callback="entryPoint"
  data-token="TODO: Add your token here"
></script>

<script>
window.entryPoint = () => {
  const id = "I63802885C8189B2B";
  const lookup = new mapkit.PlaceLookup();
  lookup.getPlace(id, annotatePlace);
};

const annotatePlace = (error, place) => {
  const center = place.coordinate;
  const span = new mapkit.CoordinateSpan(0.01, 0.01);
  const region = new mapkit.CoordinateRegion(center, span);
  const map = new mapkit.Map("map", { region });

  const annotation = new mapkit.PlaceAnnotation(place);
  map.addAnnotation(annotation);
};
</script>

<div id="map" style="width: 100dvw; height: 100dvh;"></div>

</body>

</html>
```

### Display my favorite apple stores — [7:32]

```swift
// Display my favorite apple stores

struct VisitedStoresView: View {
    var visitedStores: [MKMapItem]
    @State private var selection: MKMapItem?

    var body: some View {
        Map(selection: $selection) {
            ForEach(visitedStores, id: \.self) { store in
                Marker(item: store)
            }
            .mapItemDetailSelectionAccessory()
        }
    }
}
```

### Display a selectable annotation — [7:50]

```javascript
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    #map {
      margin: 0 auto;
    }
  </style>
</head>
<body>

<script
  crossorigin async
  src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.js"
  data-callback="entryPoint"
  data-token="TODO: Add your token here"
></script>

<script>
window.entryPoint = () => {
  const id = "I63802885C8189B2B";
  const lookup = new mapkit.PlaceLookup();
  lookup.getPlace(id, annotatePlace);
};

const annotatePlace = (error, place) => {
  const center = place.coordinate;
  const span = new mapkit.CoordinateSpan(0.01, 0.01);
  const region = new mapkit.CoordinateRegion(center, span);
  const map = new mapkit.Map("map", { region });

  const annotation = new mapkit.PlaceAnnotation(place);
  map.addAnnotation(annotation);

  const accessory = new mapkit.PlaceSelectionAccessory();
  annotation.selectionAccessory = accessory;
};
</script>

<div id="map" style="width: 100dvw; height: 100dvh;"></div>

</body>

</html>
```

### List stores and show details when selected — [9:15]

```swift
// List stores and show details when selected

struct StoreList: View {
    var stores: [MKMapItem]
    @State private var selectedStore: MKMapItem?

    var body: some View {
        List(
            stores,
            id: \.self,
            selection: $selectedStore
        ) {
            Text($0.name ?? "Apple Store")
        }
        .mapItemDetailSheet(item: $selectedStore)
    }
}
```

### Show visitor center details — [9:37]

```javascript
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    #map {
      margin: 0 auto;
    }
  </style>
</head>
<body>

<script
  crossorigin async
  src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.js"
  data-callback="entryPoint"
  data-token="TODO: Add your token here"
></script>

<script>
window.entryPoint = () => {
  const id = "I63802885C8189B2B";
  const lookup = new mapkit.PlaceLookup();
  lookup.getPlace(id, annotatePlace);
};

const annotatePlace = (error, place) => {
  const el = document.getElementById("place");
  const detail = new mapkit.PlaceDetail(el, place, {
    colorScheme: mapkit.PlaceDetail.ColorSchemes.Adaptive
  });
};
</script>

<div id="place"></div>

</body>

</html>
```

### Display a place card for the selected map feature, too — [11:17]

```swift
// Display a place card for the selected map feature, too

struct VisitedStoresView: View {
    var visitedStores: [MKMapItem]
    @State private var selection: MapSelection<MKMapItem>?

    var body: some View {
        Map(selection: $selection) {
            ForEach(visitedStores, id: \.self) { store in
                Marker(item: store)
                    .tag(MapSelection(store))
            }
            .mapItemDetailSelectionAccessory(.callout)
        }
        .mapFeatureSelectionAccessory(.callout)
    }
}
```

### Find Cupertino, then find coffee — [13:09]

```javascript
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    #map {
      margin: 0 auto;
    }
  </style>
</head>
<body>

<script
  crossorigin async
  src="https://cdn.apple-mapkit.com/mk/5.x.x/mapkit.js"
  data-callback="entryPoint"
  data-token="TODO: Add your token here"
></script>

<script>
window.entryPoint = () => {
  const addressFilter = mapkit.AddressFilter.including([
    mapkit.AddressCategory.Locality
  ]);
  const citySearch = new mapkit.Search({ addressFilter });
  citySearch.search("Cupertino", showMap);
};

const showMap = (error, cities) => {
  const center = cities.places[0].coordinate;
  const span = new mapkit.CoordinateSpan(0.01, 0.01);
  const region = new mapkit.CoordinateRegion(center, span);
  const map = new mapkit.Map("map", { region });

  const coffeeSearch = new mapkit.Search({
    region,
    regionPriority: mapkit.Search.RegionPriority.Required,
    pointOfInterestFilter: mapkit.PointOfInterestFilter.including([
      mapkit.PointOfInterestCategory.Cafe
    ])
  });
  coffeeSearch.search("coffee", (error, results) => {
    for (const place of results.places) {
      const marker = new mapkit.PlaceAnnotation(place);
      map.addAnnotation(marker);
    }
  });
};
</script>

<div id="map" style="width: 100dvw; height: 100dvh;"></div>

</body>

</html>
```

### Finding coffee in Cupertino — [14:41]

```swift
// Finding coffee in Cupertino

struct CoffeeMap: View {
    @State private var position: MapCameraPosition = .automatic
    @State private var coffeeShops: [MKMapItem] = []

    var body: some View {
        Map(position: $position) {
            ForEach(coffeeShops, id: \.self) { café in
                Marker(item: cafe)
            }
        }
        .task {
            guard let cupertino = await findCity() else {
                return
            }
            coffeeShops = await findCoffee(in: cupertino)
        }
    }

    private func findCity() async -> MKMapItem? {
        let request = MKLocalSearch.Request()
        request.naturalLanguageQuery = "cupertino"

        request.addressFilter = MKAddressFilter(
            including: .locality
        )

        let search = MKLocalSearch(request: request)
        let response = try? await search.start()
        return response?.mapItems.first
    }

    private func findCoffee(in city: MKMapItem ) async -> [MKMapItem] {
        let request = MKLocalSearch.Request()
        request.naturalLanguageQuery = "coffee"
        let downtown = MKCoordinateRegion(
            center: city.placemark.coordinate,
            span: .init(
                latitudeDelta: 0.01,
                longitudeDelta: 0.01
            )
        )
        request.region = downtown
        request.regionPriority = .required
        let search = MKLocalSearch(request: request)
        let response = try? await search.start()
        return response?.mapItems ?? []
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10097/4/D991C391-4CC9-4A32-A10F-9D4DC6D7B615/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10097/4/D991C391-4CC9-4A32-A10F-9D4DC6D7B615/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10097) — developer.apple.com. Indexed for agent consumption._