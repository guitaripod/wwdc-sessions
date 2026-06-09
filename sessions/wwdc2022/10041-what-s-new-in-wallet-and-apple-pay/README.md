---
id: "wwdc2022-10041"
event: "wwdc2022"
year: 2022
title: "What’s new in Wallet and Apple Pay"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10041"
topics: ["App Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# What’s new in Wallet and Apple Pay

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10041](https://developer.apple.com/videos/play/wwdc2022/10041)

Discover the latest updates to Wallet & Apple Pay. We'll show you how to support Orders in Wallet for your apps and websites and securely validate someone's age and identity with the Identity Verification API. We'll also explore PassKit support for SwiftUI, and discuss how you how you can improve your Apple Pay experience with Automatic Payments.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,467 words)

## Documentation & Resources

- [Example Order Packages](https://developer.apple.com/documentation/WalletOrders/example-order-packages) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WalletOrders/example-order-packages
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WalletOrders/example-order-packages.json
- [ApplePayPaymentRequest](https://developer.apple.com/documentation/ApplePayontheWeb/ApplePayPaymentRequest) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ApplePayontheWeb/ApplePayPaymentRequest
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ApplePayontheWeb/ApplePayPaymentRequest.json
- [Apple Pay Merchant Token Management API](https://developer.apple.com/documentation/MerchantTokenNotificationServices) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/MerchantTokenNotificationServices
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/MerchantTokenNotificationServices.json
- [Wallet Orders](https://developer.apple.com/documentation/WalletOrders) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WalletOrders
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WalletOrders.json
- [Human Interface Guidelines: Wallet](https://developer.apple.com/design/human-interface-guidelines/wallet) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/human-interface-guidelines/wallet
- [Verifying Wallet identity requests](https://developer.apple.com/documentation/PassKit/verifying-wallet-identity-requests) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PassKit/verifying-wallet-identity-requests
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PassKit/verifying-wallet-identity-requests.json
- [Requesting identity data from a Wallet pass](https://developer.apple.com/documentation/PassKit/requesting-identity-data-from-a-wallet-pass) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PassKit/requesting-identity-data-from-a-wallet-pass
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PassKit/requesting-identity-data-from-a-wallet-pass.json
- [Apple Pay on the Web Interactive Demo](https://applepaydemo.apple.com) _guide_
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

### AddPassToWalletButton — [2:39]

```swift
@State var addedToWallet: Bool

@ViewBuilder private var airlineButton: some View {
    if let pass = createAirlinePass() {
        AddPassToWalletButton([pass]) { added in
            addedToWallet = added
        }
        .frame(width: 250, height: 50)
        .addPassToWalletButtonStyle(.blackOutline)
    } else {
        // Fallback
    }
}
```

### PayWithApplePayButton — [3:40]

```swift
// Create a payment request
let paymentRequest = PKPaymentRequest()
// ...

// Create a payment authorization change method
func authorizationChange(phase: PayWithApplePayButtonPaymentAuthorizationPhase) { ... }

PayWithApplePayButton(
    .plain,
    request: paymentRequest,
    onPaymentAuthorizationChange: authorizationChange
) {
    // Fallback
}
.frame(width: 250, height: 50)
.payWithApplePayButtonStyle(.automatic)
```

### Multi-merchant payments — [6:34]

```swift
// Create a payment request
let paymentRequest = PKPaymentRequest()
// ...

// Set total amount
paymentRequest.paymentSummaryItems = [
    PKPaymentSummaryItem(label: "Total", amount: 500)
]

// Create a multi token context for each additional merchant in the payment
let multiTokenContexts = [
    PKPaymentTokenContext(
        merchantIdentifier: "com.example.air-travel",
        externalIdentifier: "com.example.air-travel",
        merchantName: "Air Travel",
        merchantDomain: "air-travel.example.com",
        amount: 150
    ),
    PKPaymentTokenContext(
        merchantIdentifier: "com.example.hotel",
        externalIdentifier: "com.example.hotel",
        merchantName: "Hotel",
        merchantDomain: "hotel.example.com",
        amount: 300
    ),
    PKPaymentTokenContext(
        merchantIdentifier: "com.example.car-rental",
        externalIdentifier: "com.example.car-rental",
        merchantName: "Car Rental",
        merchantDomain: "car-rental.example.com",
        amount: 50
    )
]
paymentRequest.multiTokenContexts = multiTokenContexts
```

### Automatic Payments - Recurring payment request — [10:14]

```swift
// Specify the amount and billing periods
let regularBilling = PKRecurringPaymentSummaryItem(label: "Membership", amount: 20)

let trialBilling = PKRecurringPaymentSummaryItem(label: "Trial Membership", amount: 10)

let trialEndDate = Calendar.current.date(byAdding: .month, value: 1, to: Date.now)
trialBilling.endDate = trialEndDate
regularBilling.startDate = trialEndDate

// Create a recurring payment request
let recurringPaymentRequest = PKRecurringPaymentRequest(
    paymentDescription: "Book Club Membership",
    regularBilling: regularBilling,
    managementURL: URL(string: "https://www.example.com/managementURL")!
)
recurringPaymentRequest.trialBilling = trialBilling

recurringPaymentRequest.billingAgreement = """
50% off for the first month. You will be charged $20 every month after that until you cancel. \ You may cancel at any time to avoid future charges. To cancel, go to your Account and click \ Cancel Membership.
"""

recurringPaymentRequest.tokenNotificationURL = URL(
    string: "https://www.example.com/tokenNotificationURL"
)!

// Update the payment request
let paymentRequest = PKPaymentRequest()
// ...
paymentRequest.recurringPaymentRequest = recurringPaymentRequest

// Include in the summary items
let total = PKRecurringPaymentSummaryItem(label: "Book Club", amount: 10)
total.endDate = trialEndDate
paymentRequest.paymentSummaryItems = [trialBilling, regularBilling, total]
```

### Automatic Payments - Automatic reload payment request — [12:39]

```swift
// Specify the reload amount and threshold
let automaticReloadBilling = PKAutomaticReloadPaymentSummaryItem(
    label: "Coffee Shop Reload",
    amount: 25
)
reloadItem.thresholdAmount = 5

// Create an automatic reload payment request
let automaticReloadPaymentRequest = PKAutomaticReloadPaymentRequest(
    paymentDescription: "Coffee Shop",
    automaticReloadBilling: automaticReloadBilling,
    managementURL: URL(string: "https://www.example.com/managementURL")!
)

automaticReloadPaymentRequest.billingAgreement = """
Coffee Shop will add $25.00 to your card immediately, and will automatically reload your \
card with $25.00 whenever the balance falls below $5.00. You may cancel at any time to avoid \ future charges. To cancel, go to your Account and click Cancel Reload.
"""

automaticReloadPaymentRequest.tokenNotificationURL = URL(
    string: "https://www.example.com/tokenNotificationURL"
)!

// Update the payment request
let paymentRequest = PKPaymentRequest()
// ...
paymentRequest.automaticReloadPaymentRequest = automaticReloadPaymentRequest

// Include in the summary items
let total = PKAutomaticReloadPaymentSummaryItem(
    label: "Coffee Shop",
    amount: 25
)
total.thresholdAmount = 5
paymentRequest.paymentSummaryItems = [total]
```

### Order Tracking (swift) — [19:17]

```swift
func onAuthorizationChange(phase: PayWithApplePayButtonPaymentAuthorizationPhase) {
    switch phase {
    // ...
    case .didAuthorize(let payment, let resultHandler):
        server.createOrder(with: payment) { serverResult in
            guard case .success(let orderDetails) = serverResult else { /* handle error */ }
            let result = PKPaymentAuthorizationResult(status: .success, errors: nil)
            result.orderDetails = PKPaymentOrderDetails(
                orderTypeIdentifier: orderDetails.orderTypeIdentifier,
                orderIdentifier: orderDetails.orderIdentifier,
                webServiceURL: orderDetails.webServiceURL,
                authenticationToken: orderDetails.authenticationToken,
            )
            resultHandler(result)
        }
    }
}
```

### Order Tracking (JS) — [20:13]

```javascript
paymentRequest.show().then((response) => {
    server.createOrder(response).then((orderDetails) => {
        let details = { };
        if (response.methodName === "https://apple.com/apple-pay") {
            details.data = {
                orderDetails: {
                    orderTypeIdentifier: orderDetails.orderTypeIdentifier,
                    orderIdentifier: orderDetails.orderIdentifier,
                    webServiceURL: orderDetails.webServiceURL,
                    authenticationToken: orderDetails.authenticationToken,
                },
            };
        }
        response.complete("success", details);
    });
});
```

### VerifyIdentityWithWalletButton 2 — [27:05]

```swift
@ViewBuilder var verifiyIdentityButton: some View {
    VerifyIdentityWithWalletButton(
        .verifyIdentity,
        request: createRequest(),
    ) { result in
        // ...
    } fallback: {
        // verify identity another way
    }
}
```

### Create a PKIdentityRequest — [27:18]

```swift
func createRequest() -> PKIdentityRequest {
    let descriptor = PKIdentityDriversLicenseDescriptor()
    descriptor.addElements([.age(atLeast: 18)],
                            intentToStore: .willNotStore)
    descriptor.addElements([.givenName, .familyName, .portrait],
                            intentToStore: .mayStore(days: 30))

    let request = PKIdentityRequest()
    request.descriptor = descriptor
    request.merchantIdentifier = // configured in Developer account
    request.nonce = // bound to user session
}
```

### VerifyIdentityWithWalletButton 3 — [27:19]

```swift
@ViewBuilder var verifiyIdentityButton: some View {
    VerifyIdentityWithWalletButton(
        .verifyIdentity,
        request: createRequest(),
    ) { result in
        // ...
    } fallback: {
        // verify identity another way
    }
}
```

### VerifyIdentityWithWalletButton 4 — [29:37]

```swift
@ViewBuilder var verifiyIdentityButton: some View {
    VerifyIdentityWithWalletButton(
        .verifyIdentity,
        request: createRequest(),
    ) { result in
        switch result {
        case .success(let document):
            // send document to server for decryption and verification
        case .failure(let error):
            switch error {
            case PKIdentityError.cancelled:
                // handle cancellation
            default:
                // handle other errors
            }
        }
    } fallback: {
        // verify identity another way
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10041/4/A173FAFA-9D08-4E7F-9154-7B821167B78E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10041/4/A173FAFA-9D08-4E7F-9154-7B821167B78E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10041) — developer.apple.com. Indexed for agent consumption._
