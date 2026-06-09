---
id: "wwdc2025-223"
event: "wwdc2025"
year: 2025
title: "Explore enhancements to your spatial business app"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/223"
topics: ["App Services", "Spatial Computing", "Business & Education"]
platforms: ["visionOS"]
hasTranscript: true
---

# Explore enhancements to your spatial business app

**Event:** WWDC25 · **Topic:** Business & Education · **Platforms:** visionOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-223](https://developer.apple.com/videos/play/wwdc2025/223)

Discover how the latest enhancements and APIs in visionOS 26 expand access and extend enterprise capabilities announced last year. Learn how these all-new features make it easy to build model training workflows, enhance video feeds, and enable you to align coordinate systems over a local network to develop collaborative experiences in your in-house app.

**Keywords:** `camera`, `enterprise`, `follow`, `in-house`, `license`, `stereo`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,277 words)

## Documentation & Resources

- [Implementing object tracking in your app](https://developer.apple.com/documentation/visionOS/implementing-object-tracking-in-your-app) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/implementing-object-tracking-in-your-app
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/implementing-object-tracking-in-your-app.json
- [Building spatial experiences for business apps with enterprise APIs for visionOS](https://developer.apple.com/documentation/visionOS/building-spatial-experiences-for-business-apps-with-enterprise-apis) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/visionOS/building-spatial-experiences-for-business-apps-with-enterprise-apis
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/visionOS/building-spatial-experiences-for-business-apps-with-enterprise-apis.json

## Code Snippets

### createml on the Mac command line — [3:00]

```bash
xcrun createml objecttracker -s my.usdz -o my.referenceobject
```

### VisionEntitlementServices — [4:28]

```swift
import VisionEntitlementServices

func checkLicenseStatus() {
    // Get the shared license details instance
    let license = EnterpriseLicenseDetails.shared

    // First, you might check the overall license status
    guard license.licenseStatus == .valid else {
        print("Enterprise license is not valid: \(license.licenseStatus)")
        // Optionally disable enterprise features or alert the user
        return
    }

    // Then, check for a specific entitlement before using the feature
    if license.isApproved(for: .mainCameraAccess) {
        // Safe to proceed with using the main camera API
        print("Main Camera Access approved. Enabling feature...")
        // ... enable camera functionality ...
    } else {
        // Feature not approved for this license
        print("Main Camera Access not approved.")
        // ... keep feature disabled, potentially inform user ...
    }
}
```

### SharedCoordinateSpaceModel — [10:04]

```swift
//
//  SharedCoordinateSpaceModel.swift
//

import ARKit

class SharedCoordinateSpaceModel {
    let arkitSession = ARKitSession()
    let sharedCoordinateSpace = SharedCoordinateSpaceProvider()
    let worldTracking = WorldTrackingProvider()

    func runARKitSession() async {
        do {
            try await arkitSession.run([sharedCoordinateSpace, worldTracking])
        } catch {
            reportError("Error: running session: \(error)")
        }
    }

    // Push data received from other participants
    func pushCoordinateSpaceData(_ data: Data) {
        if let coordinateSpaceData = SharedCoordinateSpaceProvider.CoordinateSpaceData(data: data) {
            sharedCoordinateSpace.push(data: coordinateSpaceData)
        }
    }

    // Poll data to be sent to other participants
    func pollCoordinateSpaceData() async {
        if let coordinateSpaceData = sharedCoordinateSpace.nextCoordinateSpaceData {
            // Send my coordinate space data
        }
    }

    // Be notified when participants connect or disconnect from the shared coordinate space
    func processEventUpdates() async {
        let participants = [UUID]()
        for await event in sharedCoordinateSpace.eventUpdates {
            switch event {
                // Participants changed
            case .connectedParticipantIdentifiers(participants: participants):
                // handle change
                print("Handle change in participants")
            case .sharingEnabled:
                print("sharing enabled")
            case .sharingDisabled:
                print("sharing disabled")
            @unknown default:
                print("handle future events")
            }
        }
    }

    // Be notified when able to add shared world anchors
    func processSharingAvailabilityUpdates() async {
        for await sharingAvailability in worldTracking.worldAnchorSharingAvailability
            where sharingAvailability == .available {
            // Able to add anchor
        }
    }
    // Add shared world anchor
    func addWorldAnchor(at transform: simd_float4x4) async throws {
        let anchor = WorldAnchor(originFromAnchorTransform: transform, sharedWithNearbyParticipants: true)
        try await worldTracking.addAnchor(anchor)
    }

    // Process shared anchor updates from local session and from other participants
    func processWorldTrackingUpdates() async {
        for await update in worldTracking.anchorUpdates {
            switch update.event {
            case .added, .updated, .removed:
                // Handle anchor updates
                print("Handle updates to shared world anchors")
            }
        }
    }
}
```

### contentCaptureProtected — [12:50]

```swift
// Example implementing contentCaptureProtected

struct SecretDocumentView: View {
    var body: some View {
        VStack {
            Text("Secrets")
                .font(.largeTitle)
                .padding()

            SensitiveDataView()
                .contentCaptureProtected()
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .top)
    }
}
```

### CameraRegionView — [16:48]

```swift
//
//  InspectorView.swift
//

import SwiftUI
import VisionKit

struct InspectorView: View {
    @Environment(CameraFeedDelivery.self) private var cameraFeedDelivery: CameraFeedDelivery

    var body: some View {
        CameraRegionView(isContrastAndVibrancyEnhancementEnabled: true) { result in
            var pixelBuffer: CVReadOnlyPixelBuffer?
            switch result {
            case .success(let value):
                pixelBuffer = value.pixelBuffer
            case .failure(let error):
                reportError("Failure: \(error.localizedDescription)")
                cameraFeedDelivery.stopFeed()
                return nil
            }

            cameraFeedDelivery.frameUpdate(pixelBuffer: pixelBuffer!)
            return nil
        }
    }
}

@main
struct EnterpriseAssistApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }

        WindowGroup(id: "InspectorView") {
            InspectorView()
        }
        .windowResizability(.contentSize)
    }
}
```

### CameraRegionAnchor — [21:15]

```swift
class CameraRegionHandler {
    let arkitSession = ARKitSession()
    var cameraRegionProvider: CameraRegionProvider?
    var cameraRegionAnchor: CameraRegionAnchor?

    func setUpNewAnchor(anchor: simd_float4x4, width: Float, height: Float) async {
        let anchor = CameraRegionAnchor(originFromAnchorTransform: anchor,
                                        width: width,
                                        height: height,
                                        cameraEnhancement: .stabilization)

        guard let cameraRegionProvider = self.cameraRegionProvider else {
            reportError("Missing CameraRegionProvider")
            return
        }

        do {
            try await cameraRegionProvider.addAnchor(anchor)
        } catch {
            reportError("Error adding anchor: \(error)")
        }
        cameraRegionAnchor = anchor

        Task {
            let updates = cameraRegionProvider.anchorUpdates(forID: anchor.id)
            for await update in updates {
                let pixelBuffer = update.anchor.pixelBuffer
                // handle pixelBuffer
            }
        }
    }

    func removeAnchor() async {
        guard let cameraRegionProvider = self.cameraRegionProvider else {
            reportError("Missing CameraRegionProvider")
            return
        }

        if let cameraRegionAnchor = self.cameraRegionAnchor {
            do {
                try await cameraRegionProvider.removeAnchor(cameraRegionAnchor)
            } catch {
                reportError("Error removing anchor: \(error.localizedDescription)")
                return
            }
            self.cameraRegionAnchor = nil
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/223/4/5af51454-839b-4a10-9b09-2f7018e9e3af/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/223/4/5af51454-839b-4a10-9b09-2f7018e9e3af/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/223) — developer.apple.com. Indexed for agent consumption._
