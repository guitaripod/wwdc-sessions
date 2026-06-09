---
id: "wwdc2023-10094"
event: "wwdc2023"
year: 2023
title: "Enhance your iPad and iPhone apps for the Shared Space"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2023/10094"
topics: ["Developer Tools", "Spatial Computing", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "visionOS"]
hasTranscript: true
---

# Enhance your iPad and iPhone apps for the Shared Space

**Event:** WWDC23 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, visionOS · **Published:** 2023-06-06 · **Session:** [wwdc2023-10094](https://developer.apple.com/videos/play/wwdc2023/10094)

Get ready to enhance your iPad and iPhone apps for the Shared Space! We’ll show you how to optimize your experience to make it feel great on visionOS and explore Designed for iPad app interaction, visual treatments, and media.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,660 words)

## Code Snippets

### Tappable VStack with hover effect — [3:02]

```swift
struct TappableCard: View {
   // Sample card
   var imageName = "BearsInWater"
   var headline = "Bear Fishing"
   var timeAgo = "42 Minutes ago"

   var body: some View {
      VStack {
         VStack(alignment: .leading) {
            Image(imageName)
               .resizable()
               .clipped()
               .aspectRatio(contentMode: .fill)
               .frame(width: 300, height: 250, alignment: .center)
            Text(headline)
               .padding([.leading])
               .font(.title2)
               .foregroundColor(.black)
         }
         Divider()
         HStack {
            HStack {
               Text(timeAgo)
                  .frame(alignment: .leading)
                  .foregroundColor(.black)
            }
            .padding([.leading])
            Spacer()
            VStack(alignment: .trailing) {
               Button { print("Present menu options") } label: {
                  Image(systemName: "ellipsis")
                     .foregroundColor(.black)
               }
            }
         }
         .padding(EdgeInsets(top: 5, leading: 5, bottom: 5, trailing: 5))
      }
      .frame(width: 300, height: 350, alignment: .top)
      .hoverEffect()
      .background(.white)
      .overlay(
         RoundedRectangle(cornerRadius: 10)
            .stroke(Color(.sRGB, red: 150/255, green: 150/255, blue: 150/255, opacity: 0.1), lineWidth: 3.0)
      )
      .cornerRadius(10)
      .onTapGesture {
         print("Present card detail")
      }
   }
}
```

### Custom player with tap targets that are larger than the hover effect bounds — [4:08]

```swift
struct ContentView: View {
   var body: some View {
      VStack {
         // Video player
         HStack {
            Button { print("Going back 10 seconds") } label: {
               Image(systemName: "gobackward.10")
                  .padding(.trailing)
                  .contentShape(.hoverEffect, CustomizedRectShape(customRect: CGRect(x: -75, y: -40, width: 100, height: 100)))
                  .foregroundStyle(.white)
                  .frame(width: 500, height: 834, alignment: .trailing)
            }
            Button { print("Play") } label: {
               Image(systemName: "play.fill")
                  .font(.title)
                  .foregroundStyle(.white)
                  .frame(width: 100, height: 100, alignment: .center)
            }
            .padding()
            Button { print("Going into the future 10 seconds") } label: {
               Image(systemName: "goforward.10")
                  .padding(.leading)
                  .contentShape(.hoverEffect, CustomizedRectShape(customRect: CGRect(x: 0, y: -40, width: 100, height: 100)))
                  .foregroundStyle(.white)
                  .frame(width: 500, height: 834, alignment: .leading)
            }
         }
         .frame(
              minWidth: 0,
              maxWidth: .infinity,
              minHeight: 0,
              maxHeight: .infinity,
              alignment: .center
         )
      }
      .frame(
           minWidth: 0,
           maxWidth: .infinity,
           minHeight: 0,
           maxHeight: .infinity,
           alignment: .topLeading
      )
      .background(.black)
   }
}

struct CustomizedRectShape: Shape {
   var customRect: CGRect

   func path(in rect: CGRect) -> Path {
      var path = Path()

      path.move(to: CGPoint(x: customRect.minX, y: customRect.minY))
      path.addLine(to: CGPoint(x: customRect.maxX, y: customRect.minY))
      path.addLine(to: CGPoint(x: customRect.maxX, y: customRect.maxY))
      path.addLine(to: CGPoint(x: customRect.minX, y: customRect.maxY))
      path.addLine(to: CGPoint(x: customRect.minX, y: customRect.minY))

      return path
   }
}
```

### Button with custom buttonStyle, then adding a hover effect to the button — [5:14]

```swift
struct ContentView: View {
    var body: some View {
        VStack {
         Button("Howdy y'all") { print("🤠") }
            .buttonStyle(SixColorButton())
        }
        .padding()
    }
}

struct SixColorButton: ButtonStyle {
   func makeBody(configuration: Configuration) -> some View {
      configuration.label
         .padding()
         .font(.title)
         .foregroundStyle(.white)
         .bold()
         .background {
            // Background color bands
            ZStack {
               Color.black
               HStack(spacing: 0) {
                  // GREEN
                  Rectangle()
                     .foregroundStyle(Color(red: 125/255, green: 186/255, blue: 66/255))
                     .frame(width: 16)
                  // YELLOW
                  Rectangle()
                     .foregroundStyle(Color(red: 240/255, green: 187/255, blue: 64/255))
                     .frame(width: 16)
                  // ORANGE
                  Rectangle()
                     .foregroundStyle(Color(red: 225/255, green: 137/255, blue: 50/255))
                     .frame(width: 16)
                  // RED
                  Rectangle()
                     .foregroundStyle(Color(red: 200/255, green: 73/255, blue: 65/255))
                     .frame(width: 16)
                  // PURPLE
                  Rectangle()
                     .foregroundStyle(Color(red: 134/255, green: 64/255, blue: 151/255))
                     .frame(width: 16)
                  // BLUE
                  Rectangle()
                     .foregroundStyle(Color(red: 75/255, green: 154/255, blue: 218/255))
                     .frame(width: 16, height: 500)
               }
               .opacity(0.7)
               .rotationEffect(.degrees(35))
            }
         }
         .cornerRadius(10)
         .hoverEffect()
   }
}
```

### Honey comb app with custom shape buttons, then adding hover effects that clip to bounds of the honey comb shape — [5:46]

```swift
struct ContentView: View {
    var body: some View {
      VStack {
         Button { print("🐝") } label: {
            // Button label
            HoneyComb()
               .fill(.yellow)
               .frame(width: 300, height: 300)
               .contentShape(.hoverEffect, HoneyComb())
            }
         }
         .frame(width: 400, height: 400, alignment: .center)
         .background(.black)
         .padding()
      }
    }
}

struct HoneyComb: Shape {
   func path(in rect: CGRect) -> Path {
      var path = Path()
      path.move(to: CGPoint(x: rect.minX + (rect.width * 0.25), y: rect.minY))
      path.addLine(to: CGPoint(x: rect.maxX - (rect.maxX * 0.25), y: rect.minY))
      path.addLine(to: CGPoint(x: rect.maxX, y: rect.midY))
      path.addLine(to: CGPoint(x: rect.maxX - (rect.maxX * 0.25), y: rect.maxY))
      path.addLine(to: CGPoint(x: rect.minX + (rect.width * 0.25), y: rect.maxY))
      path.addLine(to: CGPoint(x: rect.minX, y: rect.midY))
      path.addLine(to: CGPoint(x: rect.minX + (rect.width * 0.25), y: rect.minY))
      return path
   }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10094/4/701039CD-C751-471F-A029-A2407B622C61/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2023/10094/4/701039CD-C751-471F-A029-A2407B622C61/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2023/10094) — developer.apple.com. Indexed for agent consumption._