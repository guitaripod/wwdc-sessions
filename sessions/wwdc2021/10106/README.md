---
id: "wwdc2021-10106"
event: "wwdc2021"
year: 2021
title: "Move beyond passwords"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10106"
topics: ["Safari & Web", "Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Move beyond passwords

**Event:** WWDC21 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10106](https://developer.apple.com/videos/play/wwdc2021/10106)

Despite their prevalence, passwords inherently come with challenges that make them poorly suited to securing someone’s online accounts. Learn more about the challenges passwords pose to modern security and how to move beyond them. Explore the next frontier in account security with secure-by-design, public-key-based credentials that use the Web Authentication standard. Discover in this technology preview how Apple is approaching this standard in iOS 15 and macOS Monterey.

**Keywords:** `authenticationservices`, `icloud keychain`, `keychain`, `login`, `log in`, `logon`, `log on`, `passkey`, `passkeys`, `password`, `passwordless`, `passwords`, `phishing`, `privacy`, `safari`, `security`, `webauthn`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,666 words)

## Documentation & Resources

- [Connecting to a service with passkeys](https://developer.apple.com/documentation/AuthenticationServices/connecting-to-a-service-with-passkeys) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/connecting-to-a-service-with-passkeys
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/connecting-to-a-service-with-passkeys.json
- [Supporting Security Key Authentication Using Physical Keys](https://developer.apple.com/documentation/AuthenticationServices/supporting-security-key-authentication-using-physical-keys) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/supporting-security-key-authentication-using-physical-keys
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/supporting-security-key-authentication-using-physical-keys.json
- [Supporting passkeys](https://developer.apple.com/documentation/AuthenticationServices/supporting-passkeys) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/supporting-passkeys
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/supporting-passkeys.json
- [2020 Data Breach Investigations Report](https://enterprise.verizon.com/resources/reports/dbir/) _documentation_

## Code Snippets

### Register an account — [17:32]

```swift
// Register an account

func createAccount(with challenge: Data, name: String, userID: Data) {
    let provider = ASAuthorizationPlatformPublicKeyCredentialProvider(
            relyingPartyIdentifier: "example.com")

    let registrationRequest = provider.createCredentialRegistrationRequest(
            challenge: challenge, name: name, userID: userID)

    let controller = ASAuthorizationController(
            authorizationRequests: [ registrationRequest ])

    controller.delegate = …
    controller.presentationContextProvider = …

    controller.performRequests()
}
```

### Sign in — [17:39]

```swift
// Sign in

func signIn(with challenge: Data) {
    let provider = ASAuthorizationPlatformPublicKeyCredentialProvider(
            relyingPartyIdentifier: "example.com")

    let assertionRequest = provider.createCredentialAssertionRequest(challenge: challenge)


    let controller = ASAuthorizationController(
            authorizationRequests: [ assertionRequest ])

    controller.delegate = …
    controller.presentationContextProvider = …

    controller.performRequests()
}
```

### Handle returned credentials — [17:41]

```swift
// Handle returned credentials
func authorizationController(controller: ASAuthorizationController, 
     didCompleteWithAuthorization authorization: ASAuthorization) {
    switch authorization.credential {
        case let registration as ASAuthorizationPlatformPublicKeyCredentialRegistration:
            let attestationObject = registration.rawAttestationObject
            let clientDataJSON = registration.rawClientDataJSON
            // Verify on your server and finish creating the account.

        case let assertion as ASAuthorizationPlatformPublicKeyCredentialAssertion:
            let signature = assertion.signature
            let clientDataJSON = assertion.rawClientDataJSON
            // Verify on your server and finish signing in.

        case …:
            …
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10106/5/CAC0BED2-732C-431A-9764-DA6A1206FE0E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10106/5/CAC0BED2-732C-431A-9764-DA6A1206FE0E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10106) — developer.apple.com. Indexed for agent consumption._