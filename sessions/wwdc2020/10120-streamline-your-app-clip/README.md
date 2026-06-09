---
id: "wwdc2020-10120"
event: "wwdc2020"
year: 2020
title: "Streamline your App Clip"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10120"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Streamline your App Clip

**Event:** WWDC20 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10120](https://developer.apple.com/videos/play/wwdc2020/10120)

App Clips are best when they provide an “in the moment” experience for people using them, like ordering your favorite refreshing beverage or paying for parking. We’ll share guidelines and best practices for building focused and consistent App Clips, show you how to streamline transaction experiences by taking advantage of technologies like App Clip notifications and location confirmation, and explore how you can help people move from your App Clip over to your full app. To get the most out of this session, we recommend first watching “Explore App Clips” and “Configure and link your App Clips.”

**Keywords:** `8 hours notification`, `asset catalog`, `aswebauthenticationsession`, `ephemeral notification`, `inregion`, `location confirmation`, `nsappcliprequestephemeralusernotification`, `permission requests`, `request permissions`, `secure app group`, `sign in with apple`, `skoverlay`, `transaction`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,646 words)

## Documentation & Resources

- [App Clips](https://developer.apple.com/documentation/AppClip) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip.json
- [Responding to invocations](https://developer.apple.com/documentation/AppClip/responding-to-invocations) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip/responding-to-invocations
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip/responding-to-invocations.json
- [Fruta: Building a feature-rich app with SwiftUI](https://developer.apple.com/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip/fruta-building-a-feature-rich-app-with-swiftui.json
- [Learn more about creating app clips](https://developer.apple.com/app-clips/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/app-clips/
- [Choosing the right functionality for your App Clip](https://developer.apple.com/documentation/AppClip/choosing-the-right-functionality-for-your-app-clip) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip/choosing-the-right-functionality-for-your-app-clip
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip/choosing-the-right-functionality-for-your-app-clip.json

## Code Snippets

### Confirm a physical code's location. — [7:53]

```swift
import AppClip

guard let payload = userActivity.appClipActivationPayload else {
    return
}

let region = CLCircularRegion(center: CLLocationCoordinate2D(latitude: 37.3298193,        
    longitude: -122.0071671), radius: 100, identifier: "apple_park")

payload.confirmAcquired(in: region) { (inRegion, error) in

}
```

### Query if user has granted app clip notification on app clip card. — [9:24]

```swift
import UserNotifications

let center = UNUserNotificationCenter.current()

center.getNotificationSettings { (settings) in
   if settings.authorizationStatus == .ephemeral {
        // User has already granted ephemeral notification.
    }

}
```

### Embed SKOverlay to your app clip — [10:49]

```swift
import SwiftUI
    import StoreKit

    struct ContentView : View {
        @State private var finishedPaymentFlow = false

        var body: some View {
            NavigationView {
                CheckoutView($finishedPaymentFlow)
            }
            .appStoreOverlay(isPresented: $finishedPaymentFlow) {
                SKOverlay.AppClipConfiguration(position: .bottom)
            }
        }
    }
```

### Save user ID in app clip's secure app group. — [11:32]

```swift
// Automatically log in with Sign in with Apple
import AuthenticationServices

SignInWithAppleButton(.signUp, onRequest: { _ in
}, onCompletion: { result in
    switch result {
    case .success(let authorization):
        guard let secureAppGroupURL = 
            FileManager.default.containerURL(forSecurityApplicationGroupIdentifier:
                "group.com.example.apple-samplecode.fruta")
            else { return };
        guard let credential = authorization.credential as? ASAuthorizationAppleIDCredential 
            else { return }
        save(userID: credential.user, in: secureAppGroupURL)
    case .failure(let error):
        print(error)
   }
})
```

### Automatically sign in users to your app if they have signed into your app clip. — [11:55]

```swift
import AuthenticationServices

let provider = ASAuthorizationAppleIDProvider()
guard let secureAppGroupURL =
    FileManager.default.containerURL(forSecurityApplicationGroupIdentifier:   
        "group.com.example.apple-samplecode.fruta")
    else { return };
let user = readUserID(in: secureAppGroupURL)
provider.getCredentialState(forUserID: user) { state, error in
    if state == .authorized {
       loadFavoriteSmoothies(userID: user)
   }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10120/4/921130DC-4D6D-4D9B-8990-AE17E9068B2F/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10120) — developer.apple.com. Indexed for agent consumption._
