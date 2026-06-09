---
id: "wwdc2020-10680"
event: "wwdc2020"
year: 2020
title: "Refine Objective-C frameworks for Swift"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10680"
topics: ["Developer Tools", "Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "watchOS"]
hasTranscript: true
---

# Refine Objective-C frameworks for Swift

**Event:** WWDC20 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, watchOS · **Published:** 2020-06-26 · **Session:** [wwdc2020-10680](https://developer.apple.com/videos/play/wwdc2020/10680)

Fine-tune your Objective-C headers to work beautifully in Swift. We’ll show you how to take an unwieldy Objective-C framework and transform it into an API that feels right at home. Learn about the suite of annotations you can use to provide richer type information, more idiomatic names, and better errors to Swift. And discover Objective-C conventions you might not have known about that are key to a well-behaved Swift API. To get the most out of this session, you should be familiar with Swift and Objective-C. For more on working with Swift and Objective-C, check out our Developer Documentation and take a look at “Behind the Scenes of the Xcode Build Process” from WWDC18.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(7,317 words)

## Documentation & Resources

- [Objective-C and C Code Customization](https://developer.apple.com/documentation/Swift/objective-c-and-c-code-customization) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Swift/objective-c-and-c-code-customization
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Swift/objective-c-and-c-code-customization.json

## Code Snippets

### Describe nullability to control optionals (method and property annotations) — [4:43]

```objectivec
//
// SKMission.h
//
// View the generated interface to see how Swift imports this header.
//

#import <Foundation/Foundation.h>

@interface SKMission : NSObject

@property (readonly, nullable) NSString *name;

- (nonnull instancetype)initWithName:(nullable NSString *)name;

@end
```

### Describe nullability to control optionals (ASSUME_NONNULL blocks) — [6:53]

```objectivec
//
// SKMission.h
//
// View the generated interface to see how Swift imports this header.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface SKMission : NSObject

@property (readonly, nullable) NSString *name;

- (instancetype)initWithName:(nullable NSString *)name;

@end

NS_ASSUME_NONNULL_END
```

### Describe nullability to control optionals (qualifiers) — [7:14]

```objectivec
//
// Misc.h
//
// View the generated interface to see how Swift imports this header.
//

#import <Foundation/Foundation.h>

NSString * _Nonnull const SKRocketSaturnV;

@interface ResourceValueContainer : NSObject

- (BOOL)getResourceValue:(id _Nullable * _Nonnull)outValue error:(NSError**)error;

@end
```

### Finding nullability mistakes with Objective-C tools — [8:09]

```objectivec
//
// SKMission.h
//

#import <Foundation/Foundation.h>

@interface SKMission : NSObject

@property (strong, nonnull) NSString *rocket;
@property (strong, nonnull) NSString *capsule;

@end

//
// SKRocket.h
//

#import <Foundation/Foundation.h>

extern NSString *_Nonnull const SKRocketSaturnV;

// 
// SKMission.m
//
// Try building this file and then try analyzing it.
//

#import "SKRocket.h"
#import "SKMission.h"

@implementation SKMission @end

@interface SKMissionConfigurator : NSObject

@property (strong, nullable) SKMission *mission;

@end

@implementation SKMissionConfigurator

- (void)testBadUseWithWarning {
    [self.mission setCapsule:nil];
}

- (void)testBadUseWithStaticAnalyzer:(BOOL)missionIsSkylab1 {
    NSString *capsule = nil;

    if (!missionIsSkylab1) {
        capsule = SKCapsuleApolloCSM;
    }

    self.mission.capsule = capsule;
}

@end
```

### Use Objective-C generics for Foundation types — [11:07]

```objectivec
//
// SKAstronaut.h
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface SKAstronaut : NSObject
// Stub declaration
@end

NS_ASSUME_NONNULL_END

//
// SKMission.h
//
// View the generated interface to see how Swift imports this header.
//

#import <Foundation/Foundation.h>
#import <SpaceKit/SKAstronaut.h>

NS_ASSUME_NONNULL_BEGIN

@interface SKMission : NSObject

@property (readonly) NSArray<SKAstronaut *> *crew;

@end

NS_ASSUME_NONNULL_END
```

### Use Int for numbers—unsigned types are for bitwise operations — [11:33]

```objectivec
//
// SKRocket.h
//
// View the generated interface to see how Swift imports this header.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

NSInteger SKRocketStageCount(NSString *);

NS_ASSUME_NONNULL_END

//
// NSData+xor.h
//
// View the generated interface to see how Swift imports this header.
//

#import <Foundation/Foundation.h>

@interface NSData (xor)

- (void)xorWithByte:(uint8_t)value;

@end
```

### Strengthen stringly-typed constants — [13:23]

```objectivec
//
// SKRocket.h
//
// View the generated interface to see how Swift imports this header.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

typedef NSString *SKRocket NS_STRING_ENUM;

extern SKRocket const SKRocketAtlas;
extern SKRocket const SKRocketTitanII;
extern SKRocket const SKRocketSaturnIB;
extern SKRocket const SKRocketSaturnV;

NSInteger SKRocketStageCount(SKRocket);

NS_ASSUME_NONNULL_END
```

### Specify initializer behavior — [15:24]

```objectivec
//
// SKAstronaut.h
//
// View the generated interface to see how Swift imports this header.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface SKAstronaut : NSObject

- (instancetype)initWithNameComponents:(NSPersonNameComponents *)name NS_DESIGNATED_INITIALIZER;
- (instancetype)initWithName:(NSString *)name;
- (instancetype)init NS_UNAVAILABLE;

@property (strong, readwrite) NSPersonNameComponents *nameComponents;
@property (readonly) NSString *name;

@end

NS_ASSUME_NONNULL_END

// 
// SKAstronaut.m
// 

#import "SKAstronaut.h"

@interface SKAstronaut ()
@property (class, readonly, strong) NSPersonNameComponentsFormatter *nameFormatter;
@end

@implementation SKAstronaut

- (id)initWithNameComponents:(NSPersonNameComponents *)name {
    self = [super init];
    if (self) {
        _name = name;
    }
    return self;
}

- (id)initWithName:(NSString *)name {
    return [self initWithNameComponents:[SKAstronaut _componentsFromName:name]];
}

- (id)init {
  [self doesNotRecognizeSelector:_cmd];
  return nil;
}

- (NSString *)name {
    return [SKAstronaut.nameFormatter stringFromPersonNameComponents:self.nameComponents];
}

+ (NSPersonNameComponents*)_componentsFromName:(NSString*)name {
    return [self.nameFormatter personNameComponentsFromString:name];
}

+ (NSPersonNameComponentsFormatter *)nameFormatter {
    static NSPersonNameComponentsFormatter *singleton;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        singleton = [NSPersonNameComponentsFormatter new];
    });
    return singleton;
}

@end
```

### Follow the error handling convention — [20:00]

```objectivec
//
// SKMission.h
//
// View the generated interface to see how Swift imports this header.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface SKMission : NSObject

/// \returns \c YES if saved; \c NO with non-nil \c *error if failed to save;
///          \c NO with nil \c *error` if nothing needed to be saved.
- (BOOL)saveToURL:(NSURL *)url error:(NSError **)error NS_SWIFT_NOTHROW DEPRECATED_ATTRIBUTE;

/// @param[out] wasDirty If provided, set to \c YES if the file needed to be
///   saved or \c NO if there weren’t any changes to save.
- (BOOL)saveToURL:(NSURL *)url wasDirty:(nullable BOOL *)wasDirty error:(NSError **)error;

@end

NS_ASSUME_NONNULL_END
```

### Refine an Objective-C API for Swift users — [22:40]

```objectivec
//
// SKMission.h
//
// View the generated interface to see how Swift imports this header.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface SKMission : NSObject

/// \returns \c YES if saved; \c NO with non-nil \c *error if failed to save;
///          \c NO with nil \c *error` if nothing needed to be saved.
- (BOOL)saveToURL:(NSURL *)url error:(NSError **)error NS_SWIFT_NOTHROW DEPRECATED_ATTRIBUTE;

/// @param[out] wasDirty If provided, set to \c YES if the file needed to be
///   saved or \c NO if there weren’t any changes to save.
- (BOOL)saveToURL:(NSURL *)url wasDirty:(nullable BOOL *)wasDirty error:(NSError **)error NS_REFINED_FOR_SWIFT;

@end

NS_ASSUME_NONNULL_END

// 
// SwiftExtensions.swift
//

import Foundation

extension SKMission {
    public func save(to url: URL) throws -> Bool {
        var wasDirty: ObjCBool = false
        try self.__save(to: url, wasDirty: &wasDirty)
        return wasDirty.boolValue
    }
}
```

### Fix method names with NS_SWIFT_NAME — [31:35]

```objectivec
//
// SKMission.h
//
// View the generated interface to see how Swift imports this header.
//

#import <Foundation/Foundation.h>
#import <SKAstronaut/SKAstronaut.h>

NS_ASSUME_NONNULL_BEGIN

@interface SKMission : NSObject

- (NSSet<SKMission *> *)previousMissionsFlownByAstronaut:(SKAstronaut *)astronaut NS_SWIFT_NAME(previousMissions(flownBy:));

@end
```

### Rename and rework value types with NS_SWIFT_NAME — [33:12]

```objectivec
//
// SKFuelKind.h
//
// View the generated interface to see how Swift imports this header.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface SKFuel : NSObject
// Stub class
@end

typedef NS_ENUM(NSInteger, SKFuelKind) {
    SKFuelKindH2 = 0,
    SKFuelKindCH4 = 1,
    SKFuelKindC12H26 = 2
} NS_SWIFT_NAME(SKFuel.Kind);

NSString *SKFuelKindToNSString(SKFuelKind kind)
    NS_SWIFT_NAME(getter:SKFuelKind.description(self:));
```

### Add conformances to Objective-C types using custom Swift code — [35:59]

```swift
extension SKFuel.Kind: CustomStringConvertible {}
```

### Improve error code enums — [37:02]

```objectivec
//
//  SKError.h
//  SpaceKit
//

#import <Foundation/Foundation.h>

extern NSString *const SKErrorDomain;

typedef NS_ERROR_ENUM(SKErrorDomain, SKErrorCode) {
    SKErrorLaunchAborted = 1,
    SKErrorLaunchOutOfRange,
    SKErrorRapidUnscheduledDisassembly,
    SKErrorNotGoingToSpaceToday
};
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10680/6/733DC040-9073-4427-B411-BBF7BEE212B4/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10680) — developer.apple.com. Indexed for agent consumption._
