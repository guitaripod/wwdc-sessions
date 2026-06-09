---
id: "wwdc2026-209"
event: "wwdc2026"
year: 2026
title: "What’s new in Wallet"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/209"
topics: ["System Services", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS", "watchOS"]
hasTranscript: true
---

# What’s new in Wallet

**Event:** WWDC26 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-209](https://developer.apple.com/videos/play/wwdc2026/209)

Explore the newest design updates and developer tools for Apple Wallet passes. Refresh your passes with beautiful new styles for rich, vibrant designs. Discover new barcode formats and a flexible pass actions API. Meet Pass Designer and Pass Builder, powerful tools that simplify designing, personalizing, and distributing your passes at scale.

**Keywords:** `certificate`, `certificates`, `distribution`, `package`, `pass`, `passes`, `signature`, `signing`, `wallet`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,161 words)

## Documentation & Resources

- [Pass Builder](https://github.com/apple/pass-builder) _guide_
- [Wallet](https://developer.apple.com/documentation/PassKit/wallet) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PassKit/wallet
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PassKit/wallet.json

## Code Snippets

### Adopting Poster Generic — [1:41]

```json
// Adopting Poster Generic
"posterGeneric": {
  "headerFields": [
    {
      "key": "memberID",
      "label": "Guest No.",
      "value": "102035"
    }
  ],
  "footerFields": [
    {
      "key": "membershipType",
      "value": "Family Pass"
    }
  ]
}
```

### Adopting Poster Generic with Generic fallback — [2:11]

```json
// Adopting Poster Generic and supporting Generic on iOS 26 and earlier
"posterGeneric": {
  "headerFields": [
    {
      "key": "memberID",
      "label": "Guest No.",
      "value": "102035"
    }
  ],
  "footerFields": [
    {
      "key": "membershipType",
      "value": "Family Pass"
    }
  ]
},
"generic": {
  "headerFields": [
    {
      "key": "memberID",
      "label": "Guest No.",
      "value": "102035"
    }
  ],
  "footerFields": [
    {
      "key": "membershipType",
      "value": "Family Pass"
    }
  ]
}
```

### Barcodes: Add new types for iOS 27 — [2:52]

```json
// Adopting new barcode types
"barcodes": [
  {
    "format": "PKBarcodeFormatCodabar"
    "message": "…"
    "messageEncoding": "…"
  }
]
```

### Barcodes: Supporting iOS 26 and earlier — [3:37]

```json
// Adopting new barcode types and supporting iOS 26 and earlier.
"barcodes": [
  {
    "format": "PKBarcodeFormatCodabar"
    "message": "123456789"
    "messageEncoding": "iso-8859-1"
  },
  {
    "format": "PKBarcodeFormatQR"
    "message": "123456789"
    "messageEncoding": "iso-8859-1"
  }
]
```

### Featured actions — [4:48]

```json
// Featured actions
"featuredActions": [
  {
    "identifier": "my-offer-id",
    "type": "membershipBenefits",
    "url": "www.example.com/offers"
  }
]
```

### Package.swift — [10:56]

```swift
// Package.swift

import PackageDescription

let package = Package(
    name: "MyServer",
    products: [
          .library(
              name: "MyServer",
              targets: ["MyServer"]
        ),
    ],
    dependencies: [
        .package(path: "./path/to/PassBuilder")
    ],
    targets: [
        .target(
            name: "MyServer",
            dependencies: [
                .product(name: "PassBuilder", package: "PassBuilder")
            ]
        ),
        …
    ]
```

### CreatePass.swift — [11:05]

```swift
// CreatePass.swift

import PassBuilder

func createPass(for doggo: MemeberModel) async throws -> URL {
    var package = PassPackage(url: "template.pkpasstemplate")

    package.pass.fields.setValue(doggo.name, forKey: "DOG_NAME")
    package.pass.fields.setValue(doggo.favoriteToy, forKey: "LOVES")
    package.pass.fields.setValue(doggo.id, forKey: "MEMBER_ID")

    package.background = PassImage(url: doggo.photoURL)

    package.pass.barcodes = [
        Pass.Barcode(message: doggo.id, format: .pdf417)
    ]

    package.featuredActions = [
        Pass.Action(id: "action-1", type: "viewMembership", url: doggo.membershipURL) 
    ]
    …
}
```

### CreatePass.swift — [13:11]

```swift
// CreatePass.swift

import PassBuilder

func createPass(for doggo: MemeberModel) async throws -> URL {
    var package = PassPackage(url: "template.pkpasstemplate")

    package.pass.fields.setValue(doggo.name, forKey: "DOG_NAME")
    package.pass.fields.setValue(doggo.favoriteToy, forKey: "LOVES")
    package.pass.fields.setValue(doggo.id, forKey: "MEMBER_ID")

    package.background = PassImage(url: doggo.photoURL)

    package.pass.barcodes = [
        Pass.Barcode(message: doggo.id, format: .pdf417)
    ]

    package.featuredActions = [
        Pass.Action(id: "action-1", type: "viewMembership", url: doggo.membershipURL) 
    ]

    let passCertificate = try PassCertificate(url: "pass.p12", password: "s3cr3t")
    let wwdrCertificate = try PassCertificate(url: "wwdr.cer")

    let signer = PassSigner(
        passCertificate: passCertificate,
        wwdrCertifiate: wwdrCertificate
    )

    let destinationURL = URL(string: "/www/passes/" + doggo.id)
    try signer.signPass(package, writingTo: destinationURL)

    return destinationURL
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/209/5/25eb40d5-b64d-4677-bc99-f5c3a30d386a/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/209/5/25eb40d5-b64d-4677-bc99-f5c3a30d386a/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/209) — developer.apple.com. Indexed for agent consumption._
