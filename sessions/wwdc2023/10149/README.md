---
id: "wwdc2023-10149"
event: "wwdc2023"
year: 2023
title: "Discover Observation in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10149"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Discover Observation in SwiftUI

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10149](https://developer.apple.com/videos/play/wwdc2023/10149)

Simplify your SwiftUI data models with Observation. We’ll share how the Observable macro can help you simplify models and improve your app’s performance. Get to know Observation, learn the fundamentals of the macro, and find out how to migrate from ObservableObject to Observable.


## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,663 words)

## Code Snippets

### Using @Observable — [1:26]

```swift
@Observable class FoodTruckModel {    
    var orders: [Order] = []
    var donuts = Donut.all
}
```

### SwiftUI property tracking — [2:12]

```swift
@Observable class FoodTruckModel {    
  var orders: [Order] = []
  var donuts = Donut.all
}

struct DonutMenu: View {
  let model: FoodTruckModel

  var body: some View {
    List {
      Section("Donuts") {
        ForEach(model.donuts) { donut in
          Text(donut.name)
        }
        Button("Add new donut") {
          model.addDonut()
        }
      }
    }
  }
}
```

### SwiftUI computed property tracking — [3:12]

```swift
@Observable class FoodTruckModel {    
  var orders: [Order] = []
  var donuts = Donut.all   var orderCount: Int { orders.count }
}

struct DonutMenu: View {
  let model: FoodTruckModel

  var body: some View {
    List {
      Section("Donuts") {
        ForEach(model.donuts) { donut in
          Text(donut.name)
        }
        Button("Add new donut") {
          model.addDonut()
        }
      }
      Section("Orders") {
        LabeledContent("Count", value: "\(model.orderCount)")
      }
    }
  }
}
```

### Using @State — [4:41]

```swift
struct DonutListView: View {
    var donutList: DonutList
    @State private var donutToAdd: Donut?

    var body: some View {
        List(donutList.donuts) { DonutView(donut: $0) }
        Button("Add Donut") { donutToAdd = Donut() }
            .sheet(item: $donutToAdd) {
                TextField("Name", text: $donutToAdd.name)
                Button("Save") {
                    donutList.donuts.append(donutToAdd)
                    donutToAdd = nil
                }
                Button("Cancel") { donutToAdd = nil }
            }
    }
}
```

### Using @Environment — [5:14]

```swift
@Observable class Account {
  var userName: String?
}

struct FoodTruckMenuView : View {
  @Environment(Account.self) var account

  var body: some View {
    if let name = account.userName {
      HStack { Text(name); Button("Log out") { account.logOut() } }
    } else {
      Button("Login") { account.showLogin() }
    }
  }
}
```

### Using @Bindable — [6:27]

```swift
@Observable class Donut {
  var name: String
}

struct DonutView: View {
  @Bindable var donut: Donut

  var body: some View {
    TextField("Name", text: $donut.name)
  }
}
```

### Storing @Observable types in Array — [7:53]

```swift
@Observable class Donut {
  var name: String
}

struct DonutList: View {
  var donuts: [Donut]
  var body: some View {
    List(donuts) { donut in
      HStack {
        Text(donut.name)
        Spacer()
        Button("Randomize") {
          donut.name = randomName()
        }
      }
    }
  }
}
```

### Manual Observation — [9:18]

```swift
@Observable class Donut {
  var name: String {
    get {
      access(keyPath: \.name)
      return someNonObservableLocation.name 
    }
    set {
      withMutation(keyPath: \.name) {
        someNonObservableLocation.name = newValue
      }
    }
  } 
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10149/4/F4769BC3-3B47-49AF-B11B-6957B0A25574/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10149/4/F4769BC3-3B47-49AF-B11B-6957B0A25574/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10149) — developer.apple.com. Indexed for agent consumption._