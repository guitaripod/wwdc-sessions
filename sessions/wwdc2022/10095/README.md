---
id: "wwdc2022-10095"
event: "wwdc2022"
year: 2022
title: "Enhance collaboration experiences with Messages"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10095"
topics: ["App Services", "SwiftUI & UI Frameworks", "System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Enhance collaboration experiences with Messages

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10095](https://developer.apple.com/videos/play/wwdc2022/10095)

Discover how you can help improve communication and collaboration in your app with Collaboration in Messages. Learn how to tie a document to Messages conversations for simple sharing and discussion. Explore how you can keep everyone in the conversation up to date on the latest activity in the document. And find out how you can add customizable UI in your app to manage collaboration details and connect documents to Messages conversations and FaceTime calls. 

To learn more about the SharedWithYou framework, we recommend watching "Add Shared with You to your app.” For more information on adding collaboration APIs to apps that have custom collaboration infrastructure, check out "Integrate your custom collaboration app with Messages.”

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,762 words)

## Code Snippets

### Create a CloudKit collaboration item provider — [4:08]

```swift
// CloudKit collaboration object

// Starting collaboration
let itemProvider = NSItemProvider()
itemProvider.registerCKShare(container: container, 
                             allowedSharingOptions: CKAllowedSharingOptions.standard, 
                             preparationHandler: {
    // Create your share and save to server, or throw error
    return savedShare
})

// Inviting to existing collaboration
let itemProvider = NSItemProvider()
itemProvider.registerCKShare(share, 
                             container: container, 
                             allowedSharingOptions: CKAllowedSharingOptions.standard)
```

### Set up Share Sheet on iOS and Mac Catalyst — [7:35]

```swift
// Setting up Share Sheet - iOS and Mac Catalyst

let activityViewController = UIActivityViewController(activityItems: [collaborationObject], applicationActivities: nil)

presentingViewController.present(activityViewController, animated: true)
```

### Set up Share Popover on macOS — [7:47]

```swift
// Setting up Share Popover - macOS

let sharingServicePicker = NSSharingServicePicker(items: [collaborationObject])

sharingServicePicker.show(relativeTo: view.bounds, of: view, preferredEdge: .minY)
```

### Provide metadata for CloudKit collaboration in Share Sheet (iOS, Mac Catalyst) — [8:22]

```swift
// Providing CloudKit metadata - iOS

let configuration = UIActivityItemsConfiguration(itemProviders: [collaborationItemProvider])
configuration.perItemMetadataProvider = { (_, key) in
    switch key {
    case .linkPresentationMetadata:
        // Create LPLinkMetadata with title and imageProvider
        return metadata
    default:
        return nil
    }
}

let activityViewController = UIActivityViewController(activityItemsConfiguration: configuration)
```

### Provide metadata for CloudKit collaboration in Share Popover (macOS) — [9:03]

```swift
// Providing CloudKit metadata - macOS

let title = “Shared Item”
let image = NSImage(contentsOfFile: “Shared_Item_Preview_Image.png”)
let icon = NSImage(contentsOfFile: “App_Icon.png”) // Shared item source

let previewRepresentingItem = NSPreviewRepresentingActivityItem(item: collaborationItemProvider, 
                                                                title: title, 
                                                                image: image, 
                                                                icon: icon)

let picker = NSSharingServicePicker(items: [previewRepresentingItem])
```

### Create Transferable object for CloudKit collaboration with ShareLink — [10:21]

```swift
// SwiftUI CloudKit Transferable

struct Note: Transferable {
    // Properties of the note e.g. name, preview image, content, ID, …
    var share: CKShare?
    func saveCKShareToServer() async throws -> CKShare { … }

    static var transferRepresentation: some TransferRepresentation {
        CKShareTransferRepresentation { note in
            if let share = note.share {
                return .existing(share, container: container, options: options)
            } else {
                return .prepareShare(container: container, options: options) {
                    return try await note.saveCKShareToServer()
                }
            }
        }
    }
}
```

### Adopt ShareLink in SwiftUI — [11:34]

```swift
// SwiftUI ShareLink adoption

struct ContentView: View {
    @State let item = ShareItem()

    var body: some View {
        ShareLink(item: item, preview: SharePreview(item.title, image: item.previewImage))
    }
}
```

### Initialize the collaborationView — [14:58]

```swift
// Collaboration View

let collaborationView = SWCollaborationView(itemProvider: itemProvider)

collaborationView.activeParticipantCount = myModel.activePeople.count

collaborationView.contentView = MyView(model: myModel)

collaborationView.manageButtonTitle = "Custom Manage Button"
```

### Observe when CKShare is saved with CKSystemSharingUIObserver — [18:11]

```swift
// Observing CKShare Changes

let observer = CKSystemSharingUIObserver(container: container)

observer.systemSharingUIDidSaveShareBlock = { _, result in
    switch result {
    case .success(let share):
        // Handle successfully starting share
    case .failure(let error):
        // Handle error
    }
}
```

### Observe when CKShare is removed with CKSystemSharingUIObserver — [18:47]

```swift
// Observing CKShare Changes

observer.systemSharingUIDidStopSharingBlock = { _, result in
    switch result {
    case .success(let share):
        // Handle successfully starting share
    case .failure(let error):
        // Handle error
    }
}
```

### Posting notice for edit SWHighlightChangeEvent — [20:44]

```swift
// Post an SWHighlightChangeEvent Notice

let highlightCenter: SWHighlightCenter = self.highlightCenter

let highlight = try highlightCenter.collaborationHighlight(forURL: ckShareURL, error: &error)

let editEvent = SWHighlightChangeEvent(highlight: highlight, trigger: .edit)

highlightCenter.postNotice(for: editEvent)
```

### Post an SWHighlightMentionEvent Notice — [21:30]

```swift
// Post an SWHighlightMentionEvent Notice

let highlightCenter: SWHighlightCenter = self.highlightCenter

let highlight = try highlightCenter.collaborationHighlight(forURL: ckShareURL, error: &error)

let mentionEvent = SWHighlightMentionEvent(highlight: highlight, 
           mentionedPersonCloudKitShareHandle: ckShareParticipantHandle)

highlightCenter.postNotice(for: mentionEvent)
```

### Post an SWHighlightPersistenceEvent Notice — [21:58]

```swift
// Post an SWHighlightPersistenceEvent Notice

let highlightCenter: SWHighlightCenter = self.highlightCenter

let highlight = try highlightCenter.collaborationHighlight(forURL: ckShareURL, error: &error)

let renamedEvent = SWHighlightPersistenceEvent(highlight: highlight, trigger: .renamed)

highlightCenter.postNotice(for: renamedEvent)
```

### Post an SWHighlightMembershipEvent Notice — [22:11]

```swift
// Post an SWHighlightMembershipEvent Notice

let highlightCenter: SWHighlightCenter = self.highlightCenter

let highlight = try highlightCenter.collaborationHighlight(forURL: ckShareURL, error: &error)

let membershipEvent = SWHighlightMembershipEvent(highlight: highlight, 
                                           trigger: .addedCollaborator)

highlightCenter.postNotice(for: membershipEvent)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10095/5/DB09B90A-7453-4E3F-90E9-4AB7322DD253/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10095/5/DB09B90A-7453-4E3F-90E9-4AB7322DD253/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10095) — developer.apple.com. Indexed for agent consumption._