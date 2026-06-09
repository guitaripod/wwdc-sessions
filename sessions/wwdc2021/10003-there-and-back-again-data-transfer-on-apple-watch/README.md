---
id: "wwdc2021-10003"
event: "wwdc2021"
year: 2021
title: "There and back again: Data transfer on Apple Watch"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10003"
topics: ["System Services"]
platforms: ["watchOS"]
hasTranscript: true
---

# There and back again: Data transfer on Apple Watch

**Event:** WWDC21 · **Topic:** System Services · **Platforms:** watchOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10003](https://developer.apple.com/videos/play/wwdc2021/10003)

Advances in Apple Watch give you more ways to communicate to and from your app, and new audiences to consider. Learn what strategies are available for data communication and how to choose the right tool for the job. Compare and contrast the benefits of using technologies such as iCloud Keychain, Watch Connectivity, Core Data, and more.

**Keywords:** `⌚️`, `background app refresh`, `cloudkit`, `core data`, `family setup`, `icloud`, `keychain`, `oauth2token`, `password autofill`, `sockets`, `urlsession`, `watch connectivity`, `wcsession`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,455 words)

## Documentation & Resources

- [Keeping your complications up to date](https://developer.apple.com/documentation/ClockKit/keeping-your-complications-up-to-date) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/ClockKit/keeping-your-complications-up-to-date
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/ClockKit/keeping-your-complications-up-to-date.json
- [Downloading files from websites](https://developer.apple.com/documentation/Foundation/downloading-files-from-websites) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Foundation/downloading-files-from-websites
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Foundation/downloading-files-from-websites.json
- [WCSession](https://developer.apple.com/documentation/WatchConnectivity/WCSession) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/WatchConnectivity/WCSession
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/WatchConnectivity/WCSession.json
- [Sharing access to keychain items among a collection of apps](https://developer.apple.com/documentation/Security/sharing-access-to-keychain-items-among-a-collection-of-apps) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Security/sharing-access-to-keychain-items-among-a-collection-of-apps
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Security/sharing-access-to-keychain-items-among-a-collection-of-apps.json
- [Keeping your watchOS content up to date](https://developer.apple.com/documentation/watchOS-Apps/keeping-your-watchos-app-s-content-up-to-date) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/watchOS-Apps/keeping-your-watchos-app-s-content-up-to-date
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/watchOS-Apps/keeping-your-watchos-app-s-content-up-to-date.json
- [Supporting Associated Domains](https://developer.apple.com/documentation/xcode/supporting-associated-domains) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/xcode/supporting-associated-domains
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/xcode/supporting-associated-domains.json

## Code Snippets

### Password Autofill — [4:20]

```swift
struct LoginView: View {

    @State private var username = ""
    @State private var password = ""

    var body: some View {
        Form {
            TextField("User:", text: $username)
                .textContentType(.username)

            SecureField("Password", text: $password) 
                .textContentType(.password)

            Button {
                processLogin()
            } label: {
                Text("Login")
            }

            Button(role: .cancel) {
                cancelLogin()
            } label: {
                Label("Cancel", systemImage: "xmark.circle")
            }
        }
    }

    private func cancelLogin() {
        // Implement your cancel logic here
    }

    private func processLogin() {
        // Implement your login logic here
    }
}
```

### Store Item in Keychain — [6:25]

```swift
func storeToken(_ token: OAuth2Token, for server: String, account: String) throws {
    let query: [String: Any] = [
      kSecClass as String: kSecClassInternetPassword,
      kSecAttrServer as String: server,
      kSecAttrAccount as String: account,
      kSecAttrSynchronizable as String: true,
    ]

    let tokenData = try encodeToken(token)
    let attributes: [String: Any] = [kSecValueData as String: tokenData]

    let status = SecItemUpdate(query as CFDictionary, attributes as CFDictionary)

    guard status != errSecItemNotFound else {
        try addTokenData(tokenData, for: server, account: account)
        return
    }

    guard status == errSecSuccess else {
        throw OAuthKeychainError.updateError(status)
    }
}
```

### Add Item to Keychain — [7:59]

```swift
func addTokenData(_ tokenData: Data,
                  for server: String,
                  account: String) throws {
    let attributes: [String: Any] = [
      kSecClass as String: kSecClassInternetPassword,
      kSecAttrServer as String: server,
      kSecAttrAccount as String: account,
      kSecAttrSynchronizable as String: true,
      kSecValueData as String: tokenData,
    ]

    let status = SecItemAdd(attributes as CFDictionary, nil)

    guard status == errSecSuccess else {
        throw OAuthKeychainError.addError(status)
    }
}
```

### Retrieve Item from Keychain — [8:25]

```swift
func retrieveToken(for server: String, account: String) throws -> OAuth2Token? {
    let query: [String: Any] = [
      kSecClass as String: kSecClassInternetPassword,
      kSecAttrServer as String: server,
      kSecAttrAccount as String: account,
      kSecAttrSynchronizable as String: true,
      kSecReturnAttributes as String: false,
      kSecReturnData as String: true,
    ]

    var item: CFTypeRef?
    let status = SecItemCopyMatching(query as CFDictionary,
                                     &item)

    guard status != errSecItemNotFound else {
        // No token stored for this server account combination.
        return nil
    }

    guard status == errSecSuccess else {
        throw OAuthKeychainError.retrievalError(status)
    }

    guard let existingItem = item as? [String : Any] else {
        throw OAuthKeychainError.invalidKeychainItemFormat
    }

    guard let tokenData = existingItem[kSecValueData as String] as? Data else {
        throw OAuthKeychainError.missingTokenDataFromKeychainItem
    }

    do {
        return try JSONDecoder().decode(OAuth2Token.self, from: tokenData)
    } catch {
        throw OAuthKeychainError.tokenDecodingError(error.localizedDescription)
    }
}
```

### Remove Item from Keychain — [9:39]

```swift
func removeToken(for server: String, account: String) throws {
    let query: [String: Any] = [
      kSecClass as String: kSecClassInternetPassword,
      kSecAttrServer as String: server,
      kSecAttrAccount as String: account,
      kSecAttrSynchronizable as String: true,
    ]

    let status = SecItemDelete(query as CFDictionary)

    guard status == errSecSuccess || status == errSecItemNotFound else {
        throw OAuthKeychainError.deleteError(status)
    }
}
```

### Core Data SwiftUI View — [11:59]

```swift
import CoreData
import SwiftUI

struct CoreDataView: View {

    @Environment(\.managedObjectContext) private var viewContext

    @FetchRequest(
        sortDescriptors: [NSSortDescriptor(keyPath: \Setting.itemKey, ascending: true)],
        animation: .easeIn)
    private var settings: FetchedResults<Setting>

    var body: some View {
        List {
            ForEach(settings) { setting in
                SettingRow(setting)
            }
        }
    }
}
```

### Background URL Session Configuration — [23:04]

```swift
class BackgroundURLSession: NSObject, ObservableObject, Identifiable {
    private let sessionIDPrefix = "com.example.backgroundURLSessionID."

    enum Status {
        case notStarted
        case queued
        case inProgress(Double)
        case completed
        case failed(Error)
    }

    private var url: URL

    /// Data to send with the URL request.
    ///
    /// If this is set, the HTTP method for the request will be POST
    var body: Data?

    /// Optional content type for the URL request
    var contentType: String?

    private(set) var id = UUID()

    /// The current status of the session
    @Published var status = Status.notStarted

    /// The downloaded data (populated when status == .completed)
    @Published var downloadedURL: URL?

    private var backgroundTasks = [WKURLSessionRefreshBackgroundTask]()

    private lazy var urlSession: URLSession = {
        let config = URLSessionConfiguration.background(withIdentifier: sessionID)
            // Set isDiscretionary = true if you are sending or receiving large 
            // amounts of data. Let Watch users know that their transfers might 
            // not start until they are connected to Wi-Fi and power.
            config.isDiscretionary = false
            config.sessionSendsLaunchEvents = true
            return URLSession(configuration: config,
                              delegate: self, delegateQueue: nil)
        }()

    private var sessionID: String {
        "\(sessionIDPrefix)\(id.uuidString)"
    }

    /// Initialize the session
    /// - Parameter url: The URL for the Background URL Request
    init(url: URL) {
        self.url = url
        super.init()
    }

}
```

### Enqueue the background data transfer — [24:22]

```swift
// This is a member of the BackgroundURLSession class in the example. 
// Enqueue the URLRequest to send in the background. 
func enqueueTransfer() {
    var request = URLRequest(url: url)
    request.httpBody = body
    if body != nil {
        request.httpMethod = "POST"
    }
    if let contentType = contentType {
        request.setValue(contentType, forHTTPHeaderField: "Content-type")
    }
    let task = urlSession.downloadTask(with: request)
    task.earliestBeginDate = nextTaskStartDate

    BackgroundURLSessions.sharedInstance().sessions[sessionID] = self

    task.resume()
    status = .queued
}
```

### WatchKit Extension Delegate — [25:45]

```swift
class ExtensionDelegate: NSObject, WKExtensionDelegate {

    func applicationDidFinishLaunching() {
        // For Watch Connectivity, activate your WCSession as early as possible
        WatchConnectivityModel.shared.activateSession()
    }

    func applicationDidBecomeActive() {
        // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
    }

    func applicationWillResignActive() {
        // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
        // Use this method to pause ongoing tasks, disable timers, etc.
    }

    func handle(_ backgroundTasks: Set<WKRefreshBackgroundTask>) {
        // Sent when the system needs to launch the application in the background to process tasks. Tasks arrive in a set, so loop through and process each one.
        for task in backgroundTasks {
            // Use a switch statement to check the task type
            switch task {
            case let backgroundTask as WKApplicationRefreshBackgroundTask:
                // Be sure to complete the background task once you’re done.
                backgroundTask.setTaskCompletedWithSnapshot(false)
            case let snapshotTask as WKSnapshotRefreshBackgroundTask:
                // Snapshot tasks have a unique completion call, make sure to set your expiration date
                snapshotTask.setTaskCompleted(restoredDefaultState: true, estimatedSnapshotExpiration: Date.distantFuture, userInfo: nil)
            case let connectivityTask as WKWatchConnectivityRefreshBackgroundTask:
                // Be sure to complete the connectivity task once you’re done.
                connectivityTask.setTaskCompletedWithSnapshot(false)
            case let urlSessionTask as WKURLSessionRefreshBackgroundTask:
                if let session = BackgroundURLSessions.sharedInstance()
                        .sessions[urlSessionTask.sessionIdentifier] {
                    session.addBackgroundRefreshTask(urlSessionTask)
                } else {
                    // There is no model for this session, just set it complete
                    urlSessionTask.setTaskCompletedWithSnapshot(false)
                }
            case let relevantShortcutTask as WKRelevantShortcutRefreshBackgroundTask:
                // Be sure to complete the relevant-shortcut task once you're done.
                relevantShortcutTask.setTaskCompletedWithSnapshot(false)
            case let intentDidRunTask as WKIntentDidRunRefreshBackgroundTask:
                // Be sure to complete the intent-did-run task once you're done.
                intentDidRunTask.setTaskCompletedWithSnapshot(false)
            default:
                // make sure to complete unhandled task types
                task.setTaskCompletedWithSnapshot(false)
            }
        }
    }
}
```

### Connect the WatchKit Extension Delegate to the App — [26:43]

```swift
@main
struct MyWatchApp: App {

    @WKExtensionDelegateAdaptor(ExtensionDelegate.self) var extensionDelegate

    @SceneBuilder var body: some Scene {
        WindowGroup {
            NavigationView {
                ContentView()
            }
        }
    }
}
```

### Store the Background Refresh Task it can be completed — [27:07]

```swift
// This is a member of the BackgroundURLSession class in the example. 
// Add the Background Refresh Task to the list so it can be set to completed when the URL task is done.
func addBackgroundRefreshTask(_ task: WKURLSessionRefreshBackgroundTask) {
    backgroundTasks.append(task)
}
```

### Process Downloaded Data — [27:31]

```swift
extension BackgroundURLSession : URLSessionDownloadDelegate {

    private func saveDownloadedData(_ downloadedURL: URL) {
        // Move or quickly process this file before you return from this function.
        // The file is in a temporary location and will be deleted.
    }

    func urlSession(_ session: URLSession,
                    downloadTask: URLSessionDownloadTask,
                    didFinishDownloadingTo location: URL) {
        saveDownloadedData(location)

        // We don't need more updates on this session, so let it go.
        BackgroundURLSessions.sharedInstance().sessions[sessionID] = nil

        DispatchQueue.main.async {
            self.status = .completed
        }

        for task in backgroundTasks {
            task.setTaskCompletedWithSnapshot(false)
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10003/7/2AE1FFC2-BFF3-43AC-9488-AA5514C204FB/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10003/7/2AE1FFC2-BFF3-43AC-9488-AA5514C204FB/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10003) — developer.apple.com. Indexed for agent consumption._
