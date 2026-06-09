---
id: "wwdc2022-10116"
event: "wwdc2022"
year: 2022
title: "Meet CKTool JS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10116"
topics: ["Safari & Web", "System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Meet CKTool JS

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10116](https://developer.apple.com/videos/play/wwdc2022/10116)

Discover how you can manage and automate your iCloud containers using CKTool JS. We’ll show you how to configure CKTool JS to manage your containers’ schemas, modify records with ease, and manipulate data on the fly. We’ll also explore how you can integrate CKTool JS into your automation and tooling workflows. To get the most out of this session, we recommend familiarity with CloudKit schemas, JavaScript, and npm.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,446 words)

## Documentation & Resources

- [CloudKit Samples: Tooling](https://github.com/apple/sample-cloudkit-tooling) _samplecode_
- [CKTool JS](https://developer.apple.com/documentation/CKToolJS) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CKToolJS
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CKToolJS.json
- [Integrating a Text-Based Schema into Your Workflow](https://developer.apple.com/documentation/CloudKit/integrating-a-text-based-schema-into-your-workflow) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/CloudKit/integrating-a-text-based-schema-into-your-workflow
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/CloudKit/integrating-a-text-based-schema-into-your-workflow.json

## Code Snippets

### Create security and default arguments objects — [6:43]

```javascript
// Create security object and setup default args

const { CKEnvironment } = require("@apple/cktool.database");

const security = {
    "ManagementTokenAuth": "<YOUR_MANAGEMENT_TOKEN>",
    "UserTokenAuth": "<YOUR_USER_TOKEN>"
};

const defaultArgs = {
    "teamId": "<YOUR_TEAM_ID>",
    "containerId": "<YOUR_CONTAINER_ID>",
    "environment": CKEnvironment.DEVELOPMENT
};
```

### Create configuration and API objects — [7:17]

```javascript
// Create configuration and API objects

const { createConfiguration } = require("@apple/cktool.target.nodejs");
const { PromisesApi } = require("@apple/cktool.database");

const configuration = createConfiguration();
const api = new PromisesApi({
    "configuration": configuration,
    "security": security
});
```

### Reset to production and import schema — [10:00]

```javascript
// Create a function to apply a schema

const { File } = require("@apple/cktool.target.nodejs");
const fs = require("fs/promises");
const path = require("path");

const importMySchema = async () => {
    const schemaPath = "<YOUR_SCHEMA_FILE>.ckdb";
    const buffer = await fs.readFile(schemaPath);
    const file = new File([buffer], schemaPath);
    await api.importSchema({ ...defaultArgs, "file": file });
}

// Chain the calls
api.resetToProduction(defaultArgs)
  .then(() => importMySchema());
```

### Factory functions — [11:36]

```javascript
// Create fields with factory functions.

const {
    makeRecordFieldValue
} = require("@apple/cktool.database");

const value = makeRecordFieldValue.int64(2007);
```

### Create database arguments object — [12:02]

```javascript
// Create a database arguments object.

const {
    CKDatabaseType, CKEnvironment
} = require("@apple/cktool.database");

const databaseArgs = {
    "containerID": "<YOUR_CONTAINER_ID>",
    "environment": CKEnvironment.DEVELOPMENT,
    "databaseType": CKDatabaseType.PRIVATE,
    "zoneName": "_defaultZone"
};
```

### Query for records — [12:16]

```javascript
// Define helper function for querying records

const { CKDBQueryFilterType } = require("@apple/cktool.database");
const countryQueryRecordForCountryCode3 = async (countryCode3) => {
    const response = await api.queryRecords({
        ...databaseArgs,
        "body": {
            "query": {
                "recordType": "Countries",
                "filters": [{
                    "fieldName": "isoCode3",
                    "fieldValue": makeRecordFieldValue.string(countryCode3),
                    "type": CKDBQueryFilterType.EQUALS
                }]
            }
        }
    });
    return response.result.records[0];
}
```

### Create field values — [12:58]

```javascript
// Define a helper function for creating field values

const {
    makeRecordFieldValue, CKDBRecordReferenceAction
} = require("@apple/cktool.database");

const makeCoinFieldValues = ({ countryRecordName, issueYear, nominalValue }) => ({
    "country": makeRecordFieldValue.reference({
        recordName: countryRecordName,
        action: CKDBRecordReferenceAction.DELETE_SELF
    }),
    "issueYear": makeRecordFieldValue.int64(issueYear),
    "nominalValue": makeRecordFieldValue.double(nominalValue)
});
```

### Create a record — [13:26]

```javascript
// Define helper method for creating coins

const coinCreateRecord = async (fields) => {
    const response = await api.createRecord({
        ...databaseArgs,
        "body": {
            "recordType": "Coins",
            "fields": fields
        },
    });
    return response.result.record;
}
```

### Call record creation helper method — [13:48]

```javascript
// Call coin creation method with field values

const countryRecord = await countryQueryRecordForCountryCode3("USA");

const coinRecord1 = await coinCreateRecord(
    makeCoinFieldValues({
        "countryRecordName": countryRecord.recordName,
        "issueYear": 2007,
        "nominalValue": 0.10
    })
);
```

### Define update record helper function — [14:16]

```javascript
// Define helper method for updating coins.
// Note that recordChangeTag is required

const coinUpdate =
    async (recordName, recordChangeTag, fields) => {
        const response = await api.updateRecord({
            ...databaseArgs,
            "recordName": recordName,
            "body": {
                "recordType": "Coins",
                "recordChangeTag": recordChangeTag,
                "fields": fields
            }
        });
        return response.result.record;
    }
```

### Update a record with field values — [14:44]

```javascript
// Call coin updating method with field values.
// Note that the recordChangeTag of the record
// to update is passed to the coin update function.

const countryRecord = await countryQueryRecordForCountryCode3("USA");
const updatedCoinRecord1 = await coinUpdate(
    coinRecord1.recordName,
    coinRecord1.recordChangeTag,
    makeCoinFieldValues({
        "countryRecordName": countryRecord.recordName,
        "issueYear": 2010,
        "nominalValue": 0.10
    });
);
```

### Delete a record — [14:57]

```javascript
// Deleting a record

await api.deleteRecord({
    ...databaseArgs,
   "recordName": coinRecord1.recordName
});
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10116/5/1DD917FC-5154-4B41-93E7-4D8731FB6D2E/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10116/5/1DD917FC-5154-4B41-93E7-4D8731FB6D2E/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10116) — developer.apple.com. Indexed for agent consumption._
