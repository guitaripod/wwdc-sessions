---
id: "wwdc2025-314"
event: "wwdc2025"
year: 2025
title: "Get ahead with quantum-secure cryptography"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/314"
topics: ["System Services", "Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Get ahead with quantum-secure cryptography

**Event:** WWDC25 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-314](https://developer.apple.com/videos/play/wwdc2025/314)

Learn how to protect your app’s sensitive user data from the emerging threat of quantum computing, and safeguard user privacy. We’ll explore different quantum attacks, their impact on existing cryptographic protocols, and how to defend against them using quantum-secure cryptography. You’ll learn how to use quantum-secure TLS to secure network data, and use CryptoKit’s quantum-secure APIs for securing application data.

**Keywords:** `🎈`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,655 words)

## Documentation & Resources

- [Enhancing your app’s privacy and security with quantum-secure workflows](https://developer.apple.com/documentation/CryptoKit/enhancing-your-app-s-privacy-and-security-with-quantum-secure-workflows) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CryptoKit/enhancing-your-app-s-privacy-and-security-with-quantum-secure-workflows
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CryptoKit/enhancing-your-app-s-privacy-and-security-with-quantum-secure-workflows.json
- [Prepare your network for quantum-secure encryption in TLS](https://support.apple.com/122756) _guide_
- [Message with PQ3: The new state of the art in quantum-secure messaging at scale](https://security.apple.com/blog/imessage-pq3/) _documentation_
- [Apple CryptoKit](https://developer.apple.com/documentation/CryptoKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CryptoKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CryptoKit.json

## Code Snippets

### HPKE code sample — [15:00]

```swift
let ciphersuite = HPKE.Ciphersuite.XWingMLKEM768X25519_SHA256_AES_GCM_256

// Recipient
let privateKey = try XWingMLKEM768X25519.PrivateKey.generate()
let publicKey = privateKey.publicKey

// Sender
var sender = try HPKE.Sender(recipientKey: publicKey, ciphersuite: ciphersuite, info: info)
let encapsulatedKey = sender.encapsulatedKey

// Recipient
var recipient = try HPKE.Recipient(privateKey: privateKey, ciphersuite: ciphersuite, info: info, encapsulatedKey: encapsulatedKey) 

// Sender encrypts data
let ciphertext = try sender.seal(userData, authenticating: metadata)

// Recipient decrypts message
let decryptedData = try recipient.open(ciphertext, authenticating: metadata)
#expect(userData == decryptedData)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/314/4/69450908-6907-44d0-9f37-9ffdec893aa2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/314/4/69450908-6907-44d0-9f37-9ffdec893aa2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/314) — developer.apple.com. Indexed for agent consumption._