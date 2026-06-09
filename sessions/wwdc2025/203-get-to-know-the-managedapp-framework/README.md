---
id: "wwdc2025-203"
event: "wwdc2025"
year: 2025
title: "Get to know the ManagedApp Framework"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/203"
topics: ["Business & Education"]
platforms: ["iOS", "iPadOS", "visionOS"]
hasTranscript: true
---

# Get to know the ManagedApp Framework

**Event:** WWDC25 · **Topic:** Business & Education · **Platforms:** iOS, iPadOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-203](https://developer.apple.com/videos/play/wwdc2025/203)

Discover how the ManagedApp framework helps your app adapt to managed environments. We’ll show you how to receive configuration data, manage app secrets securely, and tailor your app’s behavior based on organization-provided settings. We’ll also walk through real-world examples to show how you can build more flexible, manageable apps for enterprise and education environments.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,316 words)

## Documentation & Resources

- [Apple School Manager and Apple Business APIs](https://developer.apple.com/documentation/apple-school-and-business-manager-api) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/apple-school-and-business-manager-api
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/apple-school-and-business-manager-api.json
- [ManagedApp](https://developer.apple.com/documentation/ManagedApp) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ManagedApp
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ManagedApp.json
- [Support - Apple Platform Deployment](https://support.apple.com/guide/deployment/welcome/) _documentation_
- [Apple School Manager User Guide](https://support.apple.com/guide/apple-school-manager/) _documentation_
- [Apple Business Manager User Guide](https://support.apple.com/guide/apple-business-manager/) _guide_

## Code Snippets

### Your app's managed configuration — [0:01]

```swift
// Your app's managed configuration

struct LandmarksManagedConfig: Decodable {

    private(set) var collection: LandmarkCollection?

    private enum CodingKeys: String, CodingKey {
        case collection
    }

    init(from decoder: Decoder) throws {
        let values = try decoder.container(keyedBy: CodingKeys.self)
        collection = try values.decode(LandmarkCollection.self, forKey: .collection)
    }
}
```

### Receiving the current configuration — [0:02]

```swift
// Receiving the current configuration

import ManagedApp

// [...]

var managedCollection: LandmarkCollection?

// [...]

func loadCollections() {
    // [...]
    Task {
        let configProvider = ManagedAppConfigurationProvider()

        for await config in await configProvider.configurations(LandmarksManagedConfig.self) {
            // config's type is LandmarksManagedConfig?
            managedCollection = config?.collection
        } // Loops forever
    }
}
```

### Using an identity — [0:03]

```swift
// Using an identity

final class MyURLSessionDelegate: NSObject, URLSessionDelegate {

    func urlSession(_ session: URLSession,
                    didReceive challenge: URLAuthenticationChallenge)
        async -> (URLSession.AuthChallengeDisposition, URLCredential?) {
        switch challenge.protectionSpace.authenticationMethod {
        case NSURLAuthenticationMethodClientCertificate:

            // Look up the identity
            let provider = ManagedAppIdentitiesProvider()
            let id = "AssetDownloadClient"
            guard let identity = try? await provider.identity(withIdentifier: id) else {
                // No identity, cancel the challenge
                return (.cancelAuthenticationChallenge, nil)
            }

            // Use the identity to authenticate.
            return (.useCredential, URLCredential(identity: identity,
                                                  certificates: nil,
                                                  persistence: .forSession))
        default:
            return (.performDefaultHandling, nil)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/203/6/f89d3254-c464-4d37-80cd-45de128efd20/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/203/6/f89d3254-c464-4d37-80cd-45de128efd20/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/203) — developer.apple.com. Indexed for agent consumption._
