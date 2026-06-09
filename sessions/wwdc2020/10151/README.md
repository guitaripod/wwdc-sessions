---
id: "wwdc2020-10151"
event: "wwdc2020"
year: 2020
title: "What's new in CareKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10151"
topics: ["Health & Fitness"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# What's new in CareKit

**Event:** WWDC20 · **Topic:** Health & Fitness · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10151](https://developer.apple.com/videos/play/wwdc2020/10151)

Build feature-rich research and care apps with CareKit: Learn about the latest advancements to our health framework, including new views for its modular architecture, improvements to the data store, and tighter integration with other frameworks on iOS. And discover how the open-source community continues to leverage CareKit to allow developers to push the boundaries of digital health&nbsp;—&nbsp;all while preserving privacy.

**Keywords:** `care`, `care plan`, `client server`, `healthkit`, `health monitoring`, `hyperprotect`, `open source`, `synchronize`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,739 words)

## Documentation & Resources

- [Research and Care Website](https://www.researchandcare.org) _documentation_
- [CareKit Repository](https://github.com/carekit-apple/CareKit) _guide_

## Code Snippets

### Simple Task View — [2:23]

```swift
import CareKitUI
import SwiftUI

struct MySimpleTaskView: View {

    var body: some View {
        SimpleTaskView(
            title: Text("Stretches"),
            detail: Text("15 minutes"),
            isComplete: false)
    }
}
```

### Simple Task View - View Modifiers — [2:52]

```swift
import CareKitUI
import SwiftUI

struct MySimpleTaskView: View {

    var body: some View {
        SimpleTaskView(
            title: Text("Stretches").fontWeight(.thin),
            detail: Text("15 minutes"),
            isComplete: false)
    }
}
```

### Simple Task View - Custom Header — [3:42]

```swift
struct MySimpleTaskView: View {

    var body: some View {
        SimpleTaskView(isComplete: false) {                
            HStack {
                RoundedRectangle(cornerRadius: 5)
                    .fill(Color.accentColor)
                    .frame(width: 5)         
                HeaderView(
                    title: Text("Stretches"),
                    detail: Text("15 minutes"))
            }
            .padding()
        }
    }
}
```

### Simple Task View - Appending Views — [4:29]

```swift
import CareKitUI
import SwiftUI

struct MyComposedSimpleTaskView: View {

    var body: some View {
        CardView {
            VStack(alignment: .leading) {
								MySimpleTaskView()
                Divider()
                Text("...")
                    .font(.caption)
                    .foregroundColor(.secondary)    
            }.padding()
        }        
    }
}
```

### Labeled Value Task View — [5:24]

```swift
import CareKitUI
import SwiftUI

struct MyLabeledValueTaskView: View {

    var body: some View {
        LabeledValueTaskView(
            title: Text("Heart Rate"),
            detail: Text("Most recent measurement")
            state: .complete(
                Text("62"),
                Text("BPM")
            ))
    }
}
```

### Numeric Progress Task View — [5:57]

```swift
import CareKitUI
import SwiftUI

struct MyNumericProgressView: View {

    var body: some View {
        NumericProgressTaskView(
            title: Text("Exercise Minutes"),
            detail: Text("Anytime"),
            instructions: Text("..."),
            progress: Text("22"),
            goal: Text("30"),
            isComplete: false)
    }
}
```

### Featured Content View — [6:28]

```swift
import CareKitUI
import UIKit

let featureView = OCKFeaturedContentView()

featureView.imageView.image = UIImage(named: "groceries")
featureView.label.text = "Easy & Healthy Recipes"
```

### Detail View — [6:58]

```swift
import CareKitUI
import UIKit

let styledHTML = OCKDetailView.StyledHTML(
  html: html, 
  css: css)

let detailView = OCKDetailView(
  html: styledHTML, 
  showsCloseButton: true)

detailView.imageView.image = UIImage(named: "groceries")
```

### Link View — [7:41]

```swift
import CareKitUI
import SwiftUI

struct MyLinkView: View {

    var body: some View {
        LinkView(
            title: Text("Physical Therapist Appointment"),
            instructions: Text("..."),
            links: [
                // ...
                .website(
                    "https://www.apple.com", 
                    title: "Website")
                // ...
        ])
    }       
}
```

### Synchronized Task View 1 — [8:56]

```swift
// Synchronized Task View

import CareKit
import CareKitUI
import SwiftUI

struct MySynchronizedTaskView: View {

    let storeManager: OCKSynchronizedStoreManager

    var body: some View {
        CareKit.SimpleTaskView(
            taskID: "stretch",
            eventQuery: OCKEventQuery(for: Date()),
            storeManager: storeManager)

    }
}
```

### Synchronized Task View 2 — [9:26]

```swift
@State private var isShowingSurvey = false

var body: some View {
    CareKit.SimpleTaskView(
        taskID: "researchKitSurveyTask",
        eventQuery: OCKEventQuery(for: Date()),
        storeManager: storeManager) { controller in

            CareKitUI.SimpleTaskView(
                title: Text(controller.viewModel?.title ?? ""),
                detail: controller.viewModel?.detail.map(Text.init),
                isComplete: controller.viewModel?.isComplete ?? false) {
                    isShowingSurvey = true
                }
        }  
        .popover(isPresented: $isShowingSurvey) {
            ResearchKitSurvey()
        }
}
```

### Setting up the store — [13:43]

```swift
// Setting up the Store

import CareKit
import CareKitStore

let coreDataStore = OCKStore(name: "core-data-store")
let healthKitPassthroughStore = OCKHealthKitPassthroughStore(name: "hk-passthrough—store")

let coordinator = OCKStoreCoordinator()
coordinator.attach(store: coreDataStore)
coordinator.attach(eventStore: healthKitPassthroughStore)

let storeManager = OCKSynchronizedStoreManager(wrapping: coordinator)
```

### Adding HealthKit linked tasks to the store — [14:15]

```swift
// Adding HealthKit Linked Tasks to the Store

let schedule = OCKSchedule.dailyAtTime(
    hour: 8,
    minutes: 0, 
    start: Date(),
    end: nil,
    text: nil, 
    duration: .allDay, 
    targetValues: [OCKOutcomeValue(30.0, units: "Minutes")])

let link = OCKHealthKitLinkage(
    quantityIdentifier: .appleExerciseTime, 
    quantityType: .cumulative,
    unit: .minute())

let steps = OCKHealthKitTask(
    id: "exerciseMinutes",
    title: "Exercise Minutes",
    carePlanUUID: nil,
    schedule: schedule,
    healthKitLinkage: link)

storeManager.store.addAnyTask(steps)
```

### Encoding and decoding FHIR data — [16:57]

```swift
// Encoding and Decoding FHIR Data

import CareKitStore
import CareKitFHIR

let coder = OCKR4PatientCoder()

// CareKit entity to FHIR data
let patient = OCKPatient(...)
let json = try! coder.encode(patient)

// FHIR data to CareKit entity
let data: Data = //... 
let resourceData = OCKFHIRResourceData<R4, JSON>(data: data)
let patient: OCKPatient = try! coder.decode(resourceData)
```

### Customizing the data mapping 1 — [17:49]

```swift
// Customizing the Data Mapping

// Encoding process
coder.setFHIRName = { name, fhirPatient in // ModelsR4.Patient

    let humanName = HumanName()
    humanName.family = name.familyName.map { FHIRPrimitive(FHIRString($0)) }
    humanName.given = name.givenName.map { [FHIRPrimitive(FHIRString($0))] }

    fhirPatient.name = [humanName]
}
```

### Customizing the data mapping 2 — [18:10]

```swift
// Customizing the Data Mapping

// Encoding process
coder.setFHIRName = { name, fhirPatient in // ModelsR4.Patient

    let humanName = HumanName()
    humanName.family = name.familyName.map { FHIRPrimitive(FHIRString($0)) }
    humanName.given = name.givenName.map { [FHIRPrimitive(FHIRString($0))] }

    fhirPatient.name = [humanName]
}
```

### Creating the remote — [25:56]

```swift
private lazy var remote = OCKWatchConnectivityPeer()
```

### Setting up the remote store — [26:09]

```swift
private lazy var store = OCKStore(name: "sample-store", remote: remote)
```

### import WatchConnectivity — [26:18]

```swift
import WatchConnectivity
```

### Setting up the Watch Connectivity Session — [26:33]

```swift
WCSession.default.delegate = sessionDelegate
WCSession.default.activate()
```

### Stub out session delegate class — [26:53]

```swift
class SessionDelegate: NSObject, WCSessionDelegate {

    let remote: OCKWatchConnectivityPeer
    let store: OCKStore

    init(remote: OCKWatchConnectivityPeer, store: OCKStore) {
        self.remote = remote
        self.store = store
    }

    func session(
        _ session: WCSession,
        activationDidCompleteWith activationState: WCSessionActivationState,
        error: Error?) {

        print("New session state: \(activationState)")
    }

    func session(
        _ session: WCSession,
        didReceiveMessage message: [String: Any],
        replyHandler: @escaping ([String: Any]) -> Void) {

        print("Received message from peer!")
    }
}
```

### Kick off first synchronization — [27:02]

```swift
if activationState == .activated {
    store.synchronize { error in
        print(error?.localizedDescription ?? "Successful sync!")
    }
}
```

### Forwarding replies on CareKit's behalf — [27:11]

```swift
remote.reply(to: message, store: store) { reply in

    print("Sending reply to peer!")

    replyHandler(reply)
}
```

### Creating the delegate — [27:39]

```swift
private lazy var sessionDelegate = SessionDelegate(remote: remote, store: store)
```

### Setting up the synchronized store manager — [28:10]

```swift
private(set) lazy var storeManager = OCKSynchronizedStoreManager(wrapping: store)
```

### Defining a new environment key — [28:27]

```swift
private struct StoreManagerKey: EnvironmentKey {

    static var defaultValue: OCKSynchronizedStoreManager {

        let extensionDelegate = WKExtension.shared().delegate as! ExtensionDelegate

        return extensionDelegate.storeManager
    }
}
```

### Defining a store manager environment value — [28:51]

```swift
extension EnvironmentValues {

    var storeManager: OCKSynchronizedStoreManager {
        get {
            self[StoreManagerKey.self]
        }

        set {
            self[StoreManagerKey.self] = newValue
        }
    }
}
```

### Adding an environment variable to the view — [28:57]

```swift
@Environment(\.storeManager) private var storeManager
```

### Setting up the scroll view — [29:04]

```swift
ScrollView {

}.accentColor(Color(#colorLiteral(red: 0.9960784314, green: 0.3725490196, blue: 0.368627451, alpha: 1)))
```

### Displaying the stretch task card — [29:22]

```swift
InstructionsTaskView(
taskID: "stretch",
eventQuery: OCKEventQuery(for: Date()),
storeManager: storeManager)
```

### Displaying the muscle cramps task card — [29:33]

```swift
SimpleTaskView(
    taskID: "cramps",
    eventQuery: OCKEventQuery(for: Date()),
    storeManager: storeManager) { controller in

    .init(title: Text(controller.viewModel?.title ?? ""),
          detail: nil,
          isComplete: controller.viewModel?.isComplete ?? false,
          action: controller.viewModel?.action ?? {})
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10151/2/2DBFC733-6021-45DC-9030-8F0FECFBE409/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10151) — developer.apple.com. Indexed for agent consumption._