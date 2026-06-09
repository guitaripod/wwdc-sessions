---
id: "wwdc2022-110341"
event: "wwdc2022"
year: 2022
title: "Explore SMS message filters"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110341"
topics: ["System Services"]
platforms: ["iOS", "iPadOS"]
hasTranscript: true
---

# Explore SMS message filters

**Event:** WWDC22 · **Topic:** System Services · **Platforms:** iOS, iPadOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-110341](https://developer.apple.com/videos/play/wwdc2022/110341)

SMS message filter extensions can help people manage Messages by filtering SMS messages from unknown senders. Discover how to create apps with message filter extensions that automatically categorize SMS messages into folders and sub-folders based on message contents and other heuristics.

**Keywords:** `junk`, `promotions`, `transactions`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,214 words)

## Code Snippets

### Message filter extension example — [7:02]

```swift
func handle(_ capabilitiesRequest: ILMessageFilterCapabilitiesQueryRequest, context: ILMessageFilterExtensionContext, completion: @escaping (ILMessageFilterCapabilitiesQueryResponse) -> Void) {
    let response = ILMessageFilterCapabilitiesQueryResponse()
    // choose up to five sub-categories supported by the filter
    response.transactionalSubActions = [.transactionalFinance,
                                        .transactionalOrders,
                                        .transactionalHealth]
    response.promotionalSubActions   = [.promotionalCoupons,
                                        .promotionalOffers]
    completion(response)
}
```

### Return categories for incoming messages — [8:16]

```swift
func handle(_ queryRequest: ILMessageFilterQueryRequest, context: ILMessageFilterExtensionContext, completion: @escaping (ILMessageFilterQueryResponse) -> Void) {
    guard let message = queryRequest.messageBody else { return }
    let response = ILMessageFilterQueryResponse()
    switch(message) {
    case _ where message.contains("debited"):
        response.filterAction = .transaction
        response.filterSubAction = .transactionalFinance
        break
    case _ where message.contains("coupon"):
        response.filterAction = .promotion
        response.filterSubAction = .promotionalCoupons
        break
     // update other cases
    }
    completion(response)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110341/3/B3803998-3525-4D12-A13D-CFE6C8435AAF/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110341/3/B3803998-3525-4D12-A13D-CFE6C8435AAF/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110341) — developer.apple.com. Indexed for agent consumption._