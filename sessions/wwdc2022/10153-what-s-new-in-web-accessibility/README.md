---
id: "wwdc2022-10153"
event: "wwdc2022"
year: 2022
title: "What's new in web accessibility"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10153"
topics: ["Essentials", "Safari & Web", "SwiftUI & UI Frameworks", "Accessibility & Inclusion"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What's new in web accessibility

**Event:** WWDC22 · **Topic:** Accessibility & Inclusion · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-09 · **Session:** [wwdc2022-10153](https://developer.apple.com/videos/play/wwdc2022/10153)

Discover techniques for building rich, accessible web apps with custom controls, SSML, and the dialog element. We'll discuss different assistive technologies and help you learn how to use them when testing the accessibility of your web apps.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,522 words)

## Documentation & Resources

- [Learn VoiceOver gestures on iPhone](https://support.apple.com/guide/iphone/learn-voiceover-gestures-iph3e2e2281/ios) _guide_
- [Speech Synthesis Markup Language (SSML)](https://www.w3.org/TR/speech-synthesis/) _guide_
- [Dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialogmodal/) _guide_

## Code Snippets

### PizzaControl class with click event listener — [3:06]

```javascript
class PizzaControl {
  constructor(id) {
    this.control = document.getElementById(id);
    this.sliceCount = 4;

    this.control.addEventListener("click", (event) => {
      const newSliceCount = this.computeSliceCount(event);
      this.update(newSliceCount);
    });
  }
}
```

### PizzaControl HTML markup — [4:23]

```markdown
<div id="pizza-input" 
     role="slider" tabindex="0"
     aria-valuemin="0" aria-valuemax="8"
     aria-valuenow="4" aria-valuetext="4 slices">
</div>
```

### PizzaControl class with keydown event listener — [5:15]

```javascript
class PizzaControl {
  constructor(id) {
    this.control = document.getElementById(id);
    this.sliceCount = 4;

    // …click event listener…

    this.control.addEventListener("keydown", (event) => {
      const key = event.key;
      if (key === "ArrowRight" || key === "ArrowUp")
        this.update(this.sliceCount + 1);
      else if (key === "ArrowLeft" || key === "ArrowDown")
        this.update(this.sliceCount - 1);
    });
  }
}
```

### PizzaControl class update function — [5:41]

```javascript
class PizzaControl {
  // …constructor…

  update(newSliceCount) {
    this.sliceCount = Math.max(0, Math.min(newSliceCount, 8));

    // Visually re-render `this.sliceCount` slices
    // …

    // Update the ARIA representation of the control
    this.control.setAttribute("aria-valuenow", this.sliceCount);
    const sliceModifier = this.sliceCount === 1 ? "slice" : "slices";
    this.control.setAttribute("aria-valuetext", `${this.sliceCount} ${sliceModifier}`);
  }
}
```

### SSML examples — [7:52]

```markdown
<speak>
  Breathe in <break time="3s"/> and breathe out.
</speak>

<speak>
  <phoneme alphabet="ipa" ph="təˈmeɪtoʊ">tomato</phoneme>
  <phoneme alphabet="ipa" ph="təˈmɑːtəʊ">tomato</phoneme>
</speak>

<speak>
  <prosody pitch="-2st" rate="slow" volume="loud">
    Hello world!
  </prosody>
</speak>
```

### "Read question" button HTML markup — [8:45]

```markdown
<button id="read-question-btn">
  Read question<span aria-hidden="true">🔊</span>
</button>
```

### wrapWithSSML JavaScript function — [8:57]

```javascript
function wrapWithSSML(phrase, locale) {
  return `
    <break time=“100ms"/>
    <prosody rate=“80%">
      <lang xml:lang="${locale}">
        ${phrase}
      </lang>
    </prosody>
  `;
}
```

### Read question button click event listener — [9:24]

```javascript
const readQuestionButton =
  document.getElementById("read-question-btn");

readQuestionButton.addEventListener("click", () => {
  const ssml = `
    <speak>
      How do you say
        ${wrapWithSSML("the water", "en-US")}
      in Spanish?
      ${wrapWithSSML("El agua", "es-MX")}
      ${wrapWithSSML("La abuela", "es-MX")}
      ${wrapWithSSML("La abeja", "es-MX")}
      ${wrapWithSSML("El árbol", "es-MX")}
    </speak>
  `;
  const utterance = new SpeechSynthesisUtterance(ssml);
  window.speechSynthesis.speak(utterance);
});
```

### Show score dialog HTML markup — [11:33]

```markdown
<dialog id="show-score-modal">
  <form method="dialog">
    You got all six questions correct. Great work!
    <button type="submit">Close</button>
  </form>
</dialog>
```

### JavaScript to open show score dialog — [11:51]

```javascript
const showScoreButton =
  document.getElementById("show-score-btn");

showScoreButton.addEventListener("click", () => {
  document
    .getElementById("show-score-modal")
    .showModal();
});
```

### Show score dialog with autofocus and aria-labelledby attribute — [13:23]

```markdown
<dialog id="show-score-modal" aria-labelledby="modal-content">
  <form method="dialog">
    <span id="modal-content">
      You got all six questions correct. Great work!
    </span>
    <button type="submit" autofocus>Close</button>
  </form>
</dialog>
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10153/6/390C5399-8CDD-4D3E-8701-29B14E042A94/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10153/6/390C5399-8CDD-4D3E-8701-29B14E042A94/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10153) — developer.apple.com. Indexed for agent consumption._
