---
id: "wwdc2021-10137"
event: "wwdc2021"
year: 2021
title: "Improve MDM assignment of Apps and Books"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10137"
topics: ["App Store, Distribution & Marketing", "Business & Education"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Improve MDM assignment of Apps and Books

**Event:** WWDC21 · **Topic:** Business & Education · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10137](https://developer.apple.com/videos/play/wwdc2021/10137)

Discover the Apps and Books Management API and explore how you can assign an organization’s owned apps and books to managed users and devices. Learn about the latest API improvements and find out how you can subscribe to and receive notifications around asset counts, assignments, and registered users in your organization. And discover how you can take advantage of asynchronous processing to significantly reduce the number of requests you need to make for large assignments.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,335 words)

## Documentation & Resources

- [Apple School Manager User Guide](https://support.apple.com/guide/apple-school-manager/) _documentation_
- [Apple Business Manager User Guide](https://support.apple.com/guide/apple-business-manager/) _guide_

## Code Snippets

### Asset Management Notification — [2:43]

```json
{
    "notification": {
        "assignments": [
            {
                "adamId": "408709785",
                "pricingParam": "STDQ",
                "serialNumber": "C02Y402HLCM6"
            },
            ...
        ],
        "eventId": "87cbc650-16cc-4f9e-a833-e622f377a9f7",
        "result": "SUCCESS",
        "type": "ASSOCIATE"
    },
    "notificationId": "ba8bbb23-44c2-44f6-a928-eff6ba5ffac3",
    "notificationType": "ASSET_MANAGEMENT",
    "uId": "2049025000431439"
}
```

### Get Assets Response — [4:39]

```json
{
    "assets": [
        {
            "adamId": "408709785",
            "pricingParam": "STDQ",
            "assignedCount": 5000,
            "availableCount": 10000,
            "totalCount": 15000,
            ...
        }
    ],
    "currentPageIndex": 0,
    "size": 1,
    "totalPages": 1,
    ...
}
```

### Asset Count Notification — [5:09]

```json
{
    "notification": {
        "adamId": "408709785",
        "countDelta": 50,
        "pricingParam": "STDQ"
    },
    "notificationId": "4a7801be-53f0-42e1-9505-81c0d1dc9da3",
    "notificationType": "ASSET_COUNT",
    "uId": "2049025000431439"
}
```

### Get Users Response — [6:51]

```json
{
    "currentPageIndex": 0,
    "size": 1,
    "totalPages": 1,
    "users": [
        {
            "clientUserId": "client-100",
            "email": "client-100@example.com",
            "inviteCode": "f551b37da07146628e8dcbe0111f0364",
            "status": "Registered"
        }
    ],
    "versionId": "58507d60-9cd1-11eb-b916-1926dea207f9",
    ...
}
```

### User Management Notification — [7:49]

```json
{
    "notification": {
        "users": [
            {
                "clientUserId": "client-100",
                "idHash": "leSKk3IaE2vk2KLmv2k3/200D3=",
                "status": "Associated",
                ...
            },
            ...
        ],
        "eventId": "e0def1f8-9158-4343-9c52-8dd32da50b9b",
        "result": "SUCCESS",
        "type": "UPDATE"
    },
    "notificationId": "4c0bbb9b-d5a6-4860-83ef-5cf362783c1e",
    "notificationType": "USER_MANAGEMENT",
    "uId": "2049025000431439"
}
```

### User Associated Notification — [8:33]

```json
{
    "notification": {
        "associatedUsers": [
            {
                "clientUserId": "client-100",
                "idHash": "leSKk3IaE2vk2KLmv2k3/200D3=",
                "inviteCode": "f551b37da07146628e8dcbe0111f0364",
                "status": "Associated",
                ...
            }
        ]
    },
    "notificationId": "90b83144-fb93-4837-9c52-0ae147bdc421",
    "notificationType": "USER_ASSOCIATED",
    "uId": "2049025000431439"
}
```

### Associate Assets Request — [12:25]

```json
{
    "assets": [
      {
        "adamId": "361309726",
        "pricingParam": "STDQ"
      },
      ...
    ],
    "serialNumbers": [
      "serial-1",
      ...
      "serial-1000"
    ]
}
```

### Associate Assets Response — [12:51]

```json
{
    "eventId": "92467a8e-8a50-4df9-9b30-f7ff4a99dea7",
    "tokenExpirationDate": "2021-07-06T14:12:10+0000",
    "uId": "2049025000431439"
}
```

### Asset Management Notification — [13:24]

```json
{
    "notification": {
        "assignments": [
            {
                "adamId": "361309726",
                "pricingParam": "STDQ",
                "serialNumber": "serial-1"
            },
            ...
        ],
        "eventId": "92467a8e-8a50-4df9-9b30-f7ff4a99dea7",
        "result": "SUCCESS",
        "type": "ASSOCIATE"
    },
    ...
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10137/7/FB724053-0CDB-4228-A9A7-CA326DC41FBE/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10137/7/FB724053-0CDB-4228-A9A7-CA326DC41FBE/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10137) — developer.apple.com. Indexed for agent consumption._
