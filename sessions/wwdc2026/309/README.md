---
id: "wwdc2026-309"
event: "wwdc2026"
year: 2026
title: "Explore Retention Messaging in App Store Connect"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/309"
topics: ["App Services", "App Store, Distribution & Marketing"]
platforms: ["iOS", "iPadOS", "tvOS", "visionOS"]
hasTranscript: true
---

# Explore Retention Messaging in App Store Connect

**Event:** WWDC26 · **Topic:** App Store, Distribution & Marketing · **Platforms:** iOS, iPadOS, tvOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-309](https://developer.apple.com/videos/play/wwdc2026/309)

Discover how you can use the power of Retention Messaging to reach subscribers before they cancel. Learn how to configure this feature in App Store Connect and add subscription offers, as well as leverage the Retention Messaging API to deliver real-time messaging and alternative options that encourage people to stay subscribed to your app or game.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,314 words)

## Documentation & Resources

- [Interest form: Real-time Retention Messaging](https://developer.apple.com/contact/request/retention-messaging-api/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/contact/request/retention-messaging-api/
- [Supporting monthly subscriptions with a 12-month commitment](https://developer.apple.com/documentation/StoreKit/supporting-monthly-subscriptions-with-a-12-month-commitment) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/supporting-monthly-subscriptions-with-a-12-month-commitment
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/supporting-monthly-subscriptions-with-a-12-month-commitment.json
- [Retention Messaging API](https://developer.apple.com/documentation/RetentionMessaging) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/RetentionMessaging
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/RetentionMessaging.json

## Code Snippets

### Signed transaction updates — [6:08]

```json
// Signed transaction updates

{
    "bundleId": "com.example.app",
    "productId": "Yoga_summer_2026",
    "type": "Auto-Renewable Subscription",
    "transactionReason": "RENEWAL",
    "inAppOwnershipType": "PURCHASED",
    "quantity": 1,
    "price": 0,
    "currency": "USD",
    "offerType": 5, // retention offer
    "offerIdentifier": "Yoga_2026_cancel_free_3m",
    "offerDiscountType": "FREE_TRIAL",
    "offerPeriod": "P3M", 
    "transactionId": "1000098916194"
    "originalTransactionId": "1000011859217",
    "appAccountToken": "23a91ca7-06f3-425f-bff6-820904b510a9",
    ...
}
```

### Retention Messaging API — [7:50]

```markdown
// Retention Messaging API: https://api.storekit.apple.com/inApps/v1/messaging

// URL configuration
PUT /realtime/url
GET /realtime/url
DELETE /realtime/url

// Message configuration
PUT /message/{messageIdentifier}
DELETE /message/{messageIdentifier}
GET /message/list
PUT /default/{productId}/{locale}
DELETE /default/{productId}/{locale}
GET /default/{productId}/{locale}

// Image configuration
PUT /image/{imageIdentifier}
DELETE /image/{imageIdentifier}
GET /image/list

// Performance testing - Sandbox only
POST /performanceTest // initiate test
GET /performanceTest/result/{requestId} // get results
```

### Real-time requests — [8:34]

```json
// Real-time requests

// Request from the App Store
{
    "originalTransactionId": "123456789",
    "appAppleId": 6745974591,
    "productId": "Yoga_summer_2026",
    "userLocale": "en-US",
    "requestIdentifier": "c03248af-dd76-4e9b-9c1e-4489cd19a768",
    "environment": "Production", // or Sandbox
    "signedDate": 1780920000000
}
```

### Real-time requests with message — [8:57]

```json
// Real-time requests

// Request from the App Store
{
    "originalTransactionId": "123456789",
    "appAppleId": 6745974591,
    "productId": "Yoga_summer_2026",
    "userLocale": "en-US",
    "requestIdentifier": 
        "c03248af-dd76-4e9b-9c1e-4489cd19a768",
    "environment": "Production", // or Sandbox
    "signedDate": 1780920000000
}

// Your response
{
    "message": {
        "messageIdentifier": 
            "551ee7c0-c097-418e-9dd5-2a98533a7390"
    }
}
```

### Real-time request with alternate product — [9:11]

```json
// Real-time requests

// Request from the App Store
{
    "originalTransactionId": "123456789",
    "appAppleId": 6745974591,
    "productId": "Yoga_summer_2026",
    "userLocale": "en-US",
    "requestIdentifier": 
        "c03248af-dd76-4e9b-9c1e-4489cd19a768",
    "environment": "Production", // or Sandbox
    "signedDate": 1780920000000
}

// Your response
{
    "alternateProduct": {
        "messageIdentifier":
            "ed7f25fc-5741-46a3-8502-062e0fb8afd0",
        "productId": "Yoga_summer_2026_annual"
    }
}
```

### Real-time request with promotional offer — [9:24]

```json
// Real-time requests

// Request from the App Store
{
    "originalTransactionId": "123456789",
    "appAppleId": 6745974591,
    "productId": "Yoga_summer_2026",
    "userLocale": "en-US",
    "requestIdentifier":          "c03248af-dd76-4e9b-9c1e-4489cd19a768",
    "environment": "Production", // or Sandbox
    "signedDate": 1780920000000
}

// Your response
{
    "promotionalOffer": {
        "messageIdentifier": 
            "80135e2b-ae15-4ec4-8c5c-9ecc8045c0dc",
        "promotionalOfferSignatureV2": "eyJhbGciOiJFUzI…"
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/309/4/afa0aec8-f216-43ed-bcb1-1a3742e49dac/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/309/4/afa0aec8-f216-43ed-bcb1-1a3742e49dac/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/309) — developer.apple.com. Indexed for agent consumption._