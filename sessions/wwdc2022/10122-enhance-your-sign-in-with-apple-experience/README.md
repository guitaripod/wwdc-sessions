---
id: "wwdc2022-10122"
event: "wwdc2022"
year: 2022
title: "Enhance your Sign in with Apple experience"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10122"
topics: ["Safari & Web", "System Services", "Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Enhance your Sign in with Apple experience

**Event:** WWDC22 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10122](https://developer.apple.com/videos/play/wwdc2022/10122)

Learn how you can provide safe and fast authentication in your app using Sign in with Apple. We’ll show you how you can upgrade password-based accounts into secure, single-tap login credentials, and explore how you can seamlessly handle changes to user sessions in your app. We’ll also help you take advantage of Sign In with Apple across the web and on other platforms. To get the most out of this session, we recommend having familiarity with Sign In with Apple and REST API. We’d also recommend having a basic understanding of JavaScript.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,544 words)

## Documentation & Resources

- [Token revocation](https://developer.apple.com/documentation/SigninwithAppleRESTAPI/Revoke-tokens) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SigninwithAppleRESTAPI/Revoke-tokens
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SigninwithAppleRESTAPI/Revoke-tokens.json
- [Sign in with Apple Button](https://appleid.apple.com/signinwithapple/button) _guide_
- [Implementing User Authentication with Sign in with Apple](https://developer.apple.com/documentation/AuthenticationServices/implementing-user-authentication-with-sign-in-with-apple) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/AuthenticationServices/implementing-user-authentication-with-sign-in-with-apple
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/AuthenticationServices/implementing-user-authentication-with-sign-in-with-apple.json

## Code Snippets

### Presenting Existing Credentials — [4:03]

```swift
// Requesting both Sign in with Apple and password-based accounts.

import AuthenticationServices

let controller = ASAuthorizationController(authorizationRequests: [
    ASAuthorizationAppleIDProvider().createRequest(),
    ASAuthorizationPasswordProvider().createRequest()
])

controller.delegate = self
controller.presentationContextProvider = self

if #available(iOS 16.0, *) {
    controller.performRequests(options: .preferImmediatelyAvailableCredentials)
} else {
    controller.performRequests()
}
```

### ASAuthorizationControllerDelegate Implementation — [5:14]

```swift
// ASAuthorizationControllerDelegate

func authorizationController(controller: ASAuthorizationController,
                             didCompleteWithAuthorization authorization: ASAuthorization) {
    switch authorization.credential {  
		case let appleIDCredential as ASAuthorizationAppleIDCredential:
        // Sign the user in with Apple ID credential.
        // ...

    case let passwordCredential as ASPasswordCredential:
       // Sign the user in with password credential
       // ...
   }
}

func authorizationController(controller: ASAuthorizationController, 
   didCompleteWithError error: Error) {
    // No credential found. Fall back to login UI.
}
```

### Checking Credential State — [12:00]

```swift
// Check User Credentials on app launch

let appleIDProvider = ASAuthorizationAppleIDProvider()
appleIDProvider.getCredentialState(forUserID: "currentUserIdentifier") 
{ (credentialState, error) in
    switch(credentialState){
    case .authorized:
        // Found valid Apple ID credential
    case .revoked:
        // Apple ID credential revoked. Log the user out.
    case .notFound:
        // No credential found. Show login UI.
    case .transferred:
        // Team is transferred
    }
}
```

### Register for Revocation Notification — [12:18]

```swift
// Register for revocation notification

let notificationName = ASAuthorizationAppleIDProvider.credentialRevokedNotification

NotificationCenter.default.addObserver(self, 
                                       selector: #selector(signOut(_:)),
                                       name: notificationName, 
                                       object: nil)
```

### Sample HTML and Javascript Implementation — [17:55]

```javascript
// Embed Sign in with Apple JS
<html>
    <body>
        <script type="text/javascript" src="https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js"></script>
        <div id="appleid-signin" data-color="white" data-border="true" data-type="sign in"/>
        <script type="text/javascript">
            AppleID.auth.init({
                clientId : '[CLIENT_ID]',
                scope : '[SCOPES]',
                redirectURI : '[REDIRECT_URI]',
                state : '[STATE]',
                nonce : '[NONCE]',
                usePopup : true
            });
        </script>
    </body>
</html>
```

### White Sign in with Apple Button — [18:28]

```xml
<div id="appleid-signin" data-color="white" data-border="true" data-type="sign in"/>
```

### Black Sign in with Apple Button — [18:38]

```xml
<div id="appleid-signin" data-color="black" data-border="true" data-type="sign in"/>
```

### Black Continue with Apple Button — [18:44]

```xml
<div id="appleid-signin" data-color="black" data-border="true" data-type="continue"/>
```

### Black Logo Only Button — [18:50]

```xml
<div id="appleid-signin" data-color="black" data-border="true" data-mode="logo-only"/>
```

### Sample HTML and Javascript Implementation — [19:47]

```javascript
// Embed Sign in with Apple JS
<html>
    <body>
        <script type="text/javascript" src="https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js"></script>
        <div id="appleid-signin" data-color="white" data-border="true" data-type="sign in"/>
        <script type="text/javascript">
            AppleID.auth.init({
                clientId : '[CLIENT_ID]',
                scope : '[SCOPES]',
                redirectURI : '[REDIRECT_URI]',
                state : '[STATE]',
                nonce : '[NONCE]',
                usePopup : true
            });
        </script>
    </body>
</html>
```

### Handle DOM Response — [21:11]

```javascript
// Listen for authorization success.
document.addEventListener('AppleIDSignInOnSuccess', (event) => {
    // Handle successful response.
    console.log(event.detail.data);
});

// Listen for authorization failures.
document.addEventListener('AppleIDSignInOnFailure', (event) => {
     // Handle error.
     console.log(event.detail.error);
});
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10122/5/F35FC4AA-E76F-444D-85D0-77A76E7D3E15/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10122/5/F35FC4AA-E76F-444D-85D0-77A76E7D3E15/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10122) — developer.apple.com. Indexed for agent consumption._
