---
id: "wwdc2020-10189"
event: "wwdc2020"
year: 2020
title: "Secure your app: threat modeling and anti-patterns"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10189"
topics: ["Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Secure your app: threat modeling and anti-patterns

**Event:** WWDC20 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10189](https://developer.apple.com/videos/play/wwdc2020/10189)

It's more important than ever to consider vulnerabilities and potential threats and recognize where you should apply safeguards in your app. Understand how to identify potential risks through threat modeling and how to avoid common anti-patterns. Learn coding techniques and how to take advantage of platform-supplied protections to help you mitigate risk and protect people while they're using your app.

**Keywords:** `data`, `privacy`, `protection`, `security`, `trust`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(6,448 words)

## Documentation & Resources

- [iOS Security White Paper](https://www.apple.com/business/docs/iOS_Security_Guide.pdf) _documentation_

## Code Snippets

### Path traversal — [16:34]

```swift
func handleIncomingFile(_ incomingResourceURL: URL, with name: String, from fromID: String) {
    guard
         case let safeFileName = name.lastPathComponent, 
         safeFileName.count > 0,
         safeFileName != "..", safeFileName != "." else { return }

    let destinationFileURL = URL(fileURLWithPath: NSTemporaryDirectory())
                                 .appendingPathComponent(safeFileName)

    // Copy the file into a temporary directory
    try! FileManager.default.copyItem(at: incomingResourceURL, to: destinationFileURL)

}
```

### State management — [22:26]

```swift
func handleSessionInviteAccepted(with message: RemoteMessage, from fromID: String) {
    guard session = sessionsByIdentifier[message.sessionIdentifier],
          session.state == .inviting,
          session.invitedFromIdentifiers.contains(fromID) else { return }

    session.state = .connected
    session.setupSocket(to: fromID) { socket in
        cameraController.send(to: socket)
    }
}
```

### Safe dynamic allowedClasses — [30:56]

```objectivec
NSSet *classesWhichConformToProtocol(Protocol *protocol) {
    NSMutableSet *conformingClasses = [NSMutableSet set];

    unsigned int classesCount = 0;
    Class *classes = objc_copyClassList(&classesCount);
    if (classes != NULL) {
        for (unsigned int i = 0; i < classesCount; i++) {
            if (class_conformsToProtocol(classes[i], protocol)) {
                [conformingClasses addObject: classes[i]];
            }
        }
        free(classes);
    }
    return conformingClasses;
}
```

### Buffer overflows — [34:23]

```objectivec
@implementation
- (BOOL)unpackTeaClubRecord:(CKRecord *)record {
    ...
    NSData *data = [record objectForKey:@"uuid"];
    if (data == nil ||
        ![data isKindOfClass:[NSData class]] ||
        data.length != sizeof(_uuid)) {
        return NO;
    }
    memcpy(&_uuid, data.bytes, data.length);
    ...
```

### Integer overflows — [36:06]

```objectivec
@implementation
- (BOOL)unpackTeaClubRecord:(CKRecord *)record {
    ...
    NSData *name = [record objectForKey:@"name"];
    int32_t count = [[record objectForKey:@"nameCount"] unsignedIntegerValue];
    int32_t byteCount = 0;
    if (name == nil ||
        ![name isKindOfClass:[NSData class]] ||
        os_mul_overflow(count, sizeof(unichar), &byteCount) ||
        name.length != byteCount) {
        return NO;
    }
    _name = [[NSString alloc] initWithCharacters:name.bytes 
                                          length:count];
    ...
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10189/4/164A0FEB-D524-40E7-89C9-A40F22CAA89C/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10189) — developer.apple.com. Indexed for agent consumption._
