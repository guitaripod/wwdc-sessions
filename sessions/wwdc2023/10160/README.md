---
id: "wwdc2023-10160"
event: "wwdc2023"
year: 2023
title: "Demystify SwiftUI performance"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10160"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Demystify SwiftUI performance

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10160](https://developer.apple.com/videos/play/wwdc2023/10160)

Learn how you can build a mental model for performance in SwiftUI and write faster, more efficient code. We’ll share some of the common causes behind performance issues and help you triage hangs and hitches in SwiftUI to create more responsive views in your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,752 words)

## Code Snippets

### DogView — [3:59]

```swift
struct DogView: View {
  @Environment(\.isPlayTime) private var isPlayTime
  var dog: Dog
  var body: some View {
  	Text(dog.name)
  		.font(nameFont)
  	Text(dog.breed)
  		.font(breedFont)
  		.foregroundStyle(.secondary)

  	ScalableDogImage(dog)

  	DogDetailView(dog)

  	LetsPlayButton()
  		.disabled(dog.isTired)
  }
 }
}
```

### ScalableDogImage — [4:00]

```swift
struct ScalableDogImage: View {
	@State private var scaleToFill = false
	var dog: Dog

	var body: some View {
		dog.image
			.resizable()
			.aspectRatio(
				contentMode: scaleToFill ? .fill : .fit)
			.frame(maxHeight: scaleToFill ? 500 : nil)
			.padding(.vertical, 16)
			.onTapGesture {
				withAnimation { scaleToFill.toggle() }
			}
	}
}
```

### printChanges — [4:01]

```bash
expression Self._printChanges()
```

### ScalableDogImage + printChanges — [4:02]

```swift
struct ScalableDogImage: View {
	@State private var scaleToFill = false
	var dog: Dog

	var body: some View {
    let _ = Self._printChanges()
		dog.image
			.resizable()
			.aspectRatio(
				contentMode: scaleToFill ? .fill : .fit)
			.frame(maxHeight: scaleToFill ? 500 : nil)
			.padding(.vertical, 16)
			.onTapGesture {
				withAnimation { scaleToFill.toggle() }
			}
	}
}
```

### ScaleableDogImage — [8:46]

```swift
struct ScalableDogImage: View {
	@State private var scaleToFill = false
	var dog: Dog

	var body: some View {
		dog.image
			.resizable()
			.aspectRatio(
				contentMode: scaleToFill ? .fill : .fit)
			.frame(maxHeight: scaleToFill ? 500 : nil)
			.padding(.vertical, 16)
			.onTapGesture {
				withAnimation { scaleToFill.toggle() }
			}
	}
}
```

### Updated DogView — [8:47]

```swift
struct DogView: View {
  @Environment(\.isPlayTime) private var isPlayTime
  var dog: Dog
  var body: some View {
  	Text(dog.name)
  		.font(nameFont)
  	Text(dog.breed)
  		.font(breedFont)
  		.foregroundStyle(.secondary)

  	ScalableDogImage(dog)

  	DogDetailView(dog)

  	LetsPlayButton()
  		.disabled(dog.isTired)
  }
 }
}
```

### Final DogView — [8:48]

```swift
struct DogView: View {
  @Environment(\.isPlayTime) private var isPlayTime
  var dog: Dog
  var body: some View {
  	DogHeader(name: dog.name, breed: dog.breed)

  	ScalableDogImage(dog.image)

  	DogDetailView(dog)

  	LetsPlayButton()
  		.disabled(dog.isTired)
  }
 }
}
```

### DogRootView and FetchModel — [12:22]

```swift
struct DogRootView: View {
	@State private var model = FetchModel()

	var body: some View {
		DogList(model.dogs)
	}
}

@Observable class FetchModel {
	var dogs: [Dog]

	init() {
		fetchDogs()
	}

	func fetchDogs() {
		// Takes a long time
	}
}
```

### Updated DogRootView and FetchModel — [12:23]

```swift
struct DogRootView: View {
	@State private var model = FetchModel()

	var body: some View {
		DogList(model.dogs)
			.task { await model.fetchDogs() }
	}
}

@Observable class FetchModel {
	var dogs: [Dog]

	init() {}

	func fetchDogs() async {
		// Takes a long time
	}
}
```

### List — [15:12]

```swift
List {
	ForEach(dogs) {
		DogCell(dog: $0)
	}
}
```

### List Again — [16:08]

```swift
List {
	ForEach(dogs) {
		DogCell(dog: $0)
	}
}
```

### List Fixed — [17:35]

```swift
List {
	ForEach(tennisBallDogs) { dog in
		DogCell(dog)
	}
}
```

### Sectioned List — [18:25]

```swift
// Sectioned example
struct DogsByToy: View {
	var model: DogModel
	var body: some View {
		List {
			ForEach(model.dogToys) { toy in
				Section(toy.name) {
					ForEach(model.dogs(toy: toy)) { dog in
						DogCell(dog)
					}
				}
			}
		}
	}
}
```

### DogTable — [19:21]

```swift
struct DogTable: View {
	var dogs: [Dog]
	var body: some View {
		Table(of: Dog.self) {
			// Columns
		} rows: {
			ForEach(dogs) { dog in
				TableRow(dog)
			}
		}
	}
}
```

### DogTable Brief — [19:22]

```swift
struct DogTable: View {
	var dogs: [Dog]
	var body: some View {
		Table(of: Dog.self) {
			// Columns
		} rows: {
			ForEach(dogs)
		}
	}
}
```

### DogTable Different IDs — [20:06]

```swift
struct DogTable: View {
	var dogs: [Dog]
	var body: some View {
		Table(of: Dog.self) {
			// Columns
		} rows: {
			ForEach(dogs) { dog in
				TableRow(dog.bestFriend)
			}
		}
	}
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10160/4/0FB203F2-03CD-4D44-B33B-C568C5A64F63/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10160/4/0FB203F2-03CD-4D44-B33B-C568C5A64F63/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10160) — developer.apple.com. Indexed for agent consumption._