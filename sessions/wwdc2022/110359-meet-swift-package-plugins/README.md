---
id: "wwdc2022-110359"
event: "wwdc2022"
year: 2022
title: "Meet Swift Package plugins"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110359"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Meet Swift Package plugins

**Event:** WWDC22 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-110359](https://developer.apple.com/videos/play/wwdc2022/110359)

Discover how you can perform actions on Swift packages and Xcode projects with Swift package plugins. We'll go over how these plugins work and explore how you can use them to generate source code and automate your development workflow.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,511 words)

## Code Snippets

### General structure of a package plugin with conditional support for Xcode projects when running in Xcode — [6:59]

```swift
import PackagePlugin

@main
struct MyPlugin: ... {

    // Entry points specific to plugin capability. These entry points are invoked
    // when the plugin is applied to a package.

}

#if canImport(XcodeProjectPlugin)
import XcodeProjectPlugin

extension MyPlugin: ... {

    // Entry points specific to plugin capability. These entry points are invoked
    // when the plugin is applied to an Xcdeo project.

}
#endif
```

### Structure of a command plugin with conditional support for Xcode projects when running in Xcode — [8:33]

```swift
import PackagePlugin

@main
struct MyPlugin: CommandPlugin {

    /// This entry point is called when operating on a Swift package.
    func performCommand(context: PluginContext, arguments: [String]) throws {
        debugPrint(context)
    }
}

#if canImport(XcodeProjectPlugin)
import XcodeProjectPlugin

extension MyPlugin: XcodeCommandPlugin {

    /// This entry point is called when operating on an Xcode project.
    func performCommand(context: XcodePluginContext, arguments: [String]) throws {
        debugPrint(context)
    }
}
#endif
```

### Structure of a build tool plugin with conditional support for Xcode projects when running in Xcode — [11:13]

```swift
import PackagePlugin

@main
struct MyPlugin: BuildToolPlugin {

    /// This entry point is called when operating on a Swift package.
    func createBuildCommands(context: PluginContext, target: Target) throws -> [Command]
        debugPrint(context)
        return []
    }
}

#if canImport(XcodeProjectPlugin)
import XcodeProjectPlugin

extension MyPlugin: XcodeBuildToolPlugin {

    /// This entry point is called when operating on an Xcode project.
    func createBuildCommands(context: XcodePluginContext, target: XcodeTarget) throws -> [Command]
        debugPrint(context)
        return []
    }
}
#endif
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110359/6/0515ED86-51DB-430A-9521-E5DB4FC59C61/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110359/6/0515ED86-51DB-430A-9521-E5DB4FC59C61/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110359) — developer.apple.com. Indexed for agent consumption._
