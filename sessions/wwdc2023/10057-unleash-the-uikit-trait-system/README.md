---
id: "wwdc2023-10057"
event: "wwdc2023"
year: 2023
title: "Unleash the UIKit trait system"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10057"
topics: ["App Services", "Essentials", "System Services", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# Unleash the UIKit trait system

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10057](https://developer.apple.com/videos/play/wwdc2023/10057)

Discover powerful enhancements to the trait system in UIKit. Learn how you can define custom traits to add your own data to UITraitCollection, modify the data propagated to view controllers and views with trait override APIs, and adopt APIs to improve flexibility and performance. We’ll also show you how to bridge UIKit traits with SwiftUI environment keys to seamlessly access data from both UIKit and SwiftUI components in your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,207 words)

## Documentation & Resources

- [UIMutableTraits](https://developer.apple.com/documentation/UIKit/UIMutableTraits-13ja5) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UIMutableTraits-13ja5
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UIMutableTraits-13ja5.json
- [UITraitDefinition](https://developer.apple.com/documentation/UIKit/UITraitDefinition-64c15) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/UITraitDefinition-64c15
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/UITraitDefinition-64c15.json

## Code Snippets

### Working with trait collections — [1:51]

```swift
// Build a new trait collection instance from scratch
let myTraits = UITraitCollection { mutableTraits in
    mutableTraits.userInterfaceIdiom = .phone
    mutableTraits.horizontalSizeClass = .regular
}

// Get a new instance by modifying traits of an existing one
let otherTraits = myTraits.modifyingTraits { mutableTraits in
    mutableTraits.horizontalSizeClass = .compact
    mutableTraits.userInterfaceStyle = .dark
}
```

### Implementing a simple custom trait — [9:06]

```swift
struct ContainedInSettingsTrait: UITraitDefinition {
    static let defaultValue = false
}

let traitCollection = UITraitCollection { mutableTraits in
    mutableTraits[ContainedInSettingsTrait.self] = true
}

let value = traitCollection[ContainedInSettingsTrait.self]
// true
```

### Implementing a simple custom trait with a property — [10:23]

```swift
struct ContainedInSettingsTrait: UITraitDefinition {
    static let defaultValue = false
}

extension UITraitCollection {
    var isContainedInSettings: Bool { self[ContainedInSettingsTrait.self] }
}

extension UIMutableTraits {
    var isContainedInSettings: Bool {
        get { self[ContainedInSettingsTrait.self] }
        set { self[ContainedInSettingsTrait.self] = newValue }
    }
}

let traitCollection = UITraitCollection { mutableTraits in
    mutableTraits.isContainedInSettings = true
}

let value = traitCollection.isContainedInSettings
// true
```

### Implementing a custom theme trait — [11:00]

```swift
enum MyAppTheme: Int {
    case standard, pastel, bold, monochrome
}

struct MyAppThemeTrait: UITraitDefinition {
    static let defaultValue = MyAppTheme.standard
    static let affectsColorAppearance = true
    static let name = "Theme"
    static let identifier = "com.myapp.theme"
}

extension UITraitCollection {
    var myAppTheme: MyAppTheme { self[MyAppThemeTrait.self] }
}

extension UIMutableTraits {
    var myAppTheme: MyAppTheme {
        get { self[MyAppThemeTrait.self] }
        set { self[MyAppThemeTrait.self] = newValue }
    }
}
```

### Using a custom theme trait — [12:33]

```swift
let customBackgroundColor = UIColor { traitCollection in
    switch traitCollection.myAppTheme {
    case .standard:    return UIColor(named: "StandardBackground")!
    case .pastel:      return UIColor(named: "PastelBackground")!
    case .bold:        return UIColor(named: "BoldBackground")!
    case .monochrome:  return UIColor(named: "MonochromeBackground")!
    }
}

let view = UIView()
view.backgroundColor = customBackgroundColor
```

### Managing trait overrides — [18:05]

```swift
func toggleThemeOverride(_ overrideTheme: MyAppTheme) {
    if view.traitOverrides.contains(MyAppThemeTrait.self) {
        // There's an existing theme override; remove it
        view.traitOverrides.remove(MyAppThemeTrait.self)
    } else {
        // There's no existing theme override; apply one
        view.traitOverrides.myAppTheme = overrideTheme
    }
}
```

### Trait change handling on older iOS versions — [21:00]

```swift
// Efficient implementation that only updates when necessary
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
    if traitCollection.horizontalSizeClass != previousTraitCollection?.horizontalSizeClass {
        updateViews(sizeClass: traitCollection.horizontalSizeClass)
    }
}

func updateViews(sizeClass: UIUserInterfaceSizeClass) {
    // Update views for the new size class...
}
```

### Registering for trait changes using a closure — [21:28]

```swift
// Register for horizontal size class changes on self
registerForTraitChanges(
    [UITraitHorizontalSizeClass.self]
) { (self: Self, previousTraitCollection: UITraitCollection) in
    self.updateViews(sizeClass: self.traitCollection.horizontalSizeClass)
}

// Register for changes to multiple traits on another view
let anotherView: MyView
anotherView.registerForTraitChanges(
    [UITraitHorizontalSizeClass.self, ContainedInSettingsTrait.self]
) { (view: MyView, previousTraitCollection: UITraitCollection) in
    // Handle the trait change for this view...
}
```

### Registering for trait changes using a target-action — [22:48]

```swift
// Register for horizontal size class changes on self
registerForTraitChanges(
    [UITraitHorizontalSizeClass.self],
    action: #selector(UIView.setNeedsLayout)
)

// Register for changes to multiple traits on another view
let anotherView: MyView
anotherView.registerForTraitChanges(
    [UITraitHorizontalSizeClass.self, ContainedInSettingsTrait.self],
    target: self,
    action: #selector(handleTraitChange(view:previousTraitCollection:))
)

@objc func handleTraitChange(view: MyView, previousTraitCollection: UITraitCollection) {
    // Handle the trait change for this view...
}
```

### Registering for changes to system traits affecting color appearance — [24:20]

```swift
registerForTraitChanges(
    UITraitCollection.systemTraitsAffectingColorAppearance,
    action: #selector(handleColorAppearanceChange)
)

@objc func handleColorAppearanceChange() {
    // Handle the color appearance trait changes...
}
```

### Manually unregistering for trait changes — [24:37]

```swift
// Store the returned registration token
let registration = registerForTraitChanges([UITraitHorizontalSizeClass.self], action: #selector(handleTraitChange))

// Later, use the stored registration token to manually unregister
unregisterForTraitChanges(registration)

@objc func handleTraitChange() {
    // Handle the trait change...
}
```

### Implementing a bridged UIKit trait and SwiftUI environment key — [26:19]

```swift
enum MyAppTheme: Int {
    case standard, pastel, bold, monochrome
}

// Custom UIKit trait
struct MyAppThemeTrait: UITraitDefinition {
    static let defaultValue = MyAppTheme.standard
    static let affectsColorAppearance = true
}

extension UITraitCollection {
    var myAppTheme: MyAppTheme { self[MyAppThemeTrait.self] }
}

extension UIMutableTraits {
    var myAppTheme: MyAppTheme {
        get { self[MyAppThemeTrait.self] }
        set { self[MyAppThemeTrait.self] = newValue }
    }
}

// Custom SwiftUI environment key
struct MyAppThemeKey: EnvironmentKey {
    static let defaultValue = MyAppTheme.standard
}

extension EnvironmentValues {
    var myAppTheme: MyAppTheme {
        get { self[MyAppThemeKey.self] }
        set { self[MyAppThemeKey.self] = newValue }
    }
}

// Bridge SwiftUI environment key with UIKit trait
extension MyAppThemeKey: UITraitBridgedEnvironmentKey {
    static func read(from traitCollection: UITraitCollection) -> MyAppTheme {
        traitCollection.myAppTheme
    }

    static func write(to mutableTraits: inout UIMutableTraits, value: MyAppTheme) {
        mutableTraits.myAppTheme = value
    }
}
```

### Setting a UIKit trait and reading the bridged environment value from SwiftUI — [27:01]

```swift
// UIKit trait override applied to the window scene
let windowScene: UIWindowScene
windowScene.traitOverrides.myAppTheme = .monochrome

// Cell in a UICollectionView configured to display a SwiftUI view
let cell: UICollectionViewCell
cell.contentConfiguration = UIHostingConfiguration {
    CellView()
}

// SwiftUI view displayed in the cell, which reads the bridged value from the environment
struct CellView: View {
    @Environment(\.myAppTheme) var theme: MyAppTheme

    var body: some View {
        Text("Settings")
            .foregroundStyle(theme == .monochrome ? .gray : .blue)
    }
}
```

### Setting a SwiftUI environment value and reading the bridged trait from UIKit — [28:16]

```swift
// SwiftUI environment value applied to a UIViewControllerRepresentable
struct SettingsView: View {
    var body: some View {
        SettingsControllerRepresentable()
            .environment(\.myAppTheme, .standard)
    }
}

final class SettingsControllerRepresentable: UIViewControllerRepresentable {
    func makeUIViewController(context: Context) -> SettingsViewController {
        SettingsViewController()
    }

    func updateUIViewController(_ uiViewController: SettingsViewController, context: Context) {
        // Update the view controller...
    }
}

// UIKit view controller contained in the SettingsControllerRepresentable
class SettingsViewController: UIViewController {
    override func viewWillLayoutSubviews() {
        super.viewWillLayoutSubviews()
        title = settingsTitle(for: traitCollection.myAppTheme)
    }

    func settingsTitle(for theme: MyAppTheme) -> String {
        switch theme {
        case .standard:   return "Standard"
        case .pastel:     return "Pastel"
        case .bold:       return "Bold"
        case .monochrome: return "Monochrome"
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10057/4/D79F0058-1869-464A-BABD-A1457AE857A0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10057/4/D79F0058-1869-464A-BABD-A1457AE857A0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10057) — developer.apple.com. Indexed for agent consumption._
