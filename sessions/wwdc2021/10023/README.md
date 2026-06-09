---
id: "wwdc2021-10023"
event: "wwdc2021"
year: 2021
title: "Direct and reflect focus in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10023"
topics: ["SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Direct and reflect focus in SwiftUI

**Event:** WWDC21 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10023](https://developer.apple.com/videos/play/wwdc2021/10023)

With device input — as with all things in life — where you put focus matters. Discover how you can move focus in your app with SwiftUI, programmatically dismiss the keyboard, and build large navigation targets from small views. Together, these APIs can help you simplify your app’s interface and make it more powerful for people to find what they need.

**Keywords:** `adjacency`, `attention`, `detect focus`, `direct attention`, `focus`, `.focused`, `focusedfield`, `.focussection`, `focus section`, `focusstate`, `@focusstate`, `focus state`, `input`, `move focus`, `navigation targets`, `platform convention`, `programmatically move focus`, `swiftui`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,611 words)

## Documentation & Resources

- [Input and event modifiers](https://developer.apple.com/documentation/SwiftUI/View-Input-and-Events) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/View-Input-and-Events
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/View-Input-and-Events.json

## Code Snippets

### Slide 13 - Textfield and Securefield — [3:38]

```swift
import SwiftUI
import AuthenticationServices

struct ContentView: View {

    @State private var email: String = ""
    @State private var password: String = ""

    var body: some View {
        ZStack {
            Image("backgroundImage")
                .resizable()
                .opacity(0.7)
                .ignoresSafeArea()

            VStack(alignment: .center) {
                Text("Vacation Planner")
                    .font(.custom("Baskerville-SemiBoldItalic", size: 60))
                    .foregroundColor(.black.opacity(0.8))
                    .frame(alignment: .top)

                Spacer(minLength: 30)

                TextField("Email", text: $email)
                    .submitLabel(.next)
                    .textContentType(.emailAddress)
                    .keyboardType(.emailAddress)
                    .padding()
                    .frame(height: 50)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)

                SecureField("Password", text: $password)
                    .submitLabel(.go)
                    .padding()
                    .frame(height:50)
                    .textContentType(.password)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)

                Spacer().frame(height: 20)

                HStack {
                    Rectangle().frame(height: 1)
                    Text("or").bold().padding()
                    Rectangle().frame(height: 1)
                }
                .foregroundColor(.black.opacity(0.7))

                Spacer().frame(height: 20)

                SignInWithAppleButton(.signIn) { request in
                    request.requestedScopes = [.fullName, .email]
                } onCompletion: { result in
                    switch result {
                    case .success (_):
                        print("Authorization successful.")
                    case .failure (let error):
                        print("Authorization failed: " + error.localizedDescription)
                    }
                }
                .frame(height: 50)
                .cornerRadius(15)

                Spacer().frame(height: 20)

            }
            .frame(width: 280, height: 500, alignment: .bottom)
        }
    }

}
```

### Slide 14 - Focus State — [3:49]

```swift
import SwiftUI
import AuthenticationServices

struct ContentView: View {

    @FocusState private var focusedField: Field?
    @State private var email: String = ""
    @State private var password: String = ""

    var body: some View {
        ZStack {
            Image("backgroundImage")
                .resizable()
                .opacity(0.7)
                .ignoresSafeArea()

            VStack(alignment: .center) {
                Text("Vacation Planner")
                    .font(.custom("Baskerville-SemiBoldItalic", size: 60))
                    .foregroundColor(.black.opacity(0.8))
                    .frame(alignment: .top)

                Spacer(minLength: 30)

                TextField("Email", text: $email)
                    .submitLabel(.next)
                    .textContentType(.emailAddress)
                    .keyboardType(.emailAddress)
                    .padding()
                    .frame(height: 50)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)

                SecureField("Password", text: $password)
                    .submitLabel(.go)
                    .padding()
                    .frame(height:50)
                    .textContentType(.password)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)

                Spacer().frame(height: 20)

                HStack {
                    Rectangle().frame(height: 1)
                    Text("or").bold().padding()
                    Rectangle().frame(height: 1)
                }
                .foregroundColor(.black.opacity(0.7))

                Spacer().frame(height: 20)

                SignInWithAppleButton(.signIn) { request in
                    request.requestedScopes = [.fullName, .email]
                } onCompletion: { result in
                    switch result {
                    case .success (_):
                        print("Authorization successful.")
                    case .failure (let error):
                        print("Authorization failed: " + error.localizedDescription)
                    }
                }
                .frame(height: 50)
                .cornerRadius(15)

                Spacer().frame(height: 20)

            }
            .frame(width: 280, height: 500, alignment: .bottom)
        }
    }

}
```

### Slide 15 - Focus Field — [4:07]

```swift
import SwiftUI
import AuthenticationServices

enum Field: Hashable {
    case email
    case password
}

struct ContentView: View {

    @FocusState private var focusedField: Field?
    @State private var email: String = ""
    @State private var password: String = ""

    var body: some View {
        ZStack {
            Image("backgroundImage")
                .resizable()
                .opacity(0.7)
                .ignoresSafeArea()

            VStack(alignment: .center) {
                Text("Vacation Planner")
                    .font(.custom("Baskerville-SemiBoldItalic", size: 60))
                    .foregroundColor(.black.opacity(0.8))
                    .frame(alignment: .top)

                Spacer(minLength: 30)

                TextField("Email", text: $email)
                    .submitLabel(.next)
                    .textContentType(.emailAddress)
                    .keyboardType(.emailAddress)
                    .padding()
                    .frame(height: 50)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)

                SecureField("Password", text: $password)
                    .submitLabel(.go)
                    .padding()
                    .frame(height:50)
                    .textContentType(.password)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)

                Spacer().frame(height: 20)

                HStack {
                    Rectangle().frame(height: 1)
                    Text("or").bold().padding()
                    Rectangle().frame(height: 1)
                }
                .foregroundColor(.black.opacity(0.7))

                Spacer().frame(height: 20)

                SignInWithAppleButton(.signIn) { request in
                    request.requestedScopes = [.fullName, .email]
                } onCompletion: { result in
                    switch result {
                    case .success (_):
                        print("Authorization successful.")
                    case .failure (let error):
                        print("Authorization failed: " + error.localizedDescription)
                    }
                }
                .frame(height: 50)
                .cornerRadius(15)

                Spacer().frame(height: 20)

            }
            .frame(width: 280, height: 500, alignment: .bottom)
        }
    }

}
```

### Slide 17 - focused modifiers — [4:32]

```swift
import SwiftUI
import AuthenticationServices

enum Field: Hashable {
    case email
    case password
}

struct ContentView: View {

    @FocusState private var focusedField: Field?
    @State private var email: String = ""
    @State private var password: String = ""

    var body: some View {
        ZStack {
            Image("backgroundImage")
                .resizable()
                .opacity(0.7)
                .ignoresSafeArea()

            VStack(alignment: .center) {
                Text("Vacation Planner")
                    .font(.custom("Baskerville-SemiBoldItalic", size: 60))
                    .foregroundColor(.black.opacity(0.8))
                    .frame(alignment: .top)

                Spacer(minLength: 30)

                TextField("Email", text: $email)
                    .submitLabel(.next)
                    .textContentType(.emailAddress)
                    .keyboardType(.emailAddress)
                    .padding()
                    .frame(height: 50)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)
                    .focused($focusedField, equals: .email)

                SecureField("Password", text: $password)
                    .submitLabel(.go)
                    .padding()
                    .frame(height:50)
                    .textContentType(.password)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)
                    .focused($focusedField, equals: .password)

                Spacer().frame(height: 20)

                HStack {
                    Rectangle().frame(height: 1)
                    Text("or").bold().padding()
                    Rectangle().frame(height: 1)
                }
                .foregroundColor(.black.opacity(0.7))

                Spacer().frame(height: 20)

                SignInWithAppleButton(.signIn) { request in
                    request.requestedScopes = [.fullName, .email]
                } onCompletion: { result in
                    switch result {
                    case .success (_):
                        print("Authorization successful.")
                    case .failure (let error):
                        print("Authorization failed: " + error.localizedDescription)
                    }
                }
                .frame(height: 50)
                .cornerRadius(15)

                Spacer().frame(height: 20)

            }
            .frame(width: 280, height: 500, alignment: .bottom)
        }
    }

}
```

### Slide 25 - onSubmit — [6:07]

```swift
import SwiftUI
import AuthenticationServices

enum Field: Hashable {
    case email
    case password
}

struct ContentView: View {

    @FocusState private var focusedField: Field?
    @State private var email: String = ""
    @State private var password: String = ""
    @State private var submittedEmail: String = ""

    var body: some View {
        ZStack {
            Image("backgroundImage")
                .resizable()
                .opacity(0.7)
                .ignoresSafeArea()

            VStack(alignment: .center) {
                Text("Vacation Planner")
                    .font(.custom("Baskerville-SemiBoldItalic", size: 60))
                    .foregroundColor(.black.opacity(0.8))
                    .frame(alignment: .top)

                Spacer(minLength: 30)

                TextField("Email", text: $email)
                    .submitLabel(.next)
                    .textContentType(.emailAddress)
                    .keyboardType(.emailAddress)
                    .padding()
                    .frame(height: 50)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)
                    .focused($focusedField, equals: .email)

                SecureField("Password", text: $password)
                    .submitLabel(.go)
                    .padding()
                    .frame(height:50)
                    .textContentType(.password)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)
                    .focused($focusedField, equals: .password)

                Spacer().frame(height: 20)

                HStack {
                    Rectangle().frame(height: 1)
                    Text("or").bold().padding()
                    Rectangle().frame(height: 1)
                }
                .foregroundColor(.black.opacity(0.7))

                Spacer().frame(height: 20)

                SignInWithAppleButton(.signIn) { request in
                    request.requestedScopes = [.fullName, .email]
                } onCompletion: { result in
                    switch result {
                    case .success (_):
                        print("Authorization successful.")
                    case .failure (let error):
                        print("Authorization failed: " + error.localizedDescription)
                    }
                }
                .frame(height: 50)
                .cornerRadius(15)

                Spacer().frame(height: 20)

            }
            .frame(width: 280, height: 500, alignment: .bottom)
            .onSubmit {
                submittedEmail = email
                if !isEmailValid {
                    focusedField = .email
                }
            }
        }
    }

    private var isEmailValid : Bool {
        let regex = "[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,64}"
        let predicate = NSPredicate(format:"SELF MATCHES %@", regex)
        return submittedEmail.isEmpty || predicate.evaluate(with: submittedEmail)
    }

}
```

### Slide 26 - border — [6:25]

```swift
import SwiftUI
import AuthenticationServices

enum Field: Hashable {
    case email
    case password
}

struct ContentView: View {

    @FocusState private var focusedField: Field?
    @State private var email: String = ""
    @State private var password: String = ""
    @State private var submittedEmail: String = ""

    var body: some View {
        ZStack {
            Image("backgroundImage")
                .resizable()
                .opacity(0.7)
                .ignoresSafeArea()

            VStack(alignment: .center) {
                Text("Vacation Planner")
                    .font(.custom("Baskerville-SemiBoldItalic", size: 60))
                    .foregroundColor(.black.opacity(0.8))
                    .frame(alignment: .top)

                Spacer(minLength: 30)

                TextField("Email", text: $email)
                    .submitLabel(.next)
                    .textContentType(.emailAddress)
                    .keyboardType(.emailAddress)
                    .padding()
                    .frame(height: 50)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)
                    .focused($focusedField, equals: .email)
                    .border(Color.red,
                            width: (focusedField == .email &&
                                    !isEmailValid) ? 2 : 0)

                SecureField("Password", text: $password)
                    .submitLabel(.go)
                    .padding()
                    .frame(height:50)
                    .textContentType(.password)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)
                    .focused($focusedField, equals: .password)

                Spacer().frame(height: 20)

                HStack {
                    Rectangle().frame(height: 1)
                    Text("or").bold().padding()
                    Rectangle().frame(height: 1)
                }
                .foregroundColor(.black.opacity(0.7))

                Spacer().frame(height: 20)

                SignInWithAppleButton(.signIn) { request in
                    request.requestedScopes = [.fullName, .email]
                } onCompletion: { result in
                    switch result {
                    case .success (_):
                        print("Authorization successful.")
                    case .failure (let error):
                        print("Authorization failed: " + error.localizedDescription)
                    }
                }
                .frame(height: 50)
                .cornerRadius(15)

                Spacer().frame(height: 20)

            }
            .frame(width: 280, height: 500, alignment: .bottom)
            .onSubmit {
                submittedEmail = email
                if !isEmailValid {
                    focusedField = .email
                }
            }
        }
    }

    private var isEmailValid : Bool {
        let regex = "[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,64}"
        let predicate = NSPredicate(format:"SELF MATCHES %@", regex)
        return submittedEmail.isEmpty || predicate.evaluate(with: submittedEmail)
    }

}
```

### Slide 29 - dismiss keyboard with nil — [7:17]

```swift
import SwiftUI
import AuthenticationServices

enum Field: Hashable {
    case email
    case password
}

struct ContentView: View {

    @FocusState private var focusedField: Field?
    @State private var email: String = ""
    @State private var password: String = ""
    @State private var submittedEmail: String = ""

    var body: some View {
        ZStack {
            Image("backgroundImage")
                .resizable()
                .opacity(0.7)
                .ignoresSafeArea()

            VStack(alignment: .center) {
                Text("Vacation Planner")
                    .font(.custom("Baskerville-SemiBoldItalic", size: 60))
                    .foregroundColor(.black.opacity(0.8))
                    .frame(alignment: .top)

                Spacer(minLength: 30)

                TextField("Email", text: $email)
                    .submitLabel(.next)
                    .textContentType(.emailAddress)
                    .keyboardType(.emailAddress)
                    .padding()
                    .frame(height: 50)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)
                    .focused($focusedField, equals: .email)
                    .border(Color.red,
                            width: (focusedField == .email &&
                                    !isEmailValid) ? 2 : 0)

                SecureField("Password", text: $password)
                    .submitLabel(.go)
                    .padding()
                    .frame(height:50)
                    .textContentType(.password)
                    .background(Color.white.opacity(0.9))
                    .cornerRadius(15)
                    .padding(10)
                    .focused($focusedField, equals: .password)

                Spacer().frame(height: 20)

                HStack {
                    Rectangle().frame(height: 1)
                    Text("or").bold().padding()
                    Rectangle().frame(height: 1)
                }
                .foregroundColor(.black.opacity(0.7))

                Spacer().frame(height: 20)

                SignInWithAppleButton(.signIn) { request in
                    request.requestedScopes = [.fullName, .email]
                } onCompletion: { result in
                    switch result {
                    case .success (_):
                        print("Authorization successful.")
                    case .failure (let error):
                        print("Authorization failed: " + error.localizedDescription)
                    }
                }
                .frame(height: 50)
                .cornerRadius(15)

                Spacer().frame(height: 20)

            }
            .frame(width: 280, height: 500, alignment: .bottom)
            .onSubmit {
                submittedEmail = email
                if !isEmailValid {
                    focusedField = .email
                } else {
                    focusedField = nil
                    // Show progress indicator, and log in.
                }
            }
        }
    }

    private var isEmailValid : Bool {
        let regex = "[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,64}"
        let predicate = NSPredicate(format:"SELF MATCHES %@", regex)
        return submittedEmail.isEmpty || predicate.evaluate(with: submittedEmail)
    }

}
```

### tv code — [9:24]

```swift
import SwiftUI
import AuthenticationServices


struct ContentView: View {

    @State private var email: String = ""
    @State private var password: String = ""

    var body: some View {
        HStack {
            VStack(alignment: .leading) {
                Spacer(minLength:60).frame(height: 150)
                Text("Vacation\nPlanner")
                    .font(.custom("Baskerville-SemiBoldItalic", size: 60))
                    .foregroundColor(Color.black.opacity(0.8))
                    .lineLimit(nil)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 40)

                Spacer().frame(height:80)

                TextField("Email", text: $email)
                    .submitLabel(.next)
                    .textContentType(.emailAddress)
                    .keyboardType(.emailAddress)

                Spacer().frame(height:30)

                SecureField("Password", text: $password)
                    .submitLabel(.go)
                    .textContentType(.password)

                HStack {
                    Rectangle().frame(height: 1)
                    Text("or").bold().padding()
                    Rectangle().frame(height: 1)
                }
                .foregroundColor(Color.black.opacity(0.7))

                Spacer().frame(height: 20)

                SignInWithAppleButton(.signIn) { request in
                    request.requestedScopes = [.fullName, .email]
                } onCompletion: { result in
                    switch result {
                    case .success (_):
                        print("Authorization successful.")
                    case .failure (let error):
                        print("Authorization failed: " + error.localizedDescription)
                    }
                }
                .frame(height: 50)
                Spacer()
            }
            .frame(width: 350, alignment: .center)

            VStack {
                Image(photoName)
                    .resizable()
                    .frame(width: 1400)
                    .aspectRatio(contentMode: .fit)
                    .ignoresSafeArea(edges: [.trailing])
                BrowsePhotosButton()
            }
        }.preferredColorScheme(.light)
    }
}
```

### focus section 1 — [9:47]

```swift
import SwiftUI
import AuthenticationServices


struct ContentView: View {

    @State private var email: String = ""
    @State private var password: String = ""

    var body: some View {
        HStack {
            VStack(alignment: .leading) {
                Spacer(minLength:60).frame(height: 150)
                Text("Vacation\nPlanner")
                    .font(.custom("Baskerville-SemiBoldItalic", size: 60))
                    .foregroundColor(Color.black.opacity(0.8))
                    .lineLimit(nil)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 40)

                Spacer().frame(height:80)

                TextField("Email", text: $email)
                    .submitLabel(.next)
                    .textContentType(.emailAddress)
                    .keyboardType(.emailAddress)

                Spacer().frame(height:30)

                SecureField("Password", text: $password)
                    .submitLabel(.go)
                    .textContentType(.password)

                HStack {
                    Rectangle().frame(height: 1)
                    Text("or").bold().padding()
                    Rectangle().frame(height: 1)
                }
                .foregroundColor(Color.black.opacity(0.7))

                Spacer().frame(height: 20)

                SignInWithAppleButton(.signIn) { request in
                    request.requestedScopes = [.fullName, .email]
                } onCompletion: { result in
                    switch result {
                    case .success (_):
                        print("Authorization successful.")
                    case .failure (let error):
                        print("Authorization failed: " + error.localizedDescription)
                    }
                }
                .frame(height: 50)
                Spacer()
            }
            .frame(width: 350, alignment: .center)

            VStack {
                Image(photoName)
                    .resizable()
                    .frame(width: 1400)
                    .aspectRatio(contentMode: .fit)
                    .ignoresSafeArea(edges: [.trailing])
                BrowsePhotosButton()
            }
            .focusSection()
        }.preferredColorScheme(.light)
    }
}
```

### focus section 2 — [10:06]

```swift
import SwiftUI
import AuthenticationServices


struct ContentView: View {

    @State private var email: String = ""
    @State private var password: String = ""

    var body: some View {
        HStack {
            VStack(alignment: .leading) {
                Spacer(minLength:60).frame(height: 150)
                Text("Vacation\nPlanner")
                    .font(.custom("Baskerville-SemiBoldItalic", size: 60))
                    .foregroundColor(Color.black.opacity(0.8))
                    .lineLimit(nil)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 40)

                Spacer().frame(height:80)

                TextField("Email", text: $email)
                    .submitLabel(.next)
                    .textContentType(.emailAddress)
                    .keyboardType(.emailAddress)

                Spacer().frame(height:30)

                SecureField("Password", text: $password)
                    .submitLabel(.go)
                    .textContentType(.password)

                HStack {
                    Rectangle().frame(height: 1)
                    Text("or").bold().padding()
                    Rectangle().frame(height: 1)
                }
                .foregroundColor(Color.black.opacity(0.7))

                Spacer().frame(height: 20)

                SignInWithAppleButton(.signIn) { request in
                    request.requestedScopes = [.fullName, .email]
                } onCompletion: { result in
                    switch result {
                    case .success (_):
                        print("Authorization successful.")
                    case .failure (let error):
                        print("Authorization failed: " + error.localizedDescription)
                    }
                }
                .frame(height: 50)
                Spacer()
            }
            .frame(width: 350, alignment: .center)
            .focusSection()

            VStack {
                Image(photoName)
                    .resizable()
                    .frame(width: 1400)
                    .aspectRatio(contentMode: .fit)
                    .ignoresSafeArea(edges: [.trailing])
                BrowsePhotosButton()
            }
            .focusSection()
        }.preferredColorScheme(.light)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10023/5/ED227AE3-34ED-45F7-BB9D-7E4F06876C3B/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10023/5/ED227AE3-34ED-45F7-BB9D-7E4F06876C3B/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10023) — developer.apple.com. Indexed for agent consumption._