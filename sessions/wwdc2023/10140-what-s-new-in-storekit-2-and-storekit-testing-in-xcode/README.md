---
id: "wwdc2023-10140"
event: "wwdc2023"
year: 2023
title: "What’s new in StoreKit 2 and StoreKit Testing in Xcode"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10140"
topics: ["App Store, Distribution & Marketing", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in StoreKit 2 and StoreKit Testing in Xcode

**Event:** WWDC23 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10140](https://developer.apple.com/videos/play/wwdc2023/10140)

Get to know the latest enhancements to StoreKit 2 and StoreKit Testing in Xcode. Discover API updates for promoted in-app purchases, StoreKit messages, the Transaction model, the RenewalInfo model, and the App Store sheet for managing subscriptions. Learn how to upgrade to SHA-256 for on-device receipt validation and use APIs to create SwiftUI views. We’ll also help you get started with StoreKit Testing in Xcode so that you can debug and test your in-app purchases and subscriptions. Meet the Transaction Inspector, explore the latest updates to the StoreKit configuration editor, and find out how you can simulate StoreKit errors to test your app’s error handling.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,147 words)

## Documentation & Resources

- [Testing failing subscription renewals and In-App Purchases](https://developer.apple.com/documentation/StoreKit/testing-failing-subscription-renewals-and-in-app-purchases) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/testing-failing-subscription-renewals-and-in-app-purchases
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/testing-failing-subscription-renewals-and-in-app-purchases.json
- [Message](https://developer.apple.com/documentation/StoreKit/Message) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/Message
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/Message.json
- [Supporting promoted In-App Purchases in your app](https://developer.apple.com/documentation/StoreKit/supporting-promoted-in-app-purchases-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/supporting-promoted-in-app-purchases-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/supporting-promoted-in-app-purchases-in-your-app.json
- [Turn on Family Sharing for in-app purchases in App Store Connect](https://help.apple.com/app-store-connect/#/dev45b03fab9) _documentation_
- [Setting up StoreKit Testing in Xcode](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/setting-up-storekit-testing-in-xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/setting-up-storekit-testing-in-xcode.json
- [Submit feedback](http://feedbackassistant.apple.com) _documentation_
- [StoreKit](https://developer.apple.com/documentation/StoreKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit.json

## Code Snippets

### Create a listener for promoted in-app purchases — [1:42]

```swift
// Create a listener for promoted in-app purchases
import StoreKit

let promotedPurchasesListener = Task {
    for await promotion in PurchaseIntent.intents {
        // Process promotion
        let product = promotion.product

        // Purchase promoted product
        do {
            let result = try await product.purchase()
            // Process result
        }
        catch {
            // Handle error
        }
    }
}
```

### Check promotion order — [2:57]

```swift
// Check promotion order
import StoreKit

do {
    let promotions = try await Product.PromotionInfo.currentOrder

    if promotions.isEmpty {
        // No local promotion order set
    }

    for promotion in promotions {
        let productID = promotion.productID
        let productVisibility = promotion.visibility
        // Check promoted products
    }
}
catch {
    // Handle error
}
```

### Set a promotion order — [3:26]

```swift
// Set a promotion order
import StoreKit

let newPromotionOrder: [String] = [
    "acorns.individual",
    "nectar.cup",
    "sunflowerseeds.pile"
]

do {
    try await Product.PromotionInfo.updateProductOrder(byID: newPromotionOrder)
}
catch {
    // Handle error
}
```

### Update promotion visibility — [4:02]

```swift
// Update promotion visibility
import StoreKit

// Hide “acorns.individual”
do {
    try await Product.PromotionInfo.updateProductVisibility(.hidden, for: "acorns.individual")
}
catch {
    // Handle error
}
```

### Update promotion visibility (alternative method) — [4:17]

```swift
// Update promotion visibility
import StoreKit

do {
  let promotions = try await Product.PromotionInfo.currentOrder

  // Hide the first product
  if var firstPromotion = promotions.first {
    firstPromotion.visibility = .hidden
    try await firstPromotion.update()
  }
}
catch {
  // Handle error
}
```

### Product view — [8:32]

```swift
// Product view
import SwiftUI
import StoreKit

struct BirdFoodShop: View {
    let productID: String
    let productImage: String

    var body: some View {
        ProductView(id: productID) {
            BirdFoodProductIcon(for: productID)
        }
        .productViewStyle(.large)
    }
}
```

### Store view — [8:52]

```swift
// Store view
import SwiftUI
import StoreKit

struct BirdFoodShop: View {
    let productIDs: [String]

    var body: some View {
        StoreView(ids: productIDs) { product in
            BirdFoodIcon(productID: product.id)
        }
    }
}
```

### Subscription view — [9:19]

```swift
// Subscription view
import SwiftUI
import StoreKit

struct BackyardBirdsPassShop: View {
    let groupID: String

    var body: some View {
        SubscriptionStoreView(groupID: groupID)
    }
}
```

### Simulated off-device purchase using StoreKitTest — [21:09]

```swift
// Simulated off-device purchase using StoreKitTest
import StoreKit
import StoreKitTest

func testSubscriptionRenewal() async throws {
    let session = try SKTestSession(configurationFileNamed: "Store")

    let oneYearInterval: TimeInterval = (365 * 24 * 60 * 60)
    let transaction = try await session.buyProduct(
        identifier: "birdpass.individual",
        options: [
            .purchaseDate(Date.now - oneYearInterval)
        ]
    )

    // Inspect transaction
}
```

### Set a simulated purchase error when loading products — [21:48]

```swift
// Set a simulated purchase error when loading products
import StoreKit
import StoreKitTest

func testLoadProducts() async throws {
    let session = try SKTestSession(configurationFileNamed: "Store")
    let productIDs = [
        "acorns.individual",
        "nectar.cup"
    ]

    // Set a simulated error, then load products, expecting an error
    session.setSimulatedError(.generic(.networkError), forAPI: .loadProducts)
    do {
        _ = try await Product.products(for: productIDs)
        XCTFail("Expected a network error")
    }
    catch StoreKitError.networkError(_) {
        // Expected error thrown, continue...
    }
    // Disable simulated error
    session.setSimulatedError(nil, forAPI: .loadProducts)
}
```

### Set a faster subscription renewal rate in a test session — [22:24]

```swift
// Set a faster subscription renewal rate in a test session
import StoreKit
import StoreKitTest

func testSubscriptionRenewal() async throws {
    let session = try SKTestSession(configurationFileNamed: "Store")

    // Set renewals to expire every minute
    session.timeRate = .oneRenewalEveryMinute

    let transaction = try await session.buyProduct(identifier: "birdpass.individual")

    // Wait for renewals and inspect transactions
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10140/4/F65F9FA7-3629-45A5-A4D6-A90BE40BE5E9/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10140/4/F65F9FA7-3629-45A5-A4D6-A90BE40BE5E9/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10140) — developer.apple.com. Indexed for agent consumption._
