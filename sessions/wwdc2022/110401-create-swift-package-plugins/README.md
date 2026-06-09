---
id: "wwdc2022-110401"
event: "wwdc2022"
year: 2022
title: "Create Swift Package plugins"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110401"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Create Swift Package plugins

**Event:** WWDC22 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-110401](https://developer.apple.com/videos/play/wwdc2022/110401)

Tailor your development workflow and learn how to write your own package plugins in Swift. We'll show you how you can extend Xcode’s functionality by using the PackagePlugin API to generate source code or automate release tasks and share best practices for creating great plugins.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,972 words)

## Code Snippets

### GenerateContributors plugin target — [3:40]

```swift
// MARK: Plugins

        .plugin(
            name: "GenerateContributors",
            capability: .command(
                intent: .custom(verb: "regenerate-contributors-list",
                                description: "Generates the CONTRIBUTORS.txt file based on Git logs"),
                permissions: [
                    .writeToPackageDirectory(reason: "This command write the new CONTRIBUTORS.txt to the source root.")
                ]
            )),
```

### GenerateContributors plugin implementation — [5:06]

```swift
import PackagePlugin
import Foundation

@main
struct GenerateContributors: CommandPlugin {

    func performCommand(
        context: PluginContext,
        arguments: [String]
    ) async throws {
        let process = Process()
        process.executableURL = URL(fileURLWithPath: "/usr/bin/git")
        process.arguments = ["log", "--pretty=format:- %an <%ae>%n"]

        let outputPipe = Pipe()
        process.standardOutput = outputPipe
        try process.run()
        process.waitUntilExit()

        let outputData = outputPipe.fileHandleForReading.readDataToEndOfFile()
        let output = String(decoding: outputData, as: UTF8.self)

        let contributors = Set(output.components(separatedBy: CharacterSet.newlines)).sorted().filter { !$0.isEmpty }
        try contributors.joined(separator: "\n").write(toFile: "CONTRIBUTORS.txt", atomically: true, encoding: .utf8)
    }
}
```

### Minimum Deployment Target — [10:28]

```swift
platforms: [
            .macOS("10.15"),
            .iOS("12.0"),
            .tvOS("12.0"),
            .watchOS("6.0"),
        ],
```

### Basic SwiftUI view and preview — [10:35]

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        Image("Xcode", bundle: .module)
            .resizable()
            .frame(width: 200.0, height: 200.0)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
```

### AssetConstantsExec executable target — [14:56]

```swift
.executableTarget(name: "AssetConstantsExec"),
```

### AssetConstantsExec implementation — [15:03]

```swift
import Foundation

let arguments = ProcessInfo().arguments
if arguments.count < 3 {
    print("missing arguments")
}
let (input, output) = (arguments[1], arguments[2])

struct Contents: Decodable {
    let images: [Image]
}

struct Image: Decodable {
    let filename: String?
}

var generatedCode = """
    import Foundation
    import SwiftUI

    """

try FileManager.default.contentsOfDirectory(atPath: input).forEach { dirent in
    guard dirent.hasSuffix("imageset") else {
        return
    }

    let contentsJsonURL = URL(fileURLWithPath: "\(input)/\(dirent)/Contents.json")
    let jsonData = try Data(contentsOf: contentsJsonURL)
    let asset🐱alogContents = try JSONDecoder().decode(Contents.self, from: jsonData)
    let hasImage = asset🐱alogContents.images.filter { $0.filename != nil }.isEmpty == false

    if hasImage {
        let basename = contentsJsonURL.deletingLastPathComponent().deletingPathExtension().lastPathComponent
        generatedCode.append("public let \(basename) = Image(\"\(basename)\", bundle: .module)\n")
    }
}

try generatedCode.write(to: URL(fileURLWithPath: output), atomically: true, encoding: .utf8)
```

### AssetConstantsExec plugin target — [15:48]

```swift
.plugin(name: "AssetConstants", capability: .buildTool(), dependencies: ["AssetConstantsExec"]),
```

### AssetConstantsExec plugin implementation — [16:12]

```swift
guard let target = target as? SourceModuleTarget else {
                    return []
                }

        return try target.sourceFiles(withSuffix: "xcassets").map { asset🐱alog in
                    let base = asset🐱alog.path.stem
                    let input = asset🐱alog.path
                    let output = context.pluginWorkDirectory.appending(["\(base).swift"])

                    return .buildCommand(displayName: "Generating constants for \(base)",
                                         executable: try context.tool(named: "AssetConstantsExec").path,
                                         arguments: [input.string, output.string],
                                         inputFiles: [input],
                                         outputFiles: [output])
                }
```

### GenstringsPlugin target — [20:19]

```swift
.plugin(name: "GenstringsPlugin", capability: .buildTool()),
```

### GenstringsPlugin product — [20:26]

```swift
.plugin(name: "GenstringsPlugin", targets: ["GenstringsPlugin"]),
```

### GenstringsPlugin implementation — [20:44]

```swift
guard let target = target as? SourceModuleTarget else {
                    return []
                }

        let resourcesDirectoryPath = context.pluginWorkDirectory
                    .appending(subpath: target.name)
                    .appending(subpath: "Resources")
                let localizationDirectoryPath = resourcesDirectoryPath
                    .appending(subpath: "Base.lproj")

                try FileManager.default.createDirectory(atPath: localizationDirectoryPath.string, withIntermediateDirectories: true)

        let swiftSourceFiles = target.sourceFiles(withSuffix: ".swift")
                let inputFiles = swiftSourceFiles.map(\.path)

        return [
                    .prebuildCommand(
                        displayName: "Generating localized strings from source files",
                        executable: .init("/usr/bin/xcrun"),
                        arguments: [
                            "genstrings",
                            "-SwiftUI",
                            "-o", localizationDirectoryPath
                        ] + inputFiles,
                        outputFilesDirectory: localizationDirectoryPath
                    )
                ]
```

### Localized string API — [21:10]

```swift
import Foundation

public func GetLocalizedString() -> String {
    return NSLocalizedString("World", comment: "A comment about the localizable string")
}
```

### Path-based dependency on GenstringsPlugin — [21:44]

```swift
.package(path: "../GenstringsPlugin"),
```

### Use of GenstringsPlugin in library target — [21:52]

```swift
plugins: [ .plugin(name: "GenstringsPlugin", package: "GenstringsPlugin"), ]
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110401/6/E6B6BDA3-C922-4FC4-AF6B-EB6C290568A7/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110401/6/E6B6BDA3-C922-4FC4-AF6B-EB6C290568A7/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110401) — developer.apple.com. Indexed for agent consumption._
