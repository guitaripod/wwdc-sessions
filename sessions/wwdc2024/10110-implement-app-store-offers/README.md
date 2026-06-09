---
id: "wwdc2024-10110"
event: "wwdc2024"
year: 2024
title: "Implement App Store Offers"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10110"
topics: ["App Services", "App Store, Distribution & Marketing"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Implement App Store Offers

**Event:** WWDC24 · **Topic:** App Store, Distribution & Marketing · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-13 · **Session:** [wwdc2024-10110](https://developer.apple.com/videos/play/wwdc2024/10110)

Learn how to engage customers with App Store Offers using App Store Connect, as well as the latest StoreKit features and APIs. Discover how you can set up win-back offers (a new way to re-engage previous subscribers) and generate offer codes for Mac apps. And find out how to test offers in sandbox and Xcode to make sure they work smoothly.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,940 words)

## Documentation & Resources

- [Testing win-back offers in the sandbox environment](https://developer.apple.com/documentation/StoreKit/testing-win-back-offers-in-the-sandbox-environment) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/testing-win-back-offers-in-the-sandbox-environment
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/testing-win-back-offers-in-the-sandbox-environment.json
- [Merchandising win-back offers in your app](https://developer.apple.com/documentation/StoreKit/merchandising-win-back-offers-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/merchandising-win-back-offers-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/merchandising-win-back-offers-in-your-app.json
- [Supporting win-back offers in your app](https://developer.apple.com/documentation/StoreKit/supporting-win-back-offers-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/supporting-win-back-offers-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/supporting-win-back-offers-in-your-app.json
- [Testing win-back offers in Xcode](https://developer.apple.com/documentation/StoreKit/testing-win-back-offers-in-xcode) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/testing-win-back-offers-in-xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/testing-win-back-offers-in-xcode.json
- [PurchaseIntent](https://developer.apple.com/documentation/StoreKit/PurchaseIntent) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/PurchaseIntent
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/PurchaseIntent.json
- [Supporting offer codes in your app](https://developer.apple.com/documentation/StoreKit/supporting-offer-codes-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/supporting-offer-codes-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/supporting-offer-codes-in-your-app.json
- [offer](https://developer.apple.com/documentation/StoreKit/Transaction/offer-swift.property) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/Transaction/offer-swift.property
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/Transaction/offer-swift.property.json
- [Forum: App Store Distribution & Marketing](https://developer.apple.com/forums/topics/app-store-distribution-and-marketing?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/app-store-distribution-and-marketing?cid=vf-a-0010
- [Message](https://developer.apple.com/documentation/StoreKit/Message) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/Message
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/Message.json
- [StoreKit views](https://developer.apple.com/documentation/StoreKit/storekit-views) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/storekit-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/storekit-views.json
- [Setting up StoreKit Testing in Xcode](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/setting-up-storekit-testing-in-xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/setting-up-storekit-testing-in-xcode.json
- [Submit feedback](http://feedbackassistant.apple.com) _documentation_
- [Generating a signature for promotional offers](https://developer.apple.com/documentation/StoreKit/generating-a-signature-for-promotional-offers) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/generating-a-signature-for-promotional-offers
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/generating-a-signature-for-promotional-offers.json

## Code Snippets

### Present offer code redemption sheet on macOS - SwiftUI API — [4:25]

```swift
// Present offer code redemption sheet on macOS - SwiftUI API

import SwiftUI
import StoreKit

struct MyView: View {

    @State var showOfferCodeRedemption: Bool = false

    var body: some View {
        Button("Redeem Code") {
            showOfferCodeRedemption = true
        }
        .offerCodeRedemption(isPresented: $showOfferCodeRedemption) { result in
            // Handle result
        }
    }
}
```

### Choose preferred offer in a SubscriptionStoreView — [20:15]

```swift
// Choose preferred offer in a SubscriptionStoreView

import SwiftUI
import StoreKit

struct MyView: View {
    let groupID: String

    var body: some View {
        SubscriptionStoreView(groupID: groupID)
            .preferredSubscriptionOffer { product, subscription, eligibleOffers in
                let freeTrialOffer = eligibleOffers
                    .filter { $0.paymentMode == .freeTrial }
                    .max { lhs, rhs in
                        lhs.period.value < rhs.period.value
                    }
                return freeTrialOffer ?? eligibleOffers.first
            }
    }
}
```

### Check subscription entitlement and offer eligibility — [23:05]

```swift
// Check subscription entitlement and offer eligibility

import StoreKit

func shouldShowMerchandising(
    for groupID: String,
    productIDs: [Product.ID]
) async throws -> MerchandisingVisibility {
    // Get subscription status
    let statuses = try await Product.SubscriptionInfo.status(for: groupID)

    // Check if the customer is already entitled to the subscription
    let entitlement = SubscriptionEntitlement(for: statuses)
    if entitlement.autoRenewalEnabled {
        return .hidden
    }

    // Check for offers to show in merchandising UI
    let products = try await Product.products(for: productIDs)

    let isEligibleForIntroOffer = await Product.SubscriptionInfo.isEligibleForIntroOffer(for: groupID)
    if isEligibleForIntroOffer {
        let subscriptions = products.map {
            ($0, $0.subscription?.introductoryOffer)
        }
        return .visible(subscriptions)
    }

    // Check for eligible win-back offers
    let purchasedStatus = statuses.first {
        $0.transaction.unsafePayloadValue.ownershipType == .purchased
    }
    let renewalInfo = try purchasedStatus?.renewalInfo.payloadValue
    let bestWinBackOfferID = renewalInfo?.eligibleWinBackOfferIDs.first

    // Return the product with the offer if there is one
    if let bestWinBackOfferID {
        let subscriptions: [(Product, Product.SubscriptionOffer?)] = products.map {
            let winBackOffer = $0.subscription?.winBackOffers.first {
                $0.id == bestWinBackOfferID
            }
            return ($0, winBackOffer)
        }
        return .visible(subscriptions)
    }

    // Only return the product if there is no offer
    return .visible(products.map { ($0, nil) })
}

struct SubscriptionEntitlement {
    let isEntitled: Bool
    let autoRenewalEnabled: Bool

    init(for statuses: [Product.SubscriptionInfo.Status]) {
        let entitledStatuses = statuses.filter {
            $0.state == .subscribed || $0.state == .inBillingRetryPeriod || $0.state == .inGracePeriod
        }
        isEntitled = !entitledStatuses.isEmpty
        autoRenewalEnabled = entitledStatuses.contains {
            $0.renewalInfo.unsafePayloadValue.willAutoRenew
        }
    }
}

enum MerchandisingVisibility {
    case hidden
    case visible([(Product, Product.SubscriptionOffer?)])
}
```

### Add a win-back offer to a purchase — [25:26]

```swift
// Add a win-back offer to a purchase

import StoreKit

func purchase(
    _ product: Product,
    with offer: Product.SubscriptionOffer?
) async throws {
    // Prepare the purchase options
    var purchaseOptions: Set<Product.PurchaseOption> = []

    // Add win-back offer to the purchase
    if let offer, offer.type == .winBack {
        purchaseOptions.insert(.winBackOffer(offer))
    }

    // Make the purchase
    try await product.purchase(options: purchaseOptions)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10110/4/D12EC56F-E036-4B66-BC08-8F01A5D49690/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10110/4/D12EC56F-E036-4B66-BC08-8F01A5D49690/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10110) — developer.apple.com. Indexed for agent consumption._
