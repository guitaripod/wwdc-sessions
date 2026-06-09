---
id: "wwdc2023-10156"
event: "wwdc2023"
year: 2023
title: "Explore SwiftUI animation"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10156"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Explore SwiftUI animation

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10156](https://developer.apple.com/videos/play/wwdc2023/10156)

Explore SwiftUI’s powerful animation capabilities and find out how these features work together to produce impressive visual effects. Learn how SwiftUI refreshes the rendering of a view, determines what to animate, interpolates values over time, and propagates context for the current transaction.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,832 words)

## Code Snippets

### Pet Avatar - Unanimated — [2:14]

```swift
struct Avatar: View {
    var pet: Pet
    @State private var selected: Bool = false

    var body: some View {
        Image(pet.type)
            .scaleEffect(selected ? 1.5 : 1.0)
            .onTapGesture {
                selected.toggle()
            }
    }
}
```

### Pet Avatar - Animated — [4:13]

```swift
struct Avatar: View {
    var pet: Pet
    @State private var selected: Bool = false

    var body: some View {
        Image(pet.type)
            .scaleEffect(selected ? 1.5 : 1.0)
            .onTapGesture {
                withAnimation {
                    selected.toggle()
                }
            }
    }
}
```

### Pet Avatar - Explicit Animation — [11:49]

```swift
struct Avatar: View {
    var pet: Pet
    @State private var selected: Bool = false

    var body: some View {
        Image(pet.type)
            .scaleEffect(selected ? 1.5 : 1.0)
            .onTapGesture {
                withAnimation(.bouncy) {
                    selected.toggle()
                }
            }
    }
}
```

### UnitCurve Model — [12:48]

```swift
let curve = UnitCurve(
    startControlPoint: UnitPoint(x: 0.25, y: 0.1),
    endControlPoint: UnitPoint(x: 0.25, y: 1))
curve.value(at: 0.25)
curve.velocity(at: 0.25)
```

### Spring Model — [13:56]

```swift
let spring = Spring(duration: 1.0, bounce: 0)
spring.value(target: 1, time: 0.25)
spring.velocity(target: 1, time: 0.25)
```

### MyLinearAnimation — [17:25]

```swift
struct MyLinearAnimation: CustomAnimation {
    var duration: TimeInterval

    func animate<V: VectorArithmetic>(
        value: V,
        time: TimeInterval,
        context: inout AnimationContext<V>
    ) -> V? {
        if time <= duration {
            value.scaled(by: time / duration)
        } else {
            nil // animation has finished
        }
    }
}
```

### MyLinearAnimation with Velocity — [19:50]

```swift
struct MyLinearAnimation: CustomAnimation {
    var duration: TimeInterval

    func animate<V: VectorArithmetic>(
        value: V, time: TimeInterval, context: inout AnimationContext<V>
    ) -> V? {
        if time <= duration {
            value.scaled(by: time / duration)
        } else {
            nil // animation has finished
        }
    }

    func velocity<V: VectorArithmetic>(
        value: V, time: TimeInterval, context: AnimationContext<V>
    ) -> V? {
        value.scaled(by: 1.0 / duration)
    }
}
```

### Pet Avatar - Animation Modifier — [22:44]

```swift
struct Avatar: View {
    var pet: Pet
    @Binding var selected: Bool

    var body: some View {
        Image(pet.type)
            .scaleEffect(selected ? 1.5 : 1.0)
            .animation(.bouncy, value: selected)
            .onTapGesture {
                selected.toggle()
            }
    }
}
```

### Pet Avatar - Multiple Animation Modifiers — [23:44]

```swift
struct Avatar: View {
    var pet: Pet
    @Binding var selected: Bool

    var body: some View {
        Image(pet.type)
            .shadow(radius: selected ? 12 : 8)
            .animation(.smooth, value: selected)
            .scaleEffect(selected ? 1.5 : 1.0)
            .animation(.bouncy, value: selected)
            .onTapGesture {
                selected.toggle()
            }
    }
}
```

### Generic Avatar - Scoped Animation Modifiers — [25:20]

```swift
struct Avatar<Content: View>: View {
    var content: Content
    @Binding var selected: Bool

    var body: some View {
        content
            .animation(.smooth) {
                $0.shadow(radius: selected ? 12 : 8)
            }
            .animation(.bouncy) {
                $0.scaleEffect(selected ? 1.5 : 1.0)
            }
            .onTapGesture {
                selected.toggle()
            }
    }
}
```

### Pet Avatar - Transaction Modifier — [28:45]

```swift
struct Avatar: View {
    var pet: Pet
    @Binding var selected: Bool

    var body: some View {
        Image(pet.type)
            .scaleEffect(selected ? 1.5 : 1.0)
            .transaction(value: selected) {
                $0.animation = $0.avatarTapped
                    ? .bouncy : .smooth
            }
            .onTapGesture {
                withTransaction(\.avatarTapped, true) {
                    selected.toggle()
                }
            }
    }
}

private struct AvatarTappedKey: TransactionKey {
    static let defaultValue = false
}

extension Transaction {
    var avatarTapped: Bool {
        get { self[AvatarTappedKey.self] }
        set { self[AvatarTappedKey.self] = newValue }
    }
}
```

### Generic Avatar - Scoped Transaction Modifier — [28:58]

```swift
struct Avatar<Content: View>: View {
    var content: Content
    @Binding var selected: Bool

    var body: some View {
        content
            .transaction {
                $0.animation = $0.avatarTapped
                    ? .bouncy : .smooth
            } body: {
                $0.scaleEffect(selected ? 1.5 : 1.0)
            }
            .onTapGesture {
                withTransaction(\.avatarTapped, true) {
                    selected.toggle()
                }
            }
    }
}

private struct AvatarTappedKey: TransactionKey {
    static let defaultValue = false
}

extension Transaction {
    var avatarTapped: Bool {
        get { self[AvatarTappedKey.self] }
        set { self[AvatarTappedKey.self] = newValue }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10156/4/9C42B457-119B-4939-B635-598E91D22BD6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10156/4/9C42B457-119B-4939-B635-598E91D22BD6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10156) — developer.apple.com. Indexed for agent consumption._
