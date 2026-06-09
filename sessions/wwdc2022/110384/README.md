---
id: "wwdc2022-110384"
event: "wwdc2022"
year: 2022
title: "Support multiple users in tvOS apps"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110384"
topics: ["Audio & Video", "Health & Fitness", "App Services"]
platforms: ["tvOS"]
hasTranscript: true
---

# Support multiple users in tvOS apps

**Event:** WWDC22 · **Topic:** App Services · **Platforms:** tvOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-110384](https://developer.apple.com/videos/play/wwdc2022/110384)

Discover how you can create personalized, individual experiences in your tvOS app. We’ll show you how you can offer a single checkbox to store profile data, game save states, and more, providing each person with the same level of data separation they'd have on a personal device like iPhone. We’ll also explore how the new user-independent keychain can help you maintain your existing sign on experience for multiple people in the same household.

**Keywords:** `appletv`, `apple tv`, `apple tv 4k`, `content`, `content first`, `keychain`, `login`, `log in`, `multiuser`, `multi user`, `password`, `persona`, `personalizable`, `personalization`, `personalize`, `profile`, `profiles`, `runs as current user`, `signin`, `sign in`, `tv`, `tv app`, `tv apps`, `tv dev`, `tv developer`, `tvos`, `user`, `user independent`, `user management`, `users`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,033 words)

## Documentation & Resources

- [Mapping Apple TV users to app profiles](https://developer.apple.com/documentation/TVServices/mapping-apple-tv-users-to-app-profiles) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/TVServices/mapping-apple-tv-users-to-app-profiles
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/TVServices/mapping-apple-tv-users-to-app-profiles.json

## Code Snippets

### Save item in user independent keychain — [5:25]

```swift
func save(username: String, password: String) {
    guard let passwordData = password.data(using: .utf8) else {
        return
    }

    let attributes: [CFString: AnyObject] = [
        kSecAttrService: "MyApp" as AnyObject,
        kSecClass: kSecClassGenericPassword,
        kSecAttrAccount: username,
        kSecValueData: passwordData,
        kSecUseUserIndependentKeychain: kCFBooleanTrue
    ]

    let status = SecItemAdd(attributes as CFDictionary, nil)
    if status == errSecSuccess else {
        self.credentials = (username, password)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110384/6/1F377839-E110-4222-BBC2-B0424F6E635C/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110384/6/1F377839-E110-4222-BBC2-B0424F6E635C/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110384) — developer.apple.com. Indexed for agent consumption._