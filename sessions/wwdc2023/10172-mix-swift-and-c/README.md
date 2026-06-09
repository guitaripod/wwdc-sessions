---
id: "wwdc2023-10172"
event: "wwdc2023"
year: 2023
title: "Mix Swift and C++"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10172"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Mix Swift and C++

**Event:** WWDC23 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2023-06-07 · **Session:** [wwdc2023-10172](https://developer.apple.com/videos/play/wwdc2023/10172)

Learn how you can use Swift in your C++ and Objective-C++ projects to make your code safer, faster, and easier to develop. We’ll show you how to use C++ and Swift APIs to incrementally incorporate Swift into your app.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,396 words)

## Documentation & Resources

- [Mixing Swift and C++](https://swift.org/documentation/cxx-interop) _documentation_
- [Calling APIs Across Language Boundaries](https://developer.apple.com/documentation/Swift/CallingAPIsAcrossLanguageBoundaries) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/CallingAPIsAcrossLanguageBoundaries
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/CallingAPIsAcrossLanguageBoundaries.json
- [Mixing Languages in an Xcode project](https://developer.apple.com/documentation/Swift/MixingLanguagesInAnXcodeProject) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/MixingLanguagesInAnXcodeProject
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/MixingLanguagesInAnXcodeProject.json

## Code Snippets

### Calling a C++ method from Swift — [4:10]

```swift
func loadImage(_ image: UIImage) {
    // Load an image into the shared C++ class.
    CxxImageEngine.shared.pointee.loadImage(image)
}
```

### Import a C++ framework — [4:20]

```swift
import CxxImageKit
```

### Import the Generated Header — [4:45]

```swift
#import "SampleApp-Swift.h"
```

### Calling a Swift method in C++ — [4:57]

```swift
- (IBAction)openPhotoLibrary:(UIButton *)sender {
    // Construct SwiftUI view
    SampleApp::ImagePicker::init().present(self);
}
```

### Using the SWIFT_COMPUTED_PROPERTY attribute — [8:22]

```cpp
int  getValue() const SWIFT_COMPUTED_PROPERTY;
void setValue(int newValue);
```

### Using the SWIFT_SHARED_REFERENCE attribute — [8:42]

```cpp
struct SWIFT_SHARED_REFERENCE(retain, release) CxxReferenceType;
```

### Using the SWIFT_RETURNS_INDEPENDENT_VALUE attribute — [8:52]

```cpp
SWIFT_RETURNS_INDEPENDENT_VALUE 
std::string_view networkName() const;
```

### Using a for-loop to iterate over a C++ std::vector in Swift — [10:45]

```swift
// Get every image out of the shared C++ class.
for image in CxxImageEngine.shared.pointee.getImages() {
    let uiImage = CxxImageEngine.shared.pointee.uiImageFrom(image)
    UIImageWriteToSavedPhotosAlbum(uiImage, nil, nil, nil)
}
```

### Import swift/bridging — [13:54]

```cpp
#import <swift/bridging>
```

### Applying the SWIFT_SHARED_REFERENCE attribute to CxxImageEngine — [14:01]

```cpp
struct SWIFT_SHARED_REFERENCE(IKRetain, IKRelease) CxxImageEngine {
    // ...
};
```

### Applying the SWIFT_COMPUTED_PROPERTY attribute to getImages — [14:53]

```cpp
/// \returns all images that have been loaded into the engine. Includes any modifications that were
/// applied to the images.
SWIFT_COMPUTED_PROPERTY
inline std::vector<Image *_Nonnull> getImages() const;
```

### Updated for-loop using the "images" computed property — [15:06]

```swift
// Get every image out of the shared C++ class.
for image in CxxImageEngine.shared.pointee.images {
    let uiImage = CxxImageEngine.shared.pointee.uiImageFrom(image)
    UIImageWriteToSavedPhotosAlbum(uiImage, nil, nil, nil)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10172/4/58243B95-F51E-4E6A-96C8-B85E8102E450/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10172/4/58243B95-F51E-4E6A-96C8-B85E8102E450/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10172) — developer.apple.com. Indexed for agent consumption._
