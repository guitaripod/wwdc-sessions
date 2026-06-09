---
id: "wwdc2022-10093"
event: "wwdc2022"
year: 2022
title: "Integrate your custom collaboration app with Messages"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10093"
topics: ["App Services", "SwiftUI & UI Frameworks", "System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Integrate your custom collaboration app with Messages

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10093](https://developer.apple.com/videos/play/wwdc2022/10093)

Discover how the SharedWithYou framework can augment your app's collaboration infrastructure. We'll show you how to send secure invitations to collaborative content and synchronize participant changes. We'll also cover displaying content updates within the relevant conversation. For an introduction to SharedWithYou, watch "Add Shared with You to your app" from WWDC22. For an overview of the collaboration UI APIs, watch "Enhance collaboration experiences with Messages" from WWDC22.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,763 words)

## Code Snippets

### Configure SWCollaborationMetadata — [4:21]

```swift
let localIdentifier = SWLocalCollaborationIdentifier(rawValue: "identifier")
let metadata = SWCollaborationMetadata(localIdentifier: localIdentifier)
metadata.title = "Content Title"
metadata.initiatorHandle = "user@example.com"

let formatter = PersonNameComponentsFormatter()
if let components = formatter.personNameComponents(from: "Devin") {
    metadata.initiatorNameComponents = components
}

metadata.defaultShareOptions = ...
```

### Configure SWCollaborationShareOptions — [6:34]

```swift
let permission = SWCollaborationOptionsPickerGroup(identifier: UUID().uuidString, 
                                                   options: [
    SWCollaborationOption(title: "Can make changes", identifier: UUID().uuidString),
    SWCollaborationOption(title: "Read only", identifier: UUID().uuidString)
])
permission.options[0].isSelected = true
permission.title = "Permission"

let additionalOptions = SWCollaborationOptionsGroup(identifier: UUID().uuidString, 
                                                    options: [
    SWCollaborationOption(title: "Allow mentions", identifier: UUID().uuidString),
    SWCollaborationOption(title: "Allow comments", identifier: UUID().uuidString)
])
additionalOptions.title = "Additional Settings"
let optionsGroups = [permission, additionalOptions]
metadata.defaultShareOptions = SWCollaborationShareOptions(optionsGroups: optionsGroups)
```

### SWCollaborationMetadata SwiftUI TransferRepresentation — [7:58]

```swift
struct CustomCollaboration: Transferable {
    var name: String

    static var transferRepresentation: some TransferRepresentation {
        ProxyRepresentation { customCollaboration in
            SWCollaborationMetadata(
                localIdentifier: .init(rawValue: "com.example.customcollaboration"),
                title: customCollaboration.name,
                defaultShareOptions: nil,
                initiatorHandle: "johnappleseed@apple.com",
                initiatorNameComponents: nil
            )
        }
    }
}
```

### Using a collaboration metadata TransferRepresentation with ShareLink — [8:16]

```swift
struct ContentView: View {
    var body: some View {
        ShareLink(item: CustomCollaboration(name: "Example"), preview: .init("Example"))
    }
}
```

### iOS Share Sheet — [9:08]

```swift
func presentActivityViewController(metadata: SWCollaborationMetadata) {
    let itemProvider = NSItemProvider()
    itemProvider.registerObject(metadata, visibility: .all)
    let activityConfig = UIActivityItemsConfiguration(itemProviders: [itemProvider])
    let shareSheet = UIActivityViewController(activityItemsConfiguration: activityConfig)
    present(shareSheet, animated: true)
}
```

### iOS Drag and Drop — [9:42]

```swift
func createDragItem(metadata: SWCollaborationMetadata) -> UIDragItem {
    let itemProvider = NSItemProvider()
    itemProvider.registerObject(metadata, visibility: .all)
    return UIDragItem(itemProvider: itemProvider)
}
```

### macOS Sharing Popover — [9:58]

```swift
func showSharingServicePicker(view: NSView, metadata: SWCollaborationMetadata) {
    let itemProvider = NSItemProvider()
    itemProvider.registerObject(metadata, visibility: .all)
    let picker = NSSharingServicePicker(items: [itemProvider])
    picker.show(relativeTo: view.bounds, of: view, preferredEdge: .minY)
}
```

### macOS Drag and Drop NSPasteboardItem extension — [10:18]

```swift
func createPasteboardItem(metadata: SWCollaborationMetadata) -> NSPasteboardItem {
    let pasteboardItem = NSPasteboardItem()
    pasteboardItem.collaborationMetadata = metadata
    return pasteboardItem
}
```

### Set up SWCollaborationCoordinator — [11:22]

```swift
private let collaborationCoordinator = SWCollaborationCoordinator.shared

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool {
    // Conform to the SWCollaborationActionHandler protocol
    collaborationCoordinator.actionHandler = self
}
```

### SWStartCollaborationAction — [12:27]

```swift
func collaborationCoordinator(_ coordinator: SWCollaborationCoordinator, 
                              handle action: SWStartCollaborationAction) {
    let localID = action.collaborationMetadata.localIdentifier.rawValue
    let selectedOptions = action.collaborationMetadata.userSelectedShareOptions
    let prepareRequest = APIRequest.PrepareCollaboration(localID: localID, selectedOptions)
    Task {
        do {            
            let response = try await apiController.send(request: prepareRequest)
            let identifier = response.deviceIndependentIdentifier
            action.fulfill(using: response.url, collaborationIdentifier: identifier)
        } catch {
            Log.error("Caught error while preparing the collaboration: \(error)")
            action.fail() // cancels the message
        }
    }
}
```

### SWUpdateCollaborationParticipantsAction — [13:40]

```swift
func collaborationCoordinator(_ coordinator: SWCollaborationCoordinator, 
                              handle action: SWUpdateCollaborationParticipantsAction) {
    let identifier = action.collaborationMetadata.collaborationIdentifier
    let participants: [Data] = action.addedIdentities.compactMap { $0.rootHash }
    let addParticipants = APIRequest.AddParticipants(identifier: identifier, participants)
    Task {
        do {            
            try await apiController.send(request: addParticipants)
            action.fulfill() // sends the URL provided by the start action
        } catch {
            Log.error("Caught error while adding participants to collaboration: \(error)")
            action.fail() // cancels the message 
        }
    }
}
```

### Retrieve a signed identity proof for a highlight — [19:12]

```swift
func application(_ app: UIApplication, open url: URL, 
               options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let highlightCenter: SWHighlightCenter = self.highlightCenter
    let challengeRequest = APIRequest.GetChallengeData()
    Task {
        do {
            let highlight = try highlightCenter.collaborationHighlight(for: url)
            let challenge = try await apiController.send(request: challengeRequest)
            let proof = try await highlightCenter.getSignedIdentityProof(for: highlight, 
                                                                       using: challenge.data)
    let proofOfInclusionRequest = APIRequest.SubmitProofOfInclusion(for: proof)
            let result = try await apiController.send(request: proofOfInclusionRequest)
            documentController.update(currentDocument, with: result)
        } catch {
            Log.error("Caught error while generating proof of inclusion: \(error)")
        }
    }
}
```

### Example code for root hash generation — [21:20]

```swift
func generateRootHashFromArray(localHash: SHA256Digest, inclusionHashes: [SHA256Digest], 
                       publicKeyIndex: Int) -> SHA256Digest {
    guard let firstHash = inclusionHashes.first else { return localHash }
    // Check if the node is the left or the right child
    let isLeft = publicKeyIndex.isMultiple(of: 2)
    // Calculate the combined hash
    var rootHash: SHA256Digest
    if isLeft {
        rootHash = hash(concatenate([localHash, firstHash]), using: .sha256)
    } else {
        rootHash = hash(concatenate([firstHash, localHash]), using: .sha256)
    }
    // Recursively pass in elements and move up the Merkle tree
    let newInclusionHashes = inclusionHashes.dropFirst()
    rootHash = generateRootHashFromArray(
        localHash: rootHash,
        inclusionHashes: Array(newInclusionHashes),
        publicKeyIndex: (publicKeyIndex / 2)
    )
    return rootHash
}
```

### SWUpdateCollaborationParticipantsAction - removing participants — [24:12]

```swift
func collaborationCoordinator(_ coordinator: SWCollaborationCoordinator, 
                              handle action: SWUpdateCollaborationParticipantsAction) {
    // Example of removing participants only. Handle the added identities here too.
    let identifier = action.collaborationMetadata.collaborationIdentifier
    let removed: [Data] = action.removedIdentities.compactMap { $0.rootHash }
    let removeParticipants = APIRequest.RemoveParticipants(identifier: identifier, removed)
    Task {
        do {            
            try await apiController.send(request: removeParticipants)
            action.fulfill()
        } catch {
            log.error("Caught error while adding participants to collaboration: \(error)")
            action.fail()
        }
    }
}
```

### Post an SWHighlightChangeEvent Notice — [25:54]

```swift
func postContentEditEvent(identifier: SWCollaborationIdentifier) throws {
    let highlightCenter: SWHighlightCenter = self.highlightCenter
    let highlight = try highlightCenter.collaborationHighlight(forIdentifier: identifier)

    let editEvent = SWHighlightChangeEvent(highlight: highlight, trigger: .edit)

    highlightCenter.postNotice(for: editEvent)
}
```

### Post an SWHighlightMembershipEvent Notice — [26:39]

```swift
func postContentEditEvent(identifier: SWCollaborationIdentifier) throws {
    let highlightCenter: SWHighlightCenter = self.highlightCenter
    let highlight = try highlightCenter.collaborationHighlight(forIdentifier: identifier)

    let editEvent = SWHighlightChangeEvent(highlight: highlight, trigger: .edit)

    highlightCenter.postNotice(for: editEvent)
}
```

### Post an SWHighlightMentionEvent Notice — [26:50]

```swift
func postMentionEvent(identifier: SWCollaborationIdentifier, mentionedRootHash: Data) throws {
    let mentionedIdentity = SWPerson.Identity(rootHash: mentionedRootHash)

    let highlightCenter: SWHighlightCenter = self.highlightCenter
    let highlight = try highlightCenter.collaborationHighlight(forIdentifier: identifier)

    let mentionEvent = SWHighlightMentionEvent(highlight: highlight,
                                               mentionedPersonIdentity: mentionedIdentity)
    highlightCenter.postNotice(for: mentionEvent)
}
```

### Post an SWHighlightPersistenceEvent Notice — [27:23]

```swift
func postContentRenamedEvent(identifier: SWCollaborationIdentifier) throws {
    let highlightCenter: SWHighlightCenter = self.highlightCenter
    let highlight = try highlightCenter.collaborationHighlight(forIdentifier: identifier)

    let renamedEvent = SWHighlightPersistenceEvent(highlight: highlight, trigger: .renamed)
    highlightCenter.postNotice(for: renamedEvent)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10093/3/D9CE5DEB-FE73-4FEF-9993-9551EB58CBDC/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10093/3/D9CE5DEB-FE73-4FEF-9993-9551EB58CBDC/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10093) — developer.apple.com. Indexed for agent consumption._
