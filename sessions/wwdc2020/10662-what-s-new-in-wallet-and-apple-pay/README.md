---
id: "wwdc2020-10662"
event: "wwdc2020"
year: 2020
title: "What's new in Wallet and Apple Pay"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10662"
topics: ["App Services"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# What's new in Wallet and Apple Pay

**Event:** WWDC20 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10662](https://developer.apple.com/videos/play/wwdc2020/10662)

Apple Pay makes it simple to pay for goods and services in your app and on your website. Discover how you can integrate API updates like context-specific button types, contact data formatting, and cross-platform support to make the service more effective for you and people using it. And, if you’re building app clips, adopting Apple Pay can help you unlock new commerce experiences.

**Keywords:** `banking`, `nfc`, `pass`, `ticket`, `transportation`, `web`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,621 words)

## Documentation & Resources

- [Apple Pay on the Web](https://developer.apple.com/documentation/apple_pay_on_the_web) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/apple_pay_on_the_web
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/apple_pay_on_the_web.json
- [PassKit (Apple Pay and Wallet)](https://developer.apple.com/documentation/PassKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PassKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PassKit.json
- [Apple Pay](https://developer.apple.com/documentation/passkit/apple_pay) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/passkit/apple_pay
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/passkit/apple_pay.json

## Code Snippets

### Implementing Apple Pay on the Mac — [7:44]

```swift
// PKPaymentAuthorizationControllerDelegate 

func presentationWindow(for controller: PKPaymentAuthorizationController) -> UIWindow? {
    let purchaseWindow = yourViewController.view.window
    return (purchaseWindow) // The window presenting the payment sheet.
}


func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didRequestMerchantSessionUpdate handler: @escaping (PKPaymentRequestMerchantSessionUpdate) -> Void) {
    // Get merchant session to enable the user to authorize a transaction.
    var dict = try? JSONSerialization.jsonObject(with: data, options: .allowFragments) as? [String: Any] {
        let session = PKPaymentMerchantSession(dictionary: dict)
        let update = PKPaymentRequestMerchantSessionUpdate(status: .success, merchantSession: session)
        handler(update)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10662/10/5BB96234-A10B-43DF-9223-A782EE855E87/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10662) — developer.apple.com. Indexed for agent consumption._
