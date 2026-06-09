---
id: "wwdc2025-272"
event: "wwdc2025"
year: 2025
title: "Read documents using the Vision framework"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/272"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Read documents using the Vision framework

**Event:** WWDC25 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-272](https://developer.apple.com/videos/play/wwdc2025/272)

Learn about the latest advancements in the Vision framework. We’ll introduce RecognizeDocumentsRequest, and how you can use it to read lines of text and group them into paragraphs, read tables, etc. And we’ll also dive into camera lens smudge detection, and how to identify potentially smudged images in photo libraries or your own camera capture pipeline.

**Keywords:** `machine learning &amp; vision`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,285 words)

## Documentation & Resources

- [Recognizing tables within a document](https://developer.apple.com/documentation/Vision/recognize-tables-within-a-document) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Vision/recognize-tables-within-a-document
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Vision/recognize-tables-within-a-document.json
- [Classifying Images with Vision and Core ML](https://developer.apple.com/documentation/CoreML/classifying-images-with-vision-and-core-ml) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CoreML/classifying-images-with-vision-and-core-ml
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CoreML/classifying-images-with-vision-and-core-ml.json
- [Image Classification with Vision and CoreML](https://developer.apple.com/sample-code/wwdc/2017/ImageClassificationwithVisionandCoreML.zip) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/sample-code/wwdc/2017/ImageClassificationwithVisionandCoreML.zip
- [Vision](https://developer.apple.com/documentation/Vision) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Vision
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Vision.json

## Code Snippets

### Detect tables — [6:39]

```swift
/// Process an image and return the first table detected
func extractTable(from image: Data) async throws -> DocumentObservation.Container.Table {

    // The Vision request.
    let request = RecognizeDocumentsRequest()

    // Perform the request on the image data and return the results.
    let observations = try await request.perform(on: image)

    // Get the first observation from the array.
    guard let document = observations.first?.document else {
        throw AppError.noDocument
    }

    // Extract the first table detected.
    guard let table = document.tables.first else {
        throw AppError.noTable
    }

    return table
}
```

### Parse contacts — [10:50]

```swift
/// Extract name, email addresses, and phone number from a table into a list of contacts.
private func parseTable(_ table: DocumentObservation.Container.Table) -> [Contact] {
    var contacts = [Contact]()

    // Iterate over each row in the table.
    for row in table.rows {
        // The contact name will be taken from the first column.
        guard let firstCell = row.first else {
            continue
        }
        // Extract the text content from the transcript.
        let name = firstCell.content.text.transcript

        // Look for emails and phone numbers in the remaining cells.
        var detectedPhone: String? = nil
        var detectedEmail: String? = nil

        for cell in row.dropFirst() {
            // Get all detected data in the cell, then match emails and phone numbers.
            let allDetectedData = cell.content.text.detectedData
            for data in allDetectedData {
                switch data.match.details {
                case .emailAddress(let email):
                    detectedEmail = email.emailAddress
                case .phoneNumber(let phoneNumber):
                    detectedPhone = phoneNumber.phoneNumber
                default:
                    break
                }
            }
        }
        // Create a contact if an email was detected.
        if let email = detectedEmail {
            let contact = Contact(name: name, email: email, phoneNumber: detectedPhone)
            contacts.append(contact)
        }
    }
    return contacts
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/272/4/4e80b3e0-9c62-4150-84e9-6b051c14dfa9/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/272/4/4e80b3e0-9c62-4150-84e9-6b051c14dfa9/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/272) — developer.apple.com. Indexed for agent consumption._
