---
id: "wwdc2020-10644"
event: "wwdc2020"
year: 2020
title: "Use Swift on AWS Lambda with Xcode"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10644"
topics: ["Developer Tools"]
platforms: ["macOS"]
hasTranscript: true
---

# Use Swift on AWS Lambda with Xcode

**Event:** WWDC20 · **Topic:** Developer Tools · **Platforms:** macOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10644](https://developer.apple.com/videos/play/wwdc2020/10644)

Serverless functions are increasingly becoming popular for running event-driven or otherwise ad-hoc compute tasks in the cloud, allowing developers to more easily scale and control compute costs. Discover how to use the new Swift AWS Lambda Runtime package to build serverless functions in Swift, debug locally using Xcode, and deploy these functions to the AWS Lambda platform. We’ll show you how Swift shines on AWS Lambda thanks to its low memory footprint, deterministic performance, and quick start time.

**Keywords:** `aws`, `lambda`, `server-side`, `swift`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,946 words)

## Documentation & Resources

- [Swift AWS Lambda Runtime on GitHub](https://github.com/swift-server/swift-aws-lambda-runtime/) _guide_
- [Introducing Swift AWS Lambda Runtime](https://swift.org/blog/aws-lambda-runtime/) _guide_

## Code Snippets

### Closure based Lambda function — [2:02]

```swift
import AWSLambdaRuntime

Lambda.run { (_, name: String, callback) in
    callback(.success("Hello, \(name)!"))
}
```

### EventLoop based Lambda function — [2:33]

```swift
import AWSLambdaRuntime
import NIO

struct Handler: EventLoopLambdaHandler {
    typealias In = String
    typealias Out = String

    func handle(context: Lambda.Context, event: String) -> EventLoopFuture<String> {
       context.eventLoop.makeSucceededFuture("Hello, \(event)!")
    }
}

Lambda.run(Handler())
```

### Closure and Codable based Lambda function — [2:59]

```swift
import AWSLambdaRuntime

struct Request: Codable {
    let name: String
    let password: String
}

struct Response: Codable {
    let message: String
}

Lambda.run { (_, request: Request, callback) in
    callback(.success(Response(message: "Hello, \(request.name)!")))
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10644/5/4AF78B69-A0D2-421E-A8B8-142BF9544723/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10644) — developer.apple.com. Indexed for agent consumption._
