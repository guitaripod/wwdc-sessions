---
id: "wwdc2023-10263"
event: "wwdc2023"
year: 2023
title: "Deploy passkeys at work"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10263"
topics: ["Privacy & Security", "Business & Education"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Deploy passkeys at work

**Event:** WWDC23 · **Topic:** Business & Education · **Platforms:** iOS, iPadOS, macOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10263](https://developer.apple.com/videos/play/wwdc2023/10263)

Discover how you can take advantage of passkeys in managed environments at work. We’ll explore how passkeys can work well in enterprise environments through Managed Apple ID support for iCloud Keychain. We’ll also share how administrators can manage passkeys for specific devices using Access Management controls in Apple Business Manager and Apple School Manager.

**Keywords:** `2fa`, `attestation`, `password`, `phishing`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,610 words)

## Documentation & Resources

- [Passkeys overview](https://developer.apple.com/passkeys/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/passkeys/

## Code Snippets

### Example passkey attestation configuration — [11:07]

```json
// Example configuration: com.apple.configuration.security.passkey.attestation

{
    "Type": "com.apple.configuration.security.passkey.attestation",
    "Identifier": "B1DC0125-D380-433C-913A-89D98D68BA9C",
    "ServerToken": "8EAB1785-6FC4-4B4D-BD63-1D1D2A085106",
    "Payload": {
        "AttestationIdentityAssetReference": "88999A94-B8D6-481A-8323-BF2F029F4EF9",
        "RelyingParties": [
            "www.example.com"
        ]
    }
}
```

### WebAuthn Packed Attestation Statement Format — [13:12]

```json
// WebAuthn Packed Attestation Statement Format

attestationObject: {
    "fmt": "packed",
    "attStmt": {
        "alg": -7, // for ES256
        "sig": bytes,
        "x5c": [ attestnCert: bytes, * (caCert: bytes) ]
    }
    "authData": {
        "attestedCredentialData": {
            "aaguid": “dd4ec289-e01d-41c9-bb89-70fa845d4bf2”, // for Apple devices
            <…>
        }
        <…>
    }
    <…>
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10263/6/31A324CE-DD40-456B-A7DB-8660EF139277/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10263/6/31A324CE-DD40-456B-A7DB-8660EF139277/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10263) — developer.apple.com. Indexed for agent consumption._
