---
id: "wwdc2026-272"
event: "wwdc2026"
year: 2026
title: "Use SwiftUI with AppKit and UIKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/272"
topics: ["App Services", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Use SwiftUI with AppKit and UIKit

**Event:** WWDC26 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-272](https://developer.apple.com/videos/play/wwdc2026/272)

Discover how to incrementally adopt SwiftUI in your existing AppKit or UIKit app. We’ll show you how to use the Observation framework to automatically update your views, integrate SwiftUI components into an existing view hierarchy, and bring gesture recognizers into SwiftUI. We’ll also explore how to add complete SwiftUI scenes to your app without changing your overall architecture.

**Keywords:** `screenshots`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,893 words)

## Documentation & Resources

- [Updating views automatically with observation tracking in AppKit](https://developer.apple.com/documentation/AppKit/updating-views-automatically-with-observation-tracking-in-appkit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppKit/updating-views-automatically-with-observation-tracking-in-appkit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppKit/updating-views-automatically-with-observation-tracking-in-appkit.json
- [Updating views automatically with observation tracking in UIKit](https://developer.apple.com/documentation/UIKit/updating-views-automatically-with-observation-tracking-in-uikit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/updating-views-automatically-with-observation-tracking-in-uikit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/updating-views-automatically-with-observation-tracking-in-uikit.json

## Code Snippets

### Observation in AppKit — [3:39]

```swift
// Observation in AppKit

import Observation

@Observable @MainActor
final class ColorModel {
    var hue: Double = 0.6
    var saturation: Double = 1.0
    var brightness: Double = 1.0
}
```

### Circular color picker — [6:28]

```swift
// Circular color picker

import SwiftUI
import Observation

@Observable @MainActor
final class ColorModel {
    var hue: Double = 0.6
    var saturation: Double = 1.0
    var brightness: Double = 1.0
}

// MARK: - Picker View

@Animatable
struct HSBColorPicker: View {
    var hue: Double
    var saturation: Double
    var brightness: Double
    @AnimatableIgnored var model: ColorModel

    init(model: ColorModel) {
        self.model = model
        self.hue = model.hue
        self.saturation = model.saturation
        self.brightness = model.brightness
    }

    var body: some View {
        Canvas { context, size in
            let metrics = PickerMetrics(size: size)
            drawPicker(in: &context, metrics: metrics, hue: hue, saturation: saturation, brightness: brightness)
        }
        .contentShape(Circle())
        .modifier(ColorPickerDragGesture(model: model))
        .aspectRatio(1, contentMode: .fit)
    }
}

// MARK: - Drag Gesture

private struct ColorPickerDragGesture: ViewModifier {
    var model: ColorModel

    private enum Ring { case hue, saturation, brightness }
    @State private var draggedRing: Ring?

    func body(content: Content) -> some View {
        GeometryReader { proxy in
            content.gesture(
                DragGesture(minimumDistance: 0, coordinateSpace: .local)
                    .onChanged { onDrag(to: $0.location, size: proxy.size) }
                    .onEnded { _ in draggedRing = nil }
            )
        }
    }

    private func onDrag(to location: CGPoint, size: CGSize) {
        let metrics = PickerMetrics(size: size)
        let point = CGPoint(x: location.x - metrics.mid.x, y: location.y - metrics.mid.y)
        if draggedRing == nil {
            let distance = hypot(point.x, point.y)
            if distance >= metrics.radius - metrics.ringWidth - metrics.gap / 2 {
                draggedRing = .hue
            } else if distance >= metrics.radius - metrics.ringWidth * 2 - metrics.gap {
                draggedRing = point.x > 0 ? .brightness : .saturation
            }
        }
        switch draggedRing {
        case .hue: model.hue = (angle0To2Pi(point) / (2 * .pi) + 0.25).truncatingRemainder(dividingBy: 1)
        case .saturation: model.saturation = leftSemicircleValue(point)
        case .brightness: model.brightness = 1 - rightSemicircleValue(point)
        case nil: break
        }
    }
}

// MARK: - Metrics

struct PickerMetrics {
    let mid: CGPoint
    let radius: CGFloat
    let ringWidth: CGFloat
    let gap: CGFloat = 8

    init(size: CGSize) {
        let border: CGFloat = 1 // reserve room so the outer ring's stroke isn't clipped
        mid = CGPoint(x: size.width / 2, y: size.height / 2)
        radius = (min(size.width, size.height) - 2 * border) / 2
        ringWidth = radius / 3
    }

    var diameter: CGFloat { radius * 2 }
    var innerRadius: CGFloat { (diameter - 2 * ringWidth - gap) / 2 }
    var centerRadius: CGFloat { radius - 2 * ringWidth - gap }
}

// MARK: - Geometry Helpers

func angle0To2Pi(_ point: CGPoint) -> CGFloat {
    let a = atan2(point.y, point.x)
    return a >= 0 ? a : a + 2 * .pi
}

func rightSemicircleValue(_ point: CGPoint) -> CGFloat {
    let angle = atan2(point.y, point.x)
    return point.x >= 0 ? (angle + .pi / 2) / .pi : (point.y >= 0 ? 1 : 0)
}

func leftSemicircleValue(_ point: CGPoint) -> CGFloat {
    guard point.x <= 0 else { return point.y >= 0 ? 1 : 0 }
    return (atan2(point.y, -point.x) + .pi / 2) / .pi
}

private extension Path {
    /// A circle whose stroke of `lineWidth` lands inside `radius`.
    init(ring radius: CGFloat, center: CGPoint, lineWidth: CGFloat) {
        let inset = radius - lineWidth / 2
        self.init(ellipseIn: CGRect(x: center.x - inset, y: center.y - inset, width: inset * 2, height: inset * 2))
    }
}

// MARK: - Drawing

private func drawPicker(in context: inout GraphicsContext, metrics: PickerMetrics, hue: Double, saturation: Double, brightness: Double) {
    drawHueRing(in: &context, metrics: metrics, hue: hue, saturation: saturation, brightness: brightness)
    drawValueRings(in: &context, metrics: metrics, hue: hue, saturation: saturation, brightness: brightness)
    drawCenter(in: &context, metrics: metrics, hue: hue, saturation: saturation, brightness: brightness)
}

private func drawHueRing(in context: inout GraphicsContext, metrics: PickerMetrics, hue: Double, saturation: Double, brightness: Double) {
    let ring = Path(ring: metrics.radius, center: metrics.mid, lineWidth: metrics.ringWidth)
    // A custom metal shader would be work great here as well
    let colors = stride(from: 0.0, through: 1, by: 1.0 / 64).map { Color(hue: $0, saturation: saturation, brightness: brightness) }
    context.stroke(ring, with: .conicGradient(Gradient(colors: colors), center: metrics.mid, angle: .degrees(-90)), lineWidth: metrics.ringWidth)
    context.stroke(ring.strokedPath(StrokeStyle(lineWidth: metrics.ringWidth)), with: .color(.black), lineWidth: 1)
    // Tick marks are left as a fun exercise for the reader.
    drawKnob(in: &context, metrics: metrics, radius: metrics.radius, rotation: 2 * .pi * hue + .pi)
}

private func drawValueRings(in context: inout GraphicsContext, metrics: PickerMetrics, hue: Double, saturation: Double, brightness: Double) {
    drawSemicircle(in: &context, metrics: metrics, start: .degrees(90), conicAngle: .degrees(0), stops: (0...1).map {
        Gradient.Stop(color: Color(hue: hue, saturation: 1 - Double($0), brightness: brightness), location: 0.25 + Double($0) * 0.5)
    })
    drawSemicircle(in: &context, metrics: metrics, start: .degrees(270), conicAngle: .degrees(180), stops: (0...1).map {
        Gradient.Stop(color: Color(hue: hue, saturation: saturation, brightness: 1 - Double($0)), location: 0.25 + Double($0) * 0.5)
    })
    drawKnob(in: &context, metrics: metrics, radius: metrics.innerRadius, rotation: .pi * (1 - saturation))
    drawKnob(in: &context, metrics: metrics, radius: metrics.innerRadius, rotation: .pi * (1 - brightness) + .pi)
}

private func drawSemicircle(in context: inout GraphicsContext, metrics: PickerMetrics, start: Angle, conicAngle: Angle, stops: [Gradient.Stop]) {
    var path = Path()
    path.addArc(center: metrics.mid, radius: metrics.innerRadius - metrics.ringWidth / 2, startAngle: start, endAngle: start + .degrees(180), clockwise: false)
    let band = path.strokedPath(StrokeStyle(lineWidth: metrics.ringWidth))
    context.fill(band, with: .conicGradient(Gradient(stops: stops), center: metrics.mid, angle: conicAngle))
    context.stroke(band, with: .color(.black), lineWidth: 1)
    // Tick marks are left as a fun exercise for the reader.
}

private func drawCenter(in context: inout GraphicsContext, metrics: PickerMetrics, hue: Double, saturation: Double, brightness: Double) {
    let r = metrics.centerRadius
    let disc = Path(ellipseIn: CGRect(x: metrics.mid.x - r, y: metrics.mid.y - r, width: r * 2, height: r * 2))
    context.fill(disc, with: .color(Color(hue: hue, saturation: saturation, brightness: brightness)))
    context.stroke(disc, with: .color(.black))
}

private func drawKnob(in context: inout GraphicsContext, metrics: PickerMetrics, radius: CGFloat, rotation: CGFloat) {
    let lineWidth: CGFloat = 5
    let inset: CGFloat = 3 + lineWidth / 2
    var path = Path()
    path.move(to: CGPoint(x: 0, y: radius - metrics.ringWidth + inset))
    path.addLine(to: CGPoint(x: 0, y: radius - inset))
    path = path.applying(CGAffineTransform(rotationAngle: rotation))
    path = path.applying(CGAffineTransform(translationX: metrics.mid.x, y: metrics.mid.y))
    context.stroke(path, with: .color(.black.opacity(0.8)), style: StrokeStyle(lineWidth: lineWidth + 1, lineCap: .round))
    context.stroke(path, with: .color(.white), style: StrokeStyle(lineWidth: lineWidth, lineCap: .round))
}

#Preview {
    @Previewable @State var model = ColorModel()
    HSBColorPicker(model: model)
        .frame(width: 320, height: 320)
        .padding()
}
```

### Hosting SwiftUI in AppKit — [7:21]

```swift
// Hosting SwiftUI in AppKit

NSHostingView(
    rootView: HSBColorPicker(model: model)
)
```

### Mix NSGestureRecognizer with SwiftUI — [8:14]

```swift
// Mix NSGestureRecognizer with SwiftUI

import SwiftUI
import AppKit

@Observable @MainActor
final class ColorModel {
    var hue: Double = 0.6
    var saturation: Double = 1.0
    var brightness: Double = 1.0
}

struct ForceClickReset: NSGestureRecognizerRepresentable {
    var model: ColorModel

    func makeNSGestureRecognizer(context: Context) -> ForceClickGestureRecognizer {
        ForceClickGestureRecognizer()
    }

    func handleNSGestureRecognizerAction(_ recognizer: ForceClickGestureRecognizer, context: Context) {
        withAnimation {
            model.saturation = 1
            model.brightness = 1
        }
    }
}

final class ForceClickGestureRecognizer: NSGestureRecognizer {
    private var didActivate = false

    override func pressureChange(with event: NSEvent) {
        if event.stage >= 2 && !didActivate {
            didActivate = true
            state = .ended
        }
    }

    override func mouseDown(with event: NSEvent) {
        didActivate = false
        state = .possible
    }

    override func mouseUp(with event: NSEvent) {
        didActivate = false
        state = .possible
    }
}
```

### Adding ColorMenu to the Main Menu — [9:42]

```swift
// Adding ColorMenu to the Main Menu

import AppKit
import SwiftUI
import Observation

@Observable @MainActor
final class ColorModel {
    var hue: Double = 0.6
    var saturation: Double = 1.0
    var brightness: Double = 1.0
}

// Menu definition in SwiftUI.
struct ColorMenu: View {
    var model: ColorModel

    private static let hues: [(name: String, hue: Double)] = [
        ("Red", 0), ("Yellow", 0.17), ("Green", 0.33), ("Cyan", 0.5), ("Blue", 0.67), ("Purple", 0.83),
    ]

    var body: some View {
        Button("Full Intensity") {
            withAnimation {
                model.saturation = 1
                model.brightness = 1
            }
        }
        .keyboardShortcut(.upArrow, modifiers: [.command, .shift])

        Button("Blackout") {
            withAnimation {
                model.brightness = 0
            }
        }
        .keyboardShortcut(.downArrow, modifiers: [.command, .shift])

        Divider()

        Button("Brighten") {
            withAnimation {
                model.brightness = min(1, model.brightness + 0.1)
            }
        }
        .keyboardShortcut(.upArrow, modifiers: .command)

        Button("Dim") {
            withAnimation {
                model.brightness = max(0, model.brightness - 0.1)
            }
        }
        .keyboardShortcut(.downArrow, modifiers: .command)

        Divider()

        Picker("Color", selection: Bindable(model).hue) {
            ForEach(Self.hues, id: \.hue) { entry in
                Label(entry.name, systemImage: "circle.fill")
                    .tint(Color(hue: entry.hue, saturation: 1, brightness: 1))
                    .tag(entry.hue)
            }
        }
        .pickerStyle(.palette)
    }
}

@MainActor
class AppDelegate: NSObject, NSApplicationDelegate {
    let colorModel = ColorModel()

    func setupMainMenu() {
        let mainMenu = NSMenu()

        let colorMenu = NSHostingMenu(rootView: ColorMenu(model: colorModel))
        colorMenu.title = "Color"

        let colorMenuItem = NSMenuItem()
        colorMenuItem.submenu = colorMenu
        mainMenu.addItem(colorMenuItem)
    }
}

#Preview {
    Menu("Color") {
        ColorMenu(model: ColorModel())

    }.padding()
}
```

### Adding SwiftUI scenes dynamically — [11:36]

```swift
// Adding SwiftUI scenes dynamically

import AppKit
import SwiftUI
import Observation

@MainActor
class AppDelegate: NSObject, NSApplicationDelegate {
    let model = AppModel()
    var openSettingsAction: (() -> Void)?

    func applicationWillFinishLaunching(_ notification: Notification) {
        let scenes = NSHostingSceneRepresentation {
            LightMenuBarExtra(appModel: model)
            LightSettings(appModel: model)
        }
        NSApplication.shared.addSceneRepresentation(scenes)
        openSettingsAction = {
            scenes.environment.openSettings()
        }
    }

    @IBAction func openSettings(_ sender: Any?) {
        openSettingsAction?()
    }
}

@Observable @MainActor
final class ColorModel {
    var hue: Double = 0.6
    var saturation: Double = 1.0
    var brightness: Double = 1.0

    var color: Color {
        Color(hue: hue, saturation: saturation, brightness: brightness)
    }
}

@Observable @MainActor
final class AppModel {
    var showMenuBarExtra: Bool = true

    var colorModel = ColorModel()

    var startUniverse: Int = 1
    var numberOfPixels: Int = 50

    var maxBrightness: Double = 1.0
    var isConnected: Bool = false
}

struct LightMenuBarExtra: Scene {
    var appModel: AppModel

    var body: some Scene {
        MenuBarExtra("Light Mix", systemImage: "lightbulb.fill", isInserted: Bindable(appModel).showMenuBarExtra) {
            MenuBarContent(appModel: appModel)
        }
        .menuBarExtraStyle(.window)
    }
}


struct MenuBarContent: View {
    @Bindable var appModel: AppModel

    var body: some View {
        // TODO: Use HSBColorPicker
        VStack {
            RoundedRectangle(cornerRadius: 10)
                .fill(appModel.colorModel.color)
                .frame(height: 80)
                .overlay(RoundedRectangle(cornerRadius: 10).stroke(.black.opacity(0.1)))

            LabeledContent("Brightness") {
                Slider(value: $appModel.colorModel.brightness)
                    .frame(width: 140)
            }
        }
        .padding()
        .frame(width: 280)
    }
}

struct LightSettings: Scene {
    var appModel: AppModel

    var body: some Scene {
        Settings {
            SettingsView(appModel: appModel)
        }
    }
}

struct SettingsView: View {
    var appModel: AppModel

    var body: some View {
        TabView {
            Tab("General", systemImage: "gearshape") {
                GeneralTab(appModel: appModel)
            }
            Tab("Output", systemImage: "antenna.radiowaves.left.and.right") {
                OutputTab(appModel: appModel)
            }
            Tab("About", systemImage: "info.circle") {
                AboutTab()
            }
        }
        .formStyle(.grouped)
        .scrollDisabled(true)
        .frame(width: 460)
        .fixedSize(horizontal: false, vertical: true)
    }
}

struct GeneralTab: View {
    @Bindable var appModel: AppModel

    var body: some View {
        Form {
            Section("Appearance") {
                Toggle("Show in Menu Bar", isOn: $appModel.showMenuBarExtra)
            }
            Section("DMX Configuration") {
                LabeledContent("Start Universe") {
                    TextField("", value: $appModel.startUniverse, format: .number)
                        .textFieldStyle(.roundedBorder)
                        .frame(width: 80)
                }
                LabeledContent("Number of Pixels") {
                    TextField("", value: $appModel.numberOfPixels, format: .number)
                        .textFieldStyle(.roundedBorder)
                        .frame(width: 80)
                }
            }
        }
    }
}

struct OutputTab: View {
    @Bindable var appModel: AppModel

    var body: some View {
        Form {
            Section("Output") {
                LabeledContent("Max Brightness") {
                    HStack {
                        Slider(value: $appModel.maxBrightness, in: 0...1)
                        Text("\(Int((appModel.maxBrightness * 100).rounded()))%")
                            .monospacedDigit()
                            .foregroundStyle(.secondary)
                            .frame(width: 40, alignment: .trailing)
                    }
                }
            }
        }
    }
}

struct AboutTab: View {
    var body: some View {
        VStack(spacing: 16) {
            Image(systemName: "lightbulb.fill")
                .font(.system(size: 48))
                .foregroundStyle(.yellow.gradient)

            Text("Light Mix")
                .font(.title2.bold())

            Text("WWDC26 — Bring SwiftUI to your AppKit and UIKit App")
                .multilineTextAlignment(.center)
                .foregroundStyle(.secondary)
        }
    }
}

#Preview("Menu Bar") {
    MenuBarContent(appModel: AppModel())
}

#Preview("Settings") {
    SettingsView(appModel: AppModel())
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/272/5/e1e4aa9a-cbe2-4f83-9cea-3dcaae19afd6/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/272/5/e1e4aa9a-cbe2-4f83-9cea-3dcaae19afd6/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/272) — developer.apple.com. Indexed for agent consumption._
