---
id: "wwdc2021-10236"
event: "wwdc2021"
year: 2021
title: "Host and automate your DocC documentation"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10236"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Host and automate your DocC documentation

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-08 · **Session:** [wwdc2021-10236](https://developer.apple.com/videos/play/wwdc2021/10236)

Find out how you can easily host your Swift package and framework DocC documentation online. We’ll take you through configuring your web server to host your generated DocC archives, and help you learn to use the xcodebuild tool to automate documentation generation and keep your web content synchronized and up to date.

**Keywords:** `catalog`, `docc`, `documentation`, `documentation catalog`, `host`, `website`, `xcodebuild`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,867 words)

## Documentation & Resources

- [Distributing documentation to other developers](https://developer.apple.com/documentation/Xcode/distributing-documentation-to-other-developers) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/distributing-documentation-to-other-developers
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/distributing-documentation-to-other-developers.json
- [SlothCreator: Building DocC documentation in Xcode](https://developer.apple.com/documentation/Xcode/slothcreator-building-docc-documentation-in-xcode) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/slothcreator-building-docc-documentation-in-xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/slothcreator-building-docc-documentation-in-xcode.json

## Code Snippets

### Custom routing in a .htaccess file — [4:49]

```bash
# Enable custom routing.
RewriteEngine On

# Route documentation and tutorial pages.
RewriteRule ^(documentation|tutorials)\/.*$ SlothCreator.doccarchive/index.html [L]

# Route files within the documentation archive.
RewriteRule ^(css|js|data|images|downloads|favicon\.ico|favicon\.svg|img|theme-settings\.json|videos)\/.*$ SlothCreator.doccarchive/$0 [L]
```

### Build documentation on the command line — [9:17]

```bash
# Build documentation for the project.
xcodebuild docbuild                    \
  -scheme "SlothCreator"               \
  -derivedDataPath MyDerivedDataFolder

# Find all the built documentation archives
# to copy them to another location.
find MyDerivedDataFolder               \
  -name "*.doccarchive"
```

### Build and update the hosted documentation — [9:18]

```bash
#!/bin/sh

# Build the SlothCreator documentation.
xcodebuild docbuild                  \
  -scheme "SlothCreator"             \
  -derivedDataPath MyDerivedDataPath

# Copy the documentation archive to ~/www where we
# host the SlothCreator website and documentation.
find MyDerivedDataPath               \
  -name "*.doccarchive"              \
  -exec cp -R {} ~/www \;
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10236/6/93E69517-B140-4720-B821-A542F64CC5C8/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10236/6/93E69517-B140-4720-B821-A542F64CC5C8/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10236) — developer.apple.com. Indexed for agent consumption._
