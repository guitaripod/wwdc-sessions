---
id: "wwdc2023-10168"
event: "wwdc2023"
year: 2023
title: "Generalize APIs with parameter packs"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10168"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Generalize APIs with parameter packs

**Event:** WWDC23 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10168](https://developer.apple.com/videos/play/wwdc2023/10168)

Swift parameter packs are a powerful tool to expand what is possible in your generic code while also enabling you to simplify common generic patterns. We’ll show you how to abstract over types as well as the number of arguments in generic code and simplify common generic patterns to avoid overloads. To get the most out of this session, we recommend first checking out “Embrace Swift generics" from WWDC22.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,797 words)

## Code Snippets

### radians function — [1:13]

```swift
func radians(from degrees: Double) -> Double
```

### Array type — [1:26]

```swift
struct Array<Element>
```

### radians function and Array type with concrete expressions — [1:48]

```swift
func radians(from degrees: Double) -> Double
radians(from: 180)

struct Array<Element>
Array<Int>
```

### generic query — [2:04]

```swift
func query<Payload>(_ item: Request<Payload>) -> Payload
```

### variadic query — [2:22]

```swift
func query(_ item: Request...)
```

### generic query — [3:16]

```swift
func query<Payload>(_ item: Request<Payload>) -> Payload
```

### two query overloads — [3:23]

```swift
func query<Payload>(
    _ item: Request<Payload>
) -> Payload

func query<Payload1, Payload2>(
    _ item1: Request<Payload1>,
    _ item2: Request<Payload2>
) -> (Payload1, Payload2)
```

### three query overloads — [3:28]

```swift
func query<Payload>(
    _ item: Request<Payload>
) -> Payload

func query<Payload1, Payload2>(
    _ item1: Request<Payload1>,
    _ item2: Request<Payload2>
) -> (Payload1, Payload2)

func query<Payload1, Payload2, Payload3>(
    _ item1: Request<Payload1>,
    _ item2: Request<Payload2>,
    _ item3: Request<Payload3>
) -> (Payload1, Payload2, Payload3)
```

### four query overloads with extra argument error — [3:31]

```swift
func query<Payload>(
    _ item: Request<Payload>
) -> Payload

func query<Payload1, Payload2>(
    _ item1: Request<Payload1>,
    _ item2: Request<Payload2>
) -> (Payload1, Payload2)

func query<Payload1, Payload2, Payload3>(
    _ item1: Request<Payload1>,
    _ item2: Request<Payload2>,
    _ item3: Request<Payload3>
) -> (Payload1, Payload2, Payload3)

func query<Payload1, Payload2, Payload3, Payload4>(
    _ item1: Request<Payload1>,
    _ item2: Request<Payload2>,
    _ item3: Request<Payload3>,
    _ item4: Request<Payload4>
) -> (Payload1, Payload2, Payload3, Payload4)

let _ = query(r1, r2, r3, r4, r5)
```

### for-in loop over requests — [5:52]

```swift
for request in requests {
    evaluate(request)
}
```

### four query overloads — [8:41]

```swift
func query<Payload>(
    _ item: Request<Payload>
) -> Payload

func query<Payload1, Payload2>(
    _ item1: Request<Payload1>,
    _ item2: Request<Payload2>
) -> (Payload1, Payload2)

func query<Payload1, Payload2, Payload3>(
    _ item1: Request<Payload1>,
    _ item2: Request<Payload2>,
    _ item3: Request<Payload3>
) -> (Payload1, Payload2, Payload3)

func query<Payload1, Payload2, Payload3, Payload4>(
    _ item1: Request<Payload1>,
    _ item2: Request<Payload2>,
    _ item3: Request<Payload3>,
    _ item4: Request<Payload4>
) -> (Payload1, Payload2, Payload3, Payload4)
```

### parameter pack query interface — [9:37]

```swift
func query<each Payload>(_ item: repeat Request<each Payload>) -> (repeat each Payload)
```

### parameter pack query with single argument call — [10:01]

```swift
func query<each Payload>(_ item: repeat Request<each Payload>) -> (repeat each Payload)

let result = query(Request<Int>())
```

### parameter pack query with single and triple argument calls — [10:08]

```swift
func query<each Payload>(_ item: repeat Request<each Payload>) -> (repeat each Payload)

let result = query(Request<Int>())

let results = query(Request<Int>(), Request<String>(), Request<Bool>())
```

### parameter pack query with triple argument call — [10:15]

```swift
func query<each Payload>(_ item: repeat Request<each Payload>) -> (repeat each Payload)

let results = query(Request<Int>(), Request<String>(), Request<Bool>())
```

### parameter pack query interface — [10:56]

```swift
func query<each Payload>(
    _ item: repeat Request<each Payload>
) -> (repeat each Payload)
```

### parameter pack query interface with conformance — [11:03]

```swift
func query<each Payload: Equatable>(
  _ item: repeat Request<each Payload>
) -> (repeat each Payload)
```

### parameter pack query interface with where clause — [11:17]

```swift
func query<each Payload>(
    _ item: repeat Request<each Payload>
) -> (repeat each Payload)
    where repeat each Payload: Equatable
```

### parameter pack query interface with minimum parameter count — [11:44]

```swift
func query<FirstPayload, each Payload>(
    _ first: Request<FirstPayload>, _ item: repeat Request<each Payload>
) -> (FirstPayload, repeat each Payload) 
    where FirstPayload: Equatable, repeat each Payload: Equatable
```

### parameter pack query implementation — [13:42]

```swift
struct Request<Payload> {
    func evaluate() -> Payload
}

func query<each Payload>(_ item: repeat Request<each Payload>) -> (repeat each Payload) {
    return (repeat (each item).evaluate())
}
```

### parameter pack query implementation with different input and output types — [16:04]

```swift
protocol RequestProtocol {
    associatedtype Input
    associatedtype Output
    func evaluate(_ input: Input) -> Output
}

struct Evaluator<each Request: RequestProtocol> {
    var item: (repeat each Request)

    func query(_ input: repeat (each Request).Input) -> (repeat (each Request).Output) {
        return (repeat (each item).evaluate(each input))
    }
}
```

### parameter pack query implementation with control flow break — [17:05]

```swift
protocol RequestProtocol {
    associatedtype Input
    associatedtype Output
    func evaluate(_ input: Input) throws -> Output
}

struct Evaluator<each Request: RequestProtocol> {
    var item: (repeat each Request)

    func query(_ input: repeat (each Request).Input) -> (repeat (each Request).Output)? {
        do {
            return (repeat try (each item).evaluate(each input))
        } catch {
            return nil
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10168/4/C4DB8728-EFE7-49D9-B61E-3061B8F31EF5/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10168/4/C4DB8728-EFE7-49D9-B61E-3061B8F31EF5/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10168) — developer.apple.com. Indexed for agent consumption._
