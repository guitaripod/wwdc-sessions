---
id: "wwdc2020-10060"
event: "wwdc2020"
year: 2020
title: "Design high quality Siri media interactions"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10060"
topics: ["App Services", "Developer Tools", "Audio & Video"]
platforms: ["iOS", "iPadOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Design high quality Siri media interactions

**Event:** WWDC20 · **Topic:** Audio & Video · **Platforms:** iOS, iPadOS, tvOS, watchOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10060](https://developer.apple.com/videos/play/wwdc2020/10060)

Demystify the art of designing Siri experiences for your music and audio apps: We’ll show you how to think about crafting great interactions and how you can provide custom vocabulary so that Siri can respond with more accuracy and personality. We’ll also explain how you can debug common errors and test your intents using the same methods Apple’s own Siri team employs.

**Keywords:** `conversational interaction`, `intents`, `media`, `siri`, `sirikit`, `sirikit media intents`, `voice`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,436 words)

## Code Snippets

### resolveMediaItems method — [5:46]

```swift
func resolveMediaItems(for intent: INPlayMediaIntent, with completion: @escaping ([INPlayMediaMediaItemResolutionResult]) -> Void) {
    let mediaSearch = intent.mediaSearch
    resolveMediaItems(for: mediaSearch) { optionalMediaItems in
        guard let mediaItems = optionalMediaItems else {
            return
        }
        completion(INPlayMediaMediaItemResolutionResult.successes(with: mediaItems))
    }
}
```

### User vocabulary — [10:21]

```swift
let vocabulary = INVocabulary.shared()
let playlistNames = NSOrderedSet(objects: "70s punk classics")
vocabulary.setVocabularyStrings(playlistNames, of: .mediaPlaylistTitle)
```

### Global vocabulary example — [11:28]

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>ParameterVocabularies</key>
	<array>
		<dict>
			<key>ParameterNames</key>
			<array>
				<string>INPlayMediaIntent.playlistTitle</string>
			</array>
			<key>ParameterVocabulary</key>
			<array>
				<dict>
					<key>VocabularyItemSynonyms</key>
					<array>
						<dict>
							<key>VocabularyItemPhrase</key>
							<string>70s punk anthems</string>
						</dict>
					</array>          
					<key>VocabularyItemIdentifier</key>
					<string>70s punk anthems</string>
				</dict>
			</array>
		</dict>
	</array>
</dict>
</plist>
```

### Resolve media items method — [13:07]

```swift
func resolveMediaItems(for intent: INPlayMediaIntent, with completion: @escaping ([INPlayMediaMediaItemResolutionResult]) -> Void) {
    let mediaSearch = intent.mediaSearch
    resolveMediaItems(for: mediaSearch) { optionalMediaItems in
        guard let mediaItems = optionalMediaItems else {
            return
        }
        completion(INPlayMediaMediaItemResolutionResult.successes(with: mediaItems))
    }
}
```

### User vocabulary syncing — [13:31]

```swift
// Set our playlist title in user vocabulary so we get the proper Siri intent
let vocabulary = INVocabulary.shared()
let playlistNames = NSOrderedSet(objects: "70s punk classics")
vocabulary.setVocabularyStrings(playlistNames, of: .mediaPlaylistTitle)
```

### Global vocabulary example — [14:57]

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>ParameterVocabularies</key>
	<array>
		<dict>
			<key>ParameterNames</key>
			<array>
				<string>INPlayMediaIntent.playlistTitle</string>
			</array>
			<key>ParameterVocabulary</key>
			<array>
				<dict>
					<key>VocabularyItemSynonyms</key>
					<array>
						<dict>
							<key>VocabularyItemPhrase</key>
							<string>70s punk anthems</string>
						</dict>
					</array>          
					<key>VocabularyItemIdentifier</key>
					<string>70s punk anthems</string>
				</dict>
			</array>
		</dict>
	</array>
</dict>
</plist>
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10060/9/B52BD896-A151-4C63-B521-62611009D046/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10060) — developer.apple.com. Indexed for agent consumption._
