---
id: "wwdc2021-10211"
event: "wwdc2021"
year: 2021
title: "Symbolication: Beyond the basics"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10211"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Symbolication: Beyond the basics

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-09 · **Session:** [wwdc2021-10211](https://developer.apple.com/videos/play/wwdc2021/10211)

Discover how you can achieve maximum performance and insightful debugging with your app. Symbolication is at the center of tools such as Instruments and LLDB to help bridge the layers between your application’s runtime and your source code. Learn how this process works and the steps you can take to gain the most insight into your app.

**Keywords:** `atos`, `dsym`, `dwarf`, `instruments`, `lldb`, `otool`, `symbolication`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,955 words)

## Code Snippets

### MagicNumbers — [1:11]

```swift
func selectMagicNumber(choices: [Int]) -> Int {
    return choices[MAGIC_CHOICE]
}

func randomValue() -> Int {
    return Int.random(in: 1...100)
}

func numberChoices() -> [Int] {
    var choices = [Int]()
    for _ in 1...10 {
        choices.append(randomValue())
    }
    return choices
}

func generateMagicNumber() -> Int {
    let numbers = numberChoices()
    let magic = selectMagicNumber(choices: numbers)
    return magic
}

print("The magic number is: \(generateMagicNumber())")
```

### atos symbolication — [2:51]

```bash
atos -o MagicNumbers.dSYM/Contents/Resources/DWARF/MagicNumbers -arch arm64 -l 0x10045c000 -i 0x10045fb70
```

### Load commands — [7:34]

```bash
otool -l MagicNumbers | grep LC_SEGMENT -A8
```

### Disassembly — [10:31]

```bash
otool -tV MagicNumbers -arch arm64
```

### vmmap — [11:32]

```bash
vmmap MagicNumbers | grep __TEXT
```

### Function starts — [15:09]

```bash
symbols -onlyFuncStartsData -arch arm64 MagicNumbers
```

### nlist_64 — [17:06]

```objectivec
struct nlist_64 {
    union {
        uint32_t  n_strx;
    } n_un;
    uint8_t n_type;
    uint8_t n_sect;
    uint16_t n_desc;
    uint64_t n_value; 
};
```

### Direct symbols with nm — [17:59]

```bash
nm -arch arm64 —defined-only --numeric-sort MagicNumbers
```

### Demangled direct symbols with nm — [18:30]

```bash
nm -arch arm64 —defined-only --numeric-sort MagicNumbers | xcrun swift-demangle
```

### Demangled direct symbols with the symbols tool — [18:43]

```bash
symbols -arch arm64 -onlyNListData MagicNumbers
```

### Indirect symbols with nm — [23:06]

```bash
nm -m —arch arm64 --undefined-only --numeric-sort MagicNumbers
```

### Examining dSYMs with dwarfdump — [27:16]

```bash
dwarfdump -v -debug-info -arch arm64 MagicNumbers.dSYM
```

### atos symbolication without inlined functions — [29:25]

```bash
atos -o MagicNumbers.dSYM/Contents/Resources/DWARF/MagicNumbers -arch arm64 —l 0x10045c000 0x10045fb70
```

### Examining debugging symbols — [32:29]

```bash
dsymutil --dump-debug-map -arch arm64 MagicNumbers
```

### Examining dSYM UUIDs — [33:59]

```bash
symbols -uuid MagicNumbers.dSYM
```

### Verifying DWARF — [34:03]

```bash
dwarfdump —verify MagicNumbers.dSYM
```

### Verifying entitlements and codesigning — [35:09]

```bash
codesign --display -v  --entitlements :- MagicApp.app
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10211/3/3450A29E-DC2D-49D5-9D68-5E053CC5EC9D/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10211/3/3450A29E-DC2D-49D5-9D68-5E053CC5EC9D/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10211) — developer.apple.com. Indexed for agent consumption._
