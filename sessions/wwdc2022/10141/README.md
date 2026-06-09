---
id: "wwdc2022-10141"
event: "wwdc2022"
year: 2022
title: "Explore USD tools and rendering"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10141"
topics: ["Spatial Computing", "Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Explore USD tools and rendering

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS · **Published:** 2022-06-08 · **Session:** [wwdc2022-10141](https://developer.apple.com/videos/play/wwdc2022/10141)

Discover the latest advancements in tooling to help you generate, inspect, and convert Universal Scene Description (USD) assets. We'll learn about updates to these tools and help you integrate them into your content creation pipeline. We'll also explore the power of USD Hydra rendering, and show how you can integrate it into your own apps.

For an introduction to USD, watch "Understand USD fundamentals" from WWDC22.

**Keywords:** `ar`, `arkit`, `augmented reality`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,759 words)

## Documentation & Resources

- [Creating a 3D application with hydra rendering](https://developer.apple.com/documentation/Metal/creating-a-3d-application-with-hydra-rendering) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Metal/creating-a-3d-application-with-hydra-rendering
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Metal/creating-a-3d-application-with-hydra-rendering.json
- [Introduction to Universal Scene Description (USD)](https://graphics.pixar.com/usd/docs/index.html) _documentation_
- [ASWF USD Working Group](https://wiki.aswf.io/display/WGUSD/USD+Working+Group) _documentation_

## Code Snippets

### Phyton usdconvert --help — [3:00]

```python
% python usdzconvert --help
usdzconvert 0.66
usage: usdzconvert inputFile [outputFile]
                   [-h] [-version] [-f file] [-v]
                   [-path path[+path2[...]]]
                   [-url url]
                   [-copyright copyright]
                   [-copytextures]
                   [-metersPerUnit value]
                   // ...
                   [-diffuseColor           r,g,b]
                   [-diffuseColor           <file> fr,fg,fb]
                   [-normal                 x,y,z]
                   [-normal                 <file> fx,fy,fz]
                   // ...
```

### choosing lighting in usda metadata — [9:00]

```objectivec
// asset.usda
#usda 1.0
(
    customLayerData = {
        dictionary Apple = {
             int preferredIblVersion = 2
        }
    }
)
```

### Build USD + Hydra — [17:50]

```python
// Rosetta
% arch -x86_64 /bin/zsh

// Download source code
% git clone https://github.com/PixarAnimationStudios/USD.git 

// Build USD + Hydra
% python3 USD/build_scripts/build_usd.py --generator Xcode --no-python USDInstall
```

### Load USD ViewController — [18:54]

```objectivec
// AAPLViewController.mm

- (void)viewDidAppear
{   
    NSOpenPanel* panel = [NSOpenPanel openPanel];
    panel.allowedContentTypes = @[UTTypeUSD, UTTypeUSDZ];

    [panel beginWithCompletionHandler:^(NSModalResponse result) {
        if (result == NSModalResponseOK)
        {
            NSURL* url = panel.URLs[0];
            [self->_renderer setupScene:[url path]];
        }
    }];
}

// AAPLRenderer.mm

- (bool)loadStage:(NSString*)filePath
{
    _stage = UsdStage::Open([filePath UTF8String]);
    // ...
}
```

### Create Scene Camera — [19:30]

```objectivec
// AAPLRenderer.mm

- (void)setupCamera
{
    _viewCamera = [[AAPLCamera alloc] initWithRenderer:self];

    [self calculateWorldCenterAndSize];

    [_viewCamera setDistance:_worldSize];
    [_viewCamera setFocus:_worldCenter];

}
```

### Create Scene Light — [19:54]

```objectivec
// AAPLRenderer.mm

GlfSimpleLight computeCameraLight(const GfMatrix4d& cameraTransform)
{
    GlfSimpleLight light;
    light.SetPosition(GfVec4f(cameraPosition[0], cameraPosition[1], cameraPosition[2], 1));

    return light;
}
```

### transport to storm — [20:17]

```objectivec
// AAPLRenderer.mm

- (void)initializeEngine
{
    _engine.reset(new UsdImagingGLEngine(_stage->GetPseudoRoot().GetPath(),
                                         excludedPaths,
                                         SdfPathVector(),
                                         SdfPath::AbsoluteRootPath(),
                                         driver));
}

// AAPLRenderer.mm

- (HgiTextureHandle)drawWithHydraAt:(double)timeCode
                           viewSize:(CGSize)viewSize
{
      _engine->SetCameraState(modelViewMatrix, projMatrix);
      _engine->SetLightingState(lights, _material, _sceneAmbient);

      UsdImagingGLRenderParams params;
      params.clearColor = GfVec4f(0.0f, 0.0f, 0.0f, 0.0f);
      params.frame = timeCode;

      // ... 
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10141/4/31DD4CF1-C4A2-4A5C-A3C8-B231788AE125/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10141/4/31DD4CF1-C4A2-4A5C-A3C8-B231788AE125/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10141) — developer.apple.com. Indexed for agent consumption._