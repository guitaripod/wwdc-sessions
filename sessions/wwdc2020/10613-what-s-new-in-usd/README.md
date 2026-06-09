---
id: "wwdc2020-10613"
event: "wwdc2020"
year: 2020
title: "What's new in USD"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10613"
topics: ["Graphics & Games", "Spatial Computing"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# What's new in USD

**Event:** WWDC20 · **Topic:** Spatial Computing · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10613](https://developer.apple.com/videos/play/wwdc2020/10613)

Discover proposed schema and structure updates to the Universal Scene Description (USD) standard. Learn how you can use Reality Composer to build AR content with interactive properties like anchoring, physics, behaviors, 3D text, and spatial audio that exports to USDZ. And, discover streamlined workflows that help you bring newly-created objects into your app. If you're interested to learn more about USDZ as a distribution format, check out "Working with USD.” And for more on creating AR content with Reality Composer, watch “The Artist's AR Toolkit." We’d love to hear feedback about the preliminary schemas. After you watch this session, come join us on the Developer Forums and share your thoughts.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,081 words)

## Code Snippets

### USD scene structure — [11:44]

```javascript
def Xform "Root" (
    kind = "sceneLibrary"
)
{
    def Cube "MyCubeScene" (
        sceneName = "My Cube Scene"
    )
    { 
        ... 
    }

    over Sphere "MySphereScene" (
        sceneName = "My Sphere Scene"
    )
    { 
        ... 
    }
}
```

### Adding anchoring to USD — [13:30]

```javascript
def Cube "ImageAnchoredCube" (
    prepend apiSchemas = [ "Preliminary_AnchoringAPI" ]
)
{
    uniform token preliminary:anchoring:type = "image"
    rel preliminary:imageAnchoring:referenceImage = <ImageReference>

    def Preliminary_ReferenceImage "ImageReference"
    {
        uniform asset image = @image.png@
        uniform double physicalWidth = 12
    }

    ...
}
```

### Defining a behavior — [15:11]

```javascript
def Preliminary_Behavior "TapAndBounce"
{
    rel triggers = [ <Tap> ]
    rel actions = [ <Bounce> ]

    def Preliminary_Trigger "Tap"
    {
        uniform token info:id = "tap"
        rel affectedObjects = [ </Cube> ]
    }

    def Preliminary_Action "Bounce"
    {
        uniform token info:id = "emphasize" 
        uniform token motionType = "bounce"
        rel affectedObjects = [ </Cube> ]
    }

    ...
}
```

### Compound behavior — [16:22]

```swift
def Preliminary_Behavior "TapOrGetCloseAndBounceJiggleAndFlip"
{
    rel triggers = [ <Tap>, <Proximity> ]
    rel actions = [ <Bounce>, <Jiggle>, <Flip> ]

    ...
}
```

### Defining physics — [17:19]

```swift
def Sphere "WoodenBall" (
    prepend apiSchemas = [ "Preliminary_PhysicsColliderAPI",
                           "Preliminary_PhysicsRigidBodyAPI" ]
)
{
    rel preliminary:physics:collider:convexShape = </WoodenBall>
    double preliminary:physics:rigidBody:mass = 10.0
}
```

### Applying a wood material for physics — [18:15]

```javascript
def Material "Wood" (
    prepend apiSchemas = ["Preliminary_PhysicsMaterialAPI"]
)
{
    double preliminary:physics:material:restitution = 0.603
    double preliminary:physics:material:friction:static = 0.375
    double preliminary:physics:material:friction:dynamic = 0.375
}

def Sphere "WoodenBall" (
    prepend apiSchemas = [ "Preliminary_PhysicsColliderAPI",
                           "Preliminary_PhysicsRigidBodyAPI" ]
)
{
    rel preliminary:physics:collider:convexShape = </WoodenBall>
    double preliminary:physics:rigidBody:mass = 10.0
    rel material:binding = </Wood>
}
```

### Defining a ground plane — [18:40]

```javascript
def Xform "MyScene" (
    prepend apiSchemas = ["Preliminary_PhysicsColliderAPI"]
)
{
    def Preliminary_InfiniteColliderPlane "groundPlane" (
        customData = {
            bool preliminary_isSceneGroundPlane = 1
        }
    ) {
        point3d position = (0, 0, -2)
        vector3d normal = (0, 1, 0)
        rel preliminary:physics:collider:convexShape = </MyScene/groundPlane>
    }
    rel material:binding = </Wood>
}
```

### Adding gravity — [19:08]

```swift
def Preliminary_PhysicsGravitationalForce "MoonsGravity"
{
    vector3d physics:gravitationalForce:acceleration = (0, -1.625, 0)
}
```

### Defining spatial audio — [20:28]

```javascript
def SpatialAudio "HorseNeigh"
{
    uniform asset filePath        = @Horse.m4a@
    uniform token auralMode       = "spatial"
    uniform timeCode startTime    =  65.0
    uniform double mediaOffset    =  0.33333333333
    double3 xformOp:translate = (0, 0.5, 0.1)
    uniform token[] xformOpOrder = ["xformOp:translate"]
}
```

### 3D text — [21:45]

```javascript
def Preliminary_Text "heading"
{
    string content = "#WWDC20"
    string[] font = [ "Helvetica", "Arial" ]
    token wrapMode = "singleLine"
    token horizontalAlignment = "center"
    token verticalAlignment = "baseline"
}
```

### Playback metadata — [22:46]

```javascript
#usda 1.0
(
    endTimeCode = 300
    startTimeCode = 1
    timeCodesPerSecond = 30
    playbackMode = "loop"
    autoPlay = false
)

def Xform “AnimatedCube"
{
    ...
}
```

### Scene understanding metadata — [23:08]

```swift
def Xform "Root" (
    kind = "sceneLibrary"
)
{
    def Xform "MyScene" (
        sceneName = "My Scene"
        preliminary_collidesWithEnvironment = true
    )
    {
        def Xform "DigitalBug"
        {
            ...
        }
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10613/5/2355BD15-75EB-4F6F-951C-91C1A46242E1/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10613) — developer.apple.com. Indexed for agent consumption._
