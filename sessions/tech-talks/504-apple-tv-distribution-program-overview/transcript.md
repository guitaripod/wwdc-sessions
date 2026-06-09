---
id: "tech-talks-504"
event: "tech-talks"
title: "Apple TV Distribution Program Overview"
url: "https://developer.apple.com/videos/play/tech-talks/504"
language: "eng"
words: 615
---

# Apple TV Distribution Program Overview — Transcript

[Session page](https://developer.apple.com/videos/play/tech-talks/504) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:00]** Welcome to the Apple TV Distribution Program Overview. This program is for TV providers that are interested in partnering with Apple to distribute Apple TVs to customers as an over-the-top set top box replacement. So let's get started. In this video we'll go through the Zero Sign-On user experience and how to support it with the authentication context, VideoSubscriberAccount framework, and the set top box APIs. The Apple TV Distribution Program enables Apple TV to become the center of your customers' content consumption experience. During Apple TV setup, your TV provider brand is promoted and the Apple Zero Sign-On user experience is enabled. Customers are presented with a welcome screen to your service informing them of the automatically

**[0:45]** authenticated account and the TV provider app to be installed. This allows customers to have a seamless experience with your service so they can watch video right out of the box. Oh, and one more thing, all of these features work even if the customer doesn't have an iTunes account. So that's Zero Sign-On. Next, the authentication context. The technology at the center of all of these features is your authentication context. It is what allows customers to sign-in to your TV provider service at the OS level. This system-level authentication is then leveraged to provide seamless authentication to your application and any other TV provider-supported apps on device. The authentication context is a web service hosted on your server that is downloaded to device

**[1:32]** and executed at run time. It is built using JavaScript and XML, and a single authentication context runs on both iOS and tvOS. With authentication at the system level, customers only have to sign in once with Single Sign-On or not at all with Zero Sign-On. That's authentication context. Next is the VideoSubscriberAccount framework. This framework is what allows your app and any other TV provider-supported apps to communicate with your authentication context to request its app-level authentication. When integrating with the VideoSubscriberAccount framework, it's important to remember that you're dealing with authentication at two different levels. You will need to request authentication from the system for your app. From that point forward,

**[2:17]** your app's authentication state needs to mirror the system authentication state. This requires special attention for all the different UI and UX flows coming into your app. Once implemented, you will deliver your apps to the Apple Media Products video team via TestFlight for a final QA sign-off. This is required before submitting the app to App Store review for approval and release. That's VideoSubscriberAccount framework. Last are the set top box APIs, they are what enable Apple TV to know which TV provider to feature. They also allow TV providers without an in-home auto-authentication solution to automatically authenticate customers. Apple TVs distributed by you will feature your TV service to customers in the setup process.

**[3:04]** In this same screen, customers are informed of the auto-authenticated account and app to be installed. The set top box APIs are a server-to-server communication used to assign to and remove profiles from devices. The APIs will only work with Apple TVs purchased from Apple for distribution by you. So that's the set top box APIs. Through Zero Sign-On, the authentication context, the VideoSubscriberAccount framework and set top box APIs, the Apple TV Distribution Program enables Apple TV to become the center of your customers' TV experience. In summary, the Apple TV Distribution Program highlights your TV provider brand, it promotes your applications to the customer, and eliminates the sign-in process for your customers

**[3:51]** enabling Apple Zero Sign-On. The Apple TV Distribution Program and Zero Sign-On are a win-win because your customers get a customized, streamlined experience and you get more visible promotion
