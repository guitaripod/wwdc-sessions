---
id: "wwdc2022-110349"
event: "wwdc2022"
year: 2022
title: "Create engaging content for Swift Playgrounds"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/110349"
topics: ["Business & Education", "Developer Tools", "Essentials", "Swift"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Create engaging content for Swift Playgrounds

**Event:** WWDC22 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-110349](https://developer.apple.com/videos/play/wwdc2022/110349)

Learn how you can build guided instructional content designed for Swift Playgrounds. Follow along with us as we explore how you can add a guide to a completed sample code project. We'll demonstrate how to add tasks to your learning center to show off relevant code and optional experiment tasks that encourage learners to extend the project with code of their own.

**Keywords:** `swift playgrounds`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,494 words)

## Code Snippets

### Dance Floor — [1:27]

```swift
let numOfTiles = 100
let squareLength = 150.0

    // Dance floor
    ForEach(0 ..< numOfTiles, id: \.self) { index in
        let i: CGFloat = CGFloat(index / 10)
        let j: CGFloat = CGFloat(index % 10)

        let x = (squareLength * i) - (squareLength)
        let y = (squareLength * j) - (squareLength * 2)

        Rectangle()
            .frame(width: squareLength, height: squareLength)
            .border(.black, width: 3)
            .position(x: x, y: y)
            .randomizedColorEffect(startAnimation: startParty)
    }
    .blur(radius: 15)
    .opacity(startParty ? 1.0 : 0.0)
```

### Dance — [1:47]

```swift
ForEach(data.creatures) { creature in
    Text(creature.emoji)
        .resizableFont()
        .animatedScalingEffect(startAnimation: startParty)
        .randomizedOffsetEffect(startAnimation: startParty,
                                x: midX * 0.6,
                                y: midY * 0.6)
        .animatedRotationEffect(startAnimation: startParty)
        .opacity(startParty ? 1.0 : 0.0)
}
```

### Disco Ball — [2:08]

```swift
Text("🪩")
    .resizableFont()
    .animatedRotationEffect(startAnimation: startParty)
    .opacity(startParty ? 1 : 0)
```

### Guidebook Directive — [5:12]

```markdown
@GuideBook(title: "Creature Party!", icon: icon.png, background: background.png, firstFile: CreatureDance.swift) {

}
```

### Welcome Message — [5:28]

```markdown
@WelcomeMessage(title: "Welcome to Creature Party!") {
		In Creature Party, you'll take this app of dancing creatures to the next level with the help of colors, shapes, animations, and plenty of emoji!
}
```

### Guide and Step Directives — [5:37]

```markdown
@Guide {
        @Step(title: "Pump up the jams") {

        }
    }
}
```

### Content and Media Directive — [5:53]

```markdown
@ContentAndMedia {
  	Tonight, the creatures are gonna party like it's 2022. 🐙💃🦝🕺🦦 
}
```

### Task Group Directive — [7:15]

```markdown
@TaskGroup(title: "Walkthroughs") {
		Here are the walkthroughs! These will help explain all of the new code.                 
}
```

### First Walkthrough Task — [7:57]

```markdown
@Task(type: walkthrough, id: "partyMode", title: "Setting up the Party", file: CreatureDance.swift) {
}
```

### First Walkthrough Page — [8:44]

```markdown
@Page(id: "1.modifier", title: "") {
  	This is a [view modifier](https://developer.apple.com/documentation/swiftui/viewmodifier). Modifiers let you create unique versions of a view in SwiftUI. 
}
```

### Walkthrough Highlight — [9:48]

```swift
ForEach(data.creatures) { creature in
		Text(creature.emoji)
			.resizableFont()
			/*#-code-walkthrough(1.modifier)*/
			.animatedScalingEffect(startAnimation: startParty)
			/*#-code-walkthrough(1.modifier)*/
      .randomizedOffsetEffect(startAnimation: startParty,
      												x: midX * 0.6,
				                      y: midY * 0.6)
      .animatedRotationEffect(startAnimation: startParty)
      .opacity(startParty ? 1.0 : 0.0)
}
```

### First Walkthrough extra pages — [11:56]

```markdown
@Page(id: "1.struct", title: "") {
  	Custom view modifiers are structures that contain code for explaining how to modify whatever view the given modifier is attached to.  
}
@Page(id: "1.body", title: "") {
  	The body method allows you to add custom view modifications. For example, here you're adding a scaling animation that grows and shrinks the `Creature` over a certain period of time. 
}
```

### Second Walkthrough Task — [12:18]

```markdown
@Task(type: walkthrough, id: "protocol", title: "A Little More on Protocols", file: CreatureDance.swift) {
    @Page(id: "2.protocol", title: "") {
      All custom view modifiers implement the `ViewModifier` protocol. 
    }
    @Page(id: "2.body", title: "") {
      The `ViewModifier` protocol requires all structures that implement it to write the `body(content:)` method.   
    }
    @Page(id: "2.usage", title: "") {
      After you've written content for your `body(content:)` method, you can use it on any view you want. Here you'll use it on each `Creature` to add a rotation animation.
    }
}
```

### First Experiment Task — [14:21]

```markdown
@TaskGroup(title: "Experiments") {
    Time to set this party off! You can use experiments to add some extra pazazz to the dance floor.
    @Task(type: experiment, id: "colors", title: "Dancing in the Strobe Light", file: CreatureDance.swift) {

    }
}
```

### First Experiment Page — [14:48]

```markdown
@Page(id: "3.code", title: "", isAddable: true) {
    ```
    .colorMultiply(creatureColor)
    ``` 
}
```

### Experiment Task Comment — [15:55]

```swift
ForEach(data.creatures) { creature in
		Text(creature.emoji)
    		.resizableFont()
        /*#-code-walkthrough(1.modifier)*/
        .animatedScalingEffect(startAnimation: startParty)
        /*#-code-walkthrough(1.modifier)*/
        .randomizedOffsetEffect(startAnimation: startParty,
        												x: midX * 0.6,
        												y: midY * 0.6)
        /*#-code-walkthrough(2.usage)*/
        .animatedRotationEffect(startAnimation: startParty)
        /*#-code-walkthrough(2.usage)*/
        .opacity(startParty ? 1.0 : 0.0)
        //#-learning-task(colors)
}
```

### Experiment Text — [17:42]

```markdown
@Page(id: "3.lights", title: "") {
  	Next, add some colors to the creatures so it looks like they're dancing under the lights! 
}
```

### Second Experiment Task — [17:55]

```markdown
@Task(type: experiment, id: "timer", title: "Switch it Up", file: CreatureDance.swift) {
    @Page(id: "4.lights", title: "") {
      	Now that you have some colors, you can add some code to change the color of the creatures using a timer. Let's add one!
    }
    @Page(id: "4.code", title: "", isAddable: true) {
        ```
        .onTapGesture {
          if let timer = timer {
            timer.invalidate()
            self.timer = nil
          } else {
            creatureColor = Color.randomColor
            timer = Timer.scheduledTimer(withTimeInterval: 2.0, repeats: true, block: { timer in
                                                                                       creatureColor = Color.randomColor
                                                                                      })
          }
        }
        ``` 
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110349/4/767821EC-6C4C-4F9E-8C8D-1B231B8E1226/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/110349/4/767821EC-6C4C-4F9E-8C8D-1B231B8E1226/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/110349) — developer.apple.com. Indexed for agent consumption._
