---
id: "wwdc2025-279"
event: "wwdc2025"
year: 2025
title: "What’s new in passkeys"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/279"
topics: ["Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS"]
hasTranscript: true
---

# What’s new in passkeys

**Event:** WWDC25 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-279](https://developer.apple.com/videos/play/wwdc2025/279)

Discover how iOS, iPadOS, macOS, and visionOS 26 enhance passkeys. We’ll explore key updates including: the new account creation API for streamlined sign-up, keeping passkeys up-to-date, new ways to drive passkey upgrades through automatic passkey upgrades and passkey management endpoints, and the secure import/export of passkeys. Learn how these improvements enhance user experience and security, and how to implement these updates in your apps to provide a smoother, more secure authentication experience. To get the most out of this video, first watch “Meet passkeys” from WWDC22.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,178 words)

## Documentation & Resources

- [Performing fast account creation with passkeys](https://developer.apple.com/documentation/AuthenticationServices/performing-fast-account-creation-with-passkeys) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/performing-fast-account-creation-with-passkeys
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/performing-fast-account-creation-with-passkeys.json
- [ASCredentialExportManager](https://developer.apple.com/documentation/AuthenticationServices/ASCredentialExportManager) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/ASCredentialExportManager
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/ASCredentialExportManager.json
- [ASCredentialProviderViewController](https://developer.apple.com/documentation/AuthenticationServices/ASCredentialProviderViewController) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/ASCredentialProviderViewController
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/ASCredentialProviderViewController.json

## Code Snippets

### Account creation — [6:33]

```swift
// Account creation

@Environment(\.authorizationController) var authorizationController

func performPasskeySignUp() async throws {
    let provider = ASAuthorizationAccountCreationProvider()
    let request = provider.createPlatformPublicKeyCredentialRegistrationRequest(
        acceptedContactIdentifiers: [.email, .phoneNumber],
        shouldRequestName: true,
        relyingPartyIdentifier: "example.com",
        challenge: try await fetchChallenge(),
        userID: try await fetchUserID()
    )

    do {
        let result = try await authorizationController.performRequest(request)
        if case .passkeyAccountCreation(let account) = result {
            // Register new account on backend
        }
    } catch
        ASAuthorizationError
        .deviceNotConfiguredForPasskeyCreation {
        showPasswordSignUpForm = true
    } catch ASAuthorizationError.canceled {
        showPasswordSignUpForm = true
    } catch
        ASAuthorizationError.preferSignInWithApple {
        await performSignInWithApple()
    } catch { ... }
}
```

### Changing the user name — [12:30]

```swift
// Changing the user name

try await ASCredentialUpdater()
    .reportPublicKeyCredentialUpdate(
        relyingPartyIdentifier: "example.com",
        userHandle: userHandle,
        newName: "andrew@example.com"
    )
```

### Changing the user name — [12:58]

```javascript
// Changing the user name

await PublicKeyCredential.signalCurrentUserDetails({
    rpId: "example.com",
    userId: userHandle,
    name: "andrew@example.com",
    displayName: "andrew@example.com"
});
```

### Revoking a passkey — [13:07]

```swift
// Revoking a passkey

try await ASCredentialUpdater()
    .reportAllAcceptedPublicKeyCredentials(
        relyingPartyIdentifier: "example.com",
        userHandle: userHandle,
        acceptedCredentialIDs: acceptedCredentialIDs
    )
```

### Revoking a passkey — [13:46]

```javascript
// Revoking a passkey

await PublicKeyCredential.signalAllAcceptedCredentials({
    rpId: "example.com",
    userId: userHandle,
    allAcceptedCredentalIds: acceptedCredentialIds
});
```

### Removing a password — [14:04]

```swift
// Removing a password

try await ASCredentialUpdater()
    .reportUnusedPasswordCredential(
        domain: "example.com",
        username: "andrew@example.com"
    )
```

### Automatic passkey upgrade — [15:36]

```swift
// Automatic passkey upgrade

func signIn() async throws {
    let accountDetails = try await signInWithPassword()
    guard !accountDetails.hasPasskey else { return }

    let provider = ASAuthorizationPlatformPublicKeyCredentialProvider(
        relyingPartyIdentifier: "example.com")

    let request = provider.createCredentialRegistrationRequest(
        challenge: try await fetchChallenge(),
        name: accountDetails.userName,
        userID: accountDetails.userID,
        requestStyle: .conditional
    )

    do {
        let passkey = try await authorizationController.performRequest(request)
        // Save new passkey to the backend
    } catch { ... }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/279/5/39c2b950-9bc8-4e0a-a336-98ec2ed224a2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/279/5/39c2b950-9bc8-4e0a-a336-98ec2ed224a2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/279) — developer.apple.com. Indexed for agent consumption._
