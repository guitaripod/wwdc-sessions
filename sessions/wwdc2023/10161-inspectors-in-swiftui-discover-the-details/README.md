---
id: "wwdc2023-10161"
event: "wwdc2023"
year: 2023
title: "Inspectors in SwiftUI: Discover the details"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10161"
topics: ["Essentials", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Inspectors in SwiftUI: Discover the details

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10161](https://developer.apple.com/videos/play/wwdc2023/10161)

Meet Inspectors — a structural API that can help bring a new level of detail to your apps. We’ll take you through the fundamentals of the API and show you how to adopt it. Learn about the latest updates to sheet presentation customizations and find out how you can combine the two to create perfect presentation experiences.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,614 words)

## Code Snippets

### Sample models and views — [3:35]

```swift
// Copy+Paste the below into an Xcode project to support building and running the session's code snippets

import SwiftUI

@main
struct SwiftUIInspectors: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(AnimalStore())
        }
    }
}

struct AnimalInspectorForm: View {
    var animal: Binding<Animal>?
    @EnvironmentObject private var animalStore: AnimalStore

    var body: some View {
        Form {
            if let animal = animal {
                SelectedAnimalInspector(animal: animal, animalStore: animalStore)
            } else {
                ContentUnavailableView {
                    Image(systemName: "magnifyingglass.circle")
                } description: {
                    Text("Select a suspect to inspect")
                } actions: {
                    Text("Fill out details from the interview")
                }
            }
        }
        #if os(iOS)
        .navigationBarTitleDisplayMode(.inline)
        #endif
    }
}

struct SelectedAnimalInspector: View {
    @Binding var animal: Animal
    @ObservedObject var animalStore: AnimalStore

    var body: some View {
            Section("Identity") {
                TextField("Name", text: $animal.name)
                Picker("Paw Size", selection: $animal.pawSize) {
                    Text("Small").tag(PawSize.small)
                    Text("Medium").tag(PawSize.medium)
                    Text("Large").tag(PawSize.large)
                }
                FruitList(selectedFruits: $animal.favoriteFruits, fruits: allFruits)
            }

            Section {
                TextField(text: animalStore(\.alibi, for: animal), prompt: Text("What was \(animal.name) doing at the time of nibbling?"), axis: .vertical) {
                    Text("Alibi")
                }
                .lineLimit(4, reservesSpace: true)
                if let schedule = Binding(animalStore(\.sleepSchedule, for: animal)) {
                    SleepScheduleView(schedule: schedule)
                } else {
                    Button("Add Sleep Schedule") {
                        animalStore.write(\.sleepSchedule, value: Animal.Storage.newSleepSchedule, for: animal)
                    }
                }
                Slider(
                    value: animalStore(\.suspiciousLevel, for: animal), in: 0...1) {
                        Text("Suspicion Level")
                    } minimumValueLabel: {
                        Image(systemName: "questionmark")
                    } maximumValueLabel: {
                        Image(systemName: "exclamationmark.3")
                    }
            } header: {
                Text("Interview")
            }
            .presentationDetents([.medium, .large])
    }
}

private struct FruitList: View {
    @Binding var selectedFruits: [Fruit]
    var fruits: [Fruit]

    var body: some View {
        Section("Favorite Fruits") {
                ForEach(allFruits) { fruit in
                    Toggle(isOn: .init(get: {
                        selectedFruits.contains(fruit)
                    }, set: { newValue in
                        if newValue && !selectedFruits.contains(fruit) {
                            selectedFruits.append(fruit)
                        } else {
                            _ = selectedFruits.firstIndex(of: fruit).map {
                                selectedFruits.remove(at: $0)
                            }
                        }
                    })) {
                        HStack {
                            FruitImage(fruit: fruit, size: .init(width: 40, height: 40), bordered: true)
                            Text(fruit.name).font(.body)
                        }
                    }
                }
        }
    }

    @ViewBuilder
    private func selectionBackground(isSelected: Bool) -> some View {
        if isSelected {
            RoundedRectangle(cornerRadius: 2).inset(by: -2)
                .fill(.selection)
        }
    }
}

private struct SleepScheduleView: View {
    @Binding var schedule: Animal.Storage.SleepSchedule
    var body: some View {
        DatePicker(selection: .init(get: {
            Calendar.current.date(from: schedule.sleepTime) ?? Date()
        }, set: { newDate in
            schedule.sleepTime = Calendar.current.dateComponents([.hour, .minute], from: newDate)
        }), displayedComponents: [.hourAndMinute]) {
            Text("Sleep at: ")
        }

        DatePicker(selection: .init(get: {
            Calendar.current.date(from: schedule.wakeTime) ?? Date()
        }, set: { newDate in
            schedule.wakeTime = Calendar.current.dateComponents([.hour, .minute], from: newDate)
        }), displayedComponents: [.hourAndMinute]) {
            Text("Awake at: ")
        }
    }
}

struct AppState {
    var selection: String? = "Snail"
    var animals: [Animal] = allAnimals
    var inspectorPresented: Bool = true
    var inspectorWidth: CGFloat = 270
    var cornerRadius: CGFloat? = nil
}

extension Binding where Value == AppState {
    func binding() -> Binding<Animal>? {
        self.projectedValue.animals.first {
            $0.wrappedValue.id == self.selection.wrappedValue
        }
    }
}

extension Animal {
    struct Storage: Codable {
        var alibi: String = ""
        var sleepSchedule: SleepSchedule? = nil

        /// Value between 0 and 1 representing how suspicious the animal is.
        /// 1 is guilty.
        var suspiciousLevel: Double = 0.0

        struct SleepSchedule: Codable {
            var sleepTime: DateComponents
            var wakeTime: DateComponents
        }

        static let newSleepSchedule: SleepSchedule = {
            // Asleep at 10:30, awake at 6:30
            .init(
                sleepTime: DateComponents(hour: 22, minute: 30),
                wakeTime: DateComponents(hour: 6, minute: 30))
        }()
    }

}

final class AnimalStore: ObservableObject {

    var storage: [Animal.ID: Animal.Storage] = [:]

    /// Getter for properties of an animal stored in self
    func callAsFunction<Result>(_ keyPath: WritableKeyPath<Animal.Storage, Result>, for animal: Animal) -> Binding<Result> {
        Binding { [self] in
            storage[animal.id, default: .init()][keyPath: keyPath]
        } set: { [self] newValue in
            self.objectWillChange.send()
            var animalStore = storage[animal.id, default: .init()]
            animalStore[keyPath: keyPath] = newValue
            storage[animal.id] = animalStore
        }
    }

    func write<Value>(_ keyPath: WritableKeyPath<Animal.Storage, Value>, value: Value, for animal: Animal) {
        objectWillChange.send()
        var animalStore = storage[animal.id, default: .init()]
        animalStore[keyPath: keyPath] = value
        storage[animal.id] = animalStore
    }

    func read<Value>(_ keyPath: WritableKeyPath<Animal.Storage, Value>, for animal: Animal) -> Value {
        storage[animal.id, default: .init()][keyPath: keyPath]
    }
}

struct AnimalTable: View {
    @Binding var state: AppState
    @EnvironmentObject private var animalStore: AnimalStore
    @Environment(\.horizontalSizeClass) private var sizeClass: UserInterfaceSizeClass?


    var fruitWidth: CGFloat {
        #if os(iOS)
        40.0
        #else
        25.0
        #endif
    }

    var body: some View {
        Table(state.animals, selection: $state.selection) {
            TableColumn("Name") { animal in
                HStack {
                    Text(animal.emoji).font(.title)
                        .padding(2)
                        .background(.thickMaterial, in: RoundedRectangle(cornerRadius: 3))
                    Text(animal.name + " " + animal.species).font(.title3)
                }
            }
            TableColumn("Favorite Fruits") { animal in
                HStack {
                    ForEach(animal.favoriteFruits.prefix(3)) { fruit in
                        FruitImage(fruit: fruit, size: .init(width: fruitWidth, height: fruitWidth), scale: 2.0, bordered: state.selection == animal.id)
                    }
                }
                .padding(3.5)
            }
            TableColumn("Suspicion Level") { animal in
                SuspicionTableCell(animal: animal)
            }
        }
        #if os(macOS)
        .alternatingRowBackgrounds(.disabled)
        #endif
        .tableStyle(.inset)
    }
}

private struct SuspicionTableCell: View {
    var animal: Animal
    @Environment(\.backgroundProminence) private var backgroundProminence
    @EnvironmentObject private var animalStore: AnimalStore

    var body: some View {
        let color = SuspiciousText.model(for: animalStore.read(\.suspiciousLevel, for: animal)).1
        HStack {
            Image(
                systemName: "cellularbars",
                variableValue: animalStore.read(\.suspiciousLevel, for: animal)
            )
            .symbolRenderingMode(.hierarchical)
            SuspiciousText(
                suspiciousLevel:
                    animalStore.read(\.suspiciousLevel, for: animal),
                selected: backgroundProminence == .increased)
        }
        .foregroundStyle(backgroundProminence == .increased ? AnyShapeStyle(.white) : AnyShapeStyle(color))
    }
}

private struct SuspiciousText: View {
    var suspiciousLevel: Double
    var selected: Bool

    static fileprivate func model(for level: Double) -> (String, Color) {
        switch level {
        case 0..<0.2:
            return ("Unlikely", .green)
        case 0.2..<0.5:
            return ("Fishy", .mint)
        case 0.5..<0.9:
            return ("Very suspicious", .orange)
        case 0.9...1:
            return ("Extremely suspicious!", .red)
        default:
            return ("Suspiciously Unsuspicious", .blue)
        }
    }

    var body: some View {
        let model = Self.model(for: suspiciousLevel)
        Text(model.0)
            .font(.callout)
    }
}

struct Animal: Identifiable {
    var name: String
    var species: String
    var pawSize: PawSize
    var favoriteFruits: [Fruit]
    var emoji: String

    var id: String { species }
}

var allAnimals: [Animal] = [
    .init(name: "Fabrizio", species: "Fish", pawSize: .small, favoriteFruits: [.arbutusUnedo, .bigBerry, .elstar], emoji: "🐟"),
    .init(name: "Soloman", species: "Snail", pawSize: .small, favoriteFruits: [.elstar, .flavorKing], emoji: "🐌"),
    .init(name: "Ding", species: "Dove", pawSize: .small, favoriteFruits: [.quercusTomentella, .pinkPearlApple, .lapins], emoji: "🕊️"),
    .init(name: "Catie", species: "Crow", pawSize: .small, favoriteFruits: [.pinkPearlApple, .goldenNectar, .hauerPippin], emoji: "🐦‍⬛"),
    .init(name: "Miko", species: "Cat", pawSize: .small, favoriteFruits: [.belleDeBoskoop, .tompkinsKing, .lapins], emoji: "🐈"),
    .init(name: "Ricardo", species: "Rabbit", pawSize: .small, favoriteFruits: [.mariposa, .elephantHeart], emoji: "🐰"),
    .init(name: "Cornelius", species: "Duck", pawSize: .medium, favoriteFruits: [.greenGage, .goldenNectar], emoji: "🦆"),
    .init(name: "Maria", species: "Mouse", pawSize: .small, favoriteFruits: [.arbutusUnedo, .elephantHeart], emoji: "🐹"),
    .init(name: "Haku", species: "Hedgehog", pawSize: .small, favoriteFruits: [.christmasBerry, .creepingSnowberry, .goldenGem], emoji: "🦔"),
    .init(name: "Rénard", species: "Raccoon", pawSize: .medium, favoriteFruits: [.belleDeBoskoop, .bigBerry, .christmasBerry, .kakiFuyu], emoji: "🦝")
]

enum PawSize: Hashable {
    case small
    case medium
    case large
}

struct Fruit: Identifiable, Hashable {
    var name: String
    var color: Color
    var id: String { name }
}

struct FruitImage: View {
    var fruit: Fruit
    var size: CGSize? = .init(width: 50, height: 50)
    var scale: CGFloat = 1.0
    var bordered = false

    var body: some View {
        fruit.color // Actual assets replaced with Color
            .scaleEffect(scale)
            .scaledToFill()
            .frame(width: size?.width, height: size?.height)
            .mask { RoundedRectangle(cornerRadius: 4) }
            .overlay {
                if bordered {
                    RoundedRectangle(cornerRadius: 4)
                        .stroke(fruit.color, lineWidth: 2)
                }
            }
    }
}

extension Fruit {
    static let goldenGem = Fruit(name: "Golden Gem Apple", color: .yellow)
    static let flavorKing = Fruit(name: "Flavor King Plum", color: .purple)
    static let mariposa = Fruit(name: "Mariposa Plum", color: .red)
    static let tompkinsKing = Fruit(name: "Tompkins King Apple", color: .yellow)
    static let greenGage = Fruit(name: "Green Gage Plum", color: .green)
    static let lapins = Fruit(name: "Lapins Sweet Cherry", color: .purple)
    static let hauerPippin = Fruit(name: "Hauer Pippin Apple", color: .red)
    static let belleDeBoskoop = Fruit(name: "Belle De Boskoop Apple", color: .red)
    static let elstar = Fruit(name: "Elstar Apple", color: .yellow)
    static let goldenDeliciousApple = Fruit(name: "Golden Delicious Apple", color: .yellow)
    static let creepingSnowberry = Fruit(name: "Creeping Snowberry", color: .white)
    static let quercusTomentella = Fruit(name: "Channel Island Oak Acorn", color: .brown)
    static let elephantHeart = Fruit(name: "Elephant Heart Plum", color: .red)
    static let goldenNectar = Fruit(name: "Golden Nectar Plum", color: .yellow)
    static let pinkPearlApple = Fruit(name: "Pink Pearl Apple", color: .pink)
    static let christmasBerry = Fruit(name: "Christmas Berry", color: .red)
    static let kakiFuyu = Fruit(name: "Kaki Fuyu Persimmon", color: .orange)
    static let bigBerry = Fruit(name: "Big Berry Manzanita", color: .red)
    static let arbutusUnedo = Fruit(name: "Strawberry Tree", color: .red)
}

extension Array where Element == Fruit {
    var groupID: Fruit.ID {
        reduce("") { result, next in
            result.appending(next.id)
        }
    }
}

var allFruits: [Fruit] = [
    .goldenGem,
    .flavorKing,
    .mariposa,
    .tompkinsKing,
    .greenGage,
    .lapins,
    .hauerPippin,
    .belleDeBoskoop,
    .elstar,
    .goldenDeliciousApple,
    .creepingSnowberry,
    .quercusTomentella,
    .elephantHeart,
    .goldenNectar,
    .kakiFuyu,
    .bigBerry,
    .arbutusUnedo,
    .pinkPearlApple,
]
```

### Xcode Previews — [3:54]

```swift
import SwiftUI

#Preview("Meet Inspector", traits:
        .fixedLayout(width: 800, height: 500)
) {
    ContentView()
        .navigationTitle("SwiftUI Inspectors")
        .environmentObject(AnimalStore())
}

public struct ContentView: View {
    @State private var state = AppState()
    @State private var presented = true

    public var body: some View {
        AnimalTable(state: $state)
            .inspector(isPresented: $presented) {
                AnimalInspectorForm(animal: $state.binding())
                    .inspectorColumnWidth(
                        min: 200, ideal: 300, max: 400)
                    .toolbar {
                        Spacer()
                        Button {
                            presented.toggle()
                        } label: {
                            Label("Toggle Inspector", systemImage: "info.circle")
                        }
                    }
            }
    }
}

import MapKit

struct FruitNibbleBulletin: View {
    var fruit: Fruit = .pinkPearlApple
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(alignment: .leading) {
                    Grid(horizontalSpacing: 12, verticalSpacing: 2) {
                        GridRow {
                            FruitImage(fruit: fruit, size: .init(width: 60, height: 60), bordered: false)

                            Text("""
                            A \(fruit.name.lowercased()) was nibbled! The bite \
                            happened at 9:41 AM. The nibbler left behind only \
                            a few seeds.
                            """
                            )
                        }
                        GridRow {
                            Text("""
                            The Fruit Inspectors were on \
                            the scene moments after it happened. \
                            Unfortunately, their efforts to catch the nibbler \
                            were fruitless.
                            """).gridCellColumns(2)
                        }
                    }
                    GroupBox("Clues") {
                        LabeledContent("Paw Size") {
                            Text("Large")
                        }
                        LabeledContent("Favorite Fruit") {
                            Text("\(fruit.name.capitalized(with: .current))")
                        }
                        LabeledContent("Alibi") {
                            Text("None")
                        }
                    }
                    HStack {
                        VStack {
                            fruit.color
                                .aspectRatio(contentMode: ContentMode.fit)
                                .shadow(radius: 2.5)
                            Text("The pink pearls left behind").font(.caption)
                                .frame(alignment: .leading)
                        }
                        AppleParkMap()
                            .mask(RoundedRectangle(cornerSize: CGSize(width: 20, height: 10)))

                    }
                    Text("The Fruit Inspection team was on the scene minutes after the incident. However, their attempts to discover any meaningful clues around the identity of the nibbler were fruitless.")
                }
                .scenePadding(.horizontal)
                .toolbar {
                    ToolbarItem {
                        Button(role: .cancel) {
                            dismiss()
                        } label: {
                            Label("Close", systemImage: "xmark.circle.fill")
                        }
                        .symbolRenderingMode(.monochrome)
                        .tint(.secondary)
                    }
                }
            }
#if os(iOS)
            .navigationBarTitleDisplayMode(.inline)
#endif
            .navigationTitle("Fruit Nibble Bulletin")
        }
    }
}

struct AppleParkMap: View {
    @State private var region = MKCoordinateRegion(
        center: CLLocationCoordinate2D(latitude: 37.334_371,
                                       longitude: -122.009_558),
        latitudinalMeters: 100,
        longitudinalMeters: 100
    )

    var body: some View {
        GeometryReader { geometry in
            Map(position: .constant(.automatic), bounds: .init(centerCoordinateBounds: region, minimumDistance: 100, maximumDistance: 100), interactionModes: [], scope: .none) { }
        }
        .frame(height: 180, alignment: .center)
    }
}
```

### Inspector content inside a navigation structure — [7:14]

```swift
struct Example1: View {
    @State private var state = AppState()

    var body: some View {
        NavigationStack {
            AnimalTable(state: $state)
                .inspector(isPresented: $state.inspectorPresented) {
                    AnimalInspectorForm(animal: $state.binding())
                }
                .toolbar {
                    Button {
                        state.inspectorPresented.toggle()
                    } label: {
                        Label("Toggle Inspector", systemImage: "info.circle")
                    }
                }
        }
    }
}
```

### Inspector content outside a navigation structure — [7:55]

```swift
struct Example2: View {
    @State private var state = AppState()

    var body: some View {
        NavigationStack {
            AnimalTable(state: $state)
        }
        .inspector(isPresented: $state.inspectorPresented) {
            AnimalInspectorForm(animal: $state.binding())
                .toolbar {
                    ToolbarItem(placement: .principal) {
                        HStack {
                            Button {
                            } label: {
                                Image(systemName: "rectangle.and.pencil.and.ellipsis")
                            }
                            Button {
                            } label: {
                                Image(systemName: "pawprint.circle")
                            }
                        }
                    }
                }
        }
    }
}
```

### Inspector with NavigationSplitView: detail column — [8:56]

```swift
NavigationSplitView {
  Sidebar()
} detail: {
  AnimalTable()
    .inspector(presented: $isPresented) {
      AnimalInspectorForm()
    }
}
```

### Inspector with NavigationSplitView: Outside — [9:06]

```swift
NavigationSplitView {
  Sidebar()
} detail: {
  AnimalTable()
}
.inspector(presented: $isPresented) {
  AnimalInspectorForm()
}
```

### Presentation customizations — [9:49]

```swift
.sheet(item: $nibbledFruit) { fruit in
  FruitNibbleBulletin(fruit: fruit)
    .presentationBackground(.thinMaterial)
    .presentationDetents([.height(200), .medium, .large])
    .presentationBackgroundInteraction(.enabled(upThrough: .height(200)))
}
```

### Presentation customizations on Inspector — [11:58]

```swift
.inspector(presented: $state.inspectorPresented) {
  AnimalInspectorForm(animal: $state.binding())
    .presentationDetents([.height(200), .medium, .large])
    .presentationBackgroundInteraction(.enabled(upThrough: .height(200)))
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10161/4/8290EAC4-2BB0-4766-AABF-FEC196606758/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10161/4/8290EAC4-2BB0-4766-AABF-FEC196606758/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10161) — developer.apple.com. Indexed for agent consumption._
