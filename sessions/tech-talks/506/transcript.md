---
id: "tech-talks-506"
event: "tech-talks"
title: "Apple TV Set Top Box APIs"
url: "https://developer.apple.com/videos/play/tech-talks/506"
language: "eng"
words: 514
---

# Apple TV Set Top Box APIs — Transcript

[Session page](https://developer.apple.com/videos/play/tech-talks/506) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:00]** Shloka Kini: The set top box APIs are used in server-to-server communication which enable the Apple Zero Sign On experience. These APIs create and control profiles for Apple TV devices, which make the Apple TV setup easier for your customers. With the set top box APIs, the setup flow highlights the customer's TV provider when they first set up their Apple TV. The app is automatically installed and the customer is authenticated with their TV provider at the system level. No iTunes or iCloud account required. Apple TVs are matched by their serial numbers to the customers. This process involves your server calling the set top box APIs to create and assign profiles to devices. Upon activation, the appropriate profile is downloaded to device.

**[0:46]** This profile is the key to the set top box behavior. It allows tvOS to know the TV provider and contains the user token, that you create to identify your customer. This profile is installed on device when a customer activates their Apple TV. It will only be used with the customer's consent and only removed with the customer's consent. If a customer sells their Apple TV, the profile can be removed when they inform the TV provider. The set top box APIs can only successfully assign profiles to Apple TVs if those devices maintain a chain of custody from Apple to you. If they are called on any other device, the APIs will respond with an error. If a customer needs to replace a device, they can do so through you or any Apple retail store.

**[1:32]** If through you, you can enable their new Apple TV with the Zero Sign On user experience. If through an Apple retail store, the TV provider doesn't know about the hardware exchange, and there's no profile assigned to the new device. So the customer's Apple TV will have a standard retail experience with single sign-on. Also, the devices returned to Apple will be removed from your pool of devices, and their new Apple TV is added to your pool. To get started using the set top box APIs, first we need some information called onboarding data. You send this data to Apple. This includes the DUNS number identifying your business entity, the name of your company, and your phone number as they appear in DUNS. Also your company's website, the public key from a public/private key pair you generate,

**[2:18]** and an Apple customer number that was used for purchasing your Apple TVs. With this information, we can get your business entity onboard using the set top box APIs and into our program. Once you have access to the set top box APIs, you can start using them. To begin, you start an authenticated session. Once this session has started, you can create, check, and assign profiles to specific Apple TVs. You can remove a profile so that it won't redownload when the customer resets their Apple TV. You can also get the list of Apple TVs available to you with fetch devices and fetch device details. In summary, the set top box APIs
