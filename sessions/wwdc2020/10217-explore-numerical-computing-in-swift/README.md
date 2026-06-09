---
id: "wwdc2020-10217"
event: "wwdc2020"
year: 2020
title: "Explore numerical computing in Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10217"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Explore numerical computing in Swift

**Event:** WWDC20 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10217](https://developer.apple.com/videos/play/wwdc2020/10217)

Meet Swift Numerics: a new Swift package for computational mathematics. Take a tour of the protocols and types available in the package and find out how you can use them to write generic code. We'll also show you how and when to use the new Float16 type to improve performance and reduce memory usage. To get the most out of this session, you should have some familiarity with mathematics like logarithmic functions and real and imaginary numbers. You should also be familiar with generic programming in Swift. For more background, watch “Swift Generics (Expanded)” from WWDC18.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,309 words)

## Documentation & Resources

- [Float16](https://developer.apple.com/documentation/Swift/Float16) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/Float16
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/Float16.json
- [Swift Numerics on GitHub](https://github.com/apple/swift-numerics) _documentation_
- [Numeric Protocols](https://developer.apple.com/documentation/Swift/numeric-protocols) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/numeric-protocols
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/numeric-protocols.json

## Code Snippets

### The log-odds function (Double) — [1:05]

```swift
import Darwin

/// The log-odds function
///
/// https://en.wikipedia.org/wiki/Logit
///
/// - Parameter p:
///   A probability in the range 0...1.
///
/// - Returns:
///   The log of the odds, 'log(p/(1-p))'.
func logit(_ p: Double) -> Double {
    log(p) - log1p(-p)
}
```

### The log-odds function (Real) — [2:33]

```swift
import Numerics

/// The log-odds function
///
/// https://en.wikipedia.org/wiki/Logit
///
/// - Parameter p:
///   A probability in the range 0...1.
///
/// - Returns:
///   The log of the odds, 'log(p/(1-p))'.
func logit<NumberType: Real>(_ p: NumberType) -> NumberType {
    .log(p) - .log(onePlus: -p)
}
```

### The Complex type — [7:10]

```swift
import Numerics

let z = Complex(1.0, 2.0) // z = 1 + 2 i
```

### The Complex type: Basic definition — [7:38]

```swift
public struct Complex<NumberType> where NumberType: Real {
    /// The real component
    public var real: NumberType

    /// The imaginary component
    public var imaginary: NumberType

    /// Construct a complex number with specified real and imaginary parts
    public init(_ real: NumberType, _ imaginary: NumberType) {
        self.real = real
        self.imaginary = imaginary
    }
}
```

### The Complex type: Standard arithmetic operations — [8:04]

```swift
extension Complex: SignedNumeric {
    /// The sum of 'z' and 'w'
    public static func +(z: Complex, w: Complex) -> Complex {
        return Complex(z.real + w.real, z.imaginary + w.imaginary)
    }

    /// The difference of 'z' and 'w'
    public static func -(z: Complex, w: Complex) -> Complex {
        return Complex(z.real - w.real, z.imaginary - w.imaginary)
    }

    /// The product of 'z' and 'w'
    public static func *(z: Complex, w: Complex) -> Complex {
        return Complex(z.real * w.real - z.imaginary * w.imaginary,
                       z.real * w.imaginary + z.imaginary * w.real)
    }
}
```

### The Complex type: Polar coordinates — [8:19]

```swift
extension Complex {
    /// The Euclidean norm (a.k.a. 2-norm) of the number.
    public var length: NumberType {
        return .hypot(real, imaginary)
    }

    /// The phase (angle, or "argument").
    ///
    /// Returns the angle (measured above the real axis) in radians.
    public var phase: NumberType {
        return .atan2(y: imaginary, x: real)
    }

    /// A complex value with specified polar coordinates.
    public init(length: NumberType, phase: NumberType) {
        self = Complex(.cos(phase), .sin(phase)).multiplied(by: length)
    }
}
```

### Using Accelerate's Basic Linear Algebra Subroutines — [9:16]

```swift
import Numerics
import Accelerate

/// Array of 100 random Complex<Double> numbers
let z = (0 ..< 100).map {
    Complex(length: 1.0, phase: Double.random(in: -.pi ... .pi))
}

/// Compute the Euclidean norm of z
let norm = cblas_dznrm2(z.count, &z, 1)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10217/6/608C3CB1-C8BD-4B19-B5F3-5ADA44E200E3/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10217) — developer.apple.com. Indexed for agent consumption._
