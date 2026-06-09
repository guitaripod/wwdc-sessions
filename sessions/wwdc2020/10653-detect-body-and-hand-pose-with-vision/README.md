---
id: "wwdc2020-10653"
event: "wwdc2020"
year: 2020
title: "Detect Body and Hand Pose with Vision"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10653"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Detect Body and Hand Pose with Vision

**Event:** WWDC20 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2020-06-23 · **Session:** [wwdc2020-10653](https://developer.apple.com/videos/play/wwdc2020/10653)

Explore how the Vision framework can help your app detect body and hand poses in photos and video. With pose detection, your app can analyze the poses, movements, and gestures of people to offer new video editing possibilities, or to perform action classification when paired with an action classifier built in Create ML. And we’ll show you how you can bring gesture recognition into your app through hand pose, delivering a whole new form of interaction. To understand more about how you might apply body pose for Action Classification, be sure to also watch the "Build an Action Classifier with Create ML" and "Explore the Action & Vision app" sessions. And to learn more about other great features in Vision, check out the "Explore Computer Vision APIs" session.

**Keywords:** `action classification`, `action classifier`, `bean bag toss`, `body pose`, `camera`, `cornhole`, `gesture`, `hand pose`, `machine learning`, `photo`, `pose estimation`, `ui control`, `video`, `vision`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,945 words)

## Documentation & Resources

- [Detecting Hand Poses with Vision](https://developer.apple.com/documentation/Vision/detecting-hand-poses-with-vision) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Vision/detecting-hand-poses-with-vision
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Vision/detecting-hand-poses-with-vision.json
- [Vision](https://developer.apple.com/documentation/Vision) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Vision
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Vision.json

## Code Snippets

### HandPoseCameraViewController — [7:07]

```swift
extension CameraViewController: AVCaptureVideoDataOutputSampleBufferDelegate {
    public func captureOutput(_ output: AVCaptureOutput, didOutput sampleBuffer: CMSampleBuffer, from connection: AVCaptureConnection) {
        var thumbTip: CGPoint?
        var indexTip: CGPoint?

        defer {
            DispatchQueue.main.sync {
                self.processPoints(thumbTip: thumbTip, indexTip: indexTip)
            }
        }

        let handler = VNImageRequestHandler(cmSampleBuffer: sampleBuffer, orientation: .up, options: [:])
        do {
            // Perform VNDetectHumanHandPoseRequest
            try handler.perform([handPoseRequest])
            // Continue only when a hand was detected in the frame.
            // Since we set the maximumHandCount property of the request to 1, there will be at most one observation.
            guard let observation = handPoseRequest.results?.first as? VNRecognizedPointsObservation else {
                return
            }
            // Get points for thumb and index finger.
            let thumbPoints = try observation.recognizedPoints(forGroupKey: .handLandmarkRegionKeyThumb)
            let indexFingerPoints = try observation.recognizedPoints(forGroupKey: .handLandmarkRegionKeyIndexFinger)
            // Look for tip points.
            guard let thumbTipPoint = thumbPoints[.handLandmarkKeyThumbTIP], let indexTipPoint = indexFingerPoints[.handLandmarkKeyIndexTIP] else {
                return
            }
            // Ignore low confidence points.
            guard thumbTipPoint.confidence > 0.3 && indexTipPoint.confidence > 0.3 else {
                return
            }
            // Convert points from Vision coordinates to AVFoundation coordinates.
            thumbTip = CGPoint(x: thumbTipPoint.location.x, y: 1 - thumbTipPoint.location.y)
            indexTip = CGPoint(x: indexTipPoint.location.x, y: 1 - indexTipPoint.location.y)
        } catch {
            cameraFeedSession?.stopRunning()
            let error = AppError.visionError(error: error)
            DispatchQueue.main.async {
                error.displayInViewController(self)
            }
        }
    }
}
```

### HandPoseProcessPointsPair — [8:29]

```swift
init(pinchMaxDistance: CGFloat = 40, evidenceCounterStateTrigger: Int = 3) {
        self.pinchMaxDistance = pinchMaxDistance
        self.evidenceCounterStateTrigger = evidenceCounterStateTrigger
    }

    func reset() {
        state = .unknown
        pinchEvidenceCounter = 0
        apartEvidenceCounter = 0
    }

    func processPointsPair(_ pointsPair: PointsPair) {
        lastProcessedPointsPair = pointsPair
        let distance = pointsPair.indexTip.distance(from: pointsPair.thumbTip)
        if distance < pinchMaxDistance {
            // Keep accumulating evidence for pinch state.
            pinchEvidenceCounter += 1
            apartEvidenceCounter = 0
            // Set new state based on evidence amount.
            state = (pinchEvidenceCounter >= evidenceCounterStateTrigger) ? .pinched : .possiblePinch
        } else {
            // Keep accumulating evidence for apart state.
            apartEvidenceCounter += 1
            pinchEvidenceCounter = 0
            // Set new state based on evidence amount.
            state = (apartEvidenceCounter >= evidenceCounterStateTrigger) ? .apart : .possibleApart
        }
    }
```

### HandPoseHandleGestureStateChange — [9:25]

```swift
private func handleGestureStateChange(state: HandGestureProcessor.State) {
        let pointsPair = gestureProcessor.lastProcessedPointsPair
        var tipsColor: UIColor
        switch state {
        case .possiblePinch, .possibleApart:
            // We are in one of the "possible": states, meaning there is not enough evidence yet to determine
            // if we want to draw or not. For now, collect points in the evidence buffer, so we can add them
            // to a drawing path when required.
            evidenceBuffer.append(pointsPair)
            tipsColor = .orange
        case .pinched:
            // We have enough evidence to draw. Draw the points collected in the evidence buffer, if any.
            for bufferedPoints in evidenceBuffer {
                updatePath(with: bufferedPoints, isLastPointsPair: false)
            }
            // Clear the evidence buffer.
            evidenceBuffer.removeAll()
            // Finally, draw current point
            updatePath(with: pointsPair, isLastPointsPair: false)
            tipsColor = .green
        case .apart, .unknown:
            // We have enough evidence to not draw. Discard any evidence buffer points.
            evidenceBuffer.removeAll()
            // And draw the last segment of our draw path.
            updatePath(with: pointsPair, isLastPointsPair: true)
            tipsColor = .red
        }
        cameraView.showPoints([pointsPair.thumbTip, pointsPair.indexTip], color: tipsColor)
    }
```

### HandPoseHandleGesture — [10:15]

```swift
@IBAction func handleGesture(_ gesture: UITapGestureRecognizer) {
        guard gesture.state == .ended else {
            return
        }
        evidenceBuffer.removeAll()
        drawPath.removeAllPoints()
        drawOverlay.path = drawPath.cgPath
    }
```

### ActionVisionGameViewController — [20:48]

```swift
extension GameViewController: CameraViewControllerOutputDelegate {
    func cameraViewController(_ controller: CameraViewController, didReceiveBuffer buffer: CMSampleBuffer, orientation: CGImagePropertyOrientation) {
        let visionHandler = VNImageRequestHandler(cmSampleBuffer: buffer, orientation: orientation, options: [:])
        if self.gameManager.stateMachine.currentState is GameManager.TrackThrowsState {
            DispatchQueue.main.async {
                // Get the frame of rendered view
                let normalizedFrame = CGRect(x: 0, y: 0, width: 1, height: 1)
                self.jointSegmentView.frame = controller.viewRectForVisionRect(normalizedFrame)
                self.trajectoryView.frame = controller.viewRectForVisionRect(normalizedFrame)
            }
            // Perform the trajectory request in a separate dispatch queue
            trajectoryQueue.async {
                self.setUpDetectTrajectoriesRequest()
                do {
                    if let trajectoryRequest = self.detectTrajectoryRequest {
                        try visionHandler.perform([trajectoryRequest])
                    }
                } catch {
                    AppError.display(error, inViewController: self)
                }
            }
        }
        // Run bodypose request for additional GameConstants.maxPostReleasePoseObservations frames after the first trajectory observation is detected
        if !(self.trajectoryView.inFlight && self.trajectoryInFlightPoseObservations >= GameConstants.maxTrajectoryInFlightPoseObservations) {
            do {
                try visionHandler.perform([detectPlayerRequest])
                if let result = detectPlayerRequest.results?.first as? VNRecognizedPointsObservation {
                    let box = humanBoundingBox(for: result)
                    let boxView = playerBoundingBox
                    DispatchQueue.main.async {
                        let horizontalInset = CGFloat(-20.0)
                        let verticalInset = CGFloat(-20.0)
                        let viewRect = controller.viewRectForVisionRect(box).insetBy(dx: horizontalInset, dy: verticalInset)
                        self.updateBoundingBox(boxView, withRect: viewRect)
                        if !self.playerDetected && !boxView.isHidden {
                            self.gameStatusLabel.alpha = 0
                            self.resetTrajectoryRegions()
                            self.gameManager.stateMachine.enter(GameManager.DetectedPlayerState.self)
                        }
                    }
                }
            } catch {
                AppError.display(error, inViewController: self)
            }
        } else {
            // Hide player bounding box
            DispatchQueue.main.async {
                if !self.playerBoundingBox.isHidden {
                    self.playerBoundingBox.isHidden = true
                    self.jointSegmentView.resetView()
                }
            }
        }
    }
}
```

### ActionVisionHumanBoundingBox — [21:19]

```swift
func humanBoundingBox(for observation: VNRecognizedPointsObservation) -> CGRect {
        var box = CGRect.zero
        // Process body points only if the confidence is high
        guard observation.confidence > 0.6 else {
            return box
        }
        var normalizedBoundingBox = CGRect.null
        guard let points = try? observation.recognizedPoints(forGroupKey: .all) else {
            return box
        }
        for (_, point) in points {
            // Only use point if human pose joint was detected reliably
            guard point.confidence > 0.1 else { continue }
            normalizedBoundingBox = normalizedBoundingBox.union(CGRect(origin: point.location, size: .zero))
        }
        if !normalizedBoundingBox.isNull {
            box = normalizedBoundingBox
        }
        // Fetch body joints from the observation and overlay them on the player
        DispatchQueue.main.async {
            let joints = getBodyJointsFor(observation: observation)
            self.jointSegmentView.joints = joints
        }
        // Store the body pose observation in playerStats when the game is in TrackThrowsState
        // We will use these observations for action classification once the throw is complete
        if gameManager.stateMachine.currentState is GameManager.TrackThrowsState {
            playerStats.storeObservation(observation)
            if trajectoryView.inFlight {
                trajectoryInFlightPoseObservations += 1
            }
        }
        return box
    }
```

### ActionVisionStoreObservation — [21:58]

```swift
mutating func storeObservation(_ observation: VNRecognizedPointsObservation) {
        if poseObservations.count >= GameConstants.maxPoseObservations {
            poseObservations.removeFirst()
        }
        poseObservations.append(observation)
    }
```

### ActionVisionGetLastThrowType — [22:21]

```swift
mutating func getLastThrowType() -> ThrowType {
        let actionClassifier = PlayerActionClassifier().model
        guard let poseMultiArray = prepareInputWithObservations(poseObservations) else {
            return ThrowType.none
        }
        let input = PlayerActionClassifierInput(input: poseMultiArray)
        guard let predictions = try? actionClassifier.prediction(from: input),
            let output = predictions.featureValue(for: "output")?.multiArrayValue,
                let outputBuffer = try? UnsafeBufferPointer<Float32>(output) else {
            return ThrowType.none
        }
        let probabilities = Array(outputBuffer)
        guard let maxConfidence = probabilities.prefix(3).max(), let maxIndex = probabilities.firstIndex(of: maxConfidence) else {
            return ThrowType.none
        }
        let throwTypes = ThrowType.allCases
        return throwTypes[maxIndex]
    }
```

### ActionVisionPrepareInputWithObservations — [22:42]

```swift
func prepareInputWithObservations(_ observations: [VNRecognizedPointsObservation]) -> MLMultiArray? {
    let numAvailableFrames = observations.count
    let observationsNeeded = 60
    var multiArrayBuffer = [MLMultiArray]()

    // swiftlint:disable identifier_name
    for f in 0 ..< min(numAvailableFrames, observationsNeeded) {
        let pose = observations[f]
        do {
            let oneFrameMultiArray = try pose.keypointsMultiArray()
            multiArrayBuffer.append(oneFrameMultiArray)
        } catch {
            continue
        }
    }

    // If poseWindow does not have enough frames (60) yet, we need to pad 0s
    if numAvailableFrames < observationsNeeded {
        for _ in 0 ..< (observationsNeeded - numAvailableFrames) {
            do {
                let oneFrameMultiArray = try MLMultiArray(shape: [1, 3, 18], dataType: .double)
                try resetMultiArray(oneFrameMultiArray)
                multiArrayBuffer.append(oneFrameMultiArray)
            } catch {
                continue
            }
        }
    }
    return MLMultiArray(concatenating: [MLMultiArray](multiArrayBuffer), axis: 0, dataType: MLMultiArrayDataType.double)
}
```

### ActionVisionGetLastThrowType2 — [23:19]

```swift
mutating func getLastThrowType() -> ThrowType {
        let actionClassifier = PlayerActionClassifier().model
        guard let poseMultiArray = prepareInputWithObservations(poseObservations) else {
            return ThrowType.none
        }
        let input = PlayerActionClassifierInput(input: poseMultiArray)
        guard let predictions = try? actionClassifier.prediction(from: input),
            let output = predictions.featureValue(for: "output")?.multiArrayValue,
                let outputBuffer = try? UnsafeBufferPointer<Float32>(output) else {
            return ThrowType.none
        }
        let probabilities = Array(outputBuffer)
        guard let maxConfidence = probabilities.prefix(3).max(), let maxIndex = probabilities.firstIndex(of: maxConfidence) else {
            return ThrowType.none
        }
        let throwTypes = ThrowType.allCases
        return throwTypes[maxIndex]
    }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10653/8/E739CC44-25A9-46B9-8E40-1788530C5785/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10653) — developer.apple.com. Indexed for agent consumption._
