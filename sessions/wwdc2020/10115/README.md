---
id: "wwdc2020-10115"
event: "wwdc2020"
year: 2020
title: "AutoFill everywhere"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10115"
topics: ["SwiftUI & UI Frameworks", "Privacy & Security"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# AutoFill everywhere

**Event:** WWDC20 · **Topic:** Privacy & Security · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10115](https://developer.apple.com/videos/play/wwdc2020/10115)

Discover how to implement AutoFill in your app and help people enter their information into fields easily, privately, and securely. Learn how to help the system to give better suggestions that tailor to your app's functionality: offer smart location suggestions within a navigation app, for example, or provide a private way to input contact information into fields from the QuickType bar.

In macOS Big Sur, AutoFill has been extended beyond Safari, to apps. Learn about the small changes that you can make to take advantage of this feature and bring convenience, added security, and a frictionless experience to people using your macOS apps.

For more on the latest privacy improvements to our platforms, watch “Build trust through better privacy.”

**Keywords:** `auto`, `fill`, `password`, `text input`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,127 words)

## Code Snippets

### Address AutoFill — [2:06]

```swift
let streetAddressTextField = UITextField()
steetAddressTextField.textContentType = .fullStreetAddress  

//Other address granularity: 
// .addressCity, .addressCityAndState, .addressState, .countryName
// .postalCode, .streetAddressLine1, .streetAddressLine2, .sublocality
```

### Contact AutoFill — [6:17]

```swift
// AutoFill contacts' email address
let emailTextField = UITextField()
emailTextField.textContentType = .emailAddress 

// AutoFill contacts' phone number
let phoneTextField = UITextField()
phoneTextField.textContentType = .telephoneNumber 

// AutoFill contacts' address 
let streetAddressTextField = UITextField()
steetAddressTextField.textContentType = .fullStreetAddress
```

### Password AutoFill — [7:35]

```swift
let userTextField = UITextField()
userTextField.textContentType = .username

let passwordTextField = UITextField()
passwordTextField.textContentType = .password
```

### Security Code AutoFill — [8:00]

```swift
let securityCodeTextField = UITextField()
securityCodeTextField.textContentType = .oneTimeCode
```

### Automatic Strong Passwords — [8:30]

```swift
let userTextField = UITextField()
userTextField.textContentType = .username

let newPasswordTextField = UITextField()
newPasswordTextField.textContentType = .newPassword
```

### Password and Security Codes AutoFill for AppKit based apps — [9:20]

```swift
let usernameTextField = NSTextField()
usernameTextField.contentType = .username

let passwordField = NSSecureTextField()
passwordField.contentType = .password

let securityCodeTextField = NSTextField()
securityCodeTextField.contentType = .oneTimeCode
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10115/8/FFE4310A-D8B3-4E53-8BBF-D799F4F858E5/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10115) — developer.apple.com. Indexed for agent consumption._