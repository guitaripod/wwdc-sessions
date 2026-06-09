---
id: "wwdc2020-10652"
event: "wwdc2020"
year: 2020
title: "Meet the new Photos picker"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10652"
topics: ["Privacy & Security", "SwiftUI & UI Frameworks", "Photos & Camera"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Meet the new Photos picker

**Event:** WWDC20 · **Topic:** Photos & Camera · **Platforms:** iOS, iPadOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10652](https://developer.apple.com/videos/play/wwdc2020/10652)

Let people select photos and videos to use in your app without requiring full Photo Library access. Discover how the PHPicker API for iOS and Mac Catalyst ensures privacy while providing your app the features you need.

PHPicker is the modern replacement for UIImagePickerController. In addition to its privacy-focused approach, the API also provides additional features for your app like search, multi-image selection, and the ability to zoom in or out on on the photo grid. We’ll show you how PHPicker can help most apps avoid asking for direct library access and how you can implement it to improve the overall experience for people interacting with your app.

**Keywords:** `photokit`, `photo library`, `photos`, `photos api`, `picker`, `privacy`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,961 words)

## Documentation & Resources

- [Selecting Photos and Videos in iOS](https://developer.apple.com/documentation/PhotoKit/selecting-photos-and-videos-in-ios) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/PhotoKit/selecting-photos-and-videos-in-ios
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/PhotoKit/selecting-photos-and-videos-in-ios.json
- [PhotoKit](https://developer.apple.com/documentation/photokit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/photokit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/photokit.json

## Code Snippets

### PHPickerConfiguration — [2:27]

```swift
import PhotosUI

var configuration = PHPickerConfiguration()

// “unlimited” selection by specifying 0, default is 1
configuration.selectionLimit = 0

// Only show images (including Live Photos)
configuration.filter = .images
// Uncomment next line for other example: Only show videos or Live Photos (for their video complement), but no images
// configuration.filter = .any(of: [.videos, .livePhotos])
```

### PHPickerViewController — [3:07]

```swift
import UIKit
import PhotosUI

class SingleSelectionPickerViewController: UIViewController, PHPickerViewControllerDelegate {
    @IBAction func presentPicker(_ sender: Any) {
        var configuration = PHPickerConfiguration()
        // Only wants images
        configuration.filter = .images

        let picker = PHPickerViewController(configuration: configuration)
        picker.delegate = self

        // The client is responsible for presentation and dismissal
        present(picker, animated: true)
    }

    func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
        // The client is responsible for presentation and dismissal
        picker.dismiss(animated: true)

        // Get the first item provider from the results, the configuration only allowed one image to be selected
        let itemProvider = results.first?.itemProvider

        if let itemProvider = itemProvider, itemProvider.canLoadObject(ofClass: UIImage.self) {
            itemProvider.loadObject(ofClass: UIImage.self) { (image, error) in
                // TODO: Do something with the image or handle the error
            }
        } else {
            // TODO: Handle empty results or item provider not being able load UIImage
        }
    }
}
```

### Demo - Single Selection — [5:19]

```swift
import UIKit
import PhotosUI

class ViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!

    @IBAction func presentPicker(_ sender: Any) {
        var configuration = PHPickerConfiguration()
        configuration.filter = .images

        let picker = PHPickerViewController(configuration: configuration)
        picker.delegate = self
        present(picker, animated: true)
    }

}

extension ViewController: PHPickerViewControllerDelegate {

    func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
        dismiss(animated: true)

        if let itemProvider = results.first?.itemProvider, itemProvider.canLoadObject(ofClass: UIImage.self) {
            let previousImage = imageView.image
            itemProvider.loadObject(ofClass: UIImage.self) { [weak self] image, error in
                DispatchQueue.main.async {
                    guard let self = self, let image = image as? UIImage, self.imageView.image == previousImage else { return }
                    self.imageView.image = image
                }
            }
        }
    }

}
```

### Demo - Multiple Selection — [7:34]

```swift
import UIKit
import PhotosUI

class ViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!

    var itemProviders: [NSItemProvider] = []
    var iterator: IndexingIterator<[NSItemProvider]>?

    @IBAction func presentPicker(_ sender: Any) {
        var configuration = PHPickerConfiguration()
        configuration.filter = .images
        configuration.selectionLimit = 0

        let picker = PHPickerViewController(configuration: configuration)
        picker.delegate = self
        present(picker, animated: true)
    }

    func displayNextImage() {
        if let itemProvider = iterator?.next(), itemProvider.canLoadObject(ofClass: UIImage.self) {
            let previousImage = imageView.image
            itemProvider.loadObject(ofClass: UIImage.self) { [weak self] image, error in
                DispatchQueue.main.async {
                    guard let self = self, let image = image as? UIImage, self.imageView.image == previousImage else { return }
                    self.imageView.image = image
                }
            }
        }
    }

    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        displayNextImage()
    }

}

extension ViewController: PHPickerViewControllerDelegate {

    func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
        dismiss(animated: true)

        itemProviders = results.map(\.itemProvider)
        iterator = itemProviders.makeIterator()
        displayNextImage()
    }

}
```

### Using PHPicker with PhotoKit — [11:13]

```swift
import UIKit
import PhotosUI

class PhotoKitPickerViewController: UIViewController, PHPickerViewControllerDelegate {
    @IBAction func presentPicker(_ sender: Any) {
        let photoLibrary = PHPhotoLibrary.shared()
        let configuration = PHPickerConfiguration(photoLibrary: photoLibrary)
        let picker = PHPickerViewController(configuration: configuration)
        picker.delegate = self
        present(picker, animated: true)
    }

    func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
        picker.dismiss(animated: true)

        let identifiers = results.compactMap(\.assetIdentifier)
        let fetchResult = PHAsset.fetchAssets(withLocalIdentifiers: identifiers, options: nil)

        // TODO: Do something with the fetch result if you have Photos Library access
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10652/3/8660B6AC-4DDE-46E6-830D-1449B090978C/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10652) — developer.apple.com. Indexed for agent consumption._