---
id: "wwdc2021-10261"
event: "wwdc2021"
year: 2021
title: "Faster and simpler notarization for Mac apps"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10261"
topics: ["Developer Tools", "Privacy & Security", "App Store, Distribution & Marketing"]
platforms: ["macOS"]
hasTranscript: true
---

# Faster and simpler notarization for Mac apps

**Event:** WWDC21 · **Topic:** App Store, Distribution & Marketing · **Platforms:** macOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10261](https://developer.apple.com/videos/play/wwdc2021/10261)

Notarization works in tandem with macOS to help people safely download software for their Mac outside of the App Store. Discover how notarytool can help you quickly and easily notarize your Mac app for distribution. We’ll show you how you can now notarize your apps with just a single command, and how to bring notarization into your continuous integration workflows. To learn about the notarization workflow, watch the 2019 video "All About Notarization."

**Keywords:** `altool`, `malware`, `notarizing`, `notary`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(921 words)

## Code Snippets

### altool example — [4:10]

```bash
// with altool
xcrun altool --notarize-app -f path/to/submission.zip 
    --primary-bundle-id "$BUNDLE_ID"
    --apiKey "$KEY_ID" --apiIssuer "$ISSUER"
while true; do
  INFO_OUT=$(2>&1 xcrun altool --notarization-info "$SUBMISSION_ID" -u "$USER" 
      --apiKey "$KEY_ID" --apiIssuer "$ISSUER")
  STATUS=$(echo "$INFO_OUT" | grep "Status:" | sed -Ee "s|.*: (.*)$|\1|" )
  if [[ "$STATUS" != "in progress" ]]; then 
    break
  fi
  sleep 30
done
```

### notarytool example — [4:19]

```bash
// with notarytool
notarytool submit path/to/submission.zip --wait
    --key "$KEY_PATH" --key-id "$KEY_ID" --issuer "$ISSUER"
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10261/7/1C2BA450-20C2-43D2-985E-BA26B13060B2/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10261/7/1C2BA450-20C2-43D2-985E-BA26B13060B2/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10261) — developer.apple.com. Indexed for agent consumption._
