---
id: "wwdc2024-10125"
event: "wwdc2024"
year: 2024
title: "Streamline sign-in with passkey upgrades and credential managers"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10125"
topics: ["App Services", "System Services", "Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Streamline sign-in with passkey upgrades and credential managers

**Event:** WWDC24 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-10125](https://developer.apple.com/videos/play/wwdc2024/10125)

Learn how to automatically upgrade existing, password-based accounts to use passkeys. We’ll share why and how to improve account security and ease of sign-in, information about new features available for credential manager apps, and how to make your app information shine in the new Passwords app.

**Keywords:** `automatic passkey`, `automatic passkeys`, `passkey`, `passkeys`, `password`, `password app`, `passwords`, `verification codes`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,894 words)

## Documentation & Resources

- [ASCredentialProviderExtensionCapabilities](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/ASCredentialProviderExtensionCapabilities) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/ASCredentialProviderExtensionCapabilities
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/ASCredentialProviderExtensionCapabilities.json
- [Forum: Privacy & Security](https://developer.apple.com/forums/topics/privacy-and-security?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/privacy-and-security?cid=vf-a-0010
- [Passkeys overview](https://developer.apple.com/passkeys/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/passkeys/
- [About the security of passkeys](https://support.apple.com/en-us/HT213305) _guide_
- [Connecting to a service with passkeys](https://developer.apple.com/documentation/AuthenticationServices/connecting-to-a-service-with-passkeys) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/connecting-to-a-service-with-passkeys
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/connecting-to-a-service-with-passkeys.json
- [Supporting passkeys](https://developer.apple.com/documentation/AuthenticationServices/supporting-passkeys) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/supporting-passkeys
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/supporting-passkeys.json
- [Public-Private Key Authentication](https://developer.apple.com/documentation/AuthenticationServices/public-private-key-authentication) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/public-private-key-authentication
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/public-private-key-authentication.json
- [Authentication Services](https://developer.apple.com/documentation/AuthenticationServices) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices.json

## Code Snippets

### Offering a passkey upsell — [0:01]

```swift
// Offering a passkey upsell

func signIn() async throws {
    let userInfo = try await signInWithPassword()
    guard !userInfo.hasPasskey else { return }
    let provider = ASAuthorizationPlatformPublicKeyCredentialProvider(
        relyingPartyIdentifier: "example.com")

    guard try offerPasskeyUpsell() else { return }
    let request = provider.createCredentialRegistrationRequest(
        challenge: try await fetchChallenge(),
        name: userInfo.user,
        userID: userInfo.accountID)

    do {
        let passkey = try await authorizationController.performRequest(request)
        // Save new passkey to the backend
    } catch { … }
}
```

### Automatic passkey upgrade — [0:02]

```swift
// Automatic passkey upgrade

func signIn() async throws {
    let userInfo = try await signInWithPassword()
    guard !userInfo.hasPasskey else { return }
    let provider = ASAuthorizationPlatformPublicKeyCredentialProvider(
        relyingPartyIdentifier: "example.com")

    let request = provider.createCredentialRegistrationRequest(
        challenge: try await fetchChallenge(),
        name: userInfo.user,
        userID: userInfo.accountID,
        requestStyle: .conditional)

    do {
        let passkey = try await authorizationController.performRequest(request)
        // Save new passkey to the backend
    } catch { … }
}
```

### Modal passkey creation (web) — [0:03]

```javascript
// Modal passkey creation

const options = {
    "publicKey": {
        "rp": { … },
        "user": {
            "name": userInfo.user,
            …
        },
        "challenge": …,
        "pubKeyCredParams": [ … ]
    },
};

await navigator.credentials.create(options);
```

### Automatic passkey creation (web) — [0:04]

```javascript
// Automatic passkey creation

let capabilities = await PublicKeyCredential.getClientCapabilities();
if (!capabilities.conditionalCreate) { return; }

const options = {
    "publicKey": {
        "rp": { … },
        "user": {
            "name": userInfo.user,
            …
        },
        "challenge": …,
        "pubKeyCredParams": [ … ]
    },
    "mediation": "conditional"
};

await navigator.credentials.create(options);
```

### New Credential provider Info.plist keys — [0:05]

```xml
<dict>
	<key>NSExtensionAttributes</key>
	<dict>
		<key>ASCredentialProviderExtensionCapabilities</key>
		<dict>
			<key>ProvidesPasswords</key>
			<true/>
			<key>ProvidesPasskeys</key>
			<true/>
			<key>SupportsConditionalPasskeyRegistration</key>
			<true/>
			<key>ProvidesOneTimeCodes</key>
			<true/>
			<key>ProvidesTextToInsert</key>
			<true/>
		</dict>
	</dict>
</dict>
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10125/4/11A4C94C-65F3-4AE0-831C-EFE3BF97831C/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10125/4/11A4C94C-65F3-4AE0-831C-EFE3BF97831C/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10125) — developer.apple.com. Indexed for agent consumption._
