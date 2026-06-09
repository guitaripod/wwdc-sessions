---
id: "wwdc2021-10119"
event: "wwdc2021"
year: 2021
title: "SwiftUI Accessibility: Beyond the basics"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10119"
topics: ["SwiftUI & UI Frameworks", "Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# SwiftUI Accessibility: Beyond the basics

**Event:** WWDC21 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10119](https://developer.apple.com/videos/play/wwdc2021/10119)

Go beyond the basics to deliver an exceptional accessibility experience. Learn how to use the new SwiftUI Previews in Xcode to explore the latest accessibility APIs and create fantastic, accessible apps for everyone. Find out how you can customize the automatic accessibility built into SwiftUI to make your own custom controls accessible. Explore best practices and identify where to improve your app's navigation experience using grouping and focus. And help supercharge navigation for VoiceOver users with the addition of rotors.

**Keywords:** `accessibilitychildbehavior`, `accessibility children`, `accessibilitycontainer`, `accessibility container`, `accessibility element`, `.accessibilityfocus`, `accessibilityfocusstate`, `accessibility navigation`, `accessibility panel`, `accessibility preview`, `accessibilityrepresentation`, `accessibility representation`, `accessibilitysortpriority`, `accessibility sort priority`, `accessible`, `accessible by default`, `button`, `canvas`, `children`, `.combine`, `.contain`, `custom controls`, `custom element`, `.ignore`, `label`, `labels`, `previews`, `rotors`, `shapes`, `swiftui previews`, `voiceover`, `voice over`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,420 words)

## Documentation & Resources

- [Accessibility](https://developer.apple.com/documentation/swiftui/view-accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/swiftui/view-accessibility
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/swiftui/view-accessibility.json
- [Creating accessible views](https://developer.apple.com/documentation/SwiftUI/creating-accessible-views) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/creating-accessible-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/creating-accessible-views.json

## Code Snippets

### Welcome to the Accessibility Preview — [2:00]

```swift
struct ContentView: View {
    var body: some View {
        VStack {
            Text("WWDC 2021")
                .accessibilityAddTraits(.isHeader)

            Text("SwiftUI Accessibility")
            Text("Beyond the Basics")

            Image(systemName: "checkmark.seal.fill")
        }
    }
}
```

### BudgetSlider — [4:30]

```swift
struct BudgetSlider: View {
    @Binding var value: Double
    var label: String

    var body: some View {
        VStack(alignment: .leading) {
            HStack {
                Text(label)
                Text(value.toDollars()).bold()
            }
            SliderShape(value: value)
                .gesture(DragGesture().onChanged(handle))
        }
    }
}

struct SliderShape: View {
    var value: Double

    private struct BackgroundTrack: View {
        var cornerRadius: CGFloat
        var body: some View {
            RoundedRectangle(
                cornerRadius: cornerRadius,
                style: .continuous
            )
            .foregroundColor(Color(white: 0.2))
        }
    }

    private struct OverlayTrack: View {
        var cornerRadius: CGFloat
        var body: some View {
            RoundedRectangle(
                cornerRadius: cornerRadius,
                style: .continuous
            )
            .foregroundColor(Color(white: 0.95))
        }
    }

    private struct Knob: View {
        var cornerRadius: CGFloat
        var body: some View {
            RoundedRectangle(
                cornerRadius: cornerRadius,
                style: .continuous
            )
            .strokeBorder(Color(white: 0.7), lineWidth: 1)
            .shadow(radius: 3)
        }
    }

    var body: some View {
        GeometryReader { geometry in
            ZStack(alignment: .leading) {
                BackgroundTrack(cornerRadius: geometry.size.height / 2)

                OverlayTrack(cornerRadius: geometry.size.height / 2)
                    .frame(
                        width: max(geometry.size.height, geometry.size.width * CGFloat(value) + geometry.size.height / 2),
                        height: geometry.size.height)

                Knob(cornerRadius: geometry.size.height / 2)
                    .frame(
                        width: geometry.size.height,
                        height: geometry.size.height)
                    .offset(x: max(0, geometry.size.width * CGFloat(value) - geometry.size.height / 2), y: 0)
            }
        }
    }
}

extension Double {
    func toDollars() -> String {
        return "$\(Int(self))"
    }
}
```

### Slider — [5:15]

```swift
struct StandardSlider: View {
    @Binding var value: Double
    var label: String

    var body: some View {
        Slider(value: $value, in: 0...1) {
            Text(label) 
        }
    }
}
```

### Accessible BudgetSlider — [5:50]

```swift
struct BudgetSlider: View {
    @Binding var value: Double
    var label: String

    var body: some View {
        VStack(alignment: .leading) {
            HStack {
                Text(label)
                Text(value.toDollars()).bold()
            }
            SliderShape(value: value)
                .gesture(DragGesture().onChanged(handle))
                .accessibilityRepresentation {
                    Slider(value: $value, in: 0...1) {
                        Text(label)
                    }
                    .accessibilityValue(value.toDollars())
                }
        }
    }
}

struct SliderShape: View {
    var value: Double

    private struct BackgroundTrack: View {
        var cornerRadius: CGFloat
        var body: some View {
            RoundedRectangle(
                cornerRadius: cornerRadius,
                style: .continuous
            )
            .foregroundColor(Color(white: 0.2))
        }
    }

    private struct OverlayTrack: View {
        var cornerRadius: CGFloat
        var body: some View {
            RoundedRectangle(
                cornerRadius: cornerRadius,
                style: .continuous
            )
            .foregroundColor(Color(white: 0.95))
        }
    }

    private struct Knob: View {
        var cornerRadius: CGFloat
        var body: some View {
            RoundedRectangle(
                cornerRadius: cornerRadius,
                style: .continuous
            )
            .strokeBorder(Color(white: 0.7), lineWidth: 1)
            .shadow(radius: 3)
        }
    }

    var body: some View {
        GeometryReader { geometry in
            ZStack(alignment: .leading) {
                BackgroundTrack(cornerRadius: geometry.size.height / 2)

                OverlayTrack(cornerRadius: geometry.size.height / 2)
                    .frame(
                        width: max(geometry.size.height, geometry.size.width * CGFloat(value) + geometry.size.height / 2),
                        height: geometry.size.height)

                Knob(cornerRadius: geometry.size.height / 2)
                    .frame(
                        width: geometry.size.height,
                        height: geometry.size.height)
                    .offset(x: max(0, geometry.size.width * CGFloat(value) - geometry.size.height / 2), y: 0)
            }
        }
    }
}

extension Double {
    func toDollars() -> String {
        return "$\(Int(self))"
    }
}
```

### NavigationBarView — [7:05]

```swift
struct NavigationBarView: View {
    var body: some View {
        HStack {
            Text("Wallet Pal")
                .font(.largeTitle)
                .bold()

            Spacer()

            Button("Edit Budgets", action: { ... })
                .buttonStyle(
                    SymbolButtonStyle(
                        systemName: "slider.vertical.3"))
        }
    }
}

struct SymbolButtonStyle: ButtonStyle {
    let systemName: String

    func makeBody(configuration: Configuration) -> some View {
				Image(systemName: systemName)
            .accessibilityRepresentation { configuration.label }
    }
}
```

### BudgetHistoryGraph — [9:40]

```swift
struct Budget: Identifiable {
    var month: String
    var amount: Double

    var id: String { month }
}

struct BudgetHistoryGraph: View {
    var budgets: [Budget]

    var body: some View {
        GeometryReader { proxy in
            VStack {
                Canvas { ctx, size in
                    let inset: CGFloat = 25
                    let insetSize = CGSize(width: size.width, height: size.height - inset * 2)
                    let width = insetSize.width / CGFloat(budgets.count)
                    let max = budgets.map(\.amount).max() ?? 0
                    for n in budgets.indices {
                        let x = width * CGFloat(n)
                        let height = (CGFloat(budgets[n].amount) / CGFloat(max)) * insetSize.height
                        let y = insetSize.height - height
                        let p = Path(
                            roundedRect: CGRect(
                                x: x + 2.5,
                                y: y + inset,
                                width: width - 5,
                                height: height),
                            cornerRadius: 4)
                        ctx.fill(p, with: .color(Color.green))

                        ctx.draw(Text(budgets[n].amount.toDollars()), at: CGPoint(x: x + width / 2, y: y + inset / 2))

                        ctx.draw(Text(budgets[n].month), at: CGPoint(x: x + width / 2, y: y + height + 1.5*inset))
                    }
                }
                .accessibilityLabel("Budget History Graph")
                .accessibilityChildren {
                    HStack {
                        ForEach(budgets) { budget in
                            Rectangle()
                                .accessibilityLabel(budget.month)
                                .accessibilityValue(budget.amount.toDollars())

                        }
                    }
                }

            }
        }
        .padding()
        .background(
            RoundedRectangle(cornerRadius: 16)
                .foregroundColor(Color(white: 0.9)))
        .padding(.horizontal)
    }
}
```

### Composition — [12:30]

```swift
// See CompositionExample.swift in the referenced sample project
```

### FriendCellView — [13:50]

```swift
struct User: Identifiable {
    var id: Int
    var name: String
    var photo: String
}

struct FriendCellView: View {
    var user: User

    var body: some View {
        ZStack(alignment: .topLeading) {
            VStack(alignment: .center) {
                Image(user.photo)
                Text(user.name)
            }

            Button("Send Challenge", action: { /* ... */ })
                .buttonStyle(
                    SymbolButtonStyle(
                        systemName: "gamecontroller.fill"))
        }
    }
}

struct SymbolButtonStyle: ButtonStyle {
    let systemName: String

    func makeBody(configuration: Configuration) -> some View {
				Image(systemName: systemName)
            .accessibilityRepresentation { configuration.label }
    }
}
```

### FriendsView — [14:50]

```swift
struct User: Identifiable {
    var id: Int
    var name: String
    var photo: String
}

struct FriendCellView: View {
    var user: User

    var body: some View {
        ZStack(alignment: .topLeading) {
            VStack(alignment: .center) {
                Image(user.photo)
                Text(user.name)
            }

            Button("Send Challenge", action: { /* ... */ })
                .buttonStyle(
                    SymbolButtonStyle(
                        systemName: "gamecontroller.fill"))
        }
    }
}

struct FriendsView: View {
    var users: [User]

    var body: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack {
                ForEach(users) { user in
                    FriendCellView(user: user)
                        .onTapGesture { /* ... */ }
                }

                AddFriendButton()

                Spacer()
            }
        }
    }
}

struct AddFriendButton: View {
    var body: some View {
        Button(action: { /* ... */ }) {
            Circle()
                .foregroundColor(Color(white: 0.9))
                .frame(width: 50, height: 50)
                .overlay(
                    Image(systemName: "plus")
                        .resizable()
                        .foregroundColor(Color(white: 0.5))
                        .padding(15)
                )
        }
        .buttonStyle(PlainButtonStyle())
    }
}

struct SymbolButtonStyle: ButtonStyle {
    let systemName: String

    func makeBody(configuration: Configuration) -> some View {
				Image(systemName: systemName)
            .accessibilityRepresentation { configuration.label }
    }
}
```

### FriendsView with Containers — [15:10]

```swift
struct User: Identifiable {
    var id: Int
    var name: String
    var photo: String
}

struct FriendCellView: View {
    var user: User

    var body: some View {
        ZStack(alignment: .topLeading) {
            VStack(alignment: .center) {
                Image(user.photo)
                Text(user.name)
            }

            Button("Send Challenge", action: { /* ... */ })
                .buttonStyle(
                    SymbolButtonStyle(
                        systemName: "gamecontroller.fill"))
        }
    }
}

struct FriendsView: View {
    var users: [User]

    var body: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack {
                ForEach(users) { user in
                    FriendCellView(user: user)
                         .accessibilityElement(children: .contain)
                        .onTapGesture { /* ... */ }
                }

                AddFriendButton()

                Spacer()
            }
        }
    }
}

struct AddFriendButton: View {
    var body: some View {
        Button(action: { /* ... */ }) {
            Circle()
                .foregroundColor(Color(white: 0.9))
                .frame(width: 50, height: 50)
                .overlay(
                    Image(systemName: "plus")
                        .resizable()
                        .foregroundColor(Color(white: 0.5))
                        .padding(15)
                )
        }
        .buttonStyle(PlainButtonStyle())
    }
}

struct SymbolButtonStyle: ButtonStyle {
    let systemName: String

    func makeBody(configuration: Configuration) -> some View {
				Image(systemName: systemName)
            .accessibilityRepresentation { configuration.label }
    }
}
```

### FriendCellView Sort Priority — [16:20]

```swift
struct User: Identifiable {
    var id: Int
    var name: String
    var photo: String
}

struct FriendCellView: View {
    var user: User

    var body: some View {
        ZStack(alignment: .topLeading) {
            VStack(alignment: .center) {
                Image(user.photo)
                Text(user.name)
            }

            Button("Send Challenge", action: { /* ... */ })
                .buttonStyle(
                    SymbolButtonStyle(
                        systemName: "gamecontroller.fill"))
                .accessibilitySortPriority(-1)
        }
    }
}
```

### FriendsView with .combine — [16:55]

```swift
struct User: Identifiable {
    var id: Int
    var name: String
    var photo: String
}

struct FriendCellView: View {
    var user: User

    var body: some View {
        ZStack(alignment: .topLeading) {
            VStack(alignment: .center) {
                Image(user.photo)
                Text(user.name)
            }

            Button("Send Challenge", action: { /* ... */ })
                .buttonStyle(
                    SymbolButtonStyle(
                        systemName: "gamecontroller.fill"))
        }
    }
}

struct FriendsView: View {
    var users: [User]

    var body: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack {
                ForEach(users) { user in
                    FriendCellView(user: user)
                        .accessibilityElement(children: .combine)
                        .onTapGesture { /* ... */ }
                }

                AddFriendButton()

                Spacer()
            }
        }
    }
}

struct AddFriendButton: View {
    var body: some View {
        Button(action: { /* ... */ }) {
            Circle()
                .foregroundColor(Color(white: 0.9))
                .frame(width: 50, height: 50)
                .overlay(
                    Image(systemName: "plus")
                        .resizable()
                        .foregroundColor(Color(white: 0.5))
                        .padding(15)
                )
        }
        .buttonStyle(PlainButtonStyle())
    }
}

struct SymbolButtonStyle: ButtonStyle {
    let systemName: String

    func makeBody(configuration: Configuration) -> some View {
				Image(systemName: systemName)
            .accessibilityRepresentation { configuration.label }
    }
}
```

### AlertsView Implicit Rotor — [20:30]

```swift
struct Alert: Identifiable {
    var id: Int
    var isUnread: Bool
    var isFlagged: Bool
    var subject: String
    var content: String
}

struct AlertsView: View {
    var alerts: [Alert]

    var body: some View {
        VStack {
            ForEach(alerts) { alert in
                AlertCellView(alert: alert)
                    .accessibilityElement(children: .combine)
            }
        }
        .accessibilityElement(children: .contain)
        .accessibilityRotor("Warnings") {
            ForEach(alerts) { alert in
                if alert.isWarning {
                    AccessibilityRotorEntry(alert.title, id: alert.id)
                }
            }
        }
    }
}

struct AlertCell: View {
    var alert: Alert

    var body: some View {
        VStack(alignment: .leading) {
            HStack {
                if alert.isUnread {
                    Circle()
                        .foregroundColor(.blue)
                        .frame(width: 10, height: 10)
                }
                if alert.isFlagged {
                    Image(systemName: "exclamationmark.triangle.fill")
                        .foregroundColor(.orange)
                        .frame(width: 10, height: 10)
                }
                Text(alert.subject)
                    .font(.headline)
                    .fontWeight(.semibold)
                Spacer()
                Text("04/30/21")
                    .font(.subheadline)
                    .foregroundColor(.secondary)
            }
            Text(alert.content)
                .lineLimit(3)
        }
        .padding(10)
        .background(
            RoundedRectangle(cornerRadius: 8)
                .foregroundColor(Color(white: 0.9))
        )
    }
}
```

### AlertsView Explicit Rotor — [21:50]

```swift
struct Alert: Identifiable {
    var id: Int
    var isUnread: Bool
    var isFlagged: Bool
    var subject: String
    var content: String
}

struct AlertsView: View {
    var alerts: [Alert]
    @Namespace var namespace

    var body: some View {
        VStack {
            ForEach(alerts) { alert in
                VStack {
                    AlertCellView(alert: alert)
                        .accessibilityElement(children: .combine)
                        .accessibilityRotorEntry(id: alert.id, in: namespace)
                    AlertActionsView(alert: alert)
                }
            }
        }
        .accessibilityElement(children: .contain)
        .accessibilityRotor("Warnings") {
            ForEach(alerts) { alert in
                if alert.isWarning {
                    AccessibilityRotorEntry(alert.title, id: alert.id, in: namespace)
                }
            }
        }
    }
}

struct AlertCell: View {
    var alert: Alert

    var body: some View {
        VStack(alignment: .leading) {
            HStack {
                if alert.isUnread {
                    Circle()
                        .foregroundColor(.blue)
                        .frame(width: 10, height: 10)
                }
                if alert.isFlagged {
                    Image(systemName: "exclamationmark.triangle.fill")
                        .foregroundColor(.orange)
                        .frame(width: 10, height: 10)
                }
                Text(alert.subject)
                    .font(.headline)
                    .fontWeight(.semibold)
                Spacer()
                Text("04/30/21")
                    .font(.subheadline)
                    .foregroundColor(.secondary)
            }
            Text(alert.content)
                .lineLimit(3)
        }
        .padding(10)
        .background(
            RoundedRectangle(cornerRadius: 8)
                .foregroundColor(Color(white: 0.9))
        )
    }
}
```

### TextEditor Rotors — [22:20]

```swift
struct ContentView: View {
    @State var note: Note

    var body: some View {
        TextEditor($text.content)
            .accessibilityRotor("Email Addresses", textRanges: note.addressRanges)
            .accessibilityRotor("Links", textRanges: note.linkRanges)
            .accessibilityRotor("Phone Numbers", textRanges: note.phoneNumberRanges)
    }
}
```

### AlertNotificationView — [24:45]

```swift
struct Notification: Equatable {
    enum Priority {
        case low, high
    }
    var content: String
    var priority: Priority
}

struct AlertNotificationView<Content: View>: View {
    @ViewBuilder var content: Content
    @Binding var notification: Notification?
    @AccessibilityFocusState var isNotificationFocused: Bool

    var body: some View {
        ZStack(alignment: .top) {
            content

            if let notification = $notification {
                NotificationBanner(notification: notification)
                    .accessibilityFocused($isNotificationFocused)
            }
        }
        .onChange(of: notification) { notification in
            if notification?.priority == .high {
                isNotificationFocused = true
            } else {
                postAccessibilityNotification()
            }
        }
    }

    func postAccessibilityNotification() {
        guard let announcement = notification?.content else {
            return
        }
        #if os(macOS)
        NSAccessibility.post(
            element: NSApp.accessibilityWindow(),
            notification: .announcementRequested,
            userInfo: [.announcement: announcement])
        #else
        UIAccessibility.post(notification: .announcement, argument: announcement)
        #endif
    }
}

struct NotificationBanner: View {
    @Binding var notification: Notification?
    @State var timer: Timer?
    @AccessibilityFocusState var isNotificationFocused: Bool

    var body: some View {
        if let notification = notification {
            Text(notification.content)
                .accessibilityFocused($isNotificationFocused)
                .onAppear { startTimer() }
                .onDisappear { stopTimer() }
        } else {
            EmptyView()
        }
    }

    func startTimer() {
        timer = Timer.scheduledTimer(
            withTimeInterval: 3,
            repeats: true) { _ in
            if !isNotificationFocused {
                notification = nil
            }
        }
    }

    func stopTimer() {
        timer?.invalidate()
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10119/6/A3AEB1E4-C4E9-43B4-9EF6-206F6B9704E6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10119/6/A3AEB1E4-C4E9-43B4-9EF6-206F6B9704E6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10119) — developer.apple.com. Indexed for agent consumption._