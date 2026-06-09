---
id: "wwdc2020-10669"
event: "wwdc2020"
year: 2020
title: "Handling FHIR without getting burned"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10669"
topics: ["Health & Fitness"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# Handling FHIR without getting burned

**Event:** WWDC20 · **Topic:** Health & Fitness · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10669](https://developer.apple.com/videos/play/wwdc2020/10669)

Learn how FHIRModels creates native data models for all FHIR resources, provides data validation to enforce resource integrity, and prevents the creation of structurally invalid resources — across multiple versions of the FHIR specification. Whether you're working with clinical data obtained from HealthKit or direct from a clinical system, FHIRModels makes FHIR easy to handle.

**Keywords:** `fhir`, `health`, `health documents`, `medical records`, `open source`, `package`, `spm`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,088 words)

## Documentation & Resources

- [Accessing a User’s Clinical Records](https://developer.apple.com/documentation/HealthKit/accessing-a-user-s-clinical-records) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/HealthKit/accessing-a-user-s-clinical-records
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/HealthKit/accessing-a-user-s-clinical-records.json
- [FHIRModels Swift Package on GitHub](https://github.com/apple/FHIRModels) _documentation_

## Code Snippets

### Use FHIRModels with Health Records FHIR data from HealthKit — [4:32]

```swift
// Use with Health Records FHIR data from HealthKit
import HealthKit
import ModelsDSTU2

// Grab HKClinicalRecord from HealthKit API
let clinicalRecord: HKClinicalRecord
let resource = clinicalRecord.fhirResource!

// Print the prescription note
let decoder = JSONDecoder()
let prescription = try decoder.decode(MedicationOrder.self, from: resource.data)
print("\(prescription.note)")
```

### Use FHIRModels with Health Records FHIR data from HealthKit, part 2 — [5:04]

```swift
// Make using "TimingRepeat" period dates easier by writing an extension
extension TimingRepeat {
    var periodDisplayString: String? {
        if case .period(let period) = bounds {
            return "\(period.start) - \(period.end)"
        }
        return nil
    }
}

// Collect all dosage instructions on medication prescriptions
let instructions: [String] = prescription.dosageInstruction?.map { dosage in
    guard let period = dosage.timing?.repeat?.periodDisplayString else {
        return "\(dosage.text)"
    }
    return "\(period): \(dosage.text)"
}
```

### Supporting multiple FHIR releases — [6:20]

```swift
// Supporting multiple releases
import ModelsDSTU2
import ModelsR4

let decoder = JSONDecoder()
let release: FHIRRelease
let data: Data

let note: String? = nil
switch release {
case .dstu2:
    let model = try decoder.decode(ModelsDSTU2.MedicationOrder.self, from: data)
    note = model.note?.value?.string
case .r4:
    let model = try decoder.decode(ModelsR4.MedicationRequest.self, from: data)
    note = model.note?.compactMap({ $0.text.value?.string }).joined(separator: "\n")
default:
    note = "Unsupported FHIR release \(release)"
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10669/4/63009C98-F22F-4CFE-9037-5DCC0A37017F/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10669) — developer.apple.com. Indexed for agent consumption._
