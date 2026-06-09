---
id: "wwdc2023-10266"
event: "wwdc2023"
year: 2023
title: "Protect your Mac app with environment constraints"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10266"
topics: ["Privacy & Security"]
platforms: ["macOS"]
hasTranscript: true
---

# Protect your Mac app with environment constraints

**Event:** WWDC23 · **Topic:** Privacy & Security · **Platforms:** macOS · **Published:** 2023-06-08 · **Session:** [wwdc2023-10266](https://developer.apple.com/videos/play/wwdc2023/10266)

Learn how to improve the security of your Mac app by adopting environment constraints. We’ll show you how to set limits on how processes are launched, make sure your Launch Agents and Launch Daemons aren’t tampered with, and prevent unwanted code from running in your address space.

**Keywords:** `code signing`, `consent`, `control`, `gatekeeper`, `launch agent`, `launchd`, `sandbox`, `secure boot`, `transparency`, `xpc`, `xprotect`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,517 words)

## Documentation & Resources

- [Security](https://developer.apple.com/documentation/Security) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Security
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Security.json
- [Security Overview](https://developer.apple.com/security/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/security/

## Code Snippets

### Example constraint — [9:35]

```xml
// Example constraint

<dict>
    <key>$or-array</key>
    <array>
        <array>
            <string>$and</string>
            <dict>
                <key>team-identifier</key>
                <string>M2657GZ2M9</string>
            </dict>
        </array>
        <array>
            <string>$and</string>
            <dict>
                <key>signing-identifier</key>
                <string>com.smith.libraryB</string>
                <key>team-identifier</key>
                <string>P9Z4AN7VHQ</string>
            </dict>
        </array>
        <array>
            <string>$and</string>
            <dict>
                <key>signing-identifier</key>
                <string>com.friday.libraryC</string>
                <key>team-identifier</key>
                <string>TA1570ZFMZ</string>
            </dict>
        </array>
    </array>
</dict>
```

### Example parent launch constraint — [11:02]

```xml
<dict>
    <key>team-identifier</key>
    <string>M2657GZ2M9</string>
    <key>signing-identifier</key>
    <string>com.demo.MyDemo</string>
</dict>
```

### Example process launch constraint — [14:06]

```xml
<dict>
    <key>team-identifier</key>
    <string>M2657GZ2M9</string>
    <key>signing-identifier</key>
    <dict>
        <key>$in</key>
        <array>
            <string>com.demo.MyDemo</string>
            <string>com.demo.DemoMenuBar</string>
            <string>demohelper</string>
        </array>
    </dict>
</dict>
```

### Example launchd plist constraint — [14:52]

```xml
// Example launchd plist constraint

<dict>
    <key>Label</key>
    <string>com.demo.DemoMenuBar.agent</string>
    <key>BundleProgram</key>
    <string>Contents/Library/LaunchAgents/DemoMenuBar.app/Contents/MacOS/DemoMenuBar</string>
    <key>KeepAlive</key>
    <dict>
        <key>SuccessfulExit</key>
        <true/>
    </dict>
    <key>RunAtLoad</key>
    <true/>
    <key>SpawnConstraint</key>
    <dict>
        <key>team-identifier</key>
        <string>M2657GZ2M9</string>
        <key>signing-identifier</key>
        <string>com.demo.DemoMenuBar</string>
    </dict>
</dict>
```

### Example library load constraint — [15:29]

```xml
// Example library load constraint

<dict>
    <key>team-identifier</key>
    <dict>
        <key>$in</key>
        <array>
            <string>M2657GZ2M9</string>
            <string>P9Z4AN7VHQ</string>
        </array>
    </dict>
</dict>
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10266/4/24189FC4-EAA7-44E2-B039-930BF35F451F/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10266/4/24189FC4-EAA7-44E2-B039-930BF35F451F/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10266) — developer.apple.com. Indexed for agent consumption._