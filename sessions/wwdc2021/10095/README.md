---
id: "wwdc2021-10095"
event: "wwdc2021"
year: 2021
title: "Use async/await with URLSession"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10095"
topics: ["Swift", "System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Use async/await with URLSession

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10095](https://developer.apple.com/videos/play/wwdc2021/10095)

Discover how you can adopt Swift concurrency in URLSession using async/await and AsyncSequence, and how you can apply Swift concurrency concepts to improve your networking code.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,677 words)

## Documentation & Resources

- [URLSession](https://developer.apple.com/documentation/Foundation/URLSession) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Foundation/URLSession
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Foundation/URLSession.json

## Code Snippets

### Fetch photo with async/await — [2:52]

```swift
// Fetch photo with async/await

func fetchPhoto(url: URL) async throws -> UIImage
{
    let (data, response) = try await URLSession.shared.data(from: url)

    guard let httpResponse = response as? HTTPURLResponse,
          httpResponse.statusCode == 200 else {
        throw WoofError.invalidServerResponse
    }

    guard let image = UIImage(data: data) else {
        throw WoofError.unsupportedImage
    }

    return image
}
```

### URLSession.data — [3:45]

```swift
let (data, response) = try await URLSession.shared.data(from: url)
guard let httpResponse = response as? HTTPURLResponse,
      httpResponse.statusCode == 200 /* OK */ else {
    throw MyNetworkingError.invalidServerResponse
}
```

### URLSession.upload — [4:03]

```swift
var request = URLRequest(url: url)
request.httpMethod = "POST"

let (data, response) = try await URLSession.shared.upload(for: request, fromFile: fileURL)
guard let httpResponse = response as? HTTPURLResponse,
      httpResponse.statusCode == 201 /* Created */ else {
    throw MyNetworkingError.invalidServerResponse
}
```

### URLSession.download — [4:21]

```swift
let (location, response) = try await URLSession.shared.download(from: url)
guard let httpResponse = response as? HTTPURLResponse,
      httpResponse.statusCode == 200 /* OK */ else {
    throw MyNetworkingError.invalidServerResponse
}

try FileManager.default.moveItem(at: location, to: newLocation)
```

### Cancellation — [4:44]

```swift
let task = Task {
    let (data1, response1) = try await URLSession.shared.data(from: url1)

    let (data2, response2) = try await URLSession.shared.data(from: url2)

}

task.cancel()
```

### asyncSequence demo — [7:53]

```swift
let (bytes, response) = try await URLSession.shared.bytes(from: Self.eventStreamURL)
guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
    throw WoofError.invalidServerResponse
}
for try await line in bytes.lines {
    let photoMetadata = try JSONDecoder().decode(PhotoMetadata.self, from: Data(line.utf8))
    await updateFavoriteCount(with: photoMetadata)
}
```

### task specific delegate demo — [11:20]

```swift
class AuthenticationDelegate: NSObject, URLSessionTaskDelegate {
    private let signInController: SignInController

    init(signInController: SignInController) {
        self.signInController = signInController
    }

    func urlSession(_ session: URLSession,
                    task: URLSessionTask,
                    didReceive challenge: URLAuthenticationChallenge) async
    -> (URLSession.AuthChallengeDisposition, URLCredential?) {
        if challenge.protectionSpace.authenticationMethod == NSURLAuthenticationMethodHTTPBasic {
            do {
                let (username, password) = try await signInController.promptForCredential()
                return (.useCredential,
                        URLCredential(user: username, password: password, persistence: .forSession))
            } catch {
                return (.cancelAuthenticationChallenge, nil)
            }
        } else {
            return (.performDefaultHandling, nil)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10095/8/93EE04B2-8F10-42B5-B35F-D7D4A87C1DC2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10095/8/93EE04B2-8F10-42B5-B35F-D7D4A87C1DC2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10095) — developer.apple.com. Indexed for agent consumption._