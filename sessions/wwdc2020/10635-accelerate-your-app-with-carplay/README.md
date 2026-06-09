---
id: "wwdc2020-10635"
event: "wwdc2020"
year: 2020
title: "Accelerate your app with CarPlay"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10635"
topics: ["App Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Accelerate your app with CarPlay

**Event:** WWDC20 · **Topic:** App Services · **Platforms:** iOS, iPadOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10635](https://developer.apple.com/videos/play/wwdc2020/10635)

CarPlay is the smarter, safer way for people to use iPhone in the car. We’ll show you how to build great apps for the car screen, and introduce you to developing CarPlay apps in categories like EV charging, parking, and quick food ordering. We'll also share how existing audio and communication apps can take advantage of improvements to the CarPlay framework to create a more flexible UI.

**Keywords:** `🚗`, `🚙`, `audio`, `car`, `communication`, `ev charging`, `navigation`, `parking`, `quick food ordering`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,001 words)

## Documentation & Resources

- [CarPlay for developers](https://developer.apple.com/carplay) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/carplay
- [Human Interface Guidelines: CarPlay](https://developer.apple.com/design/human-interface-guidelines/carplay) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/carplay

## Code Snippets

### CarPlay scene manifest — [4:24]

```xml
// CarPlay Scene Manifest

<key>UIApplicationSceneManifest</key>
<dict>
    <key>UISceneConfigurations</key>
	<dict>
		<key>CPTemplateApplicationSceneSessionRoleApplication</key>
		<array>
			<dict>
				<key>UISceneClassName</key>
				<string>CPTemplateApplicationScene</string>
				<key>UISceneConfigurationName</key>
				<string>MyApp—Car</string>
				<key>UISceneDelegateClassName</key>
				<string>MyApp.CarPlaySceneDelegate</string>
			</dict>
		</array>
	</dict>
</dict>
```

### CarPlay app lifecycle — [5:12]

```swift
// CarPlay App Lifecycle

import CarPlay

class CarPlaySceneDelegate: UIResponder, CPTemplateApplicationSceneDelegate {
    var interfaceController: CPInterfaceController?

    func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene,
            didConnect interfaceController: CPInterfaceController) {

        self.interfaceController = interfaceController
        let item = CPListItem(text: "Rubber Soul", detailText: "The Beatles") 
        let section = CPListSection(items: [item]) 
        let listTemplate = CPListTemplate(title: "Albums", sections: [section])
        interfaceController.setRootTemplate(listTemplate, animated: true)
    }

  func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene,
            didDisconnect interfaceController: CPInterfaceController) {
    self.interfaceController = nil
}
```

### Create a CPListTemplate — [5:54]

```swift
// CPListTemplate

import CarPlay

let item = CPListItem(text: "Rubber Soul", detailText: "The Beatles") 
let section = CPListSection(items: [item]) 
let listTemplate = CPListTemplate(title: "Albums", sections: [section]) 
self.interfaceController.pushTemplate(listTemplate, animated: true)
```

### Handle user selection in a list item — [6:09]

```swift
// CPListTemplate

import CarPlay

let item = CPListItem(text: "Rubber Soul", detailText: "The Beatles") 
item.listItemHandler = { item, completion, [weak self] in
    // Start playback, then...
    self?.interfaceController.pushTemplate(CPNowPlayingTemplate.shared, animated: true)
    completion()
}

// Later...
item.image = ...
```

### Create a CPTabBarTemplate — [7:58]

```swift
// CPTabBarTemplate

import CarPlay

let item = CPListItem(text: "Rubber Soul", detailText: "The Beatles") 
let section = CPListSection(items: [item]) 
let favorites = CPListTemplate(title: "Albums", sections: [section])
favorites.tabSystemItem = .favorites
favorites.showsTabBadge = true

let albums: CPGridTemplate = ...
albums.tabTitle = "Albums"
albums.tabImage = ...

let tabBarTemplate = CPTabBarTemplate(templates: [favorites, albums])
self.interfaceController.setRootTemplate(tabBarTemplate, animated: false)

// Later...
favorites.showsTabBadge = false
tabBarTemplate.updateTemplates([favorites, albums])
```

### Create a CPListImageRowItem — [9:34]

```swift
// List Items for Audio Apps

import CarPlay

let gridImages: [UIImage] = ...
let imageRowItem = CPListImageRowItem(text: "Recent Audiobooks", images: gridImages) 

imageRowItem.listItemHandler = { item, completion in
    print("Selected image row header!")
    completion()
}

imageRowItem.listImageRowHandler = { item, index, completion in
    print("Selected artwork at index \(index)!")
    completion()
}

let section = CPListSection(items: [imageRowItem]) 
let listTemplate = CPListTemplate(title: "Listen Now", sections: [section]) 
self.interfaceController.pushTemplate(listTemplate, animated: true)
```

### Configure the shared now playing template — [12:50]

```swift
// Now Playing Template

import CarPlay

class CarPlaySceneDelegate: UIResponder, CPTemplateApplicationSceneDelegate {

    func templateApplicationScene(_ templateApplicationScene: CPTemplateApplicationScene,
            didConnect interfaceController: CPInterfaceController) {

        let nowPlayingTemplate = CPNowPlayingTemplate.shared

        let rateButton = CPNowPlayingPlaybackRateButton() { button in

            // Change the playback rate!

        }
        nowPlayingTemplate.updateNowPlayingButtons([rateButton])
    }
}
```

### Handle Point of Interest Template map region changes — [19:46]

```swift
// CPPointOfInterestTemplateDelegate

func pointOfInterestTemplate(_ template: CPPointOfInterestTemplate, 
                             didChangeMapRegion region: MKCoordinateRegion) {

    self.locationManager.locations(for: region) { locations in
        template.setPointsOfInterest(locations, selectedIndex: 0)
    }
}
```

### Create points of interest — [20:23]

```swift
// CPPointOfInterest creation

func locations(for region: MKCoordinateRegion, 
               handler: ([CPPointOfInterest]) -> Void) {
    var tempateLocations: [CPPointOfInterest] = []

    for clientModel in self.executeQuery(for: region) {
        let templateModel : CPPointOfInterest = self.locations[clientModel.mapItem] ??
                CPPointOfInterest(location: clientModel.mapItem,
                                  title: clientModel.title,
                                  subtitle: clientModel.subtitle,
                                  informativeText: clientModel.informativeText,
                                  image: clientModel.mapImage)


        tempateLocations.append(templateModel)
    }
    handler(templateLocations)
}
```

### Point of interest selection buttons — [21:05]

```swift
// Point of Interest Template location selection

let primaryButton = CPPointOfInterestButton(title: "Select") { button, [weak self] in
            let selectedIndex = ...

            if selectedIndex != NSNotFound {
                // Remove any existing selected state on previous location
                self?.selectedLocation.image = defaultMapImage
                // Change annotation for selected POI
                self?.selectedLocation = templateModel
                templateModel.image = selectedMapImage
                // Update the template with new values
                self?.pointOfInterestTemplate.selectedIndex = selectedIndex
            }
        }

let templateModel: CPPointOfInterest = ...

templateModel.primaryButton = primaryButton
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10635/8/AE50DE64-E4A1-44A8-84A7-05B91F3FE006/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10635) — developer.apple.com. Indexed for agent consumption._
