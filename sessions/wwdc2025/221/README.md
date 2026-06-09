---
id: "wwdc2025-221"
event: "wwdc2025"
year: 2025
title: "What’s new in AdAttributionKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/221"
topics: ["App Store, Distribution & Marketing", "App Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# What’s new in AdAttributionKit

**Event:** WWDC25 · **Topic:** App Services · **Platforms:** iOS, iPadOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-221](https://developer.apple.com/videos/play/wwdc2025/221)

Learn about new features in AdAttributionKit, including how to measure overlapping reengagement conversions and customize ad attribution rules for your app. Gain insight on a new postback property you can use to measure the success of ad campaigns across countries and regions. We’ll also demonstrate new functionality and best practices for testing your AdAttributionKit implementation. To get the most out of this session, we recommend first watching “Meet AdAttributionKit.”

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,616 words)

## Documentation & Resources

- [Configuring attribution rules for your app](https://developer.apple.com/documentation/AdAttributionKit/configuring-attribution-rules-for-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AdAttributionKit/configuring-attribution-rules-for-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AdAttributionKit/configuring-attribution-rules-for-your-app.json
- [Identifying conversion values with conversion tags](https://developer.apple.com/documentation/AdAttributionKit/conversion-tags) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AdAttributionKit/conversion-tags
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AdAttributionKit/conversion-tags.json
- [Creating postbacks in developer settings](https://developer.apple.com/documentation/AdAttributionKit/creating-postbacks-in-developer-settings) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AdAttributionKit/creating-postbacks-in-developer-settings
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AdAttributionKit/creating-postbacks-in-developer-settings.json
- [Supplying an install verification token](https://developer.apple.com/documentation/marketplacekit/supplying-an-install-verification-token) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/marketplacekit/supplying-an-install-verification-token
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/marketplacekit/supplying-an-install-verification-token.json
- [Verifying a postback](https://developer.apple.com/documentation/AdAttributionKit/verifying-a-postback) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AdAttributionKit/verifying-a-postback
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AdAttributionKit/verifying-a-postback.json
- [Enabling Developer Mode on a device](https://developer.apple.com/documentation/Xcode/enabling-developer-mode-on-a-device) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/enabling-developer-mode-on-a-device
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/enabling-developer-mode-on-a-device.json
- [AdAttributionKit](https://developer.apple.com/documentation/AdAttributionKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AdAttributionKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AdAttributionKit.json

## Code Snippets

### Function that retrieves a conversion tag from a URL — [5:42]

```swift
func retrieveConversionTag(fromURL url: URL) -> String? {
    guard let components = URLComponents(url: url, resolvingAgainstBaseURL: true) else {
        print("Could not get components for URL.")
        return nil
    }

    guard let queryItems = components.queryItems else {
        print("URL does not contain query items.")
        return nil
    }

    for item in queryItems {
        guard item.name == Postback.reengagementOpenURLParameter else {
            continue
        }
        return item.value
    }
    return nil
}
```

### Function that updates conversion value using a conversion tag — [6:55]

```swift
func updateConversionValue(_ conversionValue: Int, conversionTag: String) async {
    do {
        let update = PostbackUpdate(fineConversionValue: conversionValue,
                                    lockPostback: false,
                                    conversionTag: conversionTag)
        try await Postback.updateConversionValue(update)
    }
    catch {
        print("An error occurred while updating the conversion value: \(error)")
    }
}
```

### Example Info.plist for configuring attribution window — [9:32]

```json
{
 "AdAttributionKitConfigurations": {
   "AttributionWindows": {
     "com.example.adNetwork": {
       "install": {
         "click": 2,
         "view": 1
       }
     }
   }
}
```

### Example Info.plist for configuring attribution window — [9:58]

```json
{
 "AdAttributionKitConfigurations": {
   "AttributionWindows": {
     "com.example.adNetwork": {
       "install": {
         "click": 2,
         "view": 1
       }
     }
   }
}
```

### Example Info.plist for configuring attribution window — [10:14]

```json
{
 "AdAttributionKitConfigurations": {
   "AttributionWindows": {
     "com.example.adNetwork": {
       "install": {
         "click": 2,
         "ignoreInteractionType": "view"                     
       }
     }
   }
}
```

### Example Info.plist for configuring attribution window — [10:30]

```json
{
 "AdAttributionKitConfigurations": {
   "AttributionWindows": {
     "global": {
       "install": {
         "view": 3
       }
     }
     "com.example.adNetwork": {
       "install": {
         "click": 5,
         "ignoreInteractionType": "view"
       }
     }
   }
}
```

### Example Info.plist for configuring attribution window — [11:05]

```json
{
 "AdAttributionKitConfigurations": {
   "AttributionWindows": {
     "global": {
       "install": {
         "view": 3
       }
     }
     "com.example.adNetwork": {
       "install": {
         "click": 5,
         "ignoreInteractionType": "view"
       }
     }
   }
}
```

### Example Info.plist for configuring attribution cooldown — [13:52]

```json
{
  "AdAttributionKitConfigurations": {
    "AttributionCooldown": {
      "install-cooldown-hours": 6，
      "reengagement-cooldown-hours": 1
    {
  }
}
```

### Example install verification token payload — [16:02]

```json
{ 
  "iss": 13421973,
  "iat": 1745255692,
  "iid": "34890933",
  "vid": "46392455",
  "aud": "AppleDownloadVerification-v1",
  "bid": "com.example.marketplace",
  "dtype": "download",
  "nonce": "9BC2C5CC-A1F8-4F93-9D6A-4D524685B67E"
}
```

### Example install verification token payload — [16:26]

```json
{   
  "iss": 13421973,
  "iat": 1745255692,
  "iid": "34890933",
  "vid": "46392455",
  "aud": "AppleDownloadVerification-v1",
  "bid": "com.example.marketplace",
  "dtype": "download",
  "nonce": "9BC2C5CC-A1F8-4F93-9D6A-4D524685B67E",
  "ccode": "MT"
}
```

### Example postback with country code — [17:05]

```json
{
   "ad-interaction-type": "click",
   "jws-string": "eyJraWQiOiJhcHBsZS1jYXMtaWRlbnRpZmllci8wIiwiYWxnIjoiRVMyNTYifQ.eyJhZHZlcnRpc2VkLWl0ZW0taWRlbnRpZmllciI6Njg0OTM5LCJjb252ZXJzaW9uLXR5cGUiOiJyZS1lbmdhZ2VtZW50IiwibWFya2V0cGxhY2UtaWRlbnRpZmllciI6ImNvbS5hcHBsZS5BcHBTdG9yZSIsImFkLW5ldHdvcmstaWRlbnRpZmllciI6InRlc3QuYWRhdHRyaWJ1dGlvbmtpdCIsImltcHJlc3Npb24tdHlwZSI6ImFwcC1pbXByZXNzaW9uIiwicG9zdGJhY2stc2VxdWVuY2UtaW5kZXgiOjAsInNvdXJjZS1pZGVudGlmaWVyIjoiODM0NCIsImRpZC13aW4iOnRydWUsInBvc3RiYWNrLWlkZW50aWZpZXIiOiIzZjUwZmU1Ny0yOWFlLTQ4NjEtOGMwYi1hYzZhZGRkZmY3MmMiLCJwdWJsaXNoZXItaXRlbS1pZGVudGlmaWVyIjo1ODM4NDkyfQ.AemK1x2ahIPKOnFEEscG4wvipRtR1G6DzpNF4M4joPb8POIH4FJjm4VvcNgLXc9rWBrEDQPvDblduoc7MFcK5w",
   "coarse-conversion-value": "medium",
   "country-code": "MT"
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/221/4/09c47047-90c9-48df-9ed1-f6d24303043e/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/221/4/09c47047-90c9-48df-9ed1-f6d24303043e/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/221) — developer.apple.com. Indexed for agent consumption._