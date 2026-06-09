---
id: "wwdc2022-10092"
event: "wwdc2022"
year: 2022
title: "Meet passkeys"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10092"
topics: ["Safari & Web", "System Services", "Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Meet passkeys

**Event:** WWDC22 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10092](https://developer.apple.com/videos/play/wwdc2022/10092)

It’s time for a security upgrade: Learn how to add support for passkeys to create a quick and easy sign in experience for people, all while offering a radical increase to account security. Passkeys are simple and strong credentials built to eliminate phishing attacks. We’ll share how passkeys are designed with security in mind, show you how people will use them, go over how to integrate passkeys in your log in flow, and explore the platform and web APIs you need to adopt this feature.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,482 words)

## Documentation & Resources

- [About the security of passkeys](https://support.apple.com/en-us/HT213305) _guide_
- [Connecting to a service with passkeys](https://developer.apple.com/documentation/AuthenticationServices/connecting-to-a-service-with-passkeys) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/connecting-to-a-service-with-passkeys
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/connecting-to-a-service-with-passkeys.json
- [Supporting passkeys](https://developer.apple.com/documentation/AuthenticationServices/supporting-passkeys) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/supporting-passkeys
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/supporting-passkeys.json

## Code Snippets

### Associated Domains setup — [11:30]

```json
{
    "webcredentials": {
        "apps": [ "A1B2C3D4E5.com.example.Shiny" ]
    }
}
```

### Annotating user name text field — [11:47]

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    //Additional setup…

    userNameField.textContentType = .username
}
```

### AutoFill-assisted passkey sign in — [11:59]

```swift
// AutoFill-assisted passkey request

func signIn() {
    let challenge: Data = … // Fetched from server
    let provider =
        ASAuthorizationPlatformPublicKeyCredentialProvider(
            relyingPartyIdentifier: "example.com")
    let request =
        provider.createCredentialAssertionRequest(
            challenge: challenge)

    let controller =
        ASAuthorizationController(
            authorizationRequests: [request])
    controller.delegate = self
    controller.presentationContextProvider = self

    // Start the request
    controller.performAutoFillAssistedRequests()
}
```

### ASAuthorizationControllerDelegate callback — [13:29]

```swift
// Completing a passkey sign in

func authorizationController(controller: ASAuthorizationController,
     didCompleteWithAuthorization authorization: ASAuthorization) {

    guard let passkeyAssertion = authorization.credential as?
        ASAuthorizationPlatformPublicKeyCredentialAssertion
    else { … }

    let signature = passkeyAssertion.signature
    let clientDataJSON = passkeyAssertion.rawClientDataJSON

    // Pass these values to your server, and complete the sign in
…
}
```

### Modal passkey sign in — [16:05]

```swift
// Modal passkey request

func signIn() {
    let challenge: Data = … // Fetched from server
    let provider =      
        ASAuthorizationPlatformPublicKeyCredentialProvider(
            relyingPartyIdentifier: "example.com")
    let request = 
        provider.createCredentialAssertionRequest(
            challenge: challenge)

    let controller = 
        ASAuthorizationController(
            authorizationRequests: [request])
    controller.delegate = self
    controller.presentationContextProvider = self

    // Start the request
    controller.performRequests()
}
```

### HTML user name field annotation — [16:53]

```javascript
<input type="text" id="username-field" autocomplete="username webauthn" >
```

### AutoFill-assisted passkey sign in on the web — [17:09]

```javascript
// AutoFill-assisted WebAuthn request (JavaScript)

function signIn() {
    if (!PublicKeyCredential.isConditionalMediationAvailable ||
        !PublicKeyCredential.isConditionalMediationAvailable()) {
        // Browser doesn't support AutoFill-assisted requests.
        return;
    }

    const options = {
        "publicKey": {
            challenge: … // Fetched from server
        },
        mediation: "conditional"
    };

    navigator.credentials.get(options)
        .then(assertion => { 
            // Pass the assertion to your server.
        });
}
```

### Modal passkey sign in on the web — [18:14]

```javascript
// Modal WebAuthn request (JavaScript)

function signIn() {
    var options = {
        "publicKey": {
            challenge: … // Fetched from server
        }
    };

    navigator.credentials.get(options)
        .then(function (assertion) { 
            // Pass the assertion to your server.
    });
}
```

### Modal passkey request with allow list — [20:55]

```swift
// Modal request with allow list

func signIn(userName: String) {
    let challenge: Data = … // Fetched from server
    let provider = ASAuthorizationPlatformPublicKeyCredentialProvider(
        relyingPartyIdentifier:"example.com")
    let request = provider.createCredentialAssertionRequest(
        challenge: challenge)

    let credentialIDs: [Data] = … // Fetched from server for provided userName
    request.allowedCredentials = credentialIDs.map(
        ASAuthorizationPlatformPublicKeyCredentialDescriptor.init(credentialID:))

    let controller = ASAuthorizationController(authorizationRequests: [request])
    controller.delegate = self
    controller.presentationContextProvider = self

    // Start the request
    controller.performRequests()
}
```

### Modal passkey request with silent fallback — [22:56]

```swift
// Modal passkey request, silent fallback

func signIn() {
    let challenge: Data = … // Fetched from server
    let provider = ASAuthorizationPlatformPublicKeyCredentialProvider(
        relyingPartyIdentifier:"example.com")
    let request = provider.createCredentialAssertionRequest(
        challenge: challenge)

    let controller = ASAuthorizationController(authorizationRequests: [request])
    controller.delegate = self
    controller.presentationContextProvider = self

    // Start the request
    controller.performRequests(options: .preferImmediatelyAvailableCredentials)
}
```

### Silent fallback delegate callback — [23:06]

```swift
// Handling a silent fallback

func authorizationController(controller: ASAuthorizationController, 
    didCompleteWithError error: Error) {

    guard let error = error as? ASAuthorizationError else { … }

    if error.code == .canceled {
        // Either the user canceled the sheet, or there were no credentials available.
        showSignInForm()
    }
}
```

### Combined credential request — [24:40]

```swift
// Combined credential modal request

func signIn() {
    let challenge: Data = … // Fetched from server
    let passkeyProvider = ASAuthorizationPlatformPublicKeyCredentialProvider(
        relyingPartyIdentifier:"example.com")
    let passkeyRequest = passkeyProvider.createCredentialAssertionRequest(
        challenge: challenge)

    let passwordRequest = ASAuthorizationPasswordProvider().createRequest()
    let signInWithAppleRequest = ASAuthorizationAppleIDProvider().createRequest()

    let controller = ASAuthorizationController(
        authorizationRequests: [passkeyRequest, passwordRequest, signInWithAppleRequest])
    controller.delegate = self
    controller.presentationContextProvider = self

    // Start the request
    controller.performRequests()
}
```

### Combined credential callback — [25:02]

```swift
// Completing a combined credential request

func authorizationController(controller: ASAuthorizationController, 
     didCompleteWithAuthorization authorization: ASAuthorization) {

    switch authorization.credential {
    case let passkeyAssertion as ASAuthorizationPlatformPublicKeyCredentialAssertion:
        finishSignIn(with: passkeyAssertion)

    case let signInWithAppleCredential as ASAuthorizationAppleIDCredential:
        finishSignIn(with: signInWithAppleCredential)

    case let passwordCredential as ASPasswordCredential:
        finishSignIn(with: passwordCredential)

    default:
        // Handle other credential types
        break
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10092/3/E39F623F-97FE-48C0-9987-898078EB9D8B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10092/3/E39F623F-97FE-48C0-9987-898078EB9D8B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10092) — developer.apple.com. Indexed for agent consumption._