---
id: "tech-talks-10067"
event: "tech-talks"
year: 2017
title: "Bring desktop class sync to iOS with FileProvider"
type: "Video"
url: "https://developer.apple.com/videos/play/tech-talks/10067"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Bring desktop class sync to iOS with FileProvider

**Event:** Tech Talks · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-10-11 · **Session:** [tech-talks-10067](https://developer.apple.com/videos/play/tech-talks/10067)

Discover how you can sync files faster and more efficiently within your iPhone and iPad apps when you create a File Provider extension. Sync up with the File Provider team and learn how to build a modern File Provider for iOS. We’ll show you how to architect your app to support seamless file sync, uploads, and downloads. And we’ll explore how you can go stateless and fortify your file provider against unexpected conditions.

To get the most out of this session, we recommend having experience with File Providers on macOS.

**Keywords:** `cloud`, `download`, `fileprovider`, `file provider`, `files`, `filesystem`, `file system`, `sync`, `synchronization`, `synchronize`, `upload`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,483 words)

## Documentation & Resources

- [Synchronizing files using file provider extensions](https://developer.apple.com/documentation/FileProvider/synchronizing-files-using-file-provider-extensions) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FileProvider/synchronizing-files-using-file-provider-extensions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FileProvider/synchronizing-files-using-file-provider-extensions.json
- [Sending notification requests to APNs](https://developer.apple.com/documentation/UserNotifications/sending-notification-requests-to-apns) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UserNotifications/sending-notification-requests-to-apns
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UserNotifications/sending-notification-requests-to-apns.json
- [File Provider UI](https://developer.apple.com/documentation/FileProviderUI) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FileProviderUI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FileProviderUI.json
- [File Provider](https://developer.apple.com/documentation/FileProvider) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FileProvider
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FileProvider.json

## Code Snippets

### Implement a Progress Cancellation Handler — [6:04]

```swift
// Implementing a progress cancellation handler

public func modifyItem(_ item: ..., completionHandler: (..., Error?) -> Void) -> Progress {
    let progress = Progress()
    let uploadTask = Task {
        do {
            // ...
            try Task.checkCancellation()
            // ...
        } catch let error {
            completionHandler(nil, [], false, error)
        }
    }

    progress.cancellationHandler = {
        uploadTask.cancel()
    }
    return progress
}
```

### Register for Push Notifications — [6:53]

```swift
// Registering for push notifications

import PushKit

let pushRegistry = PKPushRegistry(queue: queue)

pushRegistry.delegate = self
pushRegistry.desiredPushTypes = Set([PKPushType.fileProvider])

...

// On the server: push
//
// {
//    "container-identifier" = "NSFileProviderWorkingSetContainerItemIdentifier"
//    "domain" = "<domain identifier>"
// }
//
// with topic "<your application identifier>.pushkit.fileprovider"
```

### Drag and Drop: Implement Dragging — [8:53]

```swift
// Sending out drags

var body: some View {
    Text("🥐")
    .onDrag {
        let itemProvider = NSItemProvider()
        itemProvider.registerFileRepresentation(for: .folder,
                                                openInPlace: true) { completionHandler in
            self.manager.getUserVisibleURL(for: folderItemID) { fileURL, error in
                guard let fileURL = fileURL else {
                    completionHandler(nil, false, error)
                    return
                }
                completionHandler(fileURL, true, nil)
            }
            return Progress()  
        }
        return itemProvider
    }
}
```

### Drag and Drop: Implement Dropping — [9:24]

```swift
// Receiving drops

var body: some View {
    Text("🥬")
    .onDrop(of: [.folder], isTargeted: $dropTarget) { providers in
        guard let prov = providers.first(where: { provider in
            !provider.registeredContentTypes(conformingTo: .folder).isEmpty
        }) else {
            return false
        }
        prov.loadFileRepresentation(for: .folder, openInPlace: true) { url, inPlace, err in
            guard let url = url else { return }
            Task {
                url.startAccessingSecurityScopedResource()
                // use URL
                url.stopAccessingSecurityScopedResource()
            }
        }
        return true
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/tech-talks/10067/3/F8DADC3E-4CC2-4165-AD4A-5B6A2DBFCF29/cmaf.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/tech-talks/10067) — developer.apple.com. Indexed for agent consumption._