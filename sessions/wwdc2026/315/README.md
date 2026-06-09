---
id: "wwdc2026-315"
event: "wwdc2026"
year: 2026
title: "Rediscover the HTML select element"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/315"
topics: ["Design", "Safari & Web"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Rediscover the HTML select element

**Event:** WWDC26 · **Topic:** Safari & Web · **Platforms:** iOS, iPadOS, macOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-315](https://developer.apple.com/videos/play/wwdc2026/315)

Learn how to unlock full control of styling select menus on the web. The HTML select element is getting a major upgrade with a new CSS appearance value, and new pseudo-elements. Discover how the select options can contain rich content with new possibilities in HTML. Build selects that match your design system, while keeping all the accessibility and robustness of the default element.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,523 words)

## Documentation & Resources

- [WebKit.org - Example website demonstrating Customizable Select](https://webkit.org/demos/customizable-select/) _documentation_
- [WebKit.org - CSS Grid Lanes Field Guide](https://gridlanes.webkit.org) _documentation_
- [WebKit.org – Report issues to the WebKit open-source project](https://bugs.webkit.org) _documentation_
- [Submit feedback](http://feedbackassistant.apple.com) _documentation_

## Code Snippets

### Basic markup — [1:11]

```xml
<label for="sort-select">Sort by</label>
<select id="sort-select">
    <option>Newest</option>
    <option>Oldest</option>
</select>
```

### Native form control — [2:37]

```yaml
select {

}
```

### appearance: base-select — [2:50]

```yaml
body {
    font-family: Gill Sans, sans-serif;
}

select {
    appearance: base-select;
}
```

### Style the select button — [3:07]

```yaml
select {
    appearance: base-select;
    background-color: var(--green-10);
    border: none;
    padding: 0.6em 1em;
}
```

### Picker icon — [3:08]

```yaml
select:open {
    background-color: var(--green-100);
    color: white;
}
```

### Picker icon open state — [3:29]

```yaml
select:open {
    background-color: var(--green-100);
    color: white;
}

select:open::picker-icon {
    content: url(icons/arrow-white.svg);
}
```

### Picker select — [4:08]

```yaml
::picker(select) {

}
```

### Picker select spacing — [4:21]

```yaml
::picker(select) {
    appearance: base-select;
    padding: 4px;
    margin-top: 0.5em;
}
```

### Picker select border and shadow — [4:28]

```yaml
::picker(select) {
    appearance: base-select;
    padding: 4px;
    margin-top: 0.5em;
    border: 1px solid rgba(0,0,0,0.2);
    border-radius: 9px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
}
```

### Custom option styles — [4:36]

```yaml
option:checked {
    font-weight: 600;
}

option:not(:checked) {
    color: #777;
}
```

### Picker option checkmark — [4:42]

```yaml
option::checkmark {
    content: url(checkmark.svg);
    width: 0.65em;
}
```

### Images in option — [5:31]

```xml
<option value="flower">
    <img src="flowers.svg" alt="">
    <span class="text">Flowers</span>
</option>
```

### Custom option highlight — [5:52]

```yaml
option::checkmark {
    display: none;
}

option:checked {
    background: #00857e;
    color: white;
}
```

### Grid layout in drop downs — [6:20]

```yaml
::picker(select) {
    display: grid;
    grid-template: 
       1fr 1fr / 1fr 1fr 1fr;
    gap: 1rem;
}
```

### Select with image options — [6:43]

```xml
<select>
    <option value="anywhere">
        <img src="icons/all.svg" alt="">
        <span class="text">Everything</span>
    </option>
    <option value="buildings">
        <img src="icons/buildings.svg" alt="">
        <span class="text">Buildings</span>
    </option>
    <option value="flowers">
        <img src="icons/flower.svg" alt="">
        <span class="text">Flowers</span>
    </option>

</select>
```

### Select menu — [7:11]

```xml
<select>



    <option>    </option>
    <option>    </option>
    <option>    </option>
</select>
```

### Select menu button — [7:13]

```xml
<select>
    <button>

    </button>
    <option>    </option>
    <option>    </option>
    <option>    </option>
</select>
```

### SelectedContent Element — [7:29]

```xml
<select>
    <button>
        <selectedcontent></selectedcontent>
    </button>
    <option>     </option>
    <option>     </option>
    <option>     </option>
</select>
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/315/4/f3bd9835-9ced-4f6a-a0f1-655000972674/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/315/4/f3bd9835-9ced-4f6a-a0f1-655000972674/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/315) — developer.apple.com. Indexed for agent consumption._