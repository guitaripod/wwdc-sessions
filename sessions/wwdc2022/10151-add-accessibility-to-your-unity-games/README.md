---
id: "wwdc2022-10151"
event: "wwdc2022"
year: 2022
title: "Add accessibility to your Unity games"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10151"
topics: ["Graphics & Games", "Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Add accessibility to your Unity games

**Event:** WWDC22 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10151](https://developer.apple.com/videos/play/wwdc2022/10151)

Learn how you can make your Unity games accessible on Apple platforms using our open source Accessibility plug-in. Follow along as we add support for assistive technologies like VoiceOver and Switch Control to a sample Unity game project. We'll show you how you can automatically scale text with Dynamic Type, support interface accommodations like reduced transparency or increased contrast, and more.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,823 words)

## Documentation & Resources

- [Apple Unity Plug-Ins on GitHub](https://github.com/apple/unityplugins) _download_
- [Accessibility](https://developer.apple.com/documentation/accessibility) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/accessibility
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/accessibility.json

## Code Snippets

### PlayingCard enum — [7:43]

```csharp
public enum PlayingCard
{
    AceOfSpade,
    AceOfClubs,
    AceOfDiamonds
}
```

### AccessibleCard class — [7:53]

```csharp
using Apple.Accessibility;
public class AccessibleCard : MonoBehaviour 
{
    public PlayingCard cardType;
    public bool isCovered;
    void Start()
    {
        var accessibilityNode = GetComponent<AccessibilityNode>();
        accessibilityNode.accessibilityValueDelegate = () => {
            if (isCovered) {
              return "covered";
            }
            if (cardType == PlayingCard.AceOfSpades) {
              return "Ace of Spades";
            }
        }
    }
}
```

### DynamicCardFaces — [10:35]

```csharp
public class DynamicCardFaces : MonoBehaviour
{
    public Material RegularMaterial;
    public Material LargeMaterial;
    void OnEnable()
    {
        AccessibilitySettings.onPreferredTextSizesChanged += _settingsChanged;
    }

    void _settingsChanged() 
    {
        var shouldUseLarge = AccessibilitySettings.PreferredContentSizeCategory >= 
            ContentSizeCategory.AccessibilityMedium;
        GetComponent<Renderer>().material = shouldUseLarge ? RegularMaterial :
            LargeMaterial;
    }
}
```

### Dynamic Type — [10:36]

```csharp
using UnityEngine.UI;
public class DynamicTextSize : MonoBehaviour
{
    int originalSize;
    void Start()
    {
        originalSize = GetComponent<Text>().textSize;
    }

    void OnEnable()
    {
        AccessibilitySettings.onPreferredTextSizesChanged += _settingsChanged;     }

    void _settingsChanged() 
    {
        GetComponent<Text>().textSize = (int)(originalSize *
            AccessibilitySettings.PreferredContentSizeMultiplier);
    }
}
```

### Reduce motion — [14:54]

```csharp
using Apple.Accessibility;
public class CardController : MonoBehaviour
{
    public void Flip() 
    {
        var reduceMotionOn = !AccessibilitySettings.IsReduceMotionEnabled;
        if (!reduceMotionOn)
        {
            StartCoroutine(Animate());
        }
        else 
        {
            transform.rotation = Quaternion.identify;
        }
    }
    IEnumerator Animate()
    {
    } 
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10151/5/3F44347B-F0CF-4DFC-89A8-C801EE456545/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10151/5/3F44347B-F0CF-4DFC-89A8-C801EE456545/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10151) — developer.apple.com. Indexed for agent consumption._
