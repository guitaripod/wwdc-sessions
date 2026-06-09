---
id: "wwdc2021-10235"
event: "wwdc2021"
year: 2021
title: "Build interactive tutorials using DocC"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10235"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Build interactive tutorials using DocC

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-10 · **Session:** [wwdc2021-10235](https://developer.apple.com/videos/play/wwdc2021/10235)

Discover how you can author immersive tutorials from scratch with DocC. We’ll demonstrate how you can bring together rich instructions, example code, and images through the DocC syntax to showcase your Swift framework in action. And we’ll go over how to create progressive training that can provide interactive learning opportunities and help people better understand use cases for your framework.

**Keywords:** `docc`, `documentation`, `documentation catalog`, `documentation compiler`, `tutorials`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,241 words)

## Documentation & Resources

- [DocC](https://developer.apple.com/documentation/docc) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/docc
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/docc.json
- [Interactive Tutorials](https://developer.apple.com/documentation/docc) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/docc
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/docc.json
- [Building an Interactive Tutorial](https://developer.apple.com/documentation/docc) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/docc
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/docc.json
- [SlothCreator: Building DocC documentation in Xcode](https://developer.apple.com/documentation/Xcode/slothcreator-building-docc-documentation-in-xcode) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Xcode/slothcreator-building-docc-documentation-in-xcode
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Xcode/slothcreator-building-docc-documentation-in-xcode.json

## Code Snippets

### Tutorial Table of Contents File Content — [11:26]

```markdown
@Tutorials(name: "SlothCreator") {
    @Intro(title: "Meet SlothCreator") {
        Create, catalog, and care for sloths using SlothCreator. Get started with SlothCreator by building the demo app _Slothy_.

        @Image(source: slothcreator-intro.png, alt: "An illustration of 3 iPhones in portrait mode, displaying the UI of finding, creating, and taking care of a sloth in Slothy — the sample app that you build in this collection of tutorials.")
    }

    @Chapter(name: "SlothCreator Essentials") {
        @Image(source: chapter1-slothcreatorEssentials.png, alt: "A wireframe of an app interface that has an outline of a sloth and four buttons below the sloth. The buttons display the following symbols, from left to right: snowflake, fire, wind, and lightning.")

        Create custom sloths and edit their attributes and powers using SlothCreator.

        @TutorialReference(tutorial: "doc:Creating-Custom-Sloths")
    }
}
```

### Tutorial File Name — [11:47]

```markdown
Creating Custom Sloths
```

### Tutorial Title — [12:21]

```markdown
Creating Custom Sloths
```

### Tutorial Overview — [12:27]

```markdown
This tutorial guides you through building _Slothy_ — an app for creating and caring for custom sloths. You'll start by building the sloth creation view.
```

### Tutorial Intro Image File Name — [13:04]

```markdown
creating-intro.png
```

### Section 1 Title — [14:22]

```markdown
Create a new project and add SlothCreator
```

### Section 1 Image File Name — [14:43]

```markdown
01-creating-section1.png
```

### Section 1 Image Accessible Description — [14:44]

```markdown
An arrow pointing from the SlothCreator framework icon to the Xcode app project icon.
```

### Section 1 Step 1 Image File Name — [15:43]

```markdown
creating-01-01.png
```

### Section 1 Step 1 Image Accessible Description — [15:45]

```markdown
A screenshot of the template selector in Xcode. In the top row, iOS is selected as the platform. In the Application section, App is selected as the template; there's a highlight placed over the Next button at the lower-right of the sheet.
```

### Section 1 Step 2 to Step 4 — [15:57]

```markdown
@Step {
    Enter "Slothy" as the Product Name. 

    @Image(source: creating-01-02.png, alt: "A screenshot of the project sheet, which shows the Product Name for the app being built as Slothy. The Interface is set to SwiftUI, and the Life Cycle is set to SwiftUI App.")
}

@Step {
    Select "SwiftUI" from the Interface pop-up menu and "SwiftUI App" from the Life Cycle pop-up menu, then click Next. Choose a location to save the Slothy project on your Mac.

    @Image(source: creating-01-03.png, alt: "A screenshot of the project sheet, which shows the Interface is set to SwiftUI and the Life Cycle is set to SwiftUI App.")
}

@Step {
    Add `SlothCreator` as a dependency to the project.

    @Image(source: creating-01-04.png, alt:"A screenshot shows the SlothCreator package in Xcode's navigator.")
}
```

### Section 2 Intro and Step 1 & 2 — [17:58]

```markdown
@Section(title: "Add a customization view") {
    @ContentAndMedia(layout: horizontal) {
        Add the ability for users to customize sloths and select their powers.

        @Image(source: 01-creating-section2.png, alt: "An outline of a sloth surrounded by four power type icons. The power type icons are arranged in the following order, clockwise from the top: fire, wind, lightning, and ice.")
    }

    @Steps {
        @Step {
            Create a new SwiftUI View file named `CustomizedSlothView.swift`.

            @Code(name: "CustomizedSlothView.swift", file: 01-creating-code-02-01.swift) {
                @Image(source: preview-01-creating-code-02-01.png, alt: "A screenshot from the Xcode preview as it would appear on iPhone, with the text, Hello, World!, centered in the middle of the display.")
            }
        }    

        @Step {
            Import the `SlothCreator` package.

            @Code(name: "<#display name#>", file: <#filename.swift#>)
        }    
    }
}
```

### Section 2 Step 2 Display Name — [19:05]

```markdown
CustomizedSlothView.swift
```

### Section 2 Step 2 Code File Name — [19:08]

```markdown
01-creating-code-02-02.swift
```

### Section 2 Step 2 Code File Preview Image — [19:10]

```markdown
{
                    @Image(source: preview-01-creating-code-02-01.png, alt: "A screenshot from the Xcode preview as it would appear on iPhone, with the text, Hello, World!, centered in the middle of the display.")
                }
```

### Section 2 Remaining Steps — [19:25]

```markdown
@Step {
    Create a ``Sloth`` state variable called `sloth`.

    @Code(name: "CustomizedSlothView.swift", file: 01-creating-code-02-03.swift) {
         @Image(source: preview-01-creating-code-02-01.png, alt: "A screenshot from the Xcode preview as it would appear on iPhone, with the text, Hello, World!, centered in the middle of the display.")
    }
}    

@Step {
    Delete the template `Text` view, then add a new `VStack` with trailing padding.

    This adds space around and between any views inside.

    @Code(name: "CustomizedSlothView.swift", file: 01-creating-code-02-04.swift) {
         @Image(source: preview-01-creating-code-02-04.png, alt: "A screenshot of a blank preview canvas.")
    }
}    

@Step {
    Add a `SlothView`. Specify the `sloth` state variable for the view's `sloth` binding.

    @Code(name: "CustomizedSlothView.swift", file: 01-creating-code-02-05.swift) {
         @Image(source: preview-01-creating-code-02-04.png, alt: "A screenshot of a blank preview canvas.")
    }
}    

@Step {
    Add a `PowerPicker`. Specify the `sloth`'s `power` for the picker view's `power` binding.

    @Code(name: "CustomizedSlothView.swift", file: 01-creating-code-02-06.swift) {
         @Image(source: preview-01-creating-code-02-04.png, alt: "A screenshot of a blank preview canvas.")
    }
}    

The following steps display your customized sloth view in the SwiftUI preview.

@Step {
    Add the `sloth` parameter to initialize the `CustomizedSlothView` in the preview provider, and pass a new `Sloth` instance for the value.

    @Code(name: "CustomizedSlothView.swift", file: 01-creating-code-02-07.swift) {
         @Image(source: preview-01-creating-code-02-07.png, alt: "A portrait of a generic sloth displayed in the center of the canvas.")
    }
}

@Step {
    Set the preview provider sloth's `name` to `"Super Sloth"`, `color` to `.blue`, and `power` to `.ice`.

    @Code(name: "CustomizedSlothView.swift", file: 01-creating-code-02-08.swift) {
         @Image(source: preview-01-creating-code-02-08.png, alt: "A portrait of an ice sloth on top, followed by four power icons below. The power icons, clockwise from top left, include: ice, fire, wind, and lightning. The ice icon is selected.")
    }
}
```

### Chapter 1 Tutorial 2 & 3 — [20:03]

```markdown
@TutorialReference(tutorial: "doc:Editing-Sloth")
@TutorialReference(tutorial: "doc:Adding-Accessories")
```

### Chapter 2 & 3 — [20:10]

```markdown
@Chapter(name: "Sloth Health & Happiness") {
    @Image(source: chapter2-healthAndHappiness.png, alt: "A popover window pointing at a button with a leaf symbol on it. To the right of the leaf button, there is a button with a smiley face and a button with a dumbbell.")

    Discover how to track sloth's activity levels, measure their overall happiness, and feed them their favorite foods.

    @TutorialReference(tutorial: "doc:Feeding-Sloths")
    @TutorialReference(tutorial: "doc:Tracking-Sloth-Activity")
    @TutorialReference(tutorial: "doc:Measuring-Sloth-Happiness")
}

@Chapter(name: "Finding Hidden Sloths") {
    @Image(source: chapter3-findingHiddenSloths.png, alt: "An illustration of a radar scanning over a map. The map displays a pin with a smiley sloth face in the upper left quadrant.")

    Find sloths as they move around their neighborhoods and make friends.

    @TutorialReference(tutorial: "doc:Locating-Sloths")
    @TutorialReference(tutorial: "doc:Finding-Sloth-Habitats")
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10235/6/D2C51374-4073-4A41-97CB-4217A096F2B3/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10235/6/D2C51374-4073-4A41-97CB-4217A096F2B3/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10235) — developer.apple.com. Indexed for agent consumption._
