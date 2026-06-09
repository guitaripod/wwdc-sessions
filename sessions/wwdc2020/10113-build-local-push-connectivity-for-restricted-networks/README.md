---
id: "wwdc2020-10113"
event: "wwdc2020"
year: 2020
title: "Build local push connectivity for restricted networks"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10113"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Build local push connectivity for restricted networks

**Event:** WWDC20 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10113](https://developer.apple.com/videos/play/wwdc2020/10113)

Leverage local push connectivity and deliver notifications from your application server to devices on networks without an internet connection. Learn how to construct notifications for apps running in restricted network environments, helping people communicate with the same reliability and experience they would expect when connected to the internet. We’ll explore the technical details for this technology, when you might want to use it, and how to implement it in your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,065 words)

## Documentation & Resources

- [Receiving Voice and Text Communications on a Local Network](https://developer.apple.com/documentation/NetworkExtension/receiving-voice-and-text-communications-on-a-local-network) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/NetworkExtension/receiving-voice-and-text-communications-on-a-local-network
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/NetworkExtension/receiving-voice-and-text-communications-on-a-local-network.json
- [NEAppPushProvider entitlement application](https://developer.apple.com/contact/request/network-extension-app-push-provider) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/contact/request/network-extension-app-push-provider
- [CallKit](https://developer.apple.com/documentation/CallKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CallKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CallKit.json

## Code Snippets

### Create Configuration — [10:07]

```swift
import NetworkExtension

let manager = NEAppPushManager()
manager.matchSSIDs = [ "Cruise Ship Wi-Fi", "Cruise Ship Staff Wi-Fi" ]
manager.providerBundleIdentifier = "com.myexample.SimplePush.Provider"
manager.providerConfiguration = [ "host": "cruiseship.example.com" ]
manager.isEnabled = true

manager.saveToPreferences { (error) in
    if let error = error {
        // Handle error
        return
    }
    // Report success
}
```

### App Extension life cycle management and reporting VoIP call — [11:11]

```swift
// Manage App Extension life cycle and report VoIP call 

class SimplePushProvider: NEAppPushProvider {

    override func start(completionHandler: @escaping (Error?) -> Void) {
        // Connect to your provider server       
        completionHandler(nil)
    }

    override func stop(with reason: NEProviderStopReason,
                                   completionHandler: @escaping () -> Void) {
        // Disconnect your provider server
        completionHandler()
    }

    func handleIncomingVoIPCall(callInfo: [AnyHashable : Any]) {
        reportIncomingCall(userInfo: callInfo)
    }
}
```

### Handling incoming VoIP call in the containing app — [11:57]

```swift
class AppDelegate: UIResponder, UIApplicationDelegate, NEAppPushDelegate {
    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions:       
                     [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        NEAppPushManager.loadAllFromPreferences { (managers, error) in
            // Handle non-nil error
            for manager in managers {
                manager.delegate = self
            }
        }
        return true
    }

    func appPushManager(_ manager: NEAppPushManager,
                didReceiveIncomingCallWithUserInfo userInfo: [AnyHashable: Any] = [:]) {
        // Report incoming call to CallKit and let it display call UI
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10113/4/246C06C8-0984-49BA-A51A-0EEFDABB9EF3/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10113) — developer.apple.com. Indexed for agent consumption._
