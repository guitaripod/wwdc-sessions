---
id: "wwdc2026-378"
event: "wwdc2026"
year: 2026
title: "Unlock in-game content with StoreKit and Background Assets"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/378"
topics: ["App Services", "App Store, Distribution & Marketing"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Unlock in-game content with StoreKit and Background Assets

**Event:** WWDC26 · **Topic:** App Store, Distribution & Marketing · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-378](https://developer.apple.com/videos/play/wwdc2026/378)

Unlock native Apple In-App Purchases for your Unity game with the new StoreKit plug-in. Reduce download sizes with the new Background Assets plug-in, which delivers language-specific asset packs so each player gets just what they need. Plus, a new Steam Asset Converter helps you migrate existing builds.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,506 words)

## Documentation & Resources

- [Apple Unity Plug-Ins on GitHub](https://github.com/apple/unityplugins) _download_
- [Background Assets](https://developer.apple.com/documentation/BackgroundAssets) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/BackgroundAssets
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/BackgroundAssets.json
- [StoreKit](https://developer.apple.com/documentation/StoreKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/StoreKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/StoreKit.json

## Code Snippets

### Asset pack manifest for a localized asset pack — [3:06]

```json
// Asset pack manifest

{
   "assetPackID": "voice-english",
   "downloadPolicy": { /* … */ },
   "language": "en-US",
   "sourceRoot": ".",
   "fileSelectors": [ /* … */ ],
   "platforms": [ /* … */ ]
    //… 
}
```

### Convert a Steam depot to an asset pack manifest — [3:27]

```bash
# Convert a Steam depot to an asset pack manifest
xcrun ba-package convert --asset-pack-id voice-english --l en-US --on-demand voice-english.vdf -o voice-english.json
```

### Convert an asset pack manifest to an asset pack archive — [3:28]

```bash
# Convert an asset pack manifest to an asset pack archive
xcrun ba-package voice-english.json -o voice-english.aar
```

### Fetch and purchase products with the StoreKit plug-in — [5:52]

```csharp
// Fetch and purchase products with the StoreKit plug-in

using UnityEngine;
using Apple.StoreKit;

async void Start() {
    var products = await Product.FetchProducts(new[] {
            "com.thecoast.capecod"
    });
}
```

### Fetch and purchase products with the StoreKit plug-in — [6:01]

```csharp
// Fetch and purchase products with the StoreKit plug-in

using UnityEngine;
using Apple.StoreKit;

async void Purchase(Product product) {
    var result = await product.Purchase();
    if (result.Result == PurchaseResult.ResultEnum.Success
        && result.TransactionVerification.IsVerified)
    {
        // Unlock access to purchased content

        result.TransactionVerification.SafePayload.Finish();
    }
}
```

### Listen for Transaction updates with the StoreKit plug-in — [6:23]

```csharp
// Listen for Transaction updates with the StoreKit plug-in

using UnityEngine;
using Apple.StoreKit;

public static class TransactionListener {
    public static void Initialize() => Transaction.Updates += OnUpdate;


    async void OnUpdate(VerificationResult<Transaction> result) {
        if (!result.IsVerified) return;
        var verifiedTransaction = result.SafePayload;

        // Consumables are not in CurrentEntitlements, so handle them inline
        if (verifiedTransaction.ProductType == ProductType.ProductTypeEnum.Consumable) {
            if (verifiedTransaction.RevocationDate != null) {
                // Revoke the consumable identified by verifiedTransaction.ProductId
            } else {
                // Grant access to the consumable
            }
        }else {
            // Non-consumables and subscriptions: re-read CurrentEntitlements as source of truth
            await foreach (var verificationResult in Transaction.GetCurrentEntitlements()) {
                if (!verificationResult.IsVerified) continue;
                // Grant access to the product
            }
        }
        verifiedTransaction.Finish();
    }
}
```

### Download asset packs with the Background Assets plug-in — [7:13]

```csharp
// Download asset packs with the Background Assets plug-in

using Apple.BackgroundAssets;
using UnityEngine;

async void LoadTutorial(string language) {
    try {
        string assetPackId = $"tutorial-{language}";
        AssetPackManifest manifest = await AssetPackManager.GetManifestAsync();
        AssetPack assetPack = manifest.GetAssetPack(assetPackId);
        CancellationTokenSource tokenSource = new CancellationTokenSource();
        _ = Task.Run(async () => {
            await foreach (AssetPackManager.DownloadStatusUpdate statusUpdate in AssetPackManager.DownloadStatusUpdatesAsync(assetPackId)) { 
            		// Update download progress in UI
            }
        }, tokenSource.Token);
        await AssetPackManager.EnsureLocalAvailabilityOfAssetPackAsync(assetPack);
        tokenSource.Cancel();
        // Start tutorial with the locally available assets
    } catch (Exception exception) {
        // Handle the exception
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/378/6/16c93f95-21e8-4f7f-bb96-2b3c682fa6c7/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/378/6/16c93f95-21e8-4f7f-bb96-2b3c682fa6c7/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/378) — developer.apple.com. Indexed for agent consumption._