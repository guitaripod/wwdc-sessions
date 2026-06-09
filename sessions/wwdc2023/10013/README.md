---
id: "wwdc2023-10013"
event: "wwdc2023"
year: 2023
title: "Meet StoreKit for SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10013"
topics: ["App Store, Distribution & Marketing", "SwiftUI & UI Frameworks", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Meet StoreKit for SwiftUI

**Event:** WWDC23 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10013](https://developer.apple.com/videos/play/wwdc2023/10013)

Discover how you can use App Store product metadata and Xcode Previews to add in-app purchases to your app with just a few lines of code. Explore a new collection of UI components in StoreKit and learn how you can easily merchandise your products, present subscriptions in a way that helps users make informed decisions, and more.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,481 words)

## Documentation & Resources

- [Backyard Birds: Building an app with SwiftData and widgets](https://developer.apple.com/documentation/SwiftUI/Backyard-birds-sample) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Backyard-birds-sample
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Backyard-birds-sample.json
- [StoreKit views](https://developer.apple.com/documentation/StoreKit/storekit-views) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit/storekit-views
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit/storekit-views.json
- [Submit feedback](http://feedbackassistant.apple.com) _documentation_

## Code Snippets

### Setting up the bird food shop view — [3:35]

```swift
import SwiftUI

struct BirdFoodShop: View {

  var body: some View {
    Text("Hello, world!") 
  }

}
```

### Import StoreKit to use the new merchandising views with SwiftUI — [3:42]

```swift
import SwiftUI
import StoreKit

struct BirdFoodShop: View {

  var body: some View {
    Text("Hello, world!") 
  }

}
```

### Declaring a query to access the bird food data model — [3:51]

```swift
import SwiftUI
import StoreKit

struct BirdFoodShop: View {
  @Query var birdFood: [BirdFood]

  var body: some View {
    Text("Hello, world!") 
  }

}
```

### Meet store view — [4:18]

```swift
import SwiftUI
import StoreKit

struct BirdFoodShop: View {
  @Query var birdFood: [BirdFood]

  var body: some View {
    StoreView(ids: birdFood.productIDs) 
  }

}
```

### Adding decorative icons to the store view — [4:51]

```swift
import SwiftUI
import StoreKit

struct BirdFoodShop: View {
  @Query var birdFood: [BirdFood]

  var body: some View {
    StoreView(ids: birdFood.productIDs) { product in 
      BirdFoodProductIcon(productID: product.id)
    }
  }

}
```

### Creating a container for a custom store layout — [6:38]

```swift
import SwiftUI
import StoreKit

struct BirdFoodShop: View {
  @Query var birdFood: [BirdFood]

  var body: some View {
    ScrollView {
      VStack(spacing: 10) {
        if let (birdFood, product) = birdFood.bestValue {

        }
      }
      .scrollClipDisabled()
    }
    .contentMargins(.horizontal, 20, for: .scrollContent)
    .scrollIndicators(.hidden)
    .frame(maxWidth: .infinity)
    .background(.background.secondary)  
  }

}
```

### Meet product view — [6:47]

```swift
import SwiftUI
import StoreKit

struct BirdFoodShop: View {
  @Query var birdFood: [BirdFood]

  var body: some View {
    ScrollView {
      VStack(spacing: 10) {
        if let (birdFood, product) = birdFood.bestValue {
          ProductView(id: product.id)
        }
      }
      .scrollClipDisabled()
    }
    .contentMargins(.horizontal, 20, for: .scrollContent)
    .scrollIndicators(.hidden)
    .frame(maxWidth: .infinity)
    .background(.background.secondary)  
  }

}
```

### Adding a decorative icon to the product view — [7:03]

```swift
import SwiftUI
import StoreKit

struct BirdFoodShop: View {
  @Query var birdFood: [BirdFood]

  var body: some View {
    ScrollView {
      VStack(spacing: 10) {
        if let (birdFood, product) = birdFood.bestValue {
          ProductView(id: product.id) {
            BirdFoodProductIcon(
              birdFood: birdFood,
              quantity: product.quantity
            )
          }
        }
      }
      .scrollClipDisabled()
    }
    .contentMargins(.horizontal, 20, for: .scrollContent)
    .scrollIndicators(.hidden)
    .frame(maxWidth: .infinity)
    .background(.background.secondary)  
  }

}
```

### Adding more containers to layout product views — [7:17]

```swift
import SwiftUI
import StoreKit

struct BirdFoodShop: View {
  @Query var birdFood: [BirdFood]

  var body: some View {
    ScrollView {
      VStack(spacing: 10) {
        if let (birdFood, product) = birdFood.bestValue {
          ProductView(id: product.id) {
            BirdFoodProductIcon(
              birdFood: birdFood,
              quantity: product.quantity
            )
          }
          .padding()
          .background(.background.secondary, in: .rect(cornerRadius: 20))
        }
      }
      .scrollClipDisabled()
      Text("Other Bird Food")
        .font(.title3.weight(.medium))
        .frame(maxWidth: .infinity, alignment: .leading)
      ForEach(birdFood.premiumBirdFood) { birdFood in
        BirdFoodShopShelf(title: birdFood.name) {

        }
      }
    }
    .contentMargins(.horizontal, 20, for: .scrollContent)
    .scrollIndicators(.hidden)
    .frame(maxWidth: .infinity)
    .background(.background.secondary)  
  }

}
```

### Declaring product views for the remaining products — [7:36]

```swift
import SwiftUI
import StoreKit

struct BirdFoodShop: View {
  @Query var birdFood: [BirdFood]

  var body: some View {
    ScrollView {
      VStack(spacing: 10) {
        if let (birdFood, product) = birdFood.bestValue {
          ProductView(id: product.id) {
            BirdFoodProductIcon(
              birdFood: birdFood,
              quantity: product.quantity
            )
          }
          .padding()
          .background(.background.secondary, in: .rect(cornerRadius: 20))
        }
      }
      .scrollClipDisabled()
      Text("Other Bird Food")
        .font(.title3.weight(.medium))
        .frame(maxWidth: .infinity, alignment: .leading)
      ForEach(birdFood.premiumBirdFood) { birdFood in
        BirdFoodShopShelf(title: birdFood.name) {
          ForEach(birdFood.orderedProducts) { product in
            ProductView(id: product.id) {
              BirdFoodProductIcon(
                birdFood: birdFood,
                quantity: product.quantity
              )
            }
          }
        }
      }
    }
    .contentMargins(.horizontal, 20, for: .scrollContent)
    .scrollIndicators(.hidden)
    .frame(maxWidth: .infinity)
    .background(.background.secondary)  
  }

}
```

### Choosing a product view style — [7:50]

```swift
import SwiftUI
import StoreKit

struct BirdFoodShop: View {
  @Query var birdFood: [BirdFood]

  var body: some View {
    ScrollView {
      VStack(spacing: 10) {
        if let (birdFood, product) = birdFood.bestValue {
          ProductView(id: product.id) {
            BirdFoodProductIcon(
              birdFood: birdFood,
              quantity: product.quantity
            )
          }
          .padding()
          .background(.background.secondary, in: .rect(cornerRadius: 20))
          .padding()
          .productViewStyle(.large)
        }
      }
      .scrollClipDisabled()
      Text("Other Bird Food")
        .font(.title3.weight(.medium))
        .frame(maxWidth: .infinity, alignment: .leading)
      ForEach(birdFood.premiumBirdFood) { birdFood in
        BirdFoodShopShelf(title: birdFood.name) {
          ForEach(birdFood.orderedProducts) { product in
            ProductView(id: product.id) {
              BirdFoodProductIcon(
                birdFood: birdFood,
                quantity: product.quantity
              )
            }
          }
        }
      }
    }
    .contentMargins(.horizontal, 20, for: .scrollContent)
    .scrollIndicators(.hidden)
    .frame(maxWidth: .infinity)
    .background(.background.secondary)  
  }

}
```

### Styling the store view — [8:25]

```swift
StoreView(ids: birdFood.productIDs) { product in 
    BirdFoodShopIcon(productID: product.id)
}
.productViewStyle(.compact)
```

### Setting up the Backyard Birds pass shop — [9:53]

```swift
import SwiftUI
import StoreKit

struct BackyardBirdsPassShop: View {

    var body: some View {
        Text("Hello, world!") 
    }

}
```

### Meet subscription store view — [9:57]

```swift
import SwiftUI
import StoreKit

struct BackyardBirdsPassShop: View {
    @Environment(\.shopIDs.pass) var passGroupID

    var body: some View {
        SubscriptionStoreView(groupID: passGroupID)
    }

}
```

### Customizing the subscription store view's marketing content — [10:38]

```swift
import SwiftUI
import StoreKit

struct BackyardBirdsPassShop: View {
    @Environment(\.shopIDs.pass) var passGroupID

    var body: some View {
        SubscriptionStoreView(groupID: passGroupID) {
            PassMarketingContent() 
        }
    }

}
```

### Declaring a full height container background — [10:57]

```swift
import SwiftUI
import StoreKit

struct BackyardBirdsPassShop: View {
    @Environment(\.shopIDs.pass) var passGroupID

    var body: some View {
        SubscriptionStoreView(groupID: passGroupID) {
            PassMarketingContent()
                .lightMarketingContentStyle()
                .containerBackground(for: .subscriptionStoreFullHeight) {
                    SkyBackground()
                }
        }
    }

}
```

### Configuring the control background style — [11:21]

```swift
import SwiftUI
import StoreKit

struct BackyardBirdsPassShop: View {
    @Environment(\.shopIDs.pass) var passGroupID

    var body: some View {
        SubscriptionStoreView(groupID: passGroupID) {
            PassMarketingContent()
                .lightMarketingContentStyle()
                .containerBackground(for: .subscriptionStoreFullHeight) {
                    SkyBackground()
                }
        }
        .backgroundStyle(.clear)
    }

}
```

### Choosing a subscribe button label layout — [11:44]

```swift
import SwiftUI
import StoreKit

struct BackyardBirdsPassShop: View {
    @Environment(\.shopIDs.pass) var passGroupID

    var body: some View {
        SubscriptionStoreView(groupID: passGroupID) {
            PassMarketingContent()
                .lightMarketingContentStyle()
                .containerBackground(for: .subscriptionStoreFullHeight) {
                    SkyBackground()
                }
        }
        .backgroundStyle(.clear)
        .subscriptionStoreButtonLabel(.multiline)
    }

}
```

### Choosing a subscription store picker item background — [12:01]

```swift
import SwiftUI
import StoreKit

struct BackyardBirdsPassShop: View {
    @Environment(\.shopIDs.pass) var passGroupID

    var body: some View {
        SubscriptionStoreView(groupID: passGroupID) {
            PassMarketingContent()
                .lightMarketingContentStyle()
                .containerBackground(for: .subscriptionStoreFullHeight) {
                    SkyBackground()
                }
        }
        .backgroundStyle(.clear)
        .subscriptionStoreButtonLabel(.multiline)
        .subscriptionStorePicketItemBackground(.thinMaterial)
    }

}
```

### Declaring a redeem code button — [12:20]

```swift
import SwiftUI
import StoreKit

struct BackyardBirdsPassShop: View {
    @Environment(\.shopIDs.pass) var passGroupID

    var body: some View {
        SubscriptionStoreView(groupID: passGroupID) {
            PassMarketingContent()
                .lightMarketingContentStyle()
                .containerBackground(for: .subscriptionStoreFullHeight) {
                    SkyBackground()
                }
        }
        .backgroundStyle(.clear)
        .subscriptionStoreButtonLabel(.multiline)
        .subscriptionStorePicketItemBackground(.thinMaterial)
        .storeButton(.visible, for: .redeemCode)
    }

}
```

### Reacting to completed purchases from descendant views — [14:10]

```swift
BirdFoodShop()
.onInAppPurchaseCompletion { (product: Product, result: Result<Product.PurchaseResult, Error>) in
    if case .success(.success(let transaction)) = result {
        await BirdBrain.shared.process(transaction: transaction)
        dismiss()
    }
}
```

### Reacting to in-app purchases starting — [15:43]

```swift
BirdFoodShop()
.onInAppPurchaseStart { (product: Product) in
    self.isPurchasing = true
}
```

### Declaring a subscription status dependency — [16:57]

```swift
subscriptionStatusTask(for: passGroupID) { taskState in
    if let statuses = taskState.value {
        passStatus = await BirdBrain.shared.status(for: statuses)
    }            
}
```

### Unlocking non-consumables — [19:37]

```swift
currentEntitlementTask(for: "com.example.id") { state in
    self.isPurchased = BirdBrain.shared.isPurchased(
        for: state.transaction
    )
}
```

### Declaring placeholder icons — [20:52]

```swift
ProductView(id: ids.nutritionPelletBox) {
    BoxOfNutritionPelletsIcon()
} placeholderIcon: {
    Circle()
}
```

### Using the promotional icon — [21:25]

```swift
ProductView(
    id: ids.nutritionPelletBox,
    prefersPromotionalIcon: true
) {
    BoxOfNutritionPelletsIcon()
}
```

### Using the promotional icon border — [21:56]

```swift
ProductView(id: ids.nutritionPelletBox) {
    BoxOfNutritionPelletsIcon()
        .productIconBorder()
}
```

### Composing standard styles to create custom styles — [23:02]

```swift
struct SpinnerWhenLoadingStyle: ProductViewStyle {

    func makeBody(configuration: Configuration) -> some View {
        switch configuration.state {
        case .loading:
            ProgressView()
                .progressViewStyle(.circular)
        default:
            ProductView(configuration)
        }
    }

}
```

### Applying custom styles to the product view — [23:44]

```swift
ProductView(id: ids.nutritionPelletBox) {
    BoxOfNutritionPelletsIcon()
}
.productViewStyle(SpinnerWhenLoadingStyle())
```

### Declaring custom styles — [23:58]

```swift
struct BackyardBirdsStyle: ProductViewStyle {

  func makeBody(configuration: Configuration) -> some View {
    switch configuration.state {
      case .loading: // Handle loading state here
      case .failure(let error): // Handle failure state here
      case .unavailable: // Handle unavailabiltity here
      case .success(let product):
        HStack(spacing: 12) {
          configuration.icon
          VStack(alignment: .leading, spacing: 10) {
            Text(product.displayName)
            Button(product.displayPrice) {
              configuration.purchase()
            }
            .bold()
          }
        }
        .backyardBirdsProductBackground()
    }
  }

}
```

### Declaring a dependency on products — [26:44]

```swift
@State var productsState: Product.CollectionTaskState = .loading

var body: some View {
    ZStack {
        switch productsState {
        case .loading:
            BirdFoodShopLoadingView()
        case .failed(let error):
            ContentUnavailableView(/* ... */)
        case .success(let products, let unavailableIDs):
            if products.isEmpty {
                ContentUnavailableView(/* ... */)
            }
            else {
                BirdFoodShop(products: products)
            }
        }
    }
    .storeProductsTask(for: productIDs) { state in
        self.productsState = state
    }
}
```

### Configuring the visibility of auxiliary buttons — [27:54]

```swift
SubscriptionStoreView(groupID: passGroupID) {
   // ...
}
.storeButton(.visible, for: .redeemCode)
```

### Adding a sign in action — [29:56]

```swift
@State var presentingSignInSheet = false

var body: some View {
    SubscriptionStoreView(groupID: passGroupID) {
        PassMarketingContent()
            .containerBackground(for: .subscriptionStoreFullHeight) {
                SkyBackground()
            }
    }
    .subscriptionStoreSignInAction {
        presentingSignInSheet = true
    }
    .sheet(isPresented: $presentingSignInSheet) {
        SignInToBirdAccountView()
    }
}
```

### Displaying policies from the App Store metadata — [30:32]

```swift
SubscriptionStoreView(groupID: passGroupID) {
    PassMarketingContent()
        .containerBackground(for: .subscriptionStoreFullHeight) {
            SkyBackground()
        }
}
.subscriptionStorePolicyForegroundStyle(.white)
.storeButton(.visible, for: .policies)
```

### Choosing a control style — [31:22]

```swift
SubscriptionStoreView(groupID: passGroupID) {
    PassMarketingContent()
        .containerBackground(for: .subscriptionStoreFullHeight) {
            SkyBackground()
        }
}
.subscriptionStoreControlStyle(.buttons)
```

### Declaring the layout of the subscribe button label — [32:28]

```swift
SubscriptionStoreView(groupID: passGroupID) {
    PassMarketingContent()
        .containerBackground(for: .subscriptionStoreFullHeight) {
            SkyBackground()
        }
}
.subscriptionStoreButtonLabel(.multiline)
```

### Declaring the content of the subscribe button label — [32:51]

```swift
SubscriptionStoreView(groupID: passGroupID) {
    PassMarketingContent()
        .containerBackground(for: .subscriptionStoreFullHeight) {
            SkyBackground()
        }
}
.subscriptionStoreButtonLabel(.displayName)
```

### Declaring the layout and content of the subscribe button label — [33:04]

```swift
SubscriptionStoreView(groupID: passGroupID) {
    PassMarketingContent()
        .containerBackground(for: .subscriptionStoreFullHeight) {
            SkyBackground()
        }
}
.subscriptionStoreButtonLabel(.multiline.displayName)
```

### Decorating subscription plans — [33:44]

```swift
SubscriptionStoreView(groupID: passGroupID) {
    PassMarketingContent()
        .containerBackground(for: .subscriptionStoreFullHeight) {
            SkyBackground()
        }
}
.subscriptionStoreControlIcon { subscription, info in
    Group {
        let status = PassStatus(
            levelOfService: info.groupLevel
        )
        switch status {
        case .premium:
            Image(systemName: "bird")
        case .family:
            Image(systemName: "person.3.sequence")
        default:
            Image(systemName: "wallet.pass")
        }
    }
    .foregroundStyle(.tint)
    .symbolVariant(.fill)
}
```

### Decorating subscription plans with the button control style — [34:07]

```swift
SubscriptionStoreView(groupID: passGroupID) {
    PassMarketingContent()
        .containerBackground(for: .subscriptionStoreFullHeight) {
            SkyBackground()
        }
}
.subscriptionStoreControlIcon { subscription, info in
    Group {
        let status = PassStatus(
            levelOfService: info.groupLevel
        )
        switch status {
        case .premium:
            Image(systemName: "bird")
        case .family:
            Image(systemName: "person.3.sequence")
        default:
            Image(systemName: "wallet.pass")
        }
    }
   .symbolVariant(.fill)
}
.foregroundStyle(.white)
.subscriptionStoreControlStyle(.buttons)
```

### Adding a container background — [34:14]

```swift
SubscriptionStoreView(groupID: passGroupID) {
    PassMarketingContent()
        .containerBackground(
            .accent.gradient,
            for: .subscriptionStore
        )
}
```

### Presenting upgrade offers — [35:30]

```swift
SubscriptionStoreView(
    groupID: passGroupID,
    visibleRelationships: .upgrade
) {
    PremiumMarketingContent()
        .containerBackground(for: .subscriptionStoreFullHeight) {
            SkyBackground()
        }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10013/4/451654C1-7E00-42AE-A765-A2ECE947464C/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10013/4/451654C1-7E00-42AE-A765-A2ECE947464C/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10013) — developer.apple.com. Indexed for agent consumption._