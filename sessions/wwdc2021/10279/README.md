---
id: "wwdc2021-10279"
event: "wwdc2021"
year: 2021
title: "Simplify sign in for your tvOS apps"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10279"
topics: ["Privacy & Security"]
platforms: ["tvOS"]
hasTranscript: true
---

# Simplify sign in for your tvOS apps

**Event:** WWDC21 · **Topic:** Privacy & Security · **Platforms:** tvOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10279](https://developer.apple.com/videos/play/wwdc2021/10279)

Find out how people can use Face ID or Touch ID on their iOS or iPadOS device to authorize purchases and sign into your tvOS app. Discover how you can simplify sign in for people using your app and help them get to the content they want to enjoy, faster. We’ll show you how to set up a simplified sign in process and share some best practices about creating great sign in experiences for Apple TV.

To get the most out of this session, we recommend a basic understanding of associated domains and the Authentication Services framework.

**Keywords:** `auth`, `authentication`, `keychain`, `password`, `sign-in`, `sign in with apple`, `sign-on`, `sign-up`, `username`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,168 words)

## Documentation & Resources

- [Simplifying User Authentication in a tvOS App](https://developer.apple.com/documentation/AuthenticationServices/simplifying-user-authentication-in-a-tvos-app) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/simplifying-user-authentication-in-a-tvos-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/simplifying-user-authentication-in-a-tvos-app.json

## Code Snippets

### Request a credential — [3:28]

```swift
let controller = ASAuthorizationController(authorizationRequests: [
    ASAuthorizationPasswordProvider().createRequest()
])

controller.delegate = self
controller.performRequests()
```

### Finish signing in — [4:19]

```swift
func authorizationController(controller: ASAuthorizationController,
    didCompleteWithAuthorization authorization: ASAuthorization) {
    if let credential = authorization.credential as? ASPasswordCredential {
        // Use the credential to sign in
    }
}
```

### Handle errors — [4:43]

```swift
func authorizationController(controller: ASAuthorizationController,
    didCompleteWithError error: Error) {
    if case ASAuthorizationError.canceled = error  { return }
    // Let the user know something went wrong
}
```

### Specify custom authorization methods — [6:00]

```swift
controller.customAuthorizationMethods = [
    // Sign in Manually
    .other,
    // Restore Purchase
    .restorePurchase
]
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10279/6/2634C5FD-06F9-4C34-8D8A-215A0C29356B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10279/6/2634C5FD-06F9-4C34-8D8A-215A0C29356B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10279) — developer.apple.com. Indexed for agent consumption._