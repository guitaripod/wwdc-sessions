---
id: "wwdc2020-10047"
event: "wwdc2020"
year: 2020
title: "Enable encrypted DNS"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10047"
topics: ["System Services"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Enable encrypted DNS

**Event:** WWDC20 · **Topic:** System Services · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10047](https://developer.apple.com/videos/play/wwdc2020/10047)

When people access the web within your app, their privacy is paramount. Safeguard that information by leveraging encrypted DNS across our platforms to deliver private and secure connectivity within your app. Discover how you can use system DNS settings to connect to encrypted servers or enable encrypted DNS within an app using standard networking APIs.

Enabling encrypted DNS is yet another way your app can help preserve privacy for your customers and provide them with a better and more secure experience.

**Keywords:** `fingerprinting`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,618 words)

## Code Snippets

### Create a DNS configuration — [4:16]

```swift
// Create a DNS configuration

import NetworkExtension

NEDNSSettingsManager.shared().loadFromPreferences { loadError in
    if let loadError = loadError {
        // ...handle error...
        return
    }
    let dohSettings = NEDNSOverHTTPSSettings(servers: [ "2001:db8::2" ])
    dohSettings.serverURL = URL(string: "https://dnsserver.example.net/dns-query")
    NEDNSSettingsManager.shared().dnsSettings = dohSettings
    NEDNSSettingsManager.shared().saveToPreferences { saveError in
        if let saveError = saveError {
            // ...handle error...
            return
        }
    }
}
```

### Apply network rules — [6:40]

```swift
// Apply network rules

let workWiFi = NEOnDemandRuleEvaluateConnection()
workWiFi.interfaceTypeMatch = .wiFi
workWiFi.ssidMatch = ["MyWorkWiFi"]
workWiFi.connectionRules =
    [ NEEvaluateConnectionRule(matchDomains: ["enterprise.example.net"],
                               andAction: .neverConnect) ]

let disableOnCell = NEOnDemandRuleDisconnect()
disableOnCell.interfaceTypeMatch = .cellular

let enableByDefault = NEOnDemandRuleConnect()

NEDNSSettingsManager.shared().onDemandRules = [
    workWiFi,
    disableOnCell,
    enableByDefault
]
```

### Use encrypted DNS with NWConnection — [10:47]

```swift
// Use encrypted DNS with NWConnection

import Network

let privacyContext = NWParameters.PrivacyContext(description: "EncryptedDNS")
if let url = URL(string: "https://dnsserver.example.net/dns-query") {
    let address = NWEndpoint.hostPort(host: "2001:db8::2", port: 443)
    privacyContext.requireEncryptedNameResolution(true,
        fallbackResolver: .https(url, serverAddresses: [ address ]))
}

let tlsParams = NWParameters.tls
tlsParams.setPrivacyContext(privacyContext)

let conn = NWConnection(host: "www.example.com", port: 443, using: tlsParams)
conn.start(queue: .main)
```

### Validate which DNS protocol was used — [11:35]

```swift
// Validate which DNS protocol was used

import Network

conn.requestEstablishmentReport(queue: .main) { report in
    if let report = report {
        for resolution in report.resolutions {
            switch resolution.dnsProtocol {
            case .https, .tls:
                print("Used encrypted DNS!”)
            case .udp, .tcp:
                print("Used unencrypted DNS")
            default:
                // Ignore unknown protocols
       }
    }
}
```

### Use encrypted DNS for other APIs — [12:07]

```swift
// Use encrypted DNS for other APIs

import Network

if let url = URL(string: "https://dnsserver.example.net/dns-query") {
    let address = NWEndpoint.hostPort(host: "2001:db8::2", port: 443)
    NWParameters.PrivacyContext.default.requireEncryptedNameResolution(true,
        fallbackResolver: .https(url, serverAddresses: [ address ]))
}

let task = URLSession.shared.dataTask(with: ...)
task.resume()

getaddrinfo(...)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10047/4/01915145-ACB0-4244-86DA-2FBCCFEC9B58/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10047) — developer.apple.com. Indexed for agent consumption._