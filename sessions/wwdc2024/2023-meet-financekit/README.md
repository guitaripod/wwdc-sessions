---
id: "wwdc2024-2023"
event: "wwdc2024"
year: 2024
title: "Meet FinanceKit"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/2023"
topics: ["App Services"]
platforms: ["iOS"]
hasTranscript: true
---

# Meet FinanceKit

**Event:** WWDC24 · **Topic:** App Services · **Platforms:** iOS · **Published:** 2024-06-11 · **Session:** [wwdc2024-2023](https://developer.apple.com/videos/play/wwdc2024/2023)

Learn how FinanceKit lets your financial management apps seamlessly and securely share on-device data from Apple Cash, Apple Card, and more, with user consent and control. Find out how to request one-time and ongoing access to accounts, transactions, and balances — and how to build great experiences for iOS and iPadOS.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,932 words)

## Documentation & Resources

- [FinanceKit](https://developer.apple.com/documentation/FinanceKit) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/FinanceKit
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/FinanceKit.json
- [Forum: App & System Services](https://developer.apple.com/forums/topics/app-and-system-services?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/app-and-system-services?cid=vf-a-0010

## Code Snippets

### Check if financial data is available — [5:38]

```swift
// Check if financial data is available

import FinanceKit

let available = FinanceStore.isDataAvailable(
    .financialData
)

guard available else {
    // No meaningful action can be performed
    return
}
```

### Present the transaction picker — [8:08]

```swift
// Present the transaction picker

import SwiftUI
import FinanceKit
import FinanceKitUI

struct TransactionSelector: View {
  @State private var selectedItems: [FinanceKit.Transaction] = []

  var body: some View {
    if FinanceStore.isDataAvailable(.financialData) {
      TransactionPicker(selection: $selectedItems) {
        Text("Show Transaction Picker")
      }
    }
}
```

### Requesting authorization for financial data — [12:16]

```swift
// Requesting authorization for financial data

import FinanceKit

let store = FinanceStore.shared

guard store.isDataAvailable(for: .financialData) else {
    // No meaningful action can be performed
    return
}

let authStatus = await store.requestAuthorization()

guard authStatus == .authorized else {
    // User did not grant access to financial data, stop here
    return
}
```

### Simple query to retrieve all Apple accounts — [15:24]

```swift
// Simple query to retrieve all Apple accounts

let store = FinanceStore.shared

let sortDescriptor = SortDescriptor(\Account.displayName)

let predicate = #Predicate<Account> { account in
   account.institutionName == "Apple"
}

let query = AccountQuery(
   sortDescriptors: [sortDescriptor],
   predicate: predicate
)

let accounts : [Account] = try await store.accounts(query: query)
```

### Get latest 7 available balances for account — [18:12]

```swift
// Get latest 7 available balances for account

func getBalances(account: Account) async throws -> [AccountBalance] {

    let sortDescriptor = SortDescriptor(\AccountBalance.asOfDate, order: .reverse)

    let predicate = #Predicate<AccountBalance> { balance in
        balance.available != nil &&
        balance.accountId == account.id
    }

    let query = AccountBalanceQuery(
        sortDescriptors: [sortDescriptor],
        predicate: predicate,
        limit: 7
    )
    return try await store.accountBalances(query: query).reversed()
}
```

### Retrieve all the transaction history for an account — [20:27]

```swift
// Retrieve all the transaction history for an account

import FinanceKit

let store = FinanceStore.shared
let account: Account = ...

let transactionSequence = store.transactionHistory(
    forAccountID: account.id
)

for try await change in transactionSequence {
    processChanges(change.inserted, change.updated, change.deleted)
}
```

### Use the history token to resume queries — [21:04]

```swift
// Use the history token to resume queries

import FinanceKit

let store = FinanceStore.shared
let account: Account = ...
let currentToken = loadToken()

let transactionSequence = store.transactionHistory(
    forAccountID: account.id,
    since: currentToken
)

for try await change in transactionSequence {
    processChanges(change.inserted, change.updated, change.deleted)
    persist(token: change.newToken)
}
```

### Non monitoring resumable queries — [21:41]

```swift
import FinanceKit

let store = FinanceStore.shared
let account: Account = ...
let currentToken = loadToken()

let transactionSequence = store.transactionHistory(
    forAccountID: account.id,
    since: currentToken,
    isMonitoring: false
)

for try await change in transactionSequence {
    processChanges(change.inserted, change.updated, change.deleted)
    persist(token: change.newToken)
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/2023/4/74A8DE5D-5007-4431-929F-17401D6F80CB/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/2023/4/74A8DE5D-5007-4431-929F-17401D6F80CB/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/2023) — developer.apple.com. Indexed for agent consumption._
