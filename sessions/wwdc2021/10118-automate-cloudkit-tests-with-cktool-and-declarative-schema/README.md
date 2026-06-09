---
id: "wwdc2021-10118"
event: "wwdc2021"
year: 2021
title: "Automate CloudKit tests with cktool and declarative schema"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10118"
topics: ["System Services", "Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Automate CloudKit tests with cktool and declarative schema

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10118](https://developer.apple.com/videos/play/wwdc2021/10118)

It’s never been easier to test your CloudKit containers. We’ll introduce you to cktool, a command-line utility that makes quick work of CloudKit configuration, and learn about the new schema language that allows you to rapidly prototype and evolve containers. We’ll also show you how to combine these tools and configure your containers before running tests in Xcode. To get the most out of this session, we recommend being familiar with CloudKit and its development and production environments, as well as a basic understanding of record and data types.

**Keywords:** `cd`, `ci`, `cloud`, `command line`, `database`, `developer tool`, `mock data`, `mocking`, `schema`, `terminal`, `tool`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,798 words)

## Documentation & Resources

- [Automating CloudKit Development](https://developer.apple.com/icloud/cloudkit/automating/) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/icloud/cloudkit/automating/
- [Integrating a Text-Based Schema into Your Workflow](https://developer.apple.com/documentation/CloudKit/integrating-a-text-based-schema-into-your-workflow) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CloudKit/integrating-a-text-based-schema-into-your-workflow
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CloudKit/integrating-a-text-based-schema-into-your-workflow.json
- [CloudKit](https://developer.apple.com/documentation/CloudKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CloudKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CloudKit.json

## Code Snippets

### cktool: Save tokens, get teams — [3:27]

```bash
xcrun cktool save-token --type management

xcrun cktool save-token --type user

xcrun cktool get-teams
```

### cktool: Export schema — [3:45]

```bash
xcrun cktool export-schema \
  --team-id XYZ1234567 \
  --container-id iCloud.com.WWDC21.Example \
  --environment development \
  --output-file schema.ckdb
```

### cktool: Create record — [4:07]

```bash
xcrun cktool create-record \
  --team-id XYZ1234567 \
  --container-id iCloud.com.WWDC21.Example \
  --environment development \
  --database-type public \
  --record-type Book \
  --fields-json '{
       "title": { "type": "stringType", "value": "Treasure Island" },
       "pageCount": { "type": "int64Type", "value": 304 }
    }'
```

### cktool: Test pre-action script — [5:05]

```bash
xcrun cktool reset-schema \
    --team-id XYZ1234567 \
    --container-id iCloud.com.WWDC21.Example

xcrun cktool import-schema \
    --team-id XYZ1234567 \
    --container-id iCloud.com.WWDC21.Example \
    --environment development \
    --file $PROJECT_DIR/Example/CloudKitSchema.ckdb

xcrun cktool create-record \
    --team-id XYZ1234567 \
    --container-id iCloud.com.WWDC21.Example \
    --environment development \
    --database-type public \
    --record-type Book \
    --fields-json '{
       "title": { "type": "stringType", "value": "Great Expectations" },
       "pageCount": { "type": "int64Type", "value": 544 },
       "description": { "type": "stringType", "value": "Depiction of the education of an orphan nicknamed Pip" },
       "publishedOn": { "type": "timestampType", "value": "1860-12-01T03:23:07.415Z" },
       "reviewStatus": { "type": "int64Type", "value": 1 }
    }'
```

### Schema language file: Example — [5:51]

```swift
DEFINE SCHEMA
     RECORD TYPE Book (
        "___createTime" TIMESTAMP,
        "___createdBy"  REFERENCE,
        "___etag"       STRING,
        "___modTime"    TIMESTAMP,
        "___modifiedBy" REFERENCE,
        "___recordID"   REFERENCE QUERYABLE,
        description     STRING,
        pageCount       INT64,
        publishedOn     TIMESTAMP,
        reviewStatus    INT64,
        // A single-line comment, for humans
        title           STRING QUERYABLE,
        GRANT WRITE TO "_creator",
        GRANT CREATE TO "_icloud",
        GRANT READ TO "_world"
     );
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10118/4/9B80307B-4AD2-499D-81D9-ABD4D94DFE78/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10118/4/9B80307B-4AD2-499D-81D9-ABD4D94DFE78/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10118) — developer.apple.com. Indexed for agent consumption._
