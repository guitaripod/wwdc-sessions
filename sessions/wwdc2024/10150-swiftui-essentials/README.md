---
id: "wwdc2024-10150"
event: "wwdc2024"
year: 2024
title: "SwiftUI essentials"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10150"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# SwiftUI essentials

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10150](https://developer.apple.com/videos/play/wwdc2024/10150)

Join us on a tour of SwiftUI, Apple’s declarative user interface framework. Learn essential concepts for building apps in SwiftUI, like views, state variables, and layout. Discover the breadth of APIs for building fully featured experiences and crafting unique custom components. Whether you’re brand new to SwiftUI or an experienced developer, you’ll learn how to take advantage of what SwiftUI has to offer when building great apps.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,700 words)

## Documentation & Resources

- [SwiftUI Pathway](https://developer.apple.com/pathways/swiftui/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/pathways/swiftui/
- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010
- [Learning SwiftUI](https://developer.apple.com/tutorials/swiftui-concepts) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/tutorials/swiftui-concepts
- [SwiftUI](https://developer.apple.com/documentation/SwiftUI) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI.json

## Code Snippets

### Declarative views — [2:30]

```swift
Text("Whiskers")

Image(systemName: "cat.fill")

Button("Give Treat") {
   // Give Whiskers a treat
}
```

### Declarative views: layout — [2:43]

```swift
HStack {
   Label("Whiskers", systemImage: "cat.fill")

   Spacer()

   Text("Tightrope walking")
}
```

### Declarative views: list — [2:56]

```swift
struct ContentView: View {
    @State private var pets = Pet.samplePets

    var body: some View {
        List(pets) { pet in
            HStack {
                Label("Whiskers", systemImage: "cat.fill")

                Spacer()

                Text("Tightrope walking")
            }
        }
    }
}

struct Pet: Identifiable {
    enum Kind {
        case cat
        case dog
        case fish
        case bird
        case lizard
        case turtle
        case rabbit
        case bug

        var systemImage: String {
            switch self {
            case .cat: return "cat.fill"
            case .dog: return "dog.fill"
            case .fish: return "fish.fill"
            case .bird: return "bird.fill"
            case .lizard: return "lizard.fill"
            case .turtle: return "tortoise.fill"
            case .rabbit: return "rabbit.fill"
            case .bug: return "ant.fill"
            }
        }
    }

    let id = UUID()
    var name: String
    var kind: Kind
    var trick: String

    init(_ name: String, kind: Kind, trick: String) {
        self.name = name
        self.kind = kind
        self.trick = trick
    }

    static let samplePets = [
        Pet("Whiskers", kind: .cat, trick: "Tightrope walking"),
        Pet("Roofus", kind: .dog, trick: "Home runs"),
        Pet("Bubbles", kind: .fish, trick: "100m freestyle"),
        Pet("Mango", kind: .bird, trick: "Basketball dunk"),
        Pet("Ziggy", kind: .lizard, trick: "Parkour"),
        Pet("Sheldon", kind: .turtle, trick: "Kickflip"),
        Pet("Chirpy", kind: .bug, trick: "Canon in D")
    ]
}
```

### Declarative views: list — [3:07]

```swift
struct ContentView: View {
    @State private var pets = Pet.samplePets

    var body: some View {
        List(pets) { pet in
            HStack {
                Label(pet.name, systemImage: pet.kind.systemImage)

                Spacer()

                Text(pet.trick)
            }
        }
    }
}

struct Pet: Identifiable {
    enum Kind {
        case cat
        case dog
        case fish
        case bird
        case lizard
        case turtle
        case rabbit
        case bug

        var systemImage: String {
            switch self {
            case .cat: return "cat.fill"
            case .dog: return "dog.fill"
            case .fish: return "fish.fill"
            case .bird: return "bird.fill"
            case .lizard: return "lizard.fill"
            case .turtle: return "tortoise.fill"
            case .rabbit: return "rabbit.fill"
            case .bug: return "ant.fill"
            }
        }
    }

    let id = UUID()
    var name: String
    var kind: Kind
    var trick: String

    init(_ name: String, kind: Kind, trick: String) {
        self.name = name
        self.kind = kind
        self.trick = trick
    }

    static let samplePets = [
        Pet("Whiskers", kind: .cat, trick: "Tightrope walking"),
        Pet("Roofus", kind: .dog, trick: "Home runs"),
        Pet("Bubbles", kind: .fish, trick: "100m freestyle"),
        Pet("Mango", kind: .bird, trick: "Basketball dunk"),
        Pet("Ziggy", kind: .lizard, trick: "Parkour"),
        Pet("Sheldon", kind: .turtle, trick: "Kickflip"),
        Pet("Chirpy", kind: .bug, trick: "Canon in D")
    ]
}
```

### Declarative and imperative programming — [4:24]

```swift
struct ContentView: View {
    @State private var pets = Pet.samplePets

    var body: some View {
        Button("Add Pet") {
            pets.append(Pet("Toby", kind: .dog, trick: "WWDC Presenter"))
        }

        List(pets) { pet in
            HStack {
                Label(pet.name, systemImage: pet.kind.systemImage)

                Spacer()

                Text(pet.trick)
            }
        }
    }
}

struct Pet: Identifiable {
    enum Kind {
        case cat
        case dog
        case fish
        case bird
        case lizard
        case turtle
        case rabbit
        case bug

        var systemImage: String {
            switch self {
            case .cat: return "cat.fill"
            case .dog: return "dog.fill"
            case .fish: return "fish.fill"
            case .bird: return "bird.fill"
            case .lizard: return "lizard.fill"
            case .turtle: return "tortoise.fill"
            case .rabbit: return "rabbit.fill"
            case .bug: return "ant.fill"
            }
        }
    }

    let id = UUID()
    var name: String
    var kind: Kind
    var trick: String

    init(_ name: String, kind: Kind, trick: String) {
        self.name = name
        self.kind = kind
        self.trick = trick
    }

    static let samplePets = [
        Pet("Whiskers", kind: .cat, trick: "Tightrope walking"),
        Pet("Roofus", kind: .dog, trick: "Home runs"),
        Pet("Bubbles", kind: .fish, trick: "100m freestyle"),
        Pet("Mango", kind: .bird, trick: "Basketball dunk"),
        Pet("Ziggy", kind: .lizard, trick: "Parkour"),
        Pet("Sheldon", kind: .turtle, trick: "Kickflip"),
        Pet("Chirpy", kind: .bug, trick: "Canon in D")
    ]
}
```

### Layout container — [5:33]

```swift
HStack {
   Label("Whiskers", systemImage: "cat.fill")

   Spacer()

   Text("Tightrope walking")
}
```

### Container views — [5:41]

```swift
struct ContentView: View {
    var body: some View {
        HStack {
            Image(whiskers.profileImage)

            VStack(alignment: .leading) {
                Label("Whiskers", systemImage: "cat.fill")
                Text("Tightrope walking")
            }

            Spacer()
        }
    }
}

let whiskers = Pet("Whiskers", kind: .cat, trick: "Tightrope walking", profileImage: "Whiskers")

struct Pet: Identifiable {
    enum Kind {
        case cat
        case dog
        case fish
        case bird
        case lizard
        case turtle
        case rabbit
        case bug

        var systemImage: String {
            switch self {
            case .cat: return "cat.fill"
            case .dog: return "dog.fill"
            case .fish: return "fish.fill"
            case .bird: return "bird.fill"
            case .lizard: return "lizard.fill"
            case .turtle: return "tortoise.fill"
            case .rabbit: return "rabbit.fill"
            case .bug: return "ant.fill"
            }
        }
    }

    let id = UUID()
    var name: String
    var kind: Kind
    var trick: String
    var profileImage: String

    init(_ name: String, kind: Kind, trick: String, profileImage: String) {
        self.name = name
        self.kind = kind
        self.trick = trick
        self.profileImage = profileImage
    }
}
```

### View modifiers — [6:23]

```swift
struct ContentView: View {
    var body: some View {
        Image(whiskers.profileImage)
            .clipShape(.circle)
            .shadow(radius: 3)
            .overlay {
                Circle().stroke(.green, lineWidth: 2)
            }
    }
}

let whiskers = Pet("Whiskers", kind: .cat, trick: "Tightrope walking", profileImage: "Whiskers")

struct Pet: Identifiable {
    enum Kind {
        case cat
        case dog
        case fish
        case bird
        case lizard
        case turtle
        case rabbit
        case bug

        var systemImage: String {
            switch self {
            case .cat: return "cat.fill"
            case .dog: return "dog.fill"
            case .fish: return "fish.fill"
            case .bird: return "bird.fill"
            case .lizard: return "lizard.fill"
            case .turtle: return "tortoise.fill"
            case .rabbit: return "rabbit.fill"
            case .bug: return "ant.fill"
            }
        }
    }

    let id = UUID()
    var name: String
    var kind: Kind
    var trick: String
    var profileImage: String

    init(_ name: String, kind: Kind, trick: String, profileImage: String) {
        self.name = name
        self.kind = kind
        self.trick = trick
        self.profileImage = profileImage
    }
}
```

### Custom views: Intro — [7:05]

```swift
struct PetRowView: View {
    var body: some View {
       // ...
    }
}
```

### Custom views — [7:14]

```swift
struct PetRowView: View {
    var body: some View {
        Image(whiskers.profileImage)
            .clipShape(.circle)
            .shadow(radius: 3)
            .overlay {
                Circle().stroke(.green, lineWidth: 2)
            }
    }
}

let whiskers = Pet("Whiskers", kind: .cat, trick: "Tightrope walking", profileImage: "Whiskers")

struct Pet: Identifiable {
    enum Kind {
        case cat
        case dog
        case fish
        case bird
        case lizard
        case turtle
        case rabbit
        case bug

        var systemImage: String {
            switch self {
            case .cat: return "cat.fill"
            case .dog: return "dog.fill"
            case .fish: return "fish.fill"
            case .bird: return "bird.fill"
            case .lizard: return "lizard.fill"
            case .turtle: return "tortoise.fill"
            case .rabbit: return "rabbit.fill"
            case .bug: return "ant.fill"
            }
        }
    }

    let id = UUID()
    var name: String
    var kind: Kind
    var trick: String
    var profileImage: String

    init(_ name: String, kind: Kind, trick: String, profileImage: String) {
        self.name = name
        self.kind = kind
        self.trick = trick
        self.profileImage = profileImage
    }
}
```

### Custom views: iteration — [7:20]

```swift
struct PetRowView: View {
    var body: some View {
        HStack {
            Image(whiskers.profileImage)
                .clipShape(.circle)
                .shadow(radius: 3)
                .overlay {
                    Circle()
                        .stroke(.green, lineWidth: 2)
                }

            Text("Whiskers")

            Spacer()
        }
    }
}

let whiskers = Pet("Whiskers", kind: .cat, trick: "Tightrope walking", profileImage: "Whiskers")

struct Pet: Identifiable {
    enum Kind {
        case cat
        case dog
        case fish
        case bird
        case lizard
        case turtle
        case rabbit
        case bug

        var systemImage: String {
            switch self {
            case .cat: return "cat.fill"
            case .dog: return "dog.fill"
            case .fish: return "fish.fill"
            case .bird: return "bird.fill"
            case .lizard: return "lizard.fill"
            case .turtle: return "tortoise.fill"
            case .rabbit: return "rabbit.fill"
            case .bug: return "ant.fill"
            }
        }
    }

    let id = UUID()
    var name: String
    var kind: Kind
    var trick: String
    var profileImage: String

    init(_ name: String, kind: Kind, trick: String, profileImage: String) {
        self.name = name
        self.kind = kind
        self.trick = trick
        self.profileImage = profileImage
    }
}
```

### Custom views: view properties — [7:24]

```swift
struct PetRowView: View {
    var body: some View {
        HStack {
            profileImage

            Text("Whiskers")

            Spacer()
        }
    }

    private var profileImage: some View {
        Image(whiskers.profileImage)
            .clipShape(.circle)
            .shadow(radius: 3)
            .overlay {
                Circle().stroke(.green, lineWidth: 2)
            }
    }
}

let whiskers = Pet("Whiskers", kind: .cat, trick: "Tightrope walking", profileImage: "Whiskers")

struct Pet: Identifiable {
    enum Kind {
        case cat
        case dog
        case fish
        case bird
        case lizard
        case turtle
        case rabbit
        case bug

        var systemImage: String {
            switch self {
            case .cat: return "cat.fill"
            case .dog: return "dog.fill"
            case .fish: return "fish.fill"
            case .bird: return "bird.fill"
            case .lizard: return "lizard.fill"
            case .turtle: return "tortoise.fill"
            case .rabbit: return "rabbit.fill"
            case .bug: return "ant.fill"
            }
        }
    }

    let id = UUID()
    var name: String
    var kind: Kind
    var trick: String
    var profileImage: String

    init(_ name: String, kind: Kind, trick: String, profileImage: String) {
        self.name = name
        self.kind = kind
        self.trick = trick
        self.profileImage = profileImage
    }
}
```

### Custom views: complete row view — [7:34]

```swift
struct PetRowView: View {
    var body: some View {
        HStack {
            profileImage

            VStack(alignment: .leading) {
                Text("Whiskers")
                Text("Tightrope walking")
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }

            Spacer()
        }
    }

    private var profileImage: some View {
        Image(whiskers.profileImage)
            .clipShape(.circle)
            .shadow(radius: 3)
            .overlay {
                Circle().stroke(.green, lineWidth: 2)
            }
    }
}

let whiskers = Pet("Whiskers", kind: .cat, trick: "Tightrope walking", profileImage: "Whiskers")

struct Pet: Identifiable {
    enum Kind {
        case cat
        case dog
        case fish
        case bird
        case lizard
        case turtle
        case rabbit
        case bug

        var systemImage: String {
            switch self {
            case .cat: return "cat.fill"
            case .dog: return "dog.fill"
            case .fish: return "fish.fill"
            case .bird: return "bird.fill"
            case .lizard: return "lizard.fill"
            case .turtle: return "tortoise.fill"
            case .rabbit: return "rabbit.fill"
            case .bug: return "ant.fill"
            }
        }
    }

    let id = UUID()
    var name: String
    var kind: Kind
    var trick: String
    var profileImage: String

    init(_ name: String, kind: Kind, trick: String, profileImage: String) {
        self.name = name
        self.kind = kind
        self.trick = trick
        self.profileImage = profileImage
    }
}
```

### Custom views: input properties — [7:41]

```swift
struct PetRowView: View {
    var pet: Pet
    var body: some View {
        HStack {
            profileImage

            VStack(alignment: .leading) {
                Text(pet.name)
                Text(pet.trick)
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }

            Spacer()
        }
    }

    private var profileImage: some View {
        Image(pet.profileImage)
            .clipShape(.circle)
            .shadow(radius: 3)
            .overlay {
                Circle().stroke(pet.favoriteColor, lineWidth: 2)
            }
    }
}

struct Pet: Identifiable {
    enum Kind {
        case cat
        case dog
        case fish
        case bird
        case lizard
        case turtle
        case rabbit
        case bug

        var systemImage: String {
            switch self {
            case .cat: return "cat.fill"
            case .dog: return "dog.fill"
            case .fish: return "fish.fill"
            case .bird: return "bird.fill"
            case .lizard: return "lizard.fill"
            case .turtle: return "tortoise.fill"
            case .rabbit: return "rabbit.fill"
            case .bug: return "ant.fill"
            }
        }
    }

    let id = UUID()
    var name: String
    var kind: Kind
    var trick: String
    var profileImage: String
    var favoriteColor: Color

    init(_ name: String, kind: Kind, trick: String, profileImage: String, favoriteColor: Color) {
        self.name = name
        self.kind = kind
        self.trick = trick
        self.profileImage = profileImage
        self.favoriteColor = favoriteColor
    }
}
```

### Custom views: reuse — [7:53]

```swift
PetRowView(pet: model.pet(named: "Whiskers"))

PetRowView(pet: model.pet(named: "Roofus"))

PetRowView(pet: model.pet(named: "Bubbles"))
```

### List composition — [7:59]

```swift
struct ContentView: View {
    var model: PetStore
    var body: some View {
        List(model.allPets) { pet in
            PetRowView(pet: pet)
        }
    }
}

@Observable
class PetStore {
    var allPets: [Pet] = [
        Pet("Whiskers", kind: .cat, trick: "Tightrope walking", profileImage: "Whiskers", favoriteColor: .green),
        Pet("Roofus", kind: .dog, trick: "Home runs", profileImage: "Roofus", favoriteColor: .blue),
        Pet("Bubbles", kind: .fish, trick: "100m freestyle", profileImage: "Bubbles", favoriteColor: .orange),
        Pet("Mango", kind: .bird,  trick: "Basketball dunk", profileImage: "Mango", favoriteColor: .green),
        Pet("Ziggy", kind: .lizard, trick: "Parkour", profileImage: "Ziggy", favoriteColor: .purple),
        Pet("Sheldon", kind: .turtle, trick: "Kickflip", profileImage: "Sheldon", favoriteColor: .brown),
        Pet("Chirpy", kind: .bug, trick: "Canon in D", profileImage: "Chirpy", favoriteColor: .orange)
    ]
}
```

### List composition: ForEach — [8:14]

```swift
struct ContentView: View {
    var model: PetStore
    var body: some View {
        List {
            ForEach(model.allPets) { pet in
                PetRowView(pet: pet)
            }
        }
    }
}

@Observable
class PetStore {
    var allPets: [Pet] = [
        Pet("Whiskers", kind: .cat, trick: "Tightrope walking", profileImage: "Whiskers", favoriteColor: .green),
        Pet("Roofus", kind: .dog, trick: "Home runs", profileImage: "Roofus", favoriteColor: .blue),
        Pet("Bubbles", kind: .fish, trick: "100m freestyle", profileImage: "Bubbles", favoriteColor: .orange),
        Pet("Mango", kind: .bird,  trick: "Basketball dunk", profileImage: "Mango", favoriteColor: .green),
        Pet("Ziggy", kind: .lizard, trick: "Parkour", profileImage: "Ziggy", favoriteColor: .purple),
        Pet("Sheldon", kind: .turtle, trick: "Kickflip", profileImage: "Sheldon", favoriteColor: .brown),
        Pet("Chirpy", kind: .bug, trick: "Canon in D", profileImage: "Chirpy", favoriteColor: .orange)
    ]
}
```

### List composition: sections — [8:27]

```swift
struct ContentView: View {
    var model: PetStore
    var body: some View {
        List {
            Section("My Pets") {
                ForEach(model.myPets) { pet in
                    PetRowView(pet: pet)
                }
            }
            Section("Other Pets") {
                ForEach(model.otherPets) { pet in
                    PetRowView(pet: pet)
                }
            }
        }
    }
}

@Observable
class PetStore {
    var myPets: [Pet] = [
        Pet("Roofus", kind: .dog, trick: "Home runs", profileImage: "Roofus", favoriteColor: .blue),
        Pet("Sheldon", kind: .turtle, trick: "Kickflip", profileImage: "Sheldon", favoriteColor: .brown),
    ]

    var otherPets: [Pet] = [
        Pet("Whiskers", kind: .cat, trick: "Tightrope walking", profileImage: "Whiskers", favoriteColor: .green),
        Pet("Bubbles", kind: .fish, trick: "100m freestyle", profileImage: "Bubbles", favoriteColor: .orange),
        Pet("Mango", kind: .bird,  trick: "Basketball dunk", profileImage: "Mango", favoriteColor: .green),
        Pet("Ziggy", kind: .lizard, trick: "Parkour", profileImage: "Ziggy", favoriteColor: .purple),
        Pet("Chirpy", kind: .bug, trick: "Canon in D", profileImage: "Chirpy", favoriteColor: .orange)
    ]
}
```

### List composition: section actions — [8:36]

```swift
PetRowView(pet: pet)
    .swipeActions(edge: .leading) {
        Button("Award", systemImage: "trophy") {
            // Give pet award
        }
        .tint(.orange)

        ShareLink(item: pet, preview: SharePreview("Pet", image: Image(pet.name)))
    }
```

### View updates — [9:31]

```swift
struct ContentView: View {
    var model: PetStore
    var body: some View {
        List {
            Section("My Pets") {
                ForEach(model.myPets) { pet in
                    row(pet: pet)
                }
            }
            Section("Other Pets") {
                ForEach(model.otherPets) { pet in
                    row(pet: pet)
                }
            }
        }
    }

    private func row(pet: Pet) -> some View {
        PetRowView(pet: pet)
            .swipeActions(edge: .leading) {
                Button("Award", systemImage: "trophy") {
                    pet.giveAward()
                }
                .tint(.orange)

                ShareLink(item: pet, preview: SharePreview("Pet", image: Image(pet.name)))
            }
    }
}

struct PetRowView: View {
    var pet: Pet
    var body: some View {
        HStack {
            profileImage

            VStack(alignment: .leading) {
                HStack(alignment: .firstTextBaseline) {
                    Text(pet.name)

                    if pet.hasAward {
                        Image(systemName: "trophy.fill")
                            .foregroundStyle(.orange)
                    }
                }
                Text(pet.trick)
                    .font(.subheadline)
                    .foregroundStyle(.secondary)
            }

            Spacer()
        }
    }

    private var profileImage: some View {
        Image(pet.profileImage)
            .clipShape(.circle)
            .shadow(radius: 3)
            .overlay {
                Circle().stroke(pet.favoriteColor, lineWidth: 2)
            }
    }
}

@Observable
class PetStore {
    var myPets: [Pet] = [
        Pet("Roofus", kind: .dog, trick: "Home runs", profileImage: "Roofus", favoriteColor: .blue),
        Pet("Sheldon", kind: .turtle, trick: "Kickflip", profileImage: "Sheldon", favoriteColor: .brown),
    ]

    var otherPets: [Pet] = [
        Pet("Whiskers", kind: .cat, trick: "Tightrope walking", profileImage: "Whiskers", favoriteColor: .green),
        Pet("Bubbles", kind: .fish, trick: "100m freestyle", profileImage: "Bubbles", favoriteColor: .orange),
        Pet("Mango", kind: .bird,  trick: "Basketball dunk", profileImage: "Mango", favoriteColor: .green),
        Pet("Ziggy", kind: .lizard, trick: "Parkour", profileImage: "Ziggy", favoriteColor: .purple),
        Pet("Chirpy", kind: .bug, trick: "Canon in D", profileImage: "Chirpy", favoriteColor: .orange)
    ]
}

@Observable
class Pet: Identifiable {
    enum Kind {
        case cat
        case dog
        case fish
        case bird
        case lizard
        case turtle
        case rabbit
        case bug

        var systemImage: String {
            switch self {
            case .cat: return "cat.fill"
            case .dog: return "dog.fill"
            case .fish: return "fish.fill"
            case .bird: return "bird.fill"
            case .lizard: return "lizard.fill"
            case .turtle: return "tortoise.fill"
            case .rabbit: return "rabbit.fill"
            case .bug: return "ant.fill"
            }
        }
    }

    var name: String
    var kind: Kind
    var trick: String
    var profileImage: String
    var favoriteColor: Color
    var hasAward: Bool = false

    init(_ name: String, kind: Kind, trick: String, profileImage: String, favoriteColor: Color) {
        self.name = name
        self.kind = kind
        self.trick = trick
        self.profileImage = profileImage
        self.favoriteColor = favoriteColor
    }

    func giveAward() {
        hasAward = true
    }
}

extension Pet: Transferable {
    static var transferRepresentation: some TransferRepresentation {
        ProxyRepresentation { $0.name }
    }
}
```

### State changes — [10:57]

```swift
struct RatingView: View {
    @State var rating: Int = 5

    var body: some View {
        HStack {
            Button("Decrease", systemImage: "minus.circle") {
                rating -= 1
            }
            .disabled(rating == 0)
            .labelStyle(.iconOnly)

            Text(rating, format: .number.precision(.integerLength(2)))
                .font(.title.bold())

            Button("Increase", systemImage: "plus.circle") {
                rating += 1
            }
            .disabled(rating == 10)
            .labelStyle(.iconOnly)
        }
    }
}
```

### State changes: animation — [11:51]

```swift
struct RatingView: View {
    @State var rating: Int = 5

    var body: some View {
        HStack {
            Button("Decrease", systemImage: "minus.circle") {
                withAnimation {
                    rating -= 1
                }
            }
            .disabled(rating == 0)
            .labelStyle(.iconOnly)

            Text(rating, format: .number.precision(.integerLength(2)))
                .font(.title.bold())

            Button("Increase", systemImage: "plus.circle") {
                withAnimation {
                    rating += 1
                }
            }
            .disabled(rating == 10)
            .labelStyle(.iconOnly)
        }
    }
}
```

### State changes: text content transition — [12:05]

```swift
struct RatingView: View {
    @State var rating: Int = 5

    var body: some View {
        HStack {
            Button("Decrease", systemImage: "minus.circle") {
                withAnimation {
                    rating -= 1
                }
            }
            .disabled(rating == 0)
            .labelStyle(.iconOnly)

            Text(rating, format: .number.precision(.integerLength(2)))
                .contentTransition(.numericText(value: Double(rating)))
                .font(.title.bold())

            Button("Increase", systemImage: "plus.circle") {
                withAnimation {
                    rating += 1
                }
            }
            .disabled(rating == 10)
            .labelStyle(.iconOnly)
        }
    }
}
```

### State changes: multiple state — [12:22]

```swift
struct RatingContainerView: View {
    @State private var rating: Int = 5

    var body: some View {
        Gauge(value: Double(rating), in: 0...10) {
            Text("Rating")
        }
        RatingView()
    }
}

struct RatingView: View {
    @State var rating: Int = 5

    var body: some View {
        HStack {
            Button("Decrease", systemImage: "minus.circle") {
                withAnimation {
                    rating -= 1
                }
            }
            .disabled(rating == 0)
            .labelStyle(.iconOnly)

            Text(rating, format: .number.precision(.integerLength(2)))
                .contentTransition(.numericText(value: Double(rating)))
                .font(.title.bold())

            Button("Increase", systemImage: "plus.circle") {
                withAnimation {
                    rating += 1
                }
            }
            .disabled(rating == 10)
            .labelStyle(.iconOnly)
        }
    }
}
```

### State changes: state and binding — [12:45]

```swift
struct RatingContainerView: View {
    @State private var rating: Int = 5

    var body: some View {
        Gauge(value: Double(rating), in: 0...10) {
            Text("Rating")
        }
        RatingView(rating: $rating)
    }
}

struct RatingView: View {
    @Binding var rating: Int

    var body: some View {
        HStack {
            Button("Decrease", systemImage: "minus.circle") {
                withAnimation {
                    rating -= 1
                }
            }
            .disabled(rating == 0)
            .labelStyle(.iconOnly)

            Text(rating, format: .number.precision(.integerLength(2)))
                .contentTransition(.numericText(value: Double(rating)))
                .font(.title.bold())

            Button("Increase", systemImage: "plus.circle") {
                withAnimation {
                    rating += 1
                }
            }
            .disabled(rating == 10)
            .labelStyle(.iconOnly)
        }
    }
}
```

### Adaptive buttons — [14:16]

```swift
Button("Reward", systemImage: "trophy") {
    // Give pet award
}
// .buttonStyle(.borderless)
// .buttonStyle(.bordered)
// .buttonStyle(.borderedProminent)
```

### Adaptive toggles — [14:53]

```swift
Toggle("Nocturnal Mode", systemImage: "moon", isOn: $pet.isNocturnal)
// .toggleStyle(.switch)
// .toggleStyle(.checkbox)
// .toggleStyle(.button)
```

### Searchable — [15:19]

```swift
struct PetListView: View {
    @Bindable var viewModel: PetStoreViewModel

    var body: some View {
        List {
            Section("My Pets") {
                ForEach(viewModel.myPets) { pet in
                    row(pet: pet)
                }
            }
            Section("Other Pets") {
                ForEach(viewModel.otherPets) { pet in
                    row(pet: pet)
                }
            }
        }
        .searchable(text: $viewModel.searchText)
    }

    private func row(pet: Pet) -> some View {
        PetRowView(pet: pet)
            .swipeActions(edge: .leading) {
                Button("Reward", systemImage: "trophy") {
                    pet.giveAward()
                }
                .tint(.orange)

                ShareLink(item: pet, preview: SharePreview("Pet", image: Image(pet.name)))
            }
    }
}

@Observable
class PetStoreViewModel {
    var petStore: PetStore
    var searchText: String = ""

    init(petStore: PetStore) {
        self.petStore = petStore
    }

    var myPets: [Pet] {
        // For illustration purposes only. The filtered pets should be cached.
        petStore.myPets.filter { searchText.isEmpty || $0.name.contains(searchText) }
    }
    var otherPets: [Pet] {
        // For illustration purposes only. The filtered pets should be cached.
        petStore.otherPets.filter { searchText.isEmpty || $0.name.contains(searchText) }
    }
}
```

### Searchable: customization — [15:20]

```swift
struct PetListView: View {
    @Bindable var viewModel: PetStoreViewModel

    var body: some View {
        List {
            Section("My Pets") {
                ForEach(viewModel.myPets) { pet in
                    row(pet: pet)
                }
            }
            Section("Other Pets") {
                ForEach(viewModel.otherPets) { pet in
                    row(pet: pet)
                }
            }
        }
        .searchable(text: $viewModel.searchText, editableTokens: $viewModel.searchTokens) { $token in
            Label(token.kind.name, systemImage: token.kind.systemImage)
        }
        .searchScopes($viewModel.searchScope) {
            Text("All Pets").tag(PetStoreViewModel.SearchScope.allPets)
            Text("My Pets").tag(PetStoreViewModel.SearchScope.myPets)
            Text("Other Pets").tag(PetStoreViewModel.SearchScope.otherPets)
        }
        .searchSuggestions {
            PetSearchSuggestions(viewModel: viewModel)
        }
    }

    private func row(pet: Pet) -> some View {
        PetRowView(pet: pet)
            .swipeActions(edge: .leading) {
                Button("Reward", systemImage: "trophy") {
                    pet.giveAward()
                }
                .tint(.orange)

                ShareLink(item: pet, preview: SharePreview("Pet", image: Image(pet.name)))
            }
    }
}
```

### App definition — [16:58]

```swift
@main
struct SwiftUIEssentialsApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

### App definition: multiple scenes — [17:15]

```swift
@main
struct SwiftUIEssentialsApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }

        WindowGroup("Training History", id: "history", for: TrainingHistory.ID.self) { $id in
            TrainingHistoryView(historyID: id)
        }

        WindowGroup("Pet Detail", id: "detail", for: Pet.ID.self) { $id in
            PetDetailView(petID: id)
        }
   }
}
```

### Widgets — [17:23]

```swift
struct ScoreboardWidget: Widget {
    var body: some WidgetConfiguration {
        // ...
    }
}

struct ScoreboardWidgetView: View {
    var petTrick: PetTrick

    var body: some View {
        ScoreCard(rating: petTrick.rating)
            .overlay(alignment: .bottom) {
                Text(petTrick.pet.name)
                    .padding()
            }
            .widgetURL(petTrick.pet.url)
    }
}
```

### Digital Crown rotation — [19:37]

```swift
ScoreCardStack(rating: $rating)
   .focusable()
   #if os(watchOS)
   .digitalCrownRotation($rating, from: 0, through: 10)
   #endif
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10150/4/43B9EF68-FA39-44B2-9CCD-82D0EB4CA44D/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10150/4/43B9EF68-FA39-44B2-9CCD-82D0EB4CA44D/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10150) — developer.apple.com. Indexed for agent consumption._
