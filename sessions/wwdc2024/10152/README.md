---
id: "wwdc2024-10152"
event: "wwdc2024"
year: 2024
title: "Create custom hover effects in visionOS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10152"
topics: ["Design", "Spatial Computing", "SwiftUI & UI Frameworks"]
platforms: ["visionOS"]
hasTranscript: true
---

# Create custom hover effects in visionOS

**Event:** WWDC24 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** visionOS · **Published:** 2024-06-12 · **Session:** [wwdc2024-10152](https://developer.apple.com/videos/play/wwdc2024/10152)

Learn how to develop custom hover effects that update views when people look at them. Find out how to build an expanding button effect that combines opacity, scale, and clip effects. Discover best practices for creating effects that are comfortable and respect people’s accessibility needs.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,376 words)

## Documentation & Resources

- [CustomHoverEffect](https://developer.apple.com/documentation/SwiftUI/CustomHoverEffect) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/CustomHoverEffect
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/CustomHoverEffect.json
- [Human Interface Guidelines: Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/eyes
- [Forum: UI Frameworks](https://developer.apple.com/forums/topics/ui-frameworks?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/ui-frameworks?cid=vf-a-0010
- [Destination Video](https://developer.apple.com/documentation/visionOS/destination-video) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/destination-video
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/destination-video.json

## Code Snippets

### Button with Scale Effect — [4:06]

```swift
struct ProfileButtonView: View {
    var action: () -> Void = { }
    var body: some View {
        Button(action: action) {
            HStack(spacing: 2) {
                ProfileIconView()
                ProfileDetailView()
            }
        }
        .buttonStyle(ProfileButtonStyle())
    }

    struct ProfileButtonStyle: ButtonStyle {
        func makeBody(configuration: Configuration) -> some View {
            configuration.label
                .background(.thinMaterial)
                .hoverEffect(.highlight)
                .clipShape(.capsule)
                .hoverEffect { effect, isActive, _ in
                    effect.scaleEffect(isActive ? 1.05 : 1.0)
                }
        }
    }

    struct ProfileIconView: View {
        var body: some View {
            Image(systemName: "person.crop.circle")
                .resizable()
                .scaledToFit()
                .frame(width: 44, height: 44)
                .padding(6)
        }
    }

    struct ProfileDetailView: View {
        var body: some View {
            VStack(alignment: .leading) {
                Text("Peter McCullough")
                    .font(.body)
                    .foregroundStyle(.primary)
                Text("Switch profiles")
                    .font(.footnote)
                    .foregroundStyle(.tertiary)
            }
            .padding(.trailing, 24)
        }
    }
}
```

### Button with Clip and Scale Effects — [5:37]

```swift
struct ProfileButtonView: View {
    var action: () -> Void = { }
    var body: some View {
        Button(action: action) {
            HStack(spacing: 2) {
                ProfileIconView()
                ProfileDetailView()
            }
        }
        .buttonStyle(ProfileButtonStyle())
    }

    struct ProfileButtonStyle: ButtonStyle {
        func makeBody(configuration: Configuration) -> some View {
            configuration.label
                .background(.thinMaterial)
                .hoverEffect(.highlight)
                .hoverEffect { effect, isActive, proxy in
                    effect.clipShape(.capsule.size(
                        width: isActive ? proxy.size.width : proxy.size.height,
                        height: proxy.size.height,
                        anchor: .leading
                    ))
                    .scaleEffect(isActive ? 1.05 : 1.0)
                }
        }
    }

    struct ProfileIconView: View {
        var body: some View {
            Image(systemName: "person.crop.circle")
                .resizable()
                .scaledToFit()
                .frame(
                    width: 44,
                    height: 44
                )
                .padding(6)
        }
    }

    struct ProfileDetailView: View {
        var body: some View {
            VStack(alignment: .leading) {
                Text("Peter McCullough")
                    .font(.body)
                    .foregroundStyle(.primary)
                Text("Switch profiles")
                    .font(.footnote)
                    .foregroundStyle(.tertiary)
            }
            .padding(.trailing, 24)
        }
    }
}
```

### Expanding Button with Ungrouped Fade — [6:50]

```swift
struct ProfileButtonView: View {
    var action: () -> Void = { }
    var body: some View {
        Button(action: action) {
            HStack(spacing: 2) {
                ProfileIconView()
                ProfileDetailView()
                    .hoverEffect { effect, isActive, _ in
                        effect.opacity(isActive ? 1 : 0)
                    }
            }
        }
        .buttonStyle(ProfileButtonStyle())
    }

    struct ProfileButtonStyle: ButtonStyle {
        func makeBody(configuration: Configuration) -> some View {
            configuration.label
                .background(.thinMaterial)
                .hoverEffect(.highlight)
                .hoverEffect { effect, isActive, proxy in
                    effect.clipShape(.capsule.size(
                        width: isActive ? proxy.size.width : proxy.size.height,
                        height: proxy.size.height,
                        anchor: .leading
                    ))
                    .scaleEffect(isActive ? 1.05 : 1.0)
                }
        }
    }

    struct ProfileIconView: View {
        var body: some View {
            Image(systemName: "person.crop.circle")
                .resizable()
                .scaledToFit()
                .frame(width: 44, height: 44)
                .padding(6)
        }
    }

    struct ProfileDetailView: View {
        var body: some View {
            VStack(alignment: .leading) {
                Text("Peter McCullough")
                    .font(.body)
                    .foregroundStyle(.primary)
                Text("Switch profiles")
                    .font(.footnote)
                    .foregroundStyle(.tertiary)
            }
            .padding(.trailing, 24)
        }
    }
}
```

### Expanding Button with Explicit Group — [8:19]

```swift
struct ProfileButtonView: View {
    var action: () -> Void = { }
    @Namespace var hoverNamespace
    var hoverGroup: HoverEffectGroup {
        HoverEffectGroup(hoverNamespace)
    }
    var body: some View {
        Button(action: action) {
            HStack(spacing: 2) {
                ProfileIconView()
                ProfileDetailView()
                    .hoverEffect(in: hoverGroup) { effect, isActive, _ in
                        effect.opacity(isActive ? 1 : 0)
                    }
            }
        }
        .buttonStyle(ProfileButtonStyle(hoverGroup: hoverGroup))
    }

    struct ProfileIconView: View {
        var body: some View {
            Image(systemName: "person.crop.circle")
                .resizable()
                .scaledToFit()
                .frame(width: 44, height: 44)
                .padding(6)
        }
    }

    struct ProfileDetailView: View {
        var body: some View {
            VStack(alignment: .leading) {
                Text("Peter McCullough")
                    .font(.body)
                    .foregroundStyle(.primary)
                Text("Switch profiles")
                    .font(.footnote)
                    .foregroundStyle(.tertiary)
            }
            .padding(.trailing, 24)
        }
    }
}

struct ProfileButtonStyle: ButtonStyle {
    var hoverGroup: HoverEffectGroup?
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .background(.thinMaterial)
            .hoverEffect(.highlight, in: hoverGroup)
            .hoverEffect(in: hoverGroup) { effect, isActive, proxy in
                effect.clipShape(.capsule.size(
                    width: isActive ? proxy.size.width : proxy.size.height,
                    height: proxy.size.height,
                    anchor: .leading
                ))
                .scaleEffect(isActive ? 1.05 : 1.0)
            }
    }
}
```

### Expanding Button with Implicit Group — [9:13]

```swift
struct ProfileButtonView: View {
    var action: () -> Void = { }
    var body: some View {
        Button(action: action) {
            HStack(spacing: 2) {
                ProfileIconView()
                ProfileDetailView()
                    .hoverEffect { effect, isActive, _ in
                        effect.opacity(isActive ? 1 : 0)
                    }
            }
        }
        .buttonStyle(ProfileButtonStyle())
        .hoverEffectGroup()
    }

    struct ProfileButtonStyle: ButtonStyle {
        func makeBody(configuration: Configuration) -> some View {
            configuration.label
                .background(.thinMaterial)
                .hoverEffect(.highlight)
                .hoverEffect { effect, isActive, proxy in
                    effect.clipShape(.capsule.size(
                        width: isActive ? proxy.size.width : proxy.size.height,
                        height: proxy.size.height,
                        anchor: .leading
                    ))
                    .scaleEffect(isActive ? 1.05 : 1.0)
                }
        }
    }

    struct ProfileIconView: View {
        var body: some View {
            Image(systemName: "person.crop.circle")
                .resizable()
                .scaledToFit()
                .frame(
                    width: 44,
                    height: 44
                )
                .padding(6)
        }
    }

    struct ProfileDetailView: View {
        var body: some View {
            VStack(alignment: .leading) {
                Text("Peter McCullough")
                    .font(.body)
                    .foregroundStyle(.primary)
                Text("Switch profiles")
                    .font(.footnote)
                    .foregroundStyle(.tertiary)
            }
            .padding(.trailing, 24)
        }
    }
}
```

### Expanding Button with Delayed Effect — [10:51]

```swift
struct ProfileButtonView: View {
    var action: () -> Void = { }
    var body: some View {
        Button(action: action) {
            HStack(spacing: 2) {
                ProfileIconView()
                ProfileDetailView()
                    .hoverEffect { effect, isActive, _ in
                        effect.animation(.default.delay(isActive ? 0.8 : 0.2)) {
                            $0.opacity(isActive ? 1 : 0)
                        }
                    }
            }
        }
        .buttonStyle(ProfileButtonStyle())
        .hoverEffectGroup()
    }

    struct ProfileButtonStyle: ButtonStyle {
        func makeBody(configuration: Configuration) -> some View {
            configuration.label
                .background(.thinMaterial)
                .hoverEffect(.highlight)
                .hoverEffect { effect, isActive, proxy in
                    effect.animation(.default.delay(isActive ? 0.8 : 0.2)) {
                        $0.clipShape(.capsule.size(
                            width: isActive ? proxy.size.width : proxy.size.height,
                            height: proxy.size.height,
                            anchor: .leading
                        ))
                    }.scaleEffect(isActive ? 1.05 : 1.0)
                }
        }
    }

    struct ProfileIconView: View {
        var body: some View {
            Image(systemName: "person.crop.circle")
                .resizable()
                .scaledToFit()
                .frame(
                    width: 44,
                    height: 44
                )
                .padding(6)
        }
    }

    struct ProfileDetailView: View {
        var body: some View {
            VStack(alignment: .leading) {
                Text("Peter McCullough")
                    .font(.body)
                    .foregroundStyle(.primary)
                Text("Switch profiles")
                    .font(.footnote)
                    .foregroundStyle(.tertiary)
            }
            .padding(.trailing, 24)
        }
    }
}
```

### Expanding Button with Reusable Effects — [12:50]

```swift
struct ProfileButtonView: View {
    var action: () -> Void = { }
    var body: some View {
        Button(action: action) {
            HStack(spacing: 2) {
                ProfileIconView()
                ProfileDetailView()
                    .hoverEffect(FadeEffect())
            }
        }
        .buttonStyle(ProfileButtonStyle())
        .hoverEffectGroup()
    }

    struct ProfileButtonStyle: ButtonStyle {
        func makeBody(configuration: Configuration) -> some View {
            configuration.label
                .background(.thinMaterial)
                .hoverEffect(.highlight)
                .hoverEffect(ExpandEffect())
        }
    }

    struct ExpandEffect: CustomHoverEffect {
        func body(content: Content) -> some CustomHoverEffect {
            content.hoverEffect { effect, isActive, proxy in
                effect.animation(.default.delay(isActive ? 0.8 : 0.2)) {
                    $0.clipShape(.capsule.size(
                        width: isActive ? proxy.size.width : proxy.size.height,
                        height: proxy.size.height,
                        anchor: .leading
                    ))
                }.scaleEffect(isActive ? 1.05 : 1.0)
            }
        }
    }

    struct FadeEffect: CustomHoverEffect {
        var from: Double = 0
        var to: Double = 1

        func body(content: Content) -> some CustomHoverEffect {
            content.hoverEffect { effect, isActive, _ in
                effect.animation(.default.delay(isActive ? 0.8 : 0.2)) {
                    $0.opacity(isActive ? to : from)
                }
            }
        }
    }

    struct ProfileIconView: View {
        var body: some View {
            Image(systemName: "person.crop.circle")
                .resizable()
                .scaledToFit()
                .frame(
                    width: 44,
                    height: 44
                )
                .padding(6)
        }
    }

    struct ProfileDetailView: View {
        var body: some View {
            VStack(alignment: .leading) {
                Text("Peter McCullough")
                    .font(.body)
                    .foregroundStyle(.primary)
                Text("Switch profiles")
                    .font(.footnote)
                    .foregroundStyle(.tertiary)
            }
            .padding(.trailing, 24)
        }
    }
}
```

### Final Expanding Button with Accessibility Support — [14:14]

```swift
struct ProfileButtonView: View {
    var action: () -> Void = { }
    var body: some View {
        Button(action: action) {
            HStack(spacing: 2) {
                ProfileIconView()
                ProfileDetailView()
                    .hoverEffect(FadeEffect())
            }
        }
        .buttonStyle(ProfileButtonStyle())
        .hoverEffectGroup()
    }

    struct ProfileButtonStyle: ButtonStyle {
        @Environment(\.accessibilityReduceMotion) var reduceMotion
        func makeBody(configuration: Configuration) -> some View {
            configuration.label
                .background {
                    ZStack(alignment: .leading) {
                        Capsule()
                            .fill(.thinMaterial)
                            .hoverEffect(.highlight)
                            .hoverEffect(
                                reduceMotion ? HoverEffect(FadeEffect()) : HoverEffect(.empty))
                        if reduceMotion {
                            Circle()
                                .fill(.thinMaterial)
                                .hoverEffect(.highlight)
                                .hoverEffect(FadeEffect(from: 1, to: 0))
                        }
                    }
                }
                .hoverEffect(
                    reduceMotion
                    ? HoverEffect(.empty)
                    : HoverEffect(ExpandEffect())
                )
        }
    }

    struct ExpandEffect: CustomHoverEffect {
        func body(content: Content) -> some CustomHoverEffect {
            content.hoverEffect { effect, isActive, proxy in
                effect.animation(.default.delay(isActive ? 0.8 : 0.2)) {
                    $0.clipShape(.capsule.size(
                        width: isActive ? proxy.size.width : proxy.size.height,
                        height: proxy.size.height,
                        anchor: .leading
                    ))
                }.scaleEffect(isActive ? 1.05 : 1.0)
            }
        }
    }

    struct FadeEffect: CustomHoverEffect {
        var from: Double = 0
        var to: Double = 1

        func body(content: Content) -> some CustomHoverEffect {
            content.hoverEffect { effect, isActive, _ in
                effect.animation(.default.delay(isActive ? 0.8 : 0.2)) {
                    $0.opacity(isActive ? to : from)
                }
            }
        }
    }

    struct ProfileIconView: View {
        var body: some View {
            Image(systemName: "person.crop.circle")
                .resizable()
                .scaledToFit()
                .frame(
                    width: 44,
                    height: 44
                )
                .padding(6)
        }
    }

    struct ProfileDetailView: View {
        var body: some View {
            VStack(alignment: .leading) {
                Text("Peter McCullough")
                    .font(.body)
                    .foregroundStyle(.primary)
                Text("Switch profiles")
                    .font(.footnote)
                    .foregroundStyle(.tertiary)
            }
            .padding(.trailing, 24)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10152/5/A8C4BDC1-D218-446B-AABE-C4419C65C6A6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10152/5/A8C4BDC1-D218-446B-AABE-C4419C65C6A6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10152) — developer.apple.com. Indexed for agent consumption._