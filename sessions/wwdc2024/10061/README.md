---
id: "wwdc2024-10061"
event: "wwdc2024"
year: 2024
title: "What’s new in StoreKit and In-App Purchase"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10061"
topics: ["App Services", "SwiftUI & UI Frameworks", "App Store, Distribution & Marketing"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in StoreKit and In-App Purchase

**Event:** WWDC24 · **Topic:** App Store, Distribution & Marketing · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-10 · **Session:** [wwdc2024-10061](https://developer.apple.com/videos/play/wwdc2024/10061)

Learn how to build and deliver even better purchase experiences using the App Store In-App Purchase system. We’ll demo new StoreKit views control styles and new APIs to improve your subscription customization, discuss new fields for transaction-level information, and explore new testability in Xcode. We’ll also review an important StoreKit deprecation.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,036 words)

## Documentation & Resources

- [Testing in-app purchases with StoreKit transaction manager in Xcode](https://developer.apple.com/documentation/Xcode/testing-in-app-purchases-with-storeKit-transaction-manager-in-code) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/testing-in-app-purchases-with-storeKit-transaction-manager-in-code
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/testing-in-app-purchases-with-storeKit-transaction-manager-in-code.json
- [Product.SubscriptionInfo.RenewalInfo](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo.json
- [Transaction properties](https://developer.apple.com/documentation/StoreKit/transaction-properties) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/transaction-properties
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/transaction-properties.json
- [Forum: App Store Distribution & Marketing](https://developer.apple.com/forums/topics/app-store-distribution-and-marketing?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/app-store-distribution-and-marketing?cid=vf-a-0010
- [Message](https://developer.apple.com/documentation/StoreKit/Message) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/Message
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/Message.json
- [StoreKit views](https://developer.apple.com/documentation/StoreKit/storekit-views) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/storekit-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/storekit-views.json
- [Introducing StoreKit 2](https://developer.apple.com/storekit/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/storekit/
- [Setting up StoreKit Testing in Xcode](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/setting-up-storekit-testing-in-xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/setting-up-storekit-testing-in-xcode.json
- [In-App Purchase](https://developer.apple.com/documentation/StoreKit/in-app-purchase) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/in-app-purchase
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/in-app-purchase.json
- [Original API for In-App Purchase](https://developer.apple.com/documentation/StoreKit/original-api-for-in-app-purchase) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/original-api-for-in-app-purchase
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/original-api-for-in-app-purchase.json

## Code Snippets

### Destination Video Shop — [4:26]

```swift
import StoreKit
import SwiftUI

struct DestinationVideoShop: View {

  var body: some View {
    SubscriptionStoreView(groupID: Self.subscriptionGroupID) {
      SubscriptionOptionGroupSet { product in
				StreamingPassLevel(product)
      } label: { streamingPassLevel in
       	Text(streamingPassLevel.localizedTitle)
      } marketingContent: { streamingPassLevel in
        StreamingPassMarketingContent(level: streamingPassLevel)
        StreamingPassFeatures(level: streamingPassLevel)
      }
  	}
  	.subscriptionStoreControlStyle(.compactPicker, placement: .bottomBar)
	}

}
```

### Subscription Option Groups - Tabs style — [9:06]

```swift
SubscriptionStoreView(groupID: Self.subscriptionGroupID) {
  SubscriptionOptionGroupSet { product in
		StreamingPassLevel(product)
  } label: { streamingPassLevel in
    Text(streamingPassLevel.localizedTitle)
  } marketingContent: { _ in
    StreamingPassMarketingContent()
	}
}
.subscriptionStoreControlStyle(.compactPicker, placement: .bottomBar)
.subscriptionStoreOptionGroupStyle(.tabs)
```

### Subscription Option Groups - Links style — [9:20]

```swift
SubscriptionStoreView(groupID: Self.subscriptionGroupID) {
  SubscriptionOptionGroupSet { product in
		StreamingPassLevel(product)
  } label: { streamingPassLevel in
    Text(streamingPassLevel.localizedTitle)
  } marketingContent: { _ in
    StreamingPassMarketingContent()
	}
}
.subscriptionStoreControlStyle(.compactPicker, placement: .bottomBar)
.subscriptionStoreOptionGroupStyle(.links)
```

### Custom control style implementation — [13:41]

```swift
import StoreKit
import SwiftUI

struct BadgedPickerControlStyle: SubscriptionStoreControlStyle {
  func makeBody(configuration: Configuration) -> some View {
    SubscriptionPicker(configuration) { pickerOption in
      HStack(alignment: .top) {
        VStack(alignment: .leading) {
          Text(pickerOption.displayName)
          	.font(title2.bold())
          Text(priceDisplay(for: pickerOption))
          if pickerOption.isFamilyShareable {
            FamilyShareableBadge()
          }
          Text(pickerOption.description)
        }
        Spacer()
        SelectionIndicator(pickerOption.isSelected)
      }
    } confirmation: { option in
      SubscribeButton(option)
    }
  }
}

struct DestinationVideoShop: View {

  var body: some View {
    SubscriptionStoreView(groupID: Self.subscriptionGroupID) {
      SubscriptionPeriodGroupSet { _ in
        StreamingPassMarketingContent()
      }
  	}
  	.subscriptionStoreControlStyle(BadgedPickerControlStyle())
	}

}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10061/4/283D5AFD-5540-405F-A385-1B9CBB0474D4/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10061/4/283D5AFD-5540-405F-A385-1B9CBB0474D4/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10061) — developer.apple.com. Indexed for agent consumption._