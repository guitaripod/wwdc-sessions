---
id: "wwdc2022-10045"
event: "wwdc2022"
year: 2022
title: "What's new in managing Apple devices"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10045"
topics: ["Business & Education"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# What's new in managing Apple devices

**Event:** WWDC22 · **Topic:** Business & Education · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10045](https://developer.apple.com/videos/play/wwdc2022/10045)

Explore enhancements to device management across Apple platforms. Improve device deployment workflows using the latest version of Apple Configurator for iPhone. Learn about identity technologies and MDM protocol updates for macOS, iOS and iPadOS. We'll also share an exciting change in how we provide device management documentation.

**Keywords:** `configuration`, `configurator`, `dns`, `education`, `enrollment`, `enterprise`, `esim`, `identity`, `idp`, `management`, `mdm`, `networking`, `oauth`, `privacy`, `profile`, `profiles`, `security`, `shared ipad`, `software update`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,510 words)

## Documentation & Resources

- [Device Management Client Schema on GitHub](http://github.com/apple/device-management) _documentation_
- [Apple Configurator User Guide for iPhone](https://support.apple.com/guide/apple-configurator/) _documentation_
- [Apple Platform Security](https://support.apple.com/guide/security/welcome/web) _documentation_
- [AppleSeed](https://appleseed.apple.com/) _documentation_
- [Device Management](https://developer.apple.com/documentation/DeviceManagement) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/DeviceManagement
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/DeviceManagement.json
- [Apple Platform Deployment](https://support.apple.com/guide/deployment/) _documentation_

## Code Snippets

### Enrollment SSO — [9:12]

```json
{
  "iTunesStoreID": 12345678,
  "AssociatedDomains": [
    "betterbag.com"
  ],
  "AssociatedDomainsEnableDirectDownloads": false,
  "ConfigurationProfile": "Base64EncodedProfile"
}
```

### Enrollment SSO Test Mode — [11:02]

```json
{
  "AppIDs": [
"ABC123.com.example.singlesignonapp"
  ],
  "AssociatedDomains": [
    "betterbag.com"
  ],
  "AssociatedDomainsEnableDirectDownloads": false,
  "ConfigurationProfile": "Base64EncodedProfile"
}
```

### OS Update Status — [16:08]

```xml
<key>DeferralsRemaining</key>
<integer>4</integer>
<key>DownloadPercentComplete</key>
<real>0.0</real>
<key>IsDownloaded</key>
<false/>
<key>MaxDeferrals</key>
<integer>5</integer>
<key>NextScheduledInstall</key>
<date>2022-04-19T09:00:00Z</date>
<key>PastNotifications</key>
<array>
	<date>2022-04-18T17:03:51Z</date>
</array>
<key>ProductKey</key>
<string>MSU_UPDATE_22A240a_full_13.0_minor</string>
<key>ProductVersion</key>
<string>16.0</string>
```

### Web Content Filter Profile — [22:38]

```xml
<plist version="1.0">
<dict>
	<key>PayloadContent</key>
	<array>
		<dict>
			<key>PayloadType</key>
			<string>com.apple.webcontent-filter</string>
			<key>ContentFilterUUID</key>
			<string>063D927E-ACE2-445F-8024-B355A6921F50</string>
			<key>FilterType</key>
			<string>Plugin</string>
			<key>FilterBrowsers</key>
			<true/>
			<key>FilterPackets</key>
			<false/>
			<key>FilterSockets</key>
			<true/>
			…
```

### DNS Proxy Profile — [22:47]

```xml
<plist version="1.0">
<dict>
	<key>PayloadContent</key>
	<array>
		<dict>
			<key>PayloadType</key>
			<string>com.apple.dnsProxy.managed</string>
			<key>DNSProxyUUID</key>
			<string>063D927E-ACE2-445F-8024-B355A6921F50</string>
			<key>AppBundleIdentifier</key>
			<string>com.example.myDNSProxy</string>
			…
```

### InstallApplication Command — [23:05]

```xml
<plist version="1.0">
<dict>
	<key>RequestType</key>
	<string>InstallApplication</string>
	<key>iTunesStoreID</key>
	<integer>361309726</integer>
	<key>Attributes</key>
	<dict>
		<key>ContentFilterUUID</key>
		<string>063D927E-ACE2-445F-8024-B355A6921F50</string>
       <key>DNSProxyUUID</key>
		<string>063D927E-ACE2-445F-8024-B355A6921F50</string>
	</dict>
	<key>ManagementFlags</key>
	<integer>0</integer>
</dict>
</plist>
```

### ServiceSubscriptions response — [24:56]

```json
{
	"CarrierSettingsVersion": "41.7.46",
	"CurrentCarrierNetwork": "CarrierNetwork",
	"CurrentMCC": "310",
	"CurrentMNC": "410",
	"EID": "89049032004008882600004821436874",
	"ICCID": "6905 4911 1205 0650 3488",
	"IMEI": "35 309418 464558 9",
	"IsDataPreferred": false,
	"IsRoaming": false,
	"IsVoicePreferred": false,
	"Label": "Secondary",
	"LabelID": "FDG4225C-L9OY-89BM-JF38-36JR4JOL76B3",
	"MEID": "35745008005631",
	"PhoneNumber": "+14152739164",
	"Slot": "CTSubscriptionSlotTwo"
}
```

### Manage Accessibility Settings — [31:48]

```xml
<key>Settings</key>
<array>
	<dict>
		<key>Item</key>
		<string>AccessibilitySettings</string>
		<key>TextSize</key>
		<integer>5</integer>
		<key>VoiceOverEnabled</key>
		<true/>
		<key>ZoomEnabled</key>
		<true/>
		<key>TouchAccommodationsEnabled</key>
		<true/>
		<key>BoldTextEnabled</key>
		<true/>
		<key>ReduceMotionEnabled</key>
		<true/>
		<key>IncreaseContrastEnabled</key>
		<true/>
		<key>ReduceTransparencyEnabled</key>
		<true/>
	</dict>
</array>
```

### CertificateList Response — [32:55]

```xml
<plist version="1.0">
<dict>
	<key>CommandUUID</key>
	<string>0001_CertificateList</string>
	<key>Status</key>
	<string>NotNow</string>
	<key>UDID</key>
	<string>00008031-000123840A45507E</string>
</dict>
</plist>
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10045/3/F899BEB5-EBE4-422E-AE52-AEF752A194A0/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10045/3/F899BEB5-EBE4-422E-AE52-AEF752A194A0/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10045) — developer.apple.com. Indexed for agent consumption._