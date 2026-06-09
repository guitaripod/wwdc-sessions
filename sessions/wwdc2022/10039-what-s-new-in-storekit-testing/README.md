---
id: "wwdc2022-10039"
event: "wwdc2022"
year: 2022
title: "What's new in StoreKit testing"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10039"
topics: ["App Store, Distribution & Marketing"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# What's new in StoreKit testing

**Event:** WWDC22 · **Topic:** App Store, Distribution & Marketing · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10039](https://developer.apple.com/videos/play/wwdc2022/10039)

Discover the latest tools to help you test your in-app purchases and subscriptions. We’ll show you how to bring your products from App Store Connect into StoreKit Testing in Xcode, learn about improvements to the transaction manager, and explore your in-app purchase flow in Xcode Previews. We’ll also take you through best practices when setting up an Apple ID for the sandbox environment, and show you how to create tests for refund requests, price increase consent, billing retry, and much more.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,865 words)

## Documentation & Resources

- [Implementing offer codes in your app](https://developer.apple.com/documentation/StoreKit/implementing-offer-codes-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/implementing-offer-codes-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/implementing-offer-codes-in-your-app.json
- [Learn more about setting up offer codes](https://help.apple.com/app-store-connect/#/dev6a098e4b1) _guide_
- [Reducing Involuntary Subscriber Churn](https://developer.apple.com/documentation/StoreKit/reducing-involuntary-subscriber-churn) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/reducing-involuntary-subscriber-churn
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/reducing-involuntary-subscriber-churn.json
- [Testing In-App Purchases with sandbox](https://developer.apple.com/documentation/StoreKit/testing-in-app-purchases-with-sandbox) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/testing-in-app-purchases-with-sandbox
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/testing-in-app-purchases-with-sandbox.json
- [Setting up StoreKit Testing in Xcode](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/setting-up-storekit-testing-in-xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/setting-up-storekit-testing-in-xcode.json
- [Handling Subscriptions Billing](https://developer.apple.com/documentation/StoreKit/handling-subscriptions-billing) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/handling-subscriptions-billing
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/handling-subscriptions-billing.json
- [Auto-renewable subscriptions overview](https://developer.apple.com/app-store/subscriptions/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/app-store/subscriptions/

## Code Snippets

### Subscription option view — [6:58]

```swift
VStack(alignment: .leading) {
    Text(subscription.displayName)
        .font(.headline.weight(.semibold))
    Text(subscription.description)
}
```

### Refund view — [11:18]

```swift
struct RefundView: View {
    @State private var selectedTransactionID: UInt64?
    @State private var refundSheetIsPresented = false
    @Environment(\.dismiss) private var dismiss
    var body: some View {
        Button {
            refundSheetIsPresented = true
        } label: {
            Text("Request a refund")
                .bold()
                .padding(.vertical, 5)
                .frame(maxWidth: .infinity)
        }
        .buttonStyle(.borderedProminent)
        .padding([.horizontal, .bottom])
        .disabled(selectedTransactionID == nil)
        .refundRequestSheet(
            for: selectedTransactionID ?? 0,
            isPresented: $refundSheetIsPresented
        ) { result in
            if case .success(.success) = result {
                dismiss()
            }
        }
    }
}
```

### Refunds emit an updated value from the transaction updates sequence — [12:33]

```swift
for await update in Transaction.updates {
    let transaction = try update.payloadValue

    if let revocationDate = transaction.revocationDate,
  	   let revocationReason = transaction.revocationReason {
        print("\(transaction.productID) revoked on \(revocationDate)")

        switch revocationReason {
        case .developerIssue: <#Handle developer issue#>
        case .other: <#Handle other issue#>
        default: <#Handle unknown reason#>
        }

        <#Revoke access to the product#>
    }
    <#...#>
}
```

### Offer code view — [14:21]

```swift
struct SubscriptionPurchaseView: View {
    @State private var redeemSheetIsPresented = false

    var body: some View {
        Button("Redeem an offer") {
            redeemSheetIsPresented = true
        }
        .buttonStyle(.borderless)
        .frame(maxWidth: .infinity)
        .padding(.vertical)
        .offerCodeRedeemSheet(isPresented: $redeemSheetIsPresented)
    }

}
```

### Offer redemptions emit updated values from Transaction.updates and Product.SubscriptionInfo.Status.updates — [16:23]

```swift
for await verificationResult in Transaction.updates {
    guard case .verified(let transaction) = verificationResult else {
        <#Handle failed verification#>
    }
    <#Handle updated transaction#>
}

for await updatedStatus in Product.SubscriptionInfo.Status.updates {
    guard case .verified(let renewalInfo) = updatedStatus.renewalInfo else {
        <#Handle failed verification#>
    }
    <#Handle updated status#>
}
```

### Check the active offer on the transaction value — [16:31]

```swift
for await status in Product.SubscriptionInfo.Status.updates {
    let transaction = try status.transaction.payloadValue
    let renewalInfo = try status.renewalInfo.payloadValue

    if let currentOfferType = transaction.offerType {
        switch currentType {
        case .introductory: <#Handle introductory offer#>
        case .promotional:  <#Handle promotional offer#>
        case .code:         <#Handle offer for codes#>
        default:            <#Handle unknown offer type#>
        }
        self.hasCurrentOffer = true
    }

    <#...#>

}
```

### Check the next pending offer on the renewal info value — [16:49]

```swift
for await status in Product.SubscriptionInfo.Status.updates {
    let transaction = try status.transaction.payloadValue
    let renewalInfo = try status.renewalInfo.payloadValue

    <#Check active current offer#>

    if let nextOfferType = renewalInfo.offerType {
        switch currentType {
        case .introductory: <#Handle introductory offer#>
        case .promotional: <#Handle promotional offer#>
        case .code:
            print("Customer has \(renewalInfo.offerID) queued")
            <#Handle offer for codes#>
        default: <#Handle unknown offer type#>
        }
        self.hasQueuedOffer = true
    }
    <#...#>
}
```

### Messages updates loop — [18:45]

```swift
private var pendingMessages: [Message] = []

private func updatesLoop() {
    for await message in Message.messages {
      if <#Check if sensitive view is presented#>,
         let display: DisplayMessageAction = <#Get display message action#> {
           try? display(message)
      }
      else {
        pendingMessages.append(message)
      }
    }
}
```

### Price increase changes emit an updated value from the status updates sequence — [20:53]

```swift
for await status in Product.SubscriptionInfo.Status.updates {
    let renewalInfo = try status.renewalInfo.payloadValue

    if renewalInfo.priceIncreaseStatus == .agreed {
        print("Customer consented to price increase")
        <#Handle consented to price increase#>
    }
    if renewalInfo.expirationReason == .didNotConsentToPriceIncrease {
        print("Customer did not consent to price increase")
        <#Handle expired due to not consenting to price increase#>
    }

    <#...#>

}
```

### Unit testing price increases — [21:19]

```swift
let session: SKTestSession = try SKTestSession(configurationFileNamed: "<#Configuration name#>")
session.disableDialogs = true

<#Purchase a subscription#>

var transaction: SKTestTransaction! = session.allTransactions().first
session.requestPriceIncreaseConsentForTransaction(identifier: transaction.identifier)

transaction = session.allTransactions().first
XCTAssertTrue(transaction.isPendingPriceIncreaseConsent)

<#Assert app updates for pending price increase#>

// Write a test case for consenting and cancelling due to price increase:

session.consentToPriceIncreaseForTransaction(identifier: transaction.identifier)

// OR

session.declinePriceIncreaseForTransaction(identifier: transaction.identifier)
session.expireSubscription(productIdentifier: "<#Product ID#>")

<#Assert app updates for finished price increase#>
```

### Billing retry and grace period status changes emit an updated value from the status updates sequence — [24:57]

```swift
for await status in Product.SubscriptionInfo.Status.updates {
    let renewalInfo = try status.renewalInfo.payloadValue

    if let gracePeriodExpirationDate = renewalInfo.gracePeriodExpirationDate,
       gracePeriodExpirationDate < .now {
        print("In grace period until \(gracePeriodExpirationDate)”)
        <#Allow access to subscription#>
    }
    else if renewalInfo.isInBillingRetry {
        <#Handle billing retry#>
    }

    <#...#>

}
```

### Using the state property of a status value to check for billing retry states — [25:27]

```swift
struct SubscriptionStatusView: View {
    let currentSubscription: Product
    let status: Product.SubscriptionInfo.Status
    @Environment(\.openURL) var openURL
    var body: some View {
        Section("Your Subscription") {
            <#...#>
            if status.state == .inBillingRetryPeriod || status.state == .inGracePeriod {
                VStack {
                    Text("""
                    There was a problem renewing your subscription. Open the App Store to
                    update your payment information.
                    """)
                    Button("Open the App Store") {
                        openURL(URL(string: "https://apps.apple.com/account/billing")!)
                    }
                }
            }
        }
    }
}
```

### Current entitlement APIs will account for grace period — [25:41]

```swift
for await entitlement in Transaction.currentEntitlements {
    <#Grant access to product#>
}
```

### Unit testing billing retry and grace period — [25:50]

```swift
let session: SKTestSession = try SKTestSession(configurationFileNamed: "<#Configuration name#>")
session.billingGracePeriodIsEnabled = true
session.shouldEnterBillingRetryOnRenewal = true

<#Purchase a subscription#>

wait(for: [<#XCTExpectation#>], timeout: 60)

let transaction: SKTestTransaction! = session.allTransactions().first
XCTAssertTrue(transaction.hasPurchaseIssue)

<#Assert app still allows access to subscription due to grace period#>

wait(for: [<#XCTExpectation#>], timeout: 60)

<#Assert app detects billing retry and no longer allows access to subscription#>

session.resolveIssueForTransaction(identifier: transaction.identifier)

<#Assert app allows access to subscription#>
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10039/5/38FCCB56-38F1-4E4D-B7D0-CF031642775A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10039/5/38FCCB56-38F1-4E4D-B7D0-CF031642775A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10039) — developer.apple.com. Indexed for agent consumption._
