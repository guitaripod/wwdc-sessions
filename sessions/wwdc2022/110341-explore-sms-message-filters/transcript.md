---
id: "wwdc2022-110341"
event: "wwdc2022"
title: "Explore SMS message filters"
url: "https://developer.apple.com/videos/play/wwdc2022/110341"
language: "eng"
words: 1214
---

# Explore SMS message filters — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2022/110341) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:00]** ♪ ♪ Hello and welcome to WWDC. My name is Ajay Singh, and today I am excited to take you on a journey to explore SMS message filters. These allow you to create message filter extensions which help people categorize incoming SMS messages from unknown senders. First, I will describe how SMS message filters work. Next, I will talk about what's new in iOS 16. I will walk through an example of how to build a message filter extension

**[0:49]** using iOS 16 APIs, then show you what people will see in Messages when they use your extension. Finally, I will talk about enhancements to Apple's SMS filter for India. Let's talk about SMS message filters. In many countries, SMS messages are now used by businesses to notify customers about transactions, marketing campaigns, alerts, and reminders. In this example you can see a mix of SMS messages including short codes, alphanumeric codes, and standard phone numbers.

**[1:37]** This results in a very cluttered inbox, and it's really difficult to find personal messages from your loved ones. iOS does provide an option to filter messages from unknown senders, but if you receive several messages each day, even the unknown sender folder will quickly get filled with unread messages. Automated filtering of SMS messages is important to many people, and iOS provides a secure sandbox-based extension model that allow you to further classify messages from unknown senders. People can find and install SMS filter apps from the App Store.

**[2:28]** Once installed, you can turn on message filtering by going to Settings, Messages, Unknown & Spam, and turning on Filter Unknown Senders. Then, you can select your SMS filter of choice. Here we have installed two SMS filters. Note that only one filter can be active at a time. In iOS 14 and later, new folders will appear in Messages for Transactions, Promotions, and Junk. These folders help people organize and find messages

**[3:14]** that are most relevant to them. Regardless of which filter is chosen, Messages provide the same classification structure consisting of Transactions, Promotions, and Junk. We have heard from you loud and clear, that you would like to provide more detailed classifications. So in iOS 16 we are introducing enhancements to the filter classification API. Now your SMS message filter extension can classify messages into 12 additional sub-categories. Here are the new sub-categories that you can specify

**[4:00]** in your SMS filter extension. The new sub-categories fall under the existing top level categories– Transactions and Promotions. Now you can further refine incoming messages and provide an even better experience. For example, in markets like India, it's common to receive a large number of messages related to financial transactions. These include activities in their bank account and alerts for credit card spending. These messages can now be nicely organized in the Finance sub-folder under Transactions. Let's see how the flow works for SMS message filters.

**[4:50]** We can divide the flow into two phases; configuration and runtime classification. In the configuration phase, users select your message filter in Settings. This triggers a new API introduced in iOS 16 to request the capabilities supported by your filter. You can now respond with a list of supported categories and sub-categories. In this example, the filter reports that it supports the sub-categories Finance, Orders, and Coupons. iOS validates these capabilities

**[5:36]** and updates the inbox in Messages with the appropriate folders. In the runtime classification phase, every time an SMS message is received from an unknown sender, iOS queries your filter to determine which category and sub-category it belongs to. You can also see the terms action and sub-action used here. Filters must respond with one of the capabilities declared in the configuration phase. The SMS message will then appear in the corresponding sub-folder in Messages. Let's build a simple message filter extension

**[6:24]** to see how the APIs are used and what people will see in Messages. In Xcode, you start by creating a new Message Filter Extension target. The Message Filter Extension target appears as one of the options when you create a new target and go to template selection. Select the Message Filter Extension and click Next. Now give your filter a name and click Finish. When the target is created, MessageFilterExtension.swift will be auto-populated

**[7:09]** with all the required functions. In iOS 16, we have a new API handle called capabilitiesRequest. Fill in the ILMessageFilterCapabilitiesQueryResponse structure with the transactional or promotional sub-actions that you support. You can specify up to five sub-actions. Here we are indicating support for Finance, Orders, and Health sub-actions under Transactions, and Coupons and Offers sub-actions under Promotions. Now build and install your filter extension. When you choose your filter in Settings,

**[7:56]** the Message inbox will be updated with the sub-actions we declared; Finance, Orders, and Health appear under Transactions, and Coupons and Offers appear under Promotions. Now, we have confirmed that our configuration works. Let's define some simple logic to return suitable categories to iOS when an incoming SMS message is received. First, we extract the message body text from the queryRequest object. If the message contains specific keywords,

**[8:42]** we return a suitable matching action and sub-action. Here, we have added the code where if the keyword is debited then we will return filterAction as Transaction and filterSubaction as transactionalfinance. Similarly, when the message has the keyword coupon, then Promotion and PromotionalCoupons will be returned. You can also update the business logic for other sub classifications within Transactions and Promotions. Note that if you return an incorrect combination for filterAction and filterSubAction,

**[9:29]** iOS will discard the sub-action and only honor the action. For example, if we return the action Transaction and sub-action Coupons, then the message will only go to the All Transaction folder. Here, we have an example of SMS received from bank with the keyword "debited" and it has been classified under Finance sub-folder by Messages. Here is another example where we have received a Black Friday Deal with the keyword "coupon." In Messages it has been classified under the Coupons sub-folder.

**[10:17]** In iOS 16, you can choose sub-categories that are the best fit for your user demographics. In the first example, the SMS message filter shows folders for Orders, Reminders, Health, Public Services, and Weather under Transactions, while the second example shows folders for Finance, Reminders, Health, and Rewards under Transactions and Offers under Promotions. Your filter extension can use these sub-categories to provide a differentiated experience for your users.

**[11:03]** Apple provides an SMS filter in India, and we have updated it using the enhancements in iOS 16. The Apple SMS filter in India now supports additional sub-folders including Finance, Orders, and Reminders under Transactions. Your bank transactions appear in Finance, your food or commercial delivery messages are organized under Orders, while important events and to-do's appear in the Reminders folder. To wrap up, in this video we talked about SMS message filters

**[11:50]** and how they can classify messages into Transactions, Promotions, and Junk. In iOS 16, your message filter extension can now classify messages into 12 additional sub-categories. To learn more, see the API documentation in the link accompanying this video. I look forward to seeing your new and creative ideas to help people organize SMS messages. And as always, we appreciate your feedback to help us improve SMS message filtering in future.
