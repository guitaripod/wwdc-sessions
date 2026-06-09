---
id: "wwdc2020-10173"
event: "wwdc2020"
year: 2020
title: "Get the most out of Sign in with Apple"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10173"
topics: ["Safari & Web", "System Services", "Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Get the most out of Sign in with Apple

**Event:** WWDC20 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10173](https://developer.apple.com/videos/play/wwdc2020/10173)

Sign in with Apple makes it easy for people to sign in to your apps and websites with the Apple ID they already have. Fully integrate Sign in with Apple into your app using secure requests, and by handling state changes and server notifications. We’ll also introduce new APIs that allow you to let existing users switch to Sign in with Apple quickly and easily.

**Keywords:** `account`, `account security`, `sign in`, `sign in with apple`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,814 words)

## Documentation & Resources

- [Human Interface Guidelines: Sign in with Apple](https://developer.apple.com/design/Human-Interface-Guidelines/sign-in-with-apple) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/design/Human-Interface-Guidelines/sign-in-with-apple
- [Sign In with Apple](https://developer.apple.com/sign-in-with-apple/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/sign-in-with-apple/
- [Implementing User Authentication with Sign in with Apple](https://developer.apple.com/documentation/AuthenticationServices/implementing-user-authentication-with-sign-in-with-apple) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/implementing-user-authentication-with-sign-in-with-apple
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/implementing-user-authentication-with-sign-in-with-apple.json

## Code Snippets

### Create an Authorization Request — [2:02]

```swift
// Configure request, setup delegates and perform authorization request

    @objc func handleAuthorizationButtonPress() {
        let request = ASAuthorizationAppleIDProvider().createRequest()
        request.requestedScopes = [.fullName, .email]

        request.nonce = myNonceString()
        request.state = myStateString()

        let controller = ASAuthorizationController(authorizationRequests: [request])

        controller.delegate = self
        controller.presentationContextProvider = self

        controller.performRequests()
    }
```

### Get a credential from an Authorization — [5:37]

```swift
// ASAuthorizationControllerDelegate

func authorizationController(controller: ASAuthorizationController, didCompleteWithAuthorization authorization: ASAuthorization) {
        if let credential = authorization.credential as? ASAuthorizationAppleIDCredential {
            let userIdentifier = credential.user
            let fullName = credential.fullName
            let email = credential.email
            let realUserStatus = credential.realUserStatus

            let state = credential.state
            let identityToken = credential.identityToken
            let authorizationCode = credential.authorizationCode

            // Securely store the userIdentifier locally
            self.saveUserIdentifier(userIdentifier)

            // Create a session with your server and verify the information
            self.createSession(identityToken: identityToken, authorizationCode: authorizationCode)
    }
}
```

### Verify the state of a credential — [8:51]

```swift
// Getting a credential state

        let provider = ASAuthorizationAppleIDProvider()

        provider.getCredentialState(forUserID: getStoredUserIdentifier()) { 
                                                        (credentialState, error) in
            switch(credentialState) {
            case .authorized:
                // Sign in with Apple credential Valid
            case .revoked:
                // Sign in with Apple credential Revoked, Sign out
            case .notFound:
                // Credential was not found, fallback to login screen
            case .transferred:
                // Application was recently transferred, refresh User Identifier
            @unknown default:
                break
            }
        }
```

### Migrate a user identifier — [11:00]

```swift
// Migrating a user identifier

        let request = ASAuthorizationAppleIDProvider().createRequest()
        request.requestedScopes = [.fullName, .email]

        request.user = getStoredUserIdentifier()

        request.nonce = myNonceString()
        request.state = myStateString()

        let controller = ASAuthorizationController(authorizationRequests: [request])

        controller.delegate = self
        controller.presentationContextProvider = self

        controller.performRequests()
```

### Create a Sign in with Apple button — [13:54]

```swift
// SwiftUI example:

SignInWithAppleButton(.signIn) {
    onRequest: { (request) in
        request.requestedScopes = [.fullName, .email]
        request.nonce = myNonceString()
        request.state = myStateString()
    }
    onCompletion: { (result) in
        switch result {
        case .success(let authorization):
            // Handle Authorization
        case .failure(let error)
            // Handle Failure
        }
    }
}.signInWithAppleButtonStyle(.black)
```

### convertAccountToSignInWithAppleWithoutUserInteraction — [25:15]

```swift
enum VerificationResult : Int { case success; case failure; case twoFactorAuthRequired;

override func convertAccountToSignInWithAppleWithoutUserInteraction(
    for serviceIdentifier: ASCredentialServiceIdentifier, 
    existingCredential: ASPasswordCredential
) {
    verifyCredential(existingCredential) { (result: VerificationResult) in
        switch result {
        case .failure:
            self.extensionContext.cancelRequest(withError: 
                ASExtensionError(.failed))
        case .success:
          self.extensionContext.getSignInWithAppleAuthorizationWithState(state: myStateString(),
                                                                         nonce: myNonceString(),      
                                                                         {…}        
        case .twoFactorAuthRequired:
            self.extensionContext.cancelRequest(withError: 
                ASExtensionError(.userInteractionRequired))
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10173/3/4C9B78F1-0F45-456A-83FF-83624AE95E25/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10173) — developer.apple.com. Indexed for agent consumption._
