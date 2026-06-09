---
id: "wwdc2022-10097"
event: "wwdc2022"
year: 2022
title: "What's new in App Clips"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10097"
topics: ["App Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# What's new in App Clips

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** iOS, iPadOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10097](https://developer.apple.com/videos/play/wwdc2022/10097)

Explore the latest updates to App Clips! Discover how we’ve made your App Clip even easier to build with improvements to the size limit as well as CloudKit and keychain usage. We’ll also show you how to use our validation tool to verify your App Clip and automate workflows for your advanced App Clip experiences using App Store Connect.

**Keywords:** `15 mb`, `advanced app clip`, `api`, `app clip code`, `app clip experience`, `app clip testing`, `app group container`, `app store connect`, `associated domain`, `attributes`, `banner`, `cloudkit`, `developer settings`, `diagnostics`, `included`, `keychain`, `keychain migration`, `local keychain`, `migration`, `physical code`, `public database`, `qr code`, `relationships`, `resource id`, `size limit`, `smart banner`, `transferred from app clip to app`, `universal link`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,376 words)

## Documentation & Resources

- [App Clips](https://developer.apple.com/documentation/AppClip) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AppClip
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AppClip.json

## Code Snippets

### Read your CloudKit public database from your App Clip — [4:41]

```swift
// Read your CloudKit public database from your App Clip

let container = CKContainer.default()
let publicDatabase = container.publicCloudDatabase
let record = try await publicDatabase.record(for:
    CKRecord.ID(recordName: "A928D582-9BB6-E9C5-7881-E4EAF615E0CD"))

if let title = record["Title"] as? String,
    let description = record["Description"] as? String {
        print(“Fetched a food item from CloudKit: \(title) \(description)")
}
```

### Read and Write from your App Clip's keychain — [6:03]

```swift
// Write authentication token to App Clip keychain

let addSecretsQuery: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecValueData as String: "smoothie-secret".data(using: .utf8),
    kSecAttrLabel as String: "foodsample-appclip"
]
SecItemAdd(addSecretsQuery as CFDictionary, nil)

// Read authentication token from app or App Clip

var readSecretsQuery: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecReturnAttributes as String: true,
    kSecAttrLabel as String: "foodsample-appclip",
    kSecReturnData as String: true
]
var secretsCopy: AnyObject?
SecItemCopyMatching(readSecretsQuery as CFDictionary, &secretsCopy)
```

### Get your App Clip resource ID — [7:10]

```json
# Get the App Clip resource ID

GET /v1/apps/1234567890/appClips?filter[bundleId]=com.example.foodsample.Clip

# Response

{
    "data": {
        "attributes": {
            "bundleId": "com.example.foodsample.Clip"
        },
        "id": "726ad1bb-3e1b-40eb-a986-d8a9897e4f1e"
    }
}
```

### Upload a header image for the advanced App Clip experience — [7:25]

```json
# Upload a header image for the advanced App Clip experience

POST /v1/appClipAdvancedExperienceImages
{
    "data": {
        "type": "appClipAdvancedExperienceImages",
        "attributes": {
            "fileName": "Hero_image_US.png",
            "fileSize": 43500
        }
    }
}

# Response

{
    "data": {
        "attributes": "..."
        "id": "91c52741-832b-48a2-8935-1797655edbe7"
    }
}
```

### Create the advanced App Clip experience — [7:34]

```json
# Create advanced App Clip experience

POST /v1/appClipAdvancedExperiences
{
    "data": {
        "type": "appClipAdvancedExperiences",
        "attributes": {
            "action": “OPEN",
            "businessCategory": "FOOD_AND_DRINK",
            "defaultLanguage": "EN",
            "isPoweredBy": true,
            "link": "https://fruta.example.com/restauraunt/simply_salad",
            "place": {
                "names": [ "Caffe Macs" ],
                "mapAction": "RESTAURANT_ORDER_FOOD",
                "displayPoint": {
                    "coordinates": { "latitude": 37.33611, "longitude": -122.00731 },
                    "source": "CALCULATED"
                }
            }
        },
        "relationships": {
            "appClip": {
                "data": {
                    "type": "appClip",
                    "id": "726ad1bb-3e1b-40eb-a986-d8a9897e4f1e"
                }
            },
            "headerImage": {
                "data": {
                    "type": "appClipAdvancedExperienceImages",
                    "id": "91c52741-832b-48a2-8935-1797655edbe7"
                }
            }
        },
        "included": {
            "type": "appClipAdvancedExperienceLocalizations",
            "attributes": {
                "language": "EN",
                "subtitle": "Fresh salad every day",
                "title": "Simply Salad"
            }
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10097/4/1195D4FF-4AF5-48B0-BB92-948D01AF942B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10097/4/1195D4FF-4AF5-48B0-BB92-948D01AF942B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10097) — developer.apple.com. Indexed for agent consumption._
