---
id: "wwdc2025-257"
event: "wwdc2025"
year: 2025
title: "Optimize home electricity usage with EnergyKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2025/257"
topics: ["System Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Optimize home electricity usage with EnergyKit

**Event:** WWDC25 · **Topic:** System Services · **Platforms:** iOS, iPadOS · **Published:** 2025-06-09 · **Session:** [wwdc2025-257](https://developer.apple.com/videos/play/wwdc2025/257)

Learn how to support EnergyKit in your app so people can optimize electricity usage at home. This can help people run appliances or charge EVs during times when electricity is cleaner and cheaper. Get details about onboarding, generating a charging schedule, and providing energy usage insights back to people through electricity usage feedback.

**Keywords:** `apple 2030`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,997 words)

## Documentation & Resources

- [Optimizing home electricity usage](https://developer.apple.com/documentation/EnergyKit/optimizing-home-electricity-usage) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/EnergyKit/optimizing-home-electricity-usage
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/EnergyKit/optimizing-home-electricity-usage.json
- [Apple 2030](https://www.apple.com/environment/) _documentation_

## Code Snippets

### Retrive an EnergyVenue — [3:13]

```swift
// Retrieve an EnergyVenue

import EnergyKit
import Foundation

@Observable final class EnergyVenueManager  {

    let venue: EnergyVenue

    init?(venueID: UUID) async {
        guard let energyVenue = await EnergyVenue.venue(for: venueID) else {
            return nil
        }
        venue = energyVenue
    }
}
```

### Fetch Electricity Guidance at a selected EnergyVenue — [6:03]

```swift
// Fetch ElectricityGuidance

import EnergyKit
import Foundation

@Observable final class EnergyVenueManager  {
    // The current active guidance.
    var guidance: ElectricityGuidance?

    fileprivate func streamGuidance(
        venueID: UUID,
        update: (_ guidance: ElectricityGuidance) -> Void
    ) async throws {
        let query = ElectricityGuidance.Query(suggestedAction: .shift)
        for try await currentGuidance in ElectricityGuidance.sharedService.guidance(
            using: query,
            at: venueID
        ) {
            update(currentGuidance)
          	break
        }
    }
}
```

### Start monitoring Electricity Guidance — [7:00]

```swift
// Fetch ElectricityGuidance

import EnergyKit
import Foundation

@Observable final class EnergyVenueManager  {
    // The task used to stream guidance.
    private var streamGuidanceTask: Task<(), Error>?

    ///Start streaming guidance and store the value in the observed property 'guidance'.
    func startGuidanceMonitoring() {
       streamGuidanceTask?.cancel()
        streamGuidanceTask = Task.detached { [weak self] in
            if let venueID = self?.venue.id {
                try? await self?.streamGuidance(venueID: venueID) { guidance in
                    self?.guidance = guidance
                    if Task.isCancelled {
                        return
                    }
                }
            }
        }
    }
}
```

### Update charging measurements — [11:30]

```swift
// Update charging measurements

import EnergyKit

// A controller that handles an electric vehicle
@Observable class ElectricVehicleController {
    fileprivate func chargingMeasurement() -> ElectricVehicleLoadEvent.ElectricalMeasurement {
        let stateOfCharge = Int(configuration.state.stateOfCharge.rounded(.down))
        let power = Measurement<UnitPower>(
            value: configuration.properties.chargingPower * 1000000,
            unit: .milliwatts
        )
        let energy = Measurement<UnitEnergy>(
            value: configuration.state.cummulativeEnergy * 1000000,
            unit: .EnergyKit.milliwattHours
        )
        return ElectricVehicleLoadEvent.ElectricalMeasurement(
            stateOfCharge: stateOfCharge,
            direction: .imported,
            power: power,
            energy: energy
        )
    }
}
```

### Start a session — [11:50]

```swift
// Start a session

import EnergyKit

// A controller that handles an electric vehicle
@Observable class ElectricVehicleController {
    // The session
    var session: ElectricVehicleLoadEvent.Session?

    // The current guidance stored at the EV
    var currentGuidance: ElectricityGuidance

    // Whether the EV is following guidance
    var isFollowingGuidance: Bool = true

    fileprivate func beginSession() {
        session = ElectricVehicleLoadEvent.Session(
            id: UUID(),
            state: .begin,
            guidanceState: .init(
                wasFollowingGuidance: isFollowingGuidance,
                guidanceToken: currentGuidance.guidanceToken
            )
        )
    }
}
```

### Update a session — [12:25]

```swift
// Update a session

import EnergyKit

// A controller that handles an electric vehicle
@Observable class ElectricVehicleController {
    fileprivate func updateSession() {
        if let session {
            self.session = ElectricVehicleLoadEvent.Session(
                id: session.id,
                state: .active,
                guidanceState: .init(
                    wasFollowingGuidance:
                    isFollowingGuidance,
                    guidanceToken:
                    currentGuidance.guidanceToken
                )
            )
        }
    }
}
```

### End a session — [12:31]

```swift
// End a session

import EnergyKit

// A controller that handles an electric vehicle.
@Observable class ElectricVehicleController {
    fileprivate func endSession() {
        if let session {
            self.session = ElectricVehicleLoadEvent.Session(
                id: session.id,
                state: .end,
                guidanceState: .init(
                    wasFollowingGuidance:
                    isFollowingGuidance,
                    guidanceToken:
                    currentGuidance.guidanceToken
                )
            )
        }
    }
}
```

### Create a load event — [12:43]

```swift
// Create a ElectricVehicleLoadEvent

@Observable class ElectricVehicleController {
    fileprivate func createLoadEvent(
        sessionState: ElectricVehicleLoadEvent.Session.State
    ) {
        switch sessionState {
        case .begin:
            beginSession()
        case .active:
            updateSession()
        case .end:
            endSession()
        @unknown default:
            fatalError()
        }
        if let session {
            let event = ElectricVehicleLoadEvent(
                timestamp: configuration.state.timestamp,
                measurement: chargingMeasurement(),
                session: session,
                deviceID: configuration.properties.vehicleID
            )
           events.append(event)
        }
    }
}
```

### Submit events — [12:50]

```swift
// Submit events

import EnergyKit

// A controller that handles an electric vehicle
@Observable class ElectricVehicleController {
    // EnergyVenue
    // The venue at which the EV uses energy
    var currentVenue: EnergyVenue

    // Electric EV Events
    // The list of generated EV load events
    var events = [ElectricVehicleLoadEvent]()

    func submitEvents() async throws {
        try await currentVenue.submitEvents(events)
    }
}
```

### Create an insight query — [13:25]

```swift
// Create an insight query

import EnergyKit

@Observable final class EnergyVenueManager  {
    func createInsightsQuery(on date: Date) -> ElectricityInsightQuery {
        return ElectricityInsightQuery(
            options: .cleanliness.union(.tariff),
            range: self.dayInterval(date: date),
            granularity: .daily,
            flowDirection: .imported
        )
    }
}
```

### Request insights — [13:43]

```swift
// Request an insights

import EnergyKit

@Observable final class EnergyVenueManager  {
    func generateInsights(for vehicleIdentifier: String, on date: Date) async throws ->     ElectricityInsightRecord<Measurement<UnitEnergy>>? {
        let query = createInsightsQuery(on: date)
        return try await ElectricityInsightService.shared.energyInsights(
            forDeviceID: vehicleIdentifier,
            using: query,
            atVenue: self.venue.id
        ).first { record in
            return record.range.start == query.range.start
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2025/257/5/af3f4fb6-a561-4208-8035-3f6a77252946/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2025/257/5/af3f4fb6-a561-4208-8035-3f6a77252946/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2025/257) — developer.apple.com. Indexed for agent consumption._
