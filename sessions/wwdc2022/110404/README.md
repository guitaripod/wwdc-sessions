---
id: "wwdc2022-110404"
event: "wwdc2022"
year: 2022
title: "Implement proactive in-app purchase restore"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110404"
topics: ["App Store, Distribution & Marketing"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Implement proactive in-app purchase restore

**Event:** WWDC22 · **Topic:** App Store, Distribution & Marketing · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-110404](https://developer.apple.com/videos/play/wwdc2022/110404)

Learn how you can restore someone’s in-app purchases access proactively when they first open your app. We’ll show you how you can deliver instant access to existing subscriptions using StoreKit or StoreKit 2 and cover best practices for both your client and server implementations. Find out more about how you can determine customer purchase state and create a personalized onboarding experience for your app.

**Keywords:** `storekit`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,185 words)

## Documentation & Resources

- [Implementing a store in your app using the StoreKit API](https://developer.apple.com/documentation/StoreKit/implementing-a-store-in-your-app-using-the-storekit-api) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/implementing-a-store-in-your-app-using-the-storekit-api
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/implementing-a-store-in-your-app-using-the-storekit-api.json
- [Introducing StoreKit 2](https://developer.apple.com/storekit/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/storekit/
- [App Store Server Notifications](https://developer.apple.com/documentation/appstoreservernotifications) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/appstoreservernotifications
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/appstoreservernotifications.json
- [Determining service entitlement on the server](https://developer.apple.com/documentation/StoreKit/determining-service-entitlement-on-the-server) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/determining-service-entitlement-on-the-server
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/determining-service-entitlement-on-the-server.json
- [Reducing Involuntary Subscriber Churn](https://developer.apple.com/documentation/StoreKit/reducing-involuntary-subscriber-churn) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/reducing-involuntary-subscriber-churn
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/reducing-involuntary-subscriber-churn.json
- [CloudKit](https://developer.apple.com/documentation/CloudKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CloudKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CloudKit.json

## Code Snippets

### Transaction Listener at app launch — [11:16]

```swift
//Transaction Listener at app launch
func listenForTransactions() -> Task<Void, Error> {
    return Task.detached {
        //Iterate through any transactions which didn't come from a direct call to `purchase()`.
        for await result in Transaction.updates {
            do {
                let transaction = try self.checkVerified(result)

                //Deliver products to the user.
                await self.updateCustomerProductStatus()

                //Always finish a transaction
                await transaction.finish()

            } catch {
                //StoreKit transaction failed verification, don't deliver content to user.
                print("Transaction failed verification")
            }
        }
    }
}
```

### Determine customer product state — [12:27]

```swift
//Determine customer product state
func updateCustomerProductStatus() async {

    var purchasedCars: [Product] = []
    var purchasedSubscriptions: [Product] = []
    var purchasedNonRenewableSubscriptions: [Product] = []

    //Iterate through all of the user's purchased products.
    for await result in Transaction.currentEntitlements {

       do {
         //First check if the transaction is verified. If the transaction is not verified
         //we'll catch the `failedVerification` error.
         let transaction = try checkVerified(result)

         //Check the `productType` of the transaction and get the corresponding product 
           from the store.
         switch transaction.productType {

         case .nonConsumable:

             if let car = cars.first(where: { $0.id == transaction.productID }) {
                        purchasedCars.append(car)
             }
         //..
```

### Determine customer product state — [12:56]

```swift
//Determine customer product state

case .nonRenewable:

    if let nonRenewable = nonRenewables.first(where: { $0.id == transaction.productID }),
          transaction.productID == "nonRenewing.standard" {

 //Non-renewing subscriptions have no inherent expiration. 

     let currentDate = Date()
     let expirationDate = Calendar(identifier: .gregorian).date(byAdding:
                                                    DateComponents(year: 1),
                                                    to: transaction.purchaseDate)!

    if currentDate < expirationDate {
        purchasedNonRenewableSubscriptions.append(nonRenewable)

      }
   }
//..
```

### Determine customer product state — [13:09]

```swift
//Determine customer product state

case .autoRenewable:

  if let subscription = subscriptions.first(where: { $0.id == transaction.productID }) {
purchasedSubscriptions.append(subscription) }
     default:
       break
      }
  } catch {
      print()
  }
}
//Update the Store information with the purchased products.
self.purchasedCars = purchasedCars
self.purchasedNonRenewableSubscriptions = purchasedNonRenewableSubscriptions
self.purchasedSubscriptions = purchasedSubscriptions

//Check subscriptionGroupStatus to learn auto-renewable subscription state
subscriptionGroupStatus = try? await subscriptions.first?.subscription?.status.first?.state

}
```

### Updating my car view at app launch — [13:45]

```swift
//Updating my car view at app launch

if store.purchasedCars.isEmpty && store.purchasedNonRenewableSubscriptions.isEmpty 
                               && store.purchasedSubscriptions.isEmpty {

               VStack {
                    Text("SK Demo App")
                        .bold()
                        .font(.system(size: 50))
                        .padding(.bottom, 20)
                    Text("🏎💨")
                        .font(.system(size: 120))
                        .padding(.bottom, 20)
                    Text("Head over to the shop to get started!")
                        .font(.headline)
                    NavigationLink {
                        StoreView()
                    }
            //…

     }
   }
}
```

### Updating my car view at app launch — [13:59]

```swift
//Updating my car view at app launch

else {
    List {
        Section("My Cars") {

        if !store.purchasedCars.isEmpty {

              ForEach(store.purchasedCars) { product in
                  NavigationLink {
                      ProductDetailView(product: product)
                 } label: {
                      ListCellView(product: product, purchasingEnabled: false)
                }
           } 
               } else {

          Text("You don't own any car products. \nHead over to the shop to get started!")

      }
   }
//…
```

### Updating my car view at app launch — [14:20]

```swift
//Updating my car view at app launch

Section("Navigation Service") {

     if !store.purchasedNonRenewableSubscriptions.isEmpty || 
         !store.purchasedSubscriptions.isEmpty {

          ForEach(store.purchasedNonRenewableSubscriptions) { product in
               NavigationLink {
                  ProductDetailView(product: product)
              } label: {
                  ListCellView(product: product, purchasingEnabled: false)
              }
          }

          ForEach(store.purchasedSubscriptions) { product in
               NavigationLink {
                   ProductDetailView(product: product)
               } label: {
                   ListCellView(product: product, purchasingEnabled: false)
              }
        }
    }
```

### Updating my car view at app launch — [14:30]

```swift
//Updating my car view at app launch

else  {

  if let subscriptionGroupStatus = store.subscriptionGroupStatus {

     if subscriptionGroupStatus == .expired || subscriptionGroupStatus == .revoked {

         Text("Welcome Back! \nHead over to the shop to get started!")

     } else if subscriptionGroupStatus == .inBillingRetryPeriod {

        //Provide a deep link from your app to https://apps.apple.com/account/billing.
         Text("Please verify your billing details.")

     }
     } else {

       Text("You don't own any subscriptions. \nHead over to the shop to get started!")
     }
   }         
}
```

### Fetch App Receipt Data — [17:42]

```swift
//Fetch App Receipt Data

public func getReceipt() {

    if let appStoreReceiptURL = Bundle.main.appStoreReceiptURL,
        FileManager.default.fileExists(atPath: appStoreReceiptURL.path) {

        do {
            let receiptData = try Data(contentsOf: appStoreReceiptURL, 
                                          options: .alwaysMapped)
            print(receiptData)

            let receiptString = receiptData.base64EncodedString(options: [])

            print("receipt send it to your server: \(receiptString)")

            // Read receiptData
        }
        catch { 
            print("Couldn't read receipt data with error: " + error.localizedDescription) 
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110404/3/55253AC0-EEDC-49B5-884C-CE8F562CC023/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110404/3/55253AC0-EEDC-49B5-884C-CE8F562CC023/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110404) — developer.apple.com. Indexed for agent consumption._