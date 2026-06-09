---
id: "wwdc2021-10210"
event: "wwdc2021"
year: 2021
title: "Explore advanced project configuration in Xcode"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2021/10210"
topics: ["Developer Tools"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Explore advanced project configuration in Xcode

**Event:** WWDC21 · **Topic:** Developer Tools · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2021-06-11 · **Session:** [wwdc2021-10210](https://developer.apple.com/videos/play/wwdc2021/10210)

Working with more complex Xcode projects? You’ve come to the right place. Discover how you can configure your project to build for multiple Apple platforms, filter content per-platform, create custom build rules and file dependencies, and more. We’ll take you through multi-platform framework targets, detail how to optimize your project and scheme configuration, and show you how to make effective use of configuration settings files. We’ll explore configuring schemes for parallel builds and implicit dependencies, script phases, custom build rules, setting up input and output file dependencies, build phase file lists, and deduplicating work via aggregate targets. Lastly, find out more about the build settings editor, how levels work, and configuration settings file syntax.

**Keywords:** `build`, `build phase`, `build settings`, `multiplatform`, `project`, `scheme`, `script phase`, `xcconfig`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(3,678 words)

## Code Snippets

### Shell Script - Output Files — [7:38]

```bash
$(DERIVED_FILE_DIR)/$(INPUT_FILE_BASE).compiledrecipe
```

### Build Rule - code — [8:22]

```bash
"$SRCROOT/Scripts/gen-code.sh" "$SCRIPT_INPUT_FILE" "$SCRIPT_OUTPUT_FILE_0"
```

### Shell Script - code — [10:15]

```bash
# Package up the recipes.

echo "packaging..."

for i in $(seq 0 $(expr ${SCRIPT_INPUT_FILE_LIST_COUNT} - 1)) ; do
    infile_="SCRIPT_INPUT_FILE_LIST_$i"
    eval infile=\$$infile_

    while IFS= read -r file; do
        cat "$file" >> "$SCRIPT_OUTPUT_FILE_0"
    done < "$infile"
done
```

### XCFileList — [11:34]

```bash
$(SRCROOT)/Recipes/Instructions/berry-blue.md
$(SRCROOT)/Recipes/Instructions/carrot-chops.md
$(SRCROOT)/Recipes/Instructions/hulking-lemonade.md
$(SRCROOT)/Recipes/Instructions/kiwi-cutie.md
$(SRCROOT)/Recipes/Instructions/lemonberry.md
$(SRCROOT)/Recipes/Instructions/love-you-berry-much.md
$(SRCROOT)/Recipes/Instructions/mango-jambo.md
$(SRCROOT)/Recipes/Instructions/one-in-a-melon.md
$(SRCROOT)/Recipes/Instructions/papas-papaya.md
$(SRCROOT)/Recipes/Instructions/pina-y-coco.md
```

### Shell Script - Input File Lists — [11:57]

```bash
$(SRCROOT)/FileList.xcfilelist
```

### Shell Script - Output Files — [12:11]

```bash
$(PROJECT_TEMP_DIR)/instructions.mdarchive
```

### Environment Variables - Script Phases — [12:50]

```bash
// These environment variables are available in script phases:

SCRIPT_INPUT_FILE_COUNT // This specifies the number of paths from the Input Files table.
SCRIPT_INPUT_FILE_n // This specifies the absolute path of the nth file from the Input Files table, with build settings expanded.

SCRIPT_INPUT_FILE_LIST_COUNT // This specifies the number of input file lists.
SCRIPT_INPUT_FILE_LIST_n // This specifies the absolute path of the nth "resolved" input file list with contained paths made absolute, build settings expanded, and comments removed.

SCRIPT_OUTPUT_FILE_COUNT // This specifies the number of paths from the Output Files table.
SCRIPT_OUTPUT_FILE_n // This specifies the absolute path of the nth file from the Output Files table, with build settings expanded.

SCRIPT_OUTPUT_FILE_LIST_COUNT // This specifies the number of output file lists.
SCRIPT_OUTPUT_FILE_LIST_n // This specifies the absolute path of the nth "resolved" output file list with contained paths made absolute, build settings expanded, and comments removed.

* n in the above examples refers to a 0-based index.
```

### Environment Variables - Build Rules — [13:00]

```bash
// These environment variables are available in build rules:

SCRIPT_INPUT_FILE // This specifies the absolute path of the main input file being processed by the rule.

OTHER_INPUT_FILE_FLAGS // This specifies custom command line flags defined for the input file in the Compile Sources build phase.

SCRIPT_INPUT_FILE_COUNT // This specifies the number of paths from the Input Files table.
SCRIPT_INPUT_FILE_n // This specifies the absolute path of the nth file from the Input Files table, with build settings expanded.

SCRIPT_OUTPUT_FILE_COUNT // This specifies the number of paths from the Output Files table.
SCRIPT_OUTPUT_FILE_n // This specifies the absolute path of the nth file from the Output Files table, with build settings expanded.

SCRIPT_HEADER_VISIBILITY // This is set to "public" or "private" if the input file being processed is a header file in a Headers build phase, and its Header Visibility is set to one of those values.

HEADER_OUTPUT_DIR // This specifies the output directory to which the input file should be copied, if the input file being processed is a header file in a Headers build phase.

* n in the above examples refers to a 0-based index.
```

### Build setting definition — [18:17]

```bash
MY_BUILD_SETTING_NAME = "A build setting value"
```

### Build setting definition with conditions — [18:30]

```bash
MY_BUILD_SETTING_NAME = "A build setting value"
MY_BUILD_SETTING_NAME[config=Debug] = -debug_flag
MY_BUILD_SETTING_NAME[arch=arm64] = -arm64_only
MY_BUILD_SETTING_NAME[sdk=iphone*] = -ios_only
```

### Build setting composition — [19:50]

```bash
IS_BUILD_SETTING_ENABLED = NO
MY_BUILD_SETTING_NO = -use_this_one
MY_BUILD_SETTING_YES = -use_this_instead
MY_BUILD_SETTING = $(MY_BUILD_SETTING_$(IS_BUILD_SETTING_ENABLED))
```

### Build setting evaluation operators (paths) — [21:08]

```bash
$(MY_PATH:dir)
$(MY_PATH:file)
$(MY_PATH:base)
$(MY_PATH:suffix)
$(MY_PATH:standardizepath)
```

### Build setting evaluation operators (replacement) — [21:21]

```bash
$(MY_PATH:dir=/tmp)
$(MY_PATH:file=/better.swift)
$(MY_PATH:base=another)
$(MY_PATH:suffix=m)
$(MY_PATH:default=YES)
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10210/4/391A6CFB-228A-4349-AE24-4809307D58F5/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2021/10210/4/391A6CFB-228A-4349-AE24-4809307D58F5/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2021/10210) — developer.apple.com. Indexed for agent consumption._
