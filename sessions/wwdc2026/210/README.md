---
id: "wwdc2026-210"
event: "wwdc2026"
year: 2026
title: "What’s new in Apple In-App Purchase"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/210"
topics: ["App Services", "App Store, Distribution & Marketing"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in Apple In-App Purchase

**Event:** WWDC26 · **Topic:** App Store, Distribution & Marketing · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-210](https://developer.apple.com/videos/play/wwdc2026/210)

Discover how monthly subscriptions with a 12-month commitment give people a more affordable option to pay for your subscription and secure a longer-term commitment. Explore how to configure and test this new payment option using App Store Connect, StoreKit APIs, Xcode testing, and more. Plus, learn about improvements to offer code redemption APIs, and enhancements to the App Review submission experience.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,031 words)

## Documentation & Resources

- [In-App Purchase types](https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-types) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-types
- [Managing the life cycle of monthly subscriptions with a 12-month commitment](https://developer.apple.com/documentation/StoreKit/managing-lifecycle-of-monthly-subscriptions-with-a-12-month-commitment-) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/managing-lifecycle-of-monthly-subscriptions-with-a-12-month-commitment-
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/managing-lifecycle-of-monthly-subscriptions-with-a-12-month-commitment-.json
- [Supporting monthly subscriptions with a 12-month commitment](https://developer.apple.com/documentation/StoreKit/supporting-monthly-subscriptions-with-a-12-month-commitment) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/supporting-monthly-subscriptions-with-a-12-month-commitment
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/supporting-monthly-subscriptions-with-a-12-month-commitment.json
- [App Store Server Notifications V2](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2.json
- [Supporting offer codes in your app](https://developer.apple.com/documentation/StoreKit/supporting-offer-codes-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/supporting-offer-codes-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/supporting-offer-codes-in-your-app.json
- [Implementing a store in your app using the StoreKit API](https://developer.apple.com/documentation/StoreKit/implementing-a-store-in-your-app-using-the-storekit-api) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/implementing-a-store-in-your-app-using-the-storekit-api
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/implementing-a-store-in-your-app-using-the-storekit-api.json

## Code Snippets

### Merchandise pricing terms with StoreKit views — [3:29]

```swift
// Merchandise pricing terms with StoreKit views

import StoreKit
import SwiftUI

struct SubscriptionStore: View {
    var body: some View {
        SubscriptionStoreView(groupID: "3F19ED53") {
            // Custom marketing content
        }
        .preferredSubscriptionPricingTerms {_, subscriptionInfo in
            subscriptionInfo.pricingTerms.first {
                $0.billingPlanType == .monthly
            }
        }
    }
}
```

### Get subscription pricing terms and make a purchase — [4:02]

```swift
// Get subscription pricing terms and make a purchase

import StoreKit

var product: Product?
// Fetch and assign product

// Get the monthly billing plan's pricing terms for merchandising
let pricingTerms = product?.subscription?.pricingTerms
  .first(where: {$0.billingPlanType == .monthly })
if let pricingTerms {
  let monthlyPrice = pricingTerms.billingDisplayPrice
  let totalCommitmentPrice = pricingTerms.commitmentInfo.price
  // Display both monthly and total commitment price to the customer
}

let result = try? await product?.purchase(options: [.billingPlanType(.monthly)])
switch result {
  // Verify the transaction, give the customer access to
  // the purchased content, and then finish the transaction
}
```

### Sheet to manage subscriptions by subscriptionGroupID — [5:05]

```swift
// Sheet to manage subscriptions by subscriptionGroupID

import SwiftUI
import StoreKit

struct ManageSubscriptionsButton: View {
    let subscriptionGroupID: String
    @State var presentingManageSubscriptionsSheet: Bool = false

    var body: some View {
        Button("Manage Subscriptions") {
            presentingManageSubscriptionsSheet = true
        }
        .manageSubscriptionsSheet(
            isPresented: $presentingManageSubscriptionsSheet,
            subscriptionGroupID: subscriptionGroupID
        )
    }
}
```

### JWSTransaction (decoded) for a monthly subscription with a 12-month commitment — [7:45]

```json
// JWSTransaction (decoded) for a monthly subscription with a 12-month commitment

{
    // …
    "expiresDate": 1783503660000, // for this billing period
    "price": 10990, // for this billing period
    "productId": "plus.pro.annual",
    "purchaseDate": 1780911660000,
    "type": "Auto-Renewable Subscription",
    "billingPlanType": "MONTHLY",
    "commitmentInfo": {
        "billingPeriodNumber": 1,
        "totalBillingPeriods": 12,
        "commitmentExpiresDate": 1812447660000,
        "commitmentPrice": 131880,
    }
}
```

### JWSRenewalInfo (decoded) for a monthly subscription with a 12-month commitment — [7:59]

```json
// JWSRenewalInfo (decoded) for a monthly subscription with a 12-month commitment

{
    // … 
    "renewalBillingPlanType": "MONTHLY",
    "commitmentInfo": {
        "commitmentAutoRenewProductId": “plus.standard.annual”,
        "commitmentAutoRenewStatus": 0,
        "commitmentRenewalDate": 1812447660000,
        "commitmentRenewalPrice": 10990,
        "commitmentRenewalBillingPlanType": "BILLED_UPFRONT"
    }
}
```

### Sheet to redeem an offer code — [9:58]

```swift
// Sheet to redeem an offer code

struct OfferCodeRedemption: View {
    @State var presentingOfferCodeSheet: Bool = false

    var body: some View {
        Button("Redeem Offer Code") {
            presentingOfferCodeSheet = true
        }
        .offerCodeRedemption(options: [], isPresented: $presentingOfferCodeSheet) {result in
            switch result {
            case .success(let verificationResult):
                switch verificationResult {
                    // Verify the transaction, give the customer access to
                    // the purchased content, and then finish the transaction
                }
            case .failure(let error):
                // Handle error
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/210/4/f029ab19-6670-48c6-b9b1-88ac6692cdda/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/210/4/f029ab19-6670-48c6-b9b1-88ac6692cdda/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/210) — developer.apple.com. Indexed for agent consumption._