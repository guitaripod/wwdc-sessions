---
id: "wwdc2022-10016"
event: "wwdc2022"
year: 2022
title: "Get more mileage out of your app with CarPlay"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10016"
topics: ["SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Get more mileage out of your app with CarPlay

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** iOS, iPadOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10016](https://developer.apple.com/videos/play/wwdc2022/10016)

CarPlay is a smarter, safer way to use your iPhone while you drive. Learn about the latest app types for CarPlay and discover how the CarPlay Simulator can help you develop and test apps without leaving your desk. We’ll also explore how navigation apps can connect with digital instrument clusters in supported vehicles.

**Keywords:** `🚗`, `🚙`, `audio`, `car`, `communication`, `driving task`, `ev charging`, `fueling`, `navigation`, `parking`, `quick food ordering`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,140 words)

## Documentation & Resources

- [CarPlay for developers](https://developer.apple.com/carplay) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/carplay
- [Human Interface Guidelines: CarPlay](https://developer.apple.com/design/human-interface-guidelines/carplay) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/carplay

## Code Snippets

### Application scene manifest — [15:43]

```xml
<key>UIApplicationSceneManifest</key>
<dict>
    <!-- Indicate support for CarPlay dashboard -->
    <key>CPSupportsDashboardNavigationScene</key>
    <true/>
    <!-- Indicate support for instrument cluster displays -->
    <key>CPSupportsInstrumentClusterNavigationScene</key>
    <true/>
    <!-- Indicate support for multiple scenes -->
    <key>UIApplicationSupportsMultipleScenes</key>
    <true/>
    <key>UISceneConfigurations</key>
    <dict>
        <!-- For device scenes -->
        <key>UIWindowSceneSessionRoleApplication</key>
        <array>
            <dict>
                <key>UISceneClassName</key>
                <string>UIWindowScene</string>
                <key>UISceneConfigurationName</key>
                <string>Phone</string>
                <key>UISceneDelegateClassName</key>
                <string>MyAppWindowSceneDelegate</string>
            </dict>
        </array>
        <!-- For the main CarPlay scene -->
        <key>CPTemplateApplicationSceneSessionRoleApplication</key>
        <array>
            <dict>
                <key>UISceneClassName</key>
                <string>CPTemplateApplicationScene</string>
                <key>UISceneConfigurationName</key>
                <string>CarPlay</string>
                <key>UISceneDelegateClassName</key>
                <string>MyAppCarPlaySceneDelegate</string>
            </dict>
        </array>
        <!-- For the CarPlay Dashboard scene -->
        <key>CPTemplateApplicationDashboardSceneSessionRoleApplication</key>
        <array>
            <dict>
                <key>UISceneClassName</key>
                <string>CPTemplateApplicationDashboardScene</string>
                <key>UISceneConfigurationName</key>
                <string>CarPlay-Dashboard</string>
                <key>UISceneDelegateClassName</key>
                <string>MyAppCarPlayDashboardSceneDelegate</string>
            </dict>
        </array>
        <!-- For the CarPlay instrument cluster scene -->
        <key>CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication</key>
        <array>
            <dict>
                <key>UISceneClassName</key>
                <string>CPTemplateApplicationInstrumentClusterScene</string>
                <key>UISceneConfigurationName</key>
                <string>CarPlay-Instrument-Cluster</string>
                <key>UISceneDelegateClassName</key>
                <string>MyAppCarPlayInstrumentClusterSceneDelegate</string>
            </dict>
        </array>
    </dict>
</dict>
```

### Application instrument cluster scene delegate — [16:00]

```swift
extension TemplateApplicationSceneDelegate: CPTemplateApplicationInstrumentClusterSceneDelegate {

    func templateApplicationInstrumentClusterScene(
        _ templateApplicationInstrumentClusterScene: CPTemplateApplicationInstrumentClusterScene,
        didConnect instrumentClusterController: CPInstrumentClusterController) {
        // Connected to Instrument Cluster
        TemplateManager.shared.clusterController(instrumentClusterController, didConnectWith: templateApplicationInstrumentClusterScene.contentStyle)
    }

…

    func instrumentClusterControllerDidConnect(_ instrumentClusterWindow: UIWindow) {
        // Window in which to draw instrument cluster contents 
       self.instrumentClusterWindow = instrumentClusterWindow
    }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10016/4/4A58011C-EB98-4462-A8F7-8EDB8A69BBE7/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10016/4/4A58011C-EB98-4462-A8F7-8EDB8A69BBE7/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10016) — developer.apple.com. Indexed for agent consumption._
