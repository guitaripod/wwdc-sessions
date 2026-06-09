---
id: "wwdc2020-10139"
event: "wwdc2020"
year: 2020
title: "Leverage enterprise identity and authentication"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10139"
topics: ["App Store, Distribution & Marketing", "Business & Education"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Leverage enterprise identity and authentication

**Event:** WWDC20 · **Topic:** Business & Education · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10139](https://developer.apple.com/videos/play/wwdc2020/10139)

Empower your organization with the right tools while protecting privacy and security. Discover Apple’s identity management tools for enterprise, and how they can help you create a smoother experience for users when signing in to devices, apps and websites. We’ll show you how to take advantage of Federated Authentication and Single Sign-on extensions, including changes to Apple’s built-in Kerberos extension. And explore our other platform tools for enterprise users, including macOS account types and Shared iPad for Business.

**Keywords:** `authentication`, `enterprise`, `kerberos`, `mdm`, `sso`, `vpn`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,716 words)

## Documentation & Resources

- [Kerberos Single Sign-on Extension User Guide](https://www.apple.com/business/docs/site/Kerberos_Single_Sign_on_Extension_User_Guide.pdf) _documentation_
- [Apple School Manager User Guide](https://support.apple.com/guide/apple-school-manager/) _documentation_
- [Authentication Services](https://developer.apple.com/documentation/AuthenticationServices) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices.json
- [Apple Business Manager User Guide](https://support.apple.com/guide/apple-business-manager/) _guide_
- [Apple Platform Deployment](https://support.apple.com/guide/deployment/) _documentation_

## Code Snippets

### Calling App Information — [13:34]

```swift
var localizedCallerDisplayName: String

var callerTeamIdentifier: String

var isCallerManaged: Bool
```

### Profile Removal Operation — [14:12]

```swift
// existing operations
static let operationLogin: ASAuthorization.OpenIDOperation
static let operationRefresh: ASAuthorization.OpenIDOperation
static let operationLogout: ASAuthorization.OpenIDOperation

//new this year
static let configurationRemoved: ASAuthorizationProviderAuthorizationOperation
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10139/5/EE9B8782-2114-4EDC-A2CF-C26D03BB5E54/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10139) — developer.apple.com. Indexed for agent consumption._