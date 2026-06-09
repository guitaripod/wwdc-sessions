# Learn CSS Grid Lanes

**Topic:** Safari & Web · **Platforms:** iOS, iPadOS, macOS, visionOS, watchOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-314](https://developer.apple.com/videos/play/wwdc2026/314)

Build adaptive web layouts that embrace content of all shapes and sizes. Explore how Grid Lanes lets you arrange differently-shaped elements into clean, flexible designs with simple CSS. And find out how flow-tolerance helps you refine accessibility while keeping your layouts malleable.

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [WebKit.org - CSS Grid Lanes Field Guide](https://gridlanes.webkit.org) _documentation_
- [WebKit.org – Report issues to the WebKit open-source project](https://bugs.webkit.org) _documentation_
- [Submit feedback](http://feedbackassistant.apple.com) _documentation_

## Code Snippets

### Create a Grid Lanes Container — [3:58]

```javascript
.container {
	display: grid-lanes;
}
```

### Create a Grid Lanes Container — [4:02]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns: repeat(3, 1fr);
}
```

### Create a Grid Lanes Container — [4:26]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}
```

### Implement a Brick Variation — [4:33]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}
```

### Implement a Brick Variation — [4:36]

```javascript
.container {
	display: grid-lanes;
  grid-template-rows: repeat(3, 1fr);
  gap: 10px;
}
```

### Experiment with different layouts — [4:58]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
}
```

### Experiment with different layouts — [5:02]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns: 1fr 2fr 1fr;
  gap: 10px;
}
```

### Experiment with different layouts — [5:10]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns:
    repeat(auto-fill,
      minmax(200px, 1fr));
  gap: 10px;
}
```

### Experiment with different layouts — [5:24]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns:
    repeat(auto-fill,
      minmax(8rem, 1fr)
      minmax(14rem, 2fr);
  gap: 10px;
}
```

### Control Individual Items — [5:45]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
}
```

### Control Individual Items — [5:59]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
}

.item {
  grid-column: span 2;
}
```

### Control Individual Items — [6:07]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
}

.item {
  grid-column: 2 / span 2;
}
```

### Integrate Subgrid — [6:22]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
}

.item {
  grid-column: span 2;
}
```

### Integrate Subgrid — [6:34]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
}

.item {
  display: grid-lanes;
  grid-template-columns: subgrid;
  grid-column: span 2;
}
```

### Integrate Subgrid — [6:48]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 10px;
}

.item {
  display: grid;
  grid-template-columns: subgrid;
  grid-column: span 2;
}
```

### Improve item positioning — [8:37]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  flow-tolerance: normal;
}
```

### Improve item positioning — [8:41]

```javascript
.container {
	display: grid-lanes;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  flow-tolerance: 2.1em;
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/314/4/72928edd-5728-4010-b8f0-27f1a7bdec8c/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/314/4/72928edd-5728-4010-b8f0-27f1a7bdec8c/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._