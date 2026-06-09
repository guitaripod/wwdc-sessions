---
id: "wwdc2020-10670"
event: "wwdc2020"
year: 2020
title: "Meet Face ID and Touch ID for the web"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10670"
topics: ["Safari & Web", "Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Meet Face ID and Touch ID for the web

**Event:** WWDC20 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10670](https://developer.apple.com/videos/play/wwdc2020/10670)

Face ID and Touch ID provide a frictionless experience when logging in — and now you can use them on your websites in Safari with the Web Authentication API. Discover how to add this convenient and secure login alternative to your website.

**Keywords:** `applestmtformat`, `aswebauthenticationsession`, `attestation`, `authenticator`, `authenticatorattestationresponse`, `authenticatorselection`, `challenge`, `credential`, `crypto`, `cryptographic`, `cryptography`, `enroll`, `isuserverifyingplatformauthenticatoravailable`, `json`, `multi-factor`, `navigator.credentials`, `phishing`, `platform authenticator`, `private key`, `pubkeycredparams`, `public key`, `publickeycredentials`, `relying party`, `server-side`, `sfsafariviewcontroller`, `signature`, `webauthn`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,360 words)

## Documentation & Resources

- [Safari Release Notes](https://developer.apple.com/documentation/safari-release-notes) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/safari-release-notes
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/safari-release-notes.json
- [WebKit Open Source Project](https://webkit.org) _guide_

## Code Snippets

### Feature detection — [7:44]

```javascript
// Feature detection

const isAvailable = await PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable();

if (isAvailable) {
    // Continue to enrollment or sign in
    // ...
}
```

### Enrollment — [8:42]

```javascript
// Enrollment

const options = {
    publicKey: {
        rp: { name: "example.com" },
        user: {
            name: "john.appleseed@example.com",
            id: userIdBuffer,
            displayName: "John Appleseed"
        },
        pubKeyCredParams: [ { type: "public-key", alg: -7 } ],
        challenge: challengeBuffer,
        authenticatorSelection: { authenticatorAttachment: "platform" },
        attestation: "direct"
    }
};

const publicKeyCredential = await navigator.credentials.create(options);
```

### Sign in — [11:42]

```javascript
// Sign in

const options = {
    publicKey: {
        challenge: challengeBuffer,
        allowCredentials: [{
             type: "public-key",
             id: credentialIdBuffer,
             transports: ["internal"]
        }]
    }
};

const publicKeyCredential = await navigator.credentials.get(options);
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10670/5/F2522A6C-CD56-4570-8939-B8BB17427290/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10670) — developer.apple.com. Indexed for agent consumption._
