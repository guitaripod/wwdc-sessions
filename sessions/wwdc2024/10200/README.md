---
id: "wwdc2024-10200"
event: "wwdc2024"
year: 2024
title: "Extend your Xcode Cloud workflows"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10200"
topics: ["Essentials", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Extend your Xcode Cloud workflows

**Event:** WWDC24 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-13 · **Session:** [wwdc2024-10200](https://developer.apple.com/videos/play/wwdc2024/10200)

Discover how Xcode Cloud can adapt to your development needs. We’ll show you how to streamline your workflows, automate testing and distribution with start conditions, custom aliases, custom scripts, webhooks, and the App Store Connect API.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,210 words)

## Documentation & Resources

- [Forum: Developer Tools & Services](https://developer.apple.com/forums/topics/developer-tools-and-services?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/developer-tools-and-services?cid=vf-a-0010
- [Sharing macOS and Xcode versions across Xcode Cloud workflows](https://developer.apple.com/documentation/Xcode/Sharing-custom-aliases-across-Xcode-Cloud-workflows) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Sharing-custom-aliases-across-Xcode-Cloud-workflows
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Sharing-custom-aliases-across-Xcode-Cloud-workflows.json
- [Configuring webhooks in Xcode Cloud](https://developer.apple.com/documentation/Xcode/Configuring-Webhooks-in-Xcode-Cloud) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Configuring-Webhooks-in-Xcode-Cloud
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Configuring-Webhooks-in-Xcode-Cloud.json
- [Environment variable reference](https://developer.apple.com/documentation/Xcode/Environment-Variable-Reference) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Environment-Variable-Reference
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Environment-Variable-Reference.json
- [Writing custom build scripts](https://developer.apple.com/documentation/Xcode/Writing-Custom-Build-Scripts) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Writing-Custom-Build-Scripts
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Writing-Custom-Build-Scripts.json
- [Configuring start conditions](https://developer.apple.com/documentation/Xcode/Configuring-Start-Conditions) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/Configuring-Start-Conditions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/Configuring-Start-Conditions.json

## Code Snippets

### Custom Script — [10:02]

```bash
#!/bin/sh

set -e

if [[ $CI_XCODEBUILD_ACTION == "test-without-building" && $CI_WORKFLOW_ID == "82D89C93-B69C-46B5-A794-A2BCFD3EE487" ]]
then
    curl https://example.com/health --fail
fi
```

### App Store Connect API - Client Extension — [14:01]

```swift
extension Client {
    func repoID(workflowID: String) async throws -> String {
        return try await ciWorkflowsGetInstance(
            path: .init(id: workflowID),
            query: .init(include: [.repository])
        ).ok.body.json.data.relationships!.repository!.data!.id
    }

    func branchID(repoID: String, name: String) async throws -> String {
        return try await scmRepositoriesGitReferencesGetToManyRelated(
            path: .init(id: repoID)
        )
        .ok.body.json.data
        .filter { $0.attributes!.kind == .BRANCH && $0.attributes!.name == name }
        .first!.id
    }

    func startBuild(workflowID: String, gitReferenceID: String) async throws {
        _ = try await ciBuildRunsCreateInstance(
            body: .json(.init(
                data: .init(
                    _type: .ciBuildRuns,
                    relationships: .init(
                        workflow: .init(data: .init(
                            _type: .ciWorkflows,
                            id: workflowID
                        )),
                        sourceBranchOrTag: .init(data: .init(
                            _type: .scmGitReferences,
                            id: gitReferenceID
                        ))
                    )
                )
            ))
        ).created
    }
}
```

### App Store Connect API - Main Function — [14:43]

```swift
static func main() async throws {
    let client = try Client(
        serverURL: Servers.server1(),
        configuration: .init(dateTranscoder: .iso8601WithFractionalSeconds),
        transport: URLSessionTransport(),
        middlewares: [AuthMiddleware(token: ProcessInfo.processInfo.environment["TOKEN"]!)]
    )

    let workflowID = "82D89C93-B69C-46B5-A794-A2BCFD3EE487"
    let repoID = try await client.repoID(workflowID: workflowID)

    let branchName = "main"
    let branchID = try await client.branchID(repoID: repoID, name: branchName)

    try await client.startBuild(workflowID: workflowID, gitReferenceID: branchID)
}
```

### Webhook Handler Implementation — [17:09]

```swift
struct WebhookPayload: Content {
    let ciWorkflow: CiWorkflow
    let ciBuildRun: CiBuildRun

    struct CiWorkflow: Content {
        let id: String
    }

    struct CiBuildRun: Content {
        let id: String
        let executionProgress: String
        let completionStatus: String
    }
}

func routes(_ app: Application) throws {
    let deploymentService = ExampleDeploymentClient()
    let workflowID = "82D89C93-B69C-46B5-A794-A2BCFD3EE487"

    app.post("webhook") { req async throws -> HTTPStatus in

        return HTTPStatus.ok
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10200/5/28E5AAA4-9AE8-427A-B577-512070861A1A/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10200/5/28E5AAA4-9AE8-427A-B577-512070861A1A/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10200) — developer.apple.com. Indexed for agent consumption._