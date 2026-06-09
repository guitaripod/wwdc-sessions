---
id: "wwdc2026-216"
event: "wwdc2026"
year: 2026
title: "Create web extensions for Safari"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/216"
topics: ["App Store, Distribution & Marketing", "Safari & Web"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Create web extensions for Safari

**Event:** WWDC26 · **Topic:** Safari & Web · **Platforms:** iOS, iPadOS, macOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-216](https://developer.apple.com/videos/play/wwdc2026/216)

Get started with Safari web extensions by building and testing one from the ground up — no Xcode required. Explore how content blocking, page modification, native messaging, and the permissions mode work together to create a powerful, privacy-preserving browsing experience across platforms.

**Keywords:** `app store connect`, `css`, `html`, `javascript`, `json`, `safari`, `web extensions`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,967 words)

## Documentation & Resources

- [w3.org — W3C WebExtensions Community Group](https://www.w3.org/community/webextensions/) _documentation_
- [Packaging and distributing Safari Web Extensions with App Store Connect](https://developer.apple.com/documentation/SafariServices/packaging-and-distributing-safari-web-extensions-with-app-store-connect) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SafariServices/packaging-and-distributing-safari-web-extensions-with-app-store-connect
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SafariServices/packaging-and-distributing-safari-web-extensions-with-app-store-connect.json
- [WebKit.org – Report issues to the WebKit open-source project](https://bugs.webkit.org) _documentation_
- [Submit feedback](http://feedbackassistant.apple.com) _documentation_
- [MDN Web Docs - Web Extensions API](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API) _documentation_

## Code Snippets

### Manifest file — [3:44]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0
}
```

### Adding an extension icon — [4:29]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "icons": {
        "512": "images/icon.svg"
    }
}
```

### Adding an action button — [5:30]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "action": {
        "default_popup": "popup.html"
    }
}
```

### Adding custom UI to your extension — [6:17]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "options_ui": {
        "page": "options.html"
    }
}
```

### Including the UI in the extension manifest — [6:30]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "icons": {
        "512": "images/icon.svg"
    },

    "options_ui": {
        "page": "options.html"
    }
}
```

### Hello World — [6:40]

```xml
<!DOCTYPE html>
<html>
    <body>
    <p>Hello World</p>
    </body>
</html>
```

### Adding declarativeNetRequest permission — [8:18]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "icons": {
        "512": "images/icon.svg"
    },

    "options_ui": {
        "page": "options.html"
    },

    "permissions": [ "declarativeNetRequest" ]
}
```

### Blocking network requests — [8:22]

```javascript
// block rule
{
    id: 1,
    priority: 1,
    action: {
        type: "block"
    },
    condition: {
        urlFilter: "||webkit.org",
        resourceTypes: [ "main_frame" ]
    }
}
```

### Modifying network requests — [8:41]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "icons": {
        "512": "images/icon.svg"
    },

    "options_ui": {
        "page": "options.html"
    },

    "permissions": [ "declarativeNetRequest" ],

    "declarativeNetRequest": {
        "rule_resources": [
            {
                "id": "ruleset_id",
                "enabled": true,
                "path": "rules.json"
            }
        ]
    }
}
```

### Updating dynamic rules — [8:50]

```javascript
await browser.declarativeNetRequest.updateDynamicRules({
    addRules: [ rule ]
})
```

### Wiring up the static declarativeNetRequest rules — [9:19]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "icons": {
        "512": "images/icon.svg"
    },

    "options_ui": {
        "page": "options.html"
    },

    "permissions": [ 
      "declarativeNetRequest" 
    ]
}
```

### Adding block rules dynamically — [9:40]

```javascript
// A helper function to map the host to the declarative net request rule ID.
export function hostToRuleID(host) {
	let hash = 0;
	for (let i = 0; i < host.length; i++) {
		hash = ((hash << 5) + hash) + host.charCodeAt(i);
		hash |= 0;
	}
	return Math.abs(hash) || 1;
}

function createBlockRule(host) {
	return {
		id: hostToRuleID(host),
		priority: 1,
		action: {
			type: "block"
		},
		condition: {
			urlFilter: `||${host}`,
			resourceTypes: ["main_frame"]
		}
	}
}

export async function createRules(hosts) {
	try {
		await browser.declarativeNetRequest.updateDynamicRules({
			addRules: hosts.map(createBlockRule)
		})
	} catch {
		console.log("Failed to create declarative net request rules")
	}
}
```

### Handling adding hosts to the settings — [10:10]

```javascript
import { createRules, removeAllRules, removeRule } from './rules.js'

export async function addHost(host, blockingMode) {
  if (!host)
    return

  if (blockingMode === "full")
    await createRules([host])
}
```

### Redirecting network requests — [10:48]

```javascript
{
    id: 1,
    priority: 1,
    action: {
        type: "redirect",
        redirect: {
            extensionPath: "/blocked.html"
        }
    },
    condition: {
        urlFilter: "||webkit.org",
        resourceTypes: [ "main_frame" ]
    }
}
```

### Declaring optional host permissions — [11:17]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "icons": {
        "512": "images/icon.svg"
    },

    "options_ui": {
        "page": "options.html"
    },

    "permissions": [ "declarativeNetRequestWithHostAccess" ],
    "optional_host_permissions": [ "https://webkit.org/*" ]

}
```

### Declaring optional host permissions for all sites — [11:54]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "icons": {
        "512": "images/icon.svg"
    },

    "options_ui": {
        "page": "options.html"
    },

    "permissions": [ "declarativeNetRequestWithHostAccess" ],
    "optional_host_permissions": [ "*://*/*" ]

}
```

### Add the redirect rule — [13:12]

```javascript
// A helper function to map the host to the declarative net request rule ID.
export function hostToRuleID(host) {
	let hash = 0;
	for (let i = 0; i < host.length; i++) {
		hash = ((hash << 5) + hash) + host.charCodeAt(i);
		hash |= 0;
	}
	return Math.abs(hash) || 1;
}

function createBlockRule(host) {
	return {
		id: hostToRuleID(host),
		priority: 1,
		action: {
			type: "block"
		},
		condition: {
			urlFilter: `||${host}`,
			resourceTypes: ["main_frame"]
		}
	}
}

function createRedirectRule(host) {
	return {
		id: hostToRuleID(host),
		priority: 1,
		action: {
			type: "redirect",
			redirect: { extensionPath: "/blocked.html" }
		},
		condition: {
			urlFilter: `||${host}`,
			resourceTypes: ["main_frame"]
		}
	}
}

export async function createRules(hosts) {
	try {
		await browser.declarativeNetRequest.updateDynamicRules({
			addRules: hosts.map(createRedirectRule)
		})
	} catch {
		console.log("Failed to create declarative net request rules")
	}
}
```

### Dynamically ask for host permissions — [13:42]

```javascript
import { createRules, removeAllRules, removeRule } from './rules.js'

export async function addHost(host, blockingMode) {
  if (!host)
    return

  const granted = await browser.permissions.request({
    origins: [`*://${host}/*`, `*://*.${host}/*`]
  })
  if (!granted)
    return

  if (blockingMode === "full")
    await createRules([host])
}
```

### Defining content scripts — [14:55]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "icons": {
        "512": "images/icon.svg"
    },

    "options_ui": {
        "page": "options.html"
    },

    "permissions": [ "declarativeNetRequestWithHostAccess" ],
    "optional_host_permissions": [ "*://*/*" ],

    "content_scripts": [
        {
            "js": [ "content.js" ],
            "css": [ "content.css" ],
            "matches": [ "*://*.webkit.org/*" ]
        }
    ]
}
```

### Dynamically registering content scripts — [15:13]

```javascript
let script = {
    id: "id",
    js: [ "content.js" ],
    css: [ "content.css" ],
    matches: [ "*://*.webkit.org/*" ],
    persistAcrossSessions: true
}

await browser.scripting.registerContentScripts([ script ])
```

### Adding the scripting permission — [15:31]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "icons": {
        "512": "images/icon.svg"
    },

    "options_page": "options.html",

    "permissions": [
        "declarativeNetRequestWithHostAccess",
        "scripting"
    ],

    "optional_host_permissions": [ "*://*/*" ]
}
```

### Registering content scripts — [15:41]

```javascript
// scripting.js

function contentScript(host) {
    return {
        id: `cs-${host}`,
        js: [ "content.js" ],
        css: [ "content.css" ],
        matches: [ `*://${host}/*`, `*://*.${host}/*` ],
        persistAcrossSessions: true
    }
}

export function registerScripts(hosts) {
    const scripts = hosts.map(contentScript)
    try {
        await browser.scripting.registerContentScripts(scripts)
    } catch {
        console.log("Failed to register content scripts")
    }
}
```

### Adding a host — [16:02]

```javascript
// host.js

export async function addHost(host, blockMode) {
    if (!host)
        return

    const granted = await browser.permissions.request({
        origins: [`*://${host}/*`, `*://*.${host}/*`]
    })

    if (!granted)
        return

    if (blockingMode === "full")
        await createRules([ host ])

    await registerScripts([ host ])
}
```

### Web extensions storage APIs — [17:06]

```javascript
await browser.session.storage.set({
  key: value
})

await browser.local.storage.set({
  key: value
})
```

### Adding storage permission to the web extension manifest.json — [17:21]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "icons": {
        "512": "images/icon.svg"
    },

    "options_page": "options.html",

    "permissions": [
        "declarativeNetRequestWithHostAccess",
        "scripting",
        "storage"
    ],

    "optional_host_permissions": [ "*://*/*" ]
}
```

### Saving data with storage — [17:30]

```javascript
// storage.js

export async function updateHosts(hosts) {
    await browser.storage.local.set({ hosts: hosts })
}

export async function getHosts() {
    const { hosts = [] } = await browser.storage.local.get("hosts")
    return hosts
}

export async function saveBlockMode(mode) {
    await browser.storage.local.set({ blockMode: mode })
}

export async function getBlockMode() {
    const { blockMode = "full" } = await browser.storage.local.get("blockMode")
    return blockMode
}
```

### Persisting hosts to storage — [17:41]

```javascript
// host.js

export async function addHost(host, blockMode) {
    if (!host)
        return

    const granted = await browser.permissions.request({
        origins: [`*://${host}/*`, `*://*.${host}/*`]
    })

    if (!granted)
        return

    if (blockingMode === "full")
        await createRules([ host ])

    await registerScripts([ host ])

    let existingHosts = await getHosts()
    let updatedHosts = [ ...existingHosts, host ]
    await updateHosts(updatedHosts)
}
```

### Reading from storage — [17:51]

```javascript
// options.js

let existingHosts = await getHosts()
let blockMode = await getBlockMode()

displayBlocklist(existingHosts)
```

### Switching block modes — [18:00]

```javascript
// host.js

export async function userDidSwitchMode(blockMode) {
    await saveBlockMode(blockMode)

    if (blockMode === "full") {
        let hosts = await getHosts()
        await createRules(hosts)
    } else
        await removeAllRules()
}
```

### Adding a background script — [19:01]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "icons": {
        "512": "images/icon.svg"
    },

    "options_page": "options.html",

    "permissions": [
        "declarativeNetRequestWithHostAccess",
        "scripting",
        "storage"
    ],

    "optional_host_permissions": [ "*://*/*" ],

    "background": {
        "scripts": [ "background.js" ],
        "type": "module"
    }
}
```

### Background script — [19:39]

```javascript
// background.js

import { registerScripts } from "./utilities/scripting.js"
import { getHosts } from "./utilities/storage.js"

browser.runtime.onInstalled.addListener(async (details) => {
    if (details.reason !== "update")
        return

    const hosts = await getHosts()
    await registerScripts(hosts)
})
```

### Package your web extension into an app for Xcode — [22:49]

```bash
xcrun safari-web-extension-packager --copy-resources /path/to/ShinyOnTrack
```

### Adding the nativeMessaging permission — [23:32]

```json
{
    "manifest_version": 3,
    "name": "Shiny OnTrack",
    "description": "Stay on track while you browse the web",
    "version": 1.0,

    "icons": {
        "512": "images/icon.svg"
    },

    "options_page": "options.html",

    "permissions": [
        "declarativeNetRequestWithHostAccess",
        "scripting",
        "storage",
        "nativeMessaging"
    ],

    "optional_host_permissions": [ "*://*/*" ],

    "background": {
        "scripts": [ "background.js" ],
        "type": "module"
    }
}
```

### Sending a native message — [23:40]

```javascript
// background.js

import { registerScripts } from "./utilities/scripting.js"
import { getHosts } from "./utilities/storage.js"

browser.runtime.onInstalled.addListener(async (details) => {
    if (details.reason !== "update")
        return

    const hosts = await getHosts()
    await registerScripts(hosts)
})

export async function requestBioAuth() {
    const message = { message: "requestBioAuth" }
    const response = await browser.runtime.sendNativeMessage(message)
    return response?.success
}
```

### Handling native messages — [23:55]

```swift
// SafariWebExtensionHandler.swift

import LocalAuthentication

class SafariWebExtensionHandler: NSObject, NSExtensionRequestHandling {
    func beginRequest(with context: NSExtensionContext) {
        let request = context.inputItems.first as? NSExtensionItem
        let message = request?.userInfo?[SFExtensionMessageKey] as? [String: Any]

        if message?["message"] as? String == "requestBioAuth" {
            let lAContext = LAContext()
            Task {
                do {
                    let success = try await lAContext.evaluatePolicy(
                        .deviceOwnerAuthenticationWithBiometrics,
                        localizedReason: "Authenticate to change blocked sites"
                    )
                    self.reply(context: context, success: success)
                } catch {
                    self.reply(context: context, success: false)
                }
            }
        }
    }
}
```

### Replying to a native message — [24:25]

```swift
// SafariWebExtensionHandler.swift

import LocalAuthentication

class SafariWebExtensionHandler: NSObject, NSExtensionRequestHandling {
    func beginRequest(with context: NSExtensionContext) {
        let request = context.inputItems.first as? NSExtensionItem
        let message = request?.userInfo?[SFExtensionMessageKey] as? [String: Any]

        if message?["message"] as? String == "requestBioAuth" {
            let lAContext = LAContext()
            Task {
                do {
                    let success = try await lAContext.evaluatePolicy(
                        .deviceOwnerAuthenticationWithBiometrics,
                        localizedReason: "Authenticate to change blocked sites"
                    )
                    self.reply(context: context, success: success)
                } catch {
                    self.reply(context: context, success: false)
                }
            }
        }
    }

    private func reply(context: NSExtensionContext, success: Bool) {
        let response = NSExtensionItem()
        response.userInfo = [SFExtensionMessageKey: ["success": success]]
        context.completeRequest(returningItems: [response], completionHandler: nil)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/216/5/4fceecc8-1e28-465c-b894-fd0d03067c18/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/216/5/4fceecc8-1e28-465c-b894-fd0d03067c18/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/216) — developer.apple.com. Indexed for agent consumption._
