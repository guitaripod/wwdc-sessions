---
id: "wwdc2025-311"
event: "wwdc2025"
year: 2025
title: "Safely mix C, C++, and Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/311"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Safely mix C, C++, and Swift

**Event:** WWDC25 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-311](https://developer.apple.com/videos/play/wwdc2025/311)

Learn how to mix C, C++, and Swift while improving the safety of your apps. We’ll show you how to find where unsafe C and C++ APIs are called in your Swift code, how to call them more safely, and how to make your app’s existing C and C++ code safer by default.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,787 words)

## Documentation & Resources

- [Safely Mixing Swift and C++](https://www.swift.org/documentation/cxx-interop/safe-interop/) _documentation_
- [-fbounds-safety: Enforcing bounds safety for C](https://clang.llvm.org/docs/BoundsSafety.html) _documentation_

## Code Snippets

### Unsafety can be subtle — [3:19]

```swift
// Swift
var imageData = [UInt8](repeating: 0, count: imageDataSize)
filterImage(&imageData, imageData.count)
```

### Strict memory safety — [4:01]

```swift
// Swift
var imageData = [UInt8](repeating: 0, count: imageDataSize)
filterImage(&imageData, imageData.count)
//warning: Expression uses unsafe constructs but is not marked with 'unsafe'
```

### Raw pointers don't prevent out-of-bounds errors — [8:00]

```cpp
// C/C++
void invertImage(uint8_t *imagePtr, size_t imageSize);
```

### Raw pointers don't prevent out-of-bounds errors — [8:21]

```swift
// Swift
var imageData = [UInt8](repeating: 0, count: imageSize)
invertImage(&imageData, imageSize)
```

### Raw pointers don't prevent out-of-bounds errors — [8:30]

```swift
// Swift
var imageData = [UInt8](repeating: 0, count: imageSize)
invertImage(&imageData, 1000000000000)
```

### Solution for out-of-bounds error — [8:48]

```swift
// Swift
func invertImage(_ imagePtr : inout MutableSpan<UInt8>)
```

### Solution for out-of-bounds error — [8:54]

```swift
// Swift
var imageDataSpan = imageData.mutableSpan
invertImage(&imageDataSpan)
```

### Express bounds information using __counted_by — [9:58]

```cpp
// C/C++
void invertImage(uint8_t *__counted_by(imageSize) imagePtr __noescape, size_t imageSize);
```

### Unsafe function declaration taking a C++ span — [12:10]

```cpp
// C++
using CxxSpanOfByte = std::span<uint8_t>;
void applyGrayscale(CxxSpanOfByte imageView);
```

### Unsafe C++ function caching a C++ span — [13:21]

```cpp
// C++
CxxSpanOfByte cachedView;
void applyGrayscale(CxxSpanOfByte imageView) {
  cachedView = imageView;
  // Apply effect on image ...
}
```

### Swift Span prevents escaping scope — [14:08]

```swift
// Swift
var cachedView: MutableSpan<UInt8>?
func applyGrayscale(_ imageView: inout MutableSpan<UInt8>) {
  cachedView = imageView // error: lifetime dependent value escapes its scope
  // Apply effect on image ...
}
```

### Express lifetime information using __noescape — [15:18]

```cpp
// C++
CxxSpanOfByte cachedView;
void applyGrayscale(CxxSpanOfByte imageView __noescape) {
  // Apply effect on image ...
}
```

### Safely use a C++ Span as a Swift Span — [15:56]

```swift
// Swift
var imageDataSpan = &imageData.mutableSpan
applyGrayscale(&imageDataSpan)
```

### Returned C++ Span is unsafe — [17:21]

```cpp
// C++
CxxSpanOfByte scanImageRow(CxxSpanOfByte imageView,
                           size_t width, size_t rowIndex);
```

### Swift Spans prevent use-after-free by design — [18:06]

```swift
// Swift
func scanImageRow(_ imageView : inout MutableSpan<UInt8>,
                  _ width : Int, _ rowIndex : Int) -> MutableSpan<UInt8>
// error: a function with a ~Escapable result requires '@lifetime(...)'
```

### Express lifetime dependency with __lifetimebound — [18:47]

```cpp
// C++
CxxSpanOfByte scanImageRow(CxxSpanOfByte imageView __lifetimebound,
                           size_t width, size_t rowIndex);
```

### Safely return a C++ Span as a Swift Span — [18:50]

```swift
// Swift
var imageDataSpan = imageData.mutableSpan
var rowView = scanImageRow(&imageDataSpan, width, y)
```

### Import a C++ view type as SWIFT_NONESCAPABLE — [22:29]

```cpp
// C++
struct ImageView {
  std::span<uint8_t> pixelBytes;
  int width;
  int height;
} SWIFT_NONESCAPABLE;
```

### Import a C++ reference-counted type — [23:31]

```cpp
// C++
struct ImageBuffer {
  std::vector<uint8_t> data;
  int width;
  int height;
  std::atomic<unsigned> refCount;
} SWIFT_SHARED_REFERENCE(retain_image_buffer, release_image_buffer);

void retain_image_buffer(ImageBuffer *_Nonnull buf);
void release_image_buffer(ImageBuffer *_Nonnull buf);
```

### Safely return a reference-counted type — [23:57]

```cpp
// C++
ImageBuffer *_Nonnull createImage() SWIFT_RETURNS_RETAINED;
ImageBuffer *_Nonnull getCachedImage() SWIFT_RETURNS_UNRETAINED;
```

### C++ standard library hardening — [27:51]

```cpp
// C++
void fill_array_with_indices(std::span<uint8_t> buffer) {
  for (size_t i = 0; i < buffer.size(); ++i) {
    buffer[i] = i;
  }
}
```

### C++ unsafe buffer usage errors — [28:59]

```cpp
// C++
void fill_array_with_indices(uint8_t *buffer, size_t count) {
  for (size_t i = 0; i < count; ++i) {
    buffer[i] = i; // error: unsafe buffer access
  }
}
```

### Bounds safety extension for C — [30:11]

```cpp
// C
void fill_array_with_indices(uint8_t *__counted_by(count) buf, size_t count) {
  for (size_t i = 0; i < count; ++i) {
    buf[i] = i;
  }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/311/4/10e5709a-8f4f-488a-92f6-f551b4ce97c5/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/311/4/10e5709a-8f4f-488a-92f6-f551b4ce97c5/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/311) — developer.apple.com. Indexed for agent consumption._
