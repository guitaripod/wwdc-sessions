---
id: "wwdc2022-10046"
event: "wwdc2022"
year: 2022
title: "Adopt declarative device management"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10046"
topics: ["Business & Education"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Adopt declarative device management

**Event:** WWDC22 · **Topic:** Business & Education · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10046](https://developer.apple.com/videos/play/wwdc2022/10046)

Discover how you can simplify development of your device management solution with the declarative approach. We’ll take you through the latest updates to platform support and explore protocol enhancements for status and predicates.

**Keywords:** `business`, `declarative`, `device management`, `education`, `enterprise`, `mdm`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,456 words)

## Documentation & Resources

- [Device Management](https://developer.apple.com/documentation/DeviceManagement) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/DeviceManagement
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/DeviceManagement.json

## Code Snippets

### Passcode status items — [7:41]

```json
{
  "management": {
    "client-capabilities": {
     "supported-payloads": {
       "status-items": [
          ...
          "passcode.is-compliant",
          "passcode.is-present",
          ...
        ]
      }
    }
  }
}
```

### Account status items — [10:52]

```json
{
  ...
      "status-items": [
          ...
          "account.list.caldav",
          "account.list.carddav",
          "account.list.exchange",
          "account.list.google",
          "account.list.ldap",
          "account.list.mail.incoming",
          "account.list.mail.outgoing",
          "account.list.subscribed-calendar",
          ...
        ]
  ...
}
```

### Mail and subscribed calendar status item objects — [11:19]

```json
{
  "identifier": "592D763E-C15B-44F8-A1FC-F88EB1901646",
  "declaration-identifier": "BF8FD199-467B-4BA5-886D-D82B7849E517",
  "hostname": "mail.example.com",
  "port": 443,
  "username": "user01",
  "is-mail-enabled": true,
  "are-notes-enabled": false
}

{
  "identifier": "592D763E-C15B-44F8-A1FC-F88EB1901646",
  "declaration-identifier": "BF8FD199-467B-4BA5-886D-D82B7849E517",
  "calendar-url": "https://holidays.example.com/country/US.ics",
  "username": "user01",
  "is-enabled": true
}
```

### MDM app status item — [17:13]

```json
{
  "management": {
    "client-capabilities": {
     "supported-payloads": {
       "status-items": [
          ...
          "mdm.app",
          ...
        ]
      }
    }
  }
}
```

### Status report with MDM app status item — [17:35]

```json
{
  "StatusItems": {
    "mdm": {
      "app": [
        {
          "identifier": "com.apple.Pages",
          "name": "Pages",
          "version": "7358.0.134",
          "short-version": “12.0",
          "external-version-id": "844362702",
          "state": "managed"
        }
      ]
    }
  },
  "Errors": []
}
```

### Predicate subquery using the MDM app status item — [22:15]

```markdown
SUBQUERY(@status(mdm.app),
         $app,
         ($app.@key(identifier) == "com.example.app") AND ($app.@key(state) == "managed")
        ).@count == 1
```

### Management properties declaration — [24:10]

```json
{
  "management": {
    "client-capabilities": {
     "supported-payloads": {
       "declarations": {
         ...
         "management": [
          ...
          "com.apple.management.properties",
          ...
         ]
         ...
        }
      }
    }
  }
}
```

### Management properties declaration object — [24:40]

```json
{
  "Type": "com.apple.management.properties",
  "Identifier": "AAE09D73-6EF6-4F3B-9E15-11B0F86D5591",
  "ServerToken": "AB4C5B91-3E08-4D4E-A9FF-1E44FE5BFDD4",
  "Payload": {
    "name": "Student One",
    "age": 7,
    "roles": ["grade1", "spanish"]
  }
}
```

### Activation with management properties predicate — [24:53]

```json
{
  "Type": "com.apple.activation.simple",
  "Identifier": "076F928B-9D8E-4BA2-AD34-5655805C82D7",
  "ServerToken": "4FFA91BF-85AE-4053-B8FE-B1C3E507A9CB",
  "Payload": {
    "StandardConfigurations": [
      "3BBB4407-238A-44B1-ABB1-5E7AB95160E0"
    ]
  },
  "Predicate": "(@property(age) >= 18) AND ("Grade12" IN @property(roles))"
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10046/3/776B5FA8-B8C0-46DA-9EDE-7A0BE5F03772/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10046/3/776B5FA8-B8C0-46DA-9EDE-7A0BE5F03772/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10046) — developer.apple.com. Indexed for agent consumption._
