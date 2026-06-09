---
id: "wwdc2023-10006"
event: "wwdc2023"
year: 2023
title: "Build robust and resumable file transfers"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10006"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Build robust and resumable file transfers

**Event:** WWDC23 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10006](https://developer.apple.com/videos/play/wwdc2023/10006)

Find out how URLSession can help your apps transfer large files and recover from network interruptions. Learn how to pause and resume HTTP file transfers and support resumable uploads, and explore best practices for using URLSession to transfer files even when your app is suspended in the background.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,714 words)

## Documentation & Resources

- [Building a resumable upload server with SwiftNIO](https://developer.apple.com/documentation/Foundation/building-a-resumable-upload-server-with-swiftnio) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Foundation/building-a-resumable-upload-server-with-swiftnio
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Foundation/building-a-resumable-upload-server-with-swiftnio.json
- [Downloading files in the background](https://developer.apple.com/documentation/Foundation/downloading-files-in-the-background) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Foundation/downloading-files-in-the-background
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Foundation/downloading-files-in-the-background.json
- [URLSession](https://developer.apple.com/documentation/Foundation/URLSession) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Foundation/URLSession
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Foundation/URLSession.json

## Code Snippets

### Pausing and resuming a URLSessionDownloadTask — [4:53]

```swift
let downloadTask = session.downloadTask(with: request)
downloadTask.resume()
```

### Pausing and resuming a URLSessionDownloadTask — [5:21]

```swift
let downloadTask = session.downloadTask(with: request)
downloadTask.resume()

guard let resumeData = await downloadTask.cancelByProducingResumeData() else {
    // Download cannot be resumed
    return
}
```

### Pausing and resuming a URLSessionDownloadTask — [6:11]

```swift
let downloadTask = session.downloadTask(with: request)
downloadTask.resume()

guard let resumeData = await downloadTask.cancelByProducingResumeData() else {
    // Download cannot be resumed
    return
}

let newDownloadTask = session.downloadTask(withResumeData: resumeData)
newDownloadTask.resume()
```

### Retrieving resume data on error — [6:34]

```swift
do {
    let (url, response) = try await session.download(for: request)
} catch let error as URLError {
    guard let resumeData = error.downloadTaskResumeData else {
        // Download cannot be resumed
        return
    }
}
```

### Pausing and resuming a URLSessionUploadTask — [8:29]

```swift
let uploadTask = session.uploadTask(with: request, fromFile: fileURL)
uploadTask.resume()
```

### Pausing and resuming a URLSessionUploadTask — [8:37]

```swift
let uploadTask = session.uploadTask(with: request, fromFile: fileURL)
uploadTask.resume()

guard let resumeData = await uploadTask.cancelByProducingResumeData() else {
    // Upload cannot be resumed
    return
}
```

### Pausing and resuming a URLSessionUploadTask — [8:57]

```swift
let uploadTask = session.uploadTask(with: request, fromFile: fileURL)
uploadTask.resume()

guard let resumeData = await uploadTask.cancelByProducingResumeData() else {
    // Upload cannot be resumed
    return
}

let newUploadTask = session.uploadTask(withResumeData: resumeData)
newUploadTask.resume()
```

### Retrieving resume data on error — [9:22]

```swift
do {
    let (data, response) = try await session.upload(for: request, fromFile: fileURL)
} catch let error as URLError {
    guard let resumeData = error.uploadTaskResumeData else {
        // Upload cannot be resumed
        return
    }
}
```

### Before resumable uploads in Swift NIO — [13:15]

```swift
NIOTSListenerBootstrap(group: NIOTSEventLoopGroup())
.childChannelInitializer { channel in
    channel.configureHTTP2Pipeline(mode: .server) { channel in
        channel.pipeline.addHandlers([
            HTTP2FramePayloadToHTTPServerCodec(),
            ExampleChannelHandler()
        ])
    }.map { _ in () }
}
.tlsOptions(tlsOptions)
```

### Add resumable uploads in Swift NIO — [14:06]

```swift
import NIOResumableUpload

let uploadContext = HTTPResumableUploadContext(origin: "https://example.com")

NIOTSListenerBootstrap(group: NIOTSEventLoopGroup())
    .childChannelInitializer { channel in
        channel.configureHTTP2Pipeline(mode: .server) { channel in
            channel.pipeline.addHandlers([
                HTTP2FramePayloadToHTTPServerCodec(),
                HTTPResumableUploadHandler(context: uploadContext, handlers: [
                    ExampleChannelHandler()
                ])
            ])
        }.map { _ in () }
    }
    .tlsOptions(tlsOptions)
```

### Informational responses in URLSession — [15:48]

```swift
protocol URLSessionTaskDelegate : URLSessionDelegate {
    optional func urlSession(_ session: URLSession, task: URLSessionTask,
                             didReceiveInformationalResponse response: HTTPURLResponse)
}
```

### Using background URLSession — [18:19]

```swift
// Configuring your background session
let configuration = URLSessionConfiguration.background(withIdentifier: "com.example.app")
configuration.isDiscretionary = true
configuration.allowsConstrainedNetworkAccess = false
let session = URLSession(configuration: configuration, delegate: self, delegateQueue: nil)

// Configuring your background task
let backgroundTask = session.uploadTask(with: url, fromFile: fileURL)
backgroundTask.earliestBeginDate = .now.addingTimeInterval(60 * 60)
backgroundTask.countOfBytesClientExpectsToSend = 500 * 1024
backgroundTask.countOfBytesClientExpectsToReceive = 200
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10006/4/62804C33-C167-4D42-9E12-390AED4A4EE1/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10006/4/62804C33-C167-4D42-9E12-390AED4A4EE1/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10006) — developer.apple.com. Indexed for agent consumption._