---
id: "wwdc2021-10223"
event: "wwdc2021"
year: 2021
title: "Create accessible experiences for watchOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10223"
topics: ["SwiftUI & UI Frameworks", "Accessibility & Inclusion"]
platforms: ["watchOS"]
hasTranscript: true
---

# Create accessible experiences for watchOS

**Event:** WWDC21 · **Topic:** Accessibility & Inclusion · **Platforms:** watchOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10223](https://developer.apple.com/videos/play/wwdc2021/10223)

Discover how you can build a top-notch accessibility experience for watchOS when you support features like larger text sizes, VoiceOver, and AssistiveTouch. We’ll take you through adding visual and motor accessibility support to a SwiftUI app built for watchOS, including best practices around API integration, experience, and more.

**Keywords:** `🧋`, `accessibility`, `accessibilityadjustableaction`, `.accessibilityelement`, `accessibility extra large`, `accessibilitylabel`, `accessibility label`, `accessibilityrespondstouserinteraction`, `accessible element`, `assistive technology`, `assistivetouch`, `assistivetouch cursor`, `assistivetouch cursor frame`, `assitivetouch action menu`, `bold text`, `clench`, `complications`, `cursor`, `cursor frame`, `custom actions`, `double-clench`, `double-pinch`, `dwell control`, `dynamic notifications`, `dynamic type`, `element grouping`, `focusable elements`, `hand gestures`, `hand motions`, `large accessibility text`, `large text sizes`, `motion pointer`, `onscreen pointer`, `pinch`, `reduce motion`, `swiftui`, `system text size`, `text styles`, `truncating text`, `voiceover`, `watchos`, `wrap text`, `wwbubbletea`, `wwdaisy`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,391 words)

## Documentation & Resources

- [Create accessible experiences for watchOS](https://developer.apple.com/documentation/watchOS-Apps/create-accessible-experiences-for-watchos) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/watchOS-Apps/create-accessible-experiences-for-watchos
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/watchOS-Apps/create-accessible-experiences-for-watchos.json
- [Accessibility for Developers](https://developer.apple.com/accessibility/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/accessibility/

## Code Snippets

### Dynamic Type for PlantView — [4:48]

```swift
struct PlantView: View {
    @Binding var plant: Plant

    var body: some View {
        VStack(alignment: .leading) {
            Text(plant.name)
                .font(.title3)
            HStack() {
                PlantImage(plant: plant)
                PlantTaskList(plant: $plant)
            }
            PlantTaskButtons(plant: $plant)
        }
    }
}
```

### Line limits for PlantTaskLabel — [5:00]

```swift
struct PlantTaskLabel: View {
    let task: PlantTask
    @Binding var plant: Plant

    var body: some View {
        HStack {
            Image(systemName: task.systemImageName)
                .imageScale(.small)
            Text(plant.stringForTask(task: task))
        }
        .lineLimit(3)
        .font(.caption2)
    }
}
```

### Alternate layouts for PlantContainerView — [5:48]

```swift
struct PlantContainerView: View {
    @Environment(\.sizeCategory) var sizeCategory
    @Binding var plant: Plant

    var body: some View {
        if sizeCategory < .extraExtraLarge {
            PlantViewHorizontal(plant: $plant)
        } else {
            PlantViewVertical(plant: $plant)
        }
    }
}
```

### Element grouping for PlantCellView — [8:56]

```swift
struct PlantCellView: View {
    @EnvironmentObject var plantData: PlantData
    var plant: Plant

    var plantIndex: Int {
        plantData.plants.firstIndex(where: { $0.id == plant.id })!
    }

    var body: some View {
        NavigationLink(destination: PlantEditView(plant: plant).environmentObject(plantData)) {
            PlantContainerView(plant: $plantData.plants[plantIndex])
                .padding()
        }
    }
}
```

### Accessibility labels for PlantTaskLabel — [9:38]

```swift
struct PlantTaskLabel: View {
    let task: PlantTask
    @Binding var plant: Plant

    var body: some View {
        HStack {
            Image(systemName: task.systemImageName)
                .imageScale(.small)
            Text(plant.stringForTask(task: task))
                .accessibilityLabel(plant.accessibilityStringForTask(task: task))
        }
        .lineLimit(3)
        .font(.caption2)
    }
}
```

### Accessibility labels for PlantButton — [10:03]

```swift
struct PlantButton: View {
    let task: PlantTask
    let action: () -> Void
    @State private var isTapped: Bool = false

    var body: some View {
        Button(action: {
            self.isTapped.toggle()
            DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
                self.isTapped.toggle()
            }
            action()
        }) {
            Image(systemName: task.systemImageFillName)
                .foregroundColor(task.color)
                .scaleEffect(isTapped ? 1.5 : 1)
                .animation(nil, value: 0)
                .rotationEffect(.degrees(isTapped ? 360 : 0))
                .animation(.spring(), value: 0)
                .imageScale(.large)
        }
        .buttonStyle(BorderedButtonStyle())
        .accessibilityLabel("Log \(task.name)")
    }
}
```

### Custom control accessibility for PlantTaskFrequency — [11:07]

```swift
struct PlantTaskFrequency: View {
    let task: PlantTask
    @Binding var plant: Plant
    let increment: () -> Void
    let decrement: () -> Void

    var value: Int {
        switch task {
        case .water:
            return plant.wateringFrequency
        case .fertilize:
            return plant.fertilizingFrequency
        default:
            return 0
        }
    }

    var body: some View {
        Section(header: Text("\(task.name) frequency in days"), content: {
            CustomCounter(value: value, increment: increment, decrement: decrement)
                .accessibilityElement()
                .accessibilityAdjustableAction { direction in
                    switch direction {
                    case .increment:
                        increment()
                    case .decrement:
                        decrement()
                    default:
                        break
                    }
                }
                .accessibilityLabel("\(task.name) frequency")
                .accessibilityValue("\(value) days")
        })
    }
}
```

### Make static element focusable — [19:50]

```swift
struct FreeDrinkView: View {
    @State var didCancel = false
    @State var didAccept = false
    @State var showDetail = false

    var body: some View {
        VStack(spacing:10) {
            FreeDrinkTitleView()

            FreeDrinkInfoView()
                .accessibilityRespondsToUserInteraction(true)

            HStack {
                CancelButton(buttonTapped: $didCancel)
                AcceptButton(buttonTapped: $didAccept)
            }
        }
        .onTapGesture {
            showDetail.toggle()
        }
        .sheet(isPresented: $showDetail, onDismiss: dismiss) {
            DrinkDetailModalView()
        }
    }
}
```

### AssistiveTouch cursor frame — [21:12]

```swift
struct DrinkView: View {
    var currentDrink:DrinkInfo

    var body: some View {
        HStack(alignment: .firstTextBaseline) {
            DrinkInfoView(drink:currentDrink)

            Spacer()

            NavigationLink(destination: EditView()) {
                Image(systemName: "ellipsis")
                    .symbolVariant(.circle)
            }
            .contentShape(Circle().scale(1.5))
        }
    }
}
```

### AssistiveTouch Action Menu — [22:48]

```swift
PlantContainerView(plant: plant)
    .padding()
    .accessibilityElement(children: .combine)
    .accessibilityAction {
        // Edit action
    } label: {
        Label("Edit", systemImage: "ellipsis.circle")
    }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10223/6/F4C83469-5B64-46D0-9FC6-F2EC7AC47414/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10223/6/F4C83469-5B64-46D0-9FC6-F2EC7AC47414/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10223) — developer.apple.com. Indexed for agent consumption._
