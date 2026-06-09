---
id: "wwdc2022-10108"
event: "wwdc2022"
year: 2022
title: "Streamline local authorization flows"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10108"
topics: ["Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Streamline local authorization flows

**Event:** WWDC22 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10108](https://developer.apple.com/videos/play/wwdc2022/10108)

Discover how you can use the latest authorization-focused APIs in LocalAuthentication to protect the privacy and security of people’s data. We’ll show you how LocalAuthentication can authorize access to secrets, keys, and other sensitive resources in your app, all while reducing complexity and relying on the security and usability of common local authentication methods such as Touch ID and Face ID.

**Keywords:** `acl`, `biometric`, `lacontext`, `laright`, `lock`, `secure enclave`, `unlock`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,562 words)

## Documentation & Resources

- [Local Authentication](https://developer.apple.com/documentation/LocalAuthentication) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/LocalAuthentication
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/LocalAuthentication.json
- [Protecting keys with the Secure Enclave](https://developer.apple.com/documentation/Security/protecting-keys-with-the-secure-enclave) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Security/protecting-keys-with-the-secure-enclave
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Security/protecting-keys-with-the-secure-enclave.json

## Code Snippets

### LAContext (authorize a signature operation 1) — [4:58]

```swift
let query: [String: Any] = [
    kSecClass as String: kSecClassKey,
    kSecAttrTokenID as String: kSecAttrTokenIDSecureEnclave,
    kSecAttrApplicationTag as String: "com.example.app.key",
    kSecReturnAttributes as String: true,
]

var item: CFTypeRef? = nil
guard SecItemCopyMatching(query as CFDictionary, &item) == errSecSuccess, let attrs = item as? NSDictionary, let accessControl = attrs[kSecAttrAccessControl] else {
    throw .aclNotFound
}
```

### LAContext (authorize a signature operation 2) — [5:15]

```swift
let context = LAContext()
try await context.evaluateAccessControl(accessControl as! SecAccessControl, 
                      operation: .useKeySign, 
                       localizedReason: "Authentication is required to proceed")
```

### LAContext (authorize a signature operation 3) — [5:44]

```swift
let query: [String: Any] = [
    kSecClass as String: kSecClassKey,
    kSecAttrTokenID as String: kSecAttrTokenIDSecureEnclave,
    kSecAttrApplicationTag as String: "com.example.app.key",
    kSecReturnRef as String: true,
    kSecUseAuthenticationContext as String: context
]

var item: CFTypeRef? = nil
guard SecItemCopyMatching(query as CFDictionary, &item) == errSecSuccess, item != nil else { 
    throw .keyNotFound
}
```

### LAContext (authorize a signature operation 4) — [6:00]

```swift
let privateKey = item as! SecKey

var error: Unmanaged<CFError>?
guard let sgt = SecKeyCreateSignature(privateKey, self.algorithm, blob, &error) as Data? else {
    throw .signatureFailure
}
```

### LA Right (basic usage) — [8:28]

```swift
// LARight: Basic usage

func login() async {
   self.loginRight = LARight(requirement: .biometry(fallback: .devicePasscode))
   do {
       try await loginRight.checkCanAuthorize()
   } catch {
       navigateTo(section: .public)
       return
   }
   do {
      try await self.loginRight.authorize(localizedReason: self.localizedReason)
 navigateTo(section: .protected)
   } catch {
      showError(.authenticationRequired)
   }
}
```

### LARight (logout and deauthorization) — [11:01]

```swift
// LARight: Basic usage

func login() async {
   self.loginRight = LARight(requirement: .biometry(fallback: .devicePasscode))
   // ...
   do {
       try await self.loginRight.authorize(localizedReason: self.localizedReason)
  navigateTo(section: .protected)
   } catch {
       showError(.authenticationRequired)
   }
}

func logout() async {   
   await self.loginRight.deauthorize()
}
```

### LAPersistedRight — [13:44]

```swift
// LAPersistedRight: Retrieval and private key usage

func generateClientKeys() async throws -> Data {
    let login2FA = LARight(requirement: .biometryCurrentSet)
    let persisted2FA = try await LARightStore.shared.saveRight(login2FA, identifier: "2fa")
    return try await persisted2FA.key.publicKey.bytes
}

func signChallenge(_ challenge: Data, algorithm: SecKeyAlgorithm) async throws -> Data {
    let persisted2FA = try await LARightStore.shared.right(forIdentifier: "2fa")
    let localizedReason = "Biometric authentication is required to proceed"
    try await persisted2FA.authorize(localizedReason: localizedReason)
    return try await persisted2FA.key.sign(challenge, algorithm: algorithm)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10108/4/1F8BF487-ABEF-47CD-AC84-C3AC2E35885A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10108/4/1F8BF487-ABEF-47CD-AC84-C3AC2E35885A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10108) — developer.apple.com. Indexed for agent consumption._