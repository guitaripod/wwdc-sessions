---
id: "wwdc2024-10217"
event: "wwdc2024"
year: 2024
title: "Explore Swift performance"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2024/10217"
topics: ["Swift"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS", "visionOS", "watchOS"]
hasTranscript: true
---

# Explore Swift performance

**Event:** WWDC24 · **Topic:** Swift · **Platforms:** iOS, iPadOS, macOS, tvOS, visionOS, watchOS · **Published:** 2024-06-13 · **Session:** [wwdc2024-10217](https://developer.apple.com/videos/play/wwdc2024/10217)

Discover how Swift balances abstraction and performance. Learn what elements of performance to consider and how the Swift optimizer affects them. Explore the different features of Swift and how they’re implemented to further understand the tradeoffs available that can impact performance.

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,499 words)

## Documentation & Resources

- [Forum: Programming Languages](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010) _developerForum_
  - Markdown (sosumi.ai): https://sosumi.ai/forums/topics/programming-languages-topic?cid=vf-a-0010

## Code Snippets

### An example C function, with self-evident allocation — [0:24]

```cpp
int main(int argc, char **argv) {
  int count = argc - 1;
  int *arr = malloc(count * sizeof(int));
  int i;
  for (i = 0; i < count; ++i) {
    arr[i] = atoi(argv[i + 1]);
  }
  free(arr);
}
```

### An example Swift function, with a lot of implicit abstraction — [0:50]

```swift
func main(args: [String]) {
  let arr = args.map { Int($0) ?? 0 }
}
```

### An example of a function call — [4:39]

```swift
URLSession.shared.data(for: request)
```

### A Swift function that calls a method on a value of protocol type — [6:30]

```swift
func updateAll(models: [any DataModel], from source: DataSource) {
    for model in models {
        model.update(from: source)
    }
}
```

### A declaration of the method where it's a protocol requirement using dynamic dispatch — [6:40]

```swift
protocol DataModel {
    func update(from source: DataSource)
}
```

### A declaration of the method where it's a protocol extension method using static dispatch — [6:50]

```swift
protocol DataModel {
    func update(from source: DataSource, quickly: Bool)
}

extension DataModel {
    func update(from source: DataSource) {
        self.update(from: source, quickly: true)
    }
}
```

### The same function as before, which we're now talking about the local state within — [7:00]

```swift
func updateAll(models: [any DataModel],
               from source: DataSource) {
    for model in models {
        model.update(from: source)
    }
}
```

### Partial assembly code for that function, showing instructions to adjust the stack pointer — [7:18]

```swift
_$s4main9updateAll6models4fromySayAA9DataModel_pG_AA0F6SourceCtF:
    sub   sp, sp, #208
    stp   x29, x30, [sp, #192]
    …
    ldp   x29, x30, [sp, #192]
    add   sp, sp, #208
    ret
```

### A C struct showing one possible layout of the function's call frame — [7:59]

```cpp
// sizeof(CallFrame) == 208
struct CallFrame {
    Array<AnyDataModel> models;
    DataSource source;
    AnyDataModel model;
    ArrayIterator iterator;
    ...
    void *savedX29;
    void *savedX30;
};
```

### A line of code containing a single variable initialization — [10:50]

```swift
var array = [ 1.0, 2.0 ]
```

### Using the MemoryLayout type to examine a type's inline representation — [11:44]

```swift
MemoryLayout.size(ofValue: array) == 8
```

### The variable initialization from before, now placed within a function — [12:48]

```swift
func makeArray() {
    var array = [ 1.0, 2.0 ]
}
```

### Initializing a second variable with the contents of the first — [15:42]

```swift
func makeArray() {
    var array = [ 1.0, 2.0 ]
    var array2 = array
}
```

### Taking the value of an existing variable with the consume operator — [16:27]

```swift
func makeArray() {
    var array = [ 1.0, 2.0 ]
    var array2 = consume array
}
```

### A call to a mutating method — [16:58]

```swift
func makeArray() {
    var array = [ 1.0, 2.0 ]
    array.append(3.0)
}
```

### Passing an argument that should be borrowable — [17:40]

```swift
func makeArray() {
    var array = [ 1.0, 2.0 ]
    print(array)
}
```

### Passing an argument that will likely have to be defensively copied — [18:10]

```swift
func makeArray(object: MyClass) {
    object.array = [ 1.0, 2.0 ]
    print(object.array)
}
```

### Part of a large struct type — [19:27]

```swift
struct Person {
    var name: String
    var birthday: Date
    var address: String
    var relationships: [Relationship]
    ...
}
```

### A Connection struct that contains a property of the dynamically-sized URL type — [21:22]

```swift
struct Connection {
    var username: String
    var address: URL
    var options: [String: String]
}
```

### A GenericConnection struct that contains a property of an unknown type parameter type — [21:40]

```swift
struct GenericConnection<T> {
    var username: String
    var address: T
    var options: [String: String]
}
```

### The same GenericConnection struct, except with a class constraint on the type parameter — [21:51]

```swift
struct GenericConnection<T> where T: AnyObject {
    var username: String
    var address: T
    var options: [String: String]
}
```

### The same Connection struct as before — [22:27]

```swift
struct Connection {
    var username: String
    var address: URL
    var options: [String: String]
}
```

### A global variable of URL type — [23:23]

```swift
var address = URL(string: "...")
```

### A local variable of URL type — [23:42]

```swift
func workWithAddress() {
    var address = URL(string: "...")
}
```

### An async function — [25:02]

```swift
func awaitAll(tasks: [Task<Int, Never>]) async -> [Int] {
    var results = [Int]()
    for task in tasks {
        results.append(await task.value)
    }
    return results
}
```

### A function that takes an argument of function type — [28:21]

```swift
func sumTwice(f: () -> Int) -> Int {
  return f() + f()
}
```

### A C function roughly corresponding to the Swift function — [28:30]

```cpp
Int sumTwice(Int (*fFunction)(void *),
             void *fContext) {
  return fFunction(fContext)
       + fFunction(fContext);
}
```

### A function call that passes a closure expression as a function argument — [28:47]

```swift
func sumTwice(f: () -> Int) -> Int {
  return f() + f()
}

func puzzle(n: Int) -> Int {
  return sumTwice { n + 1 }
}
```

### C code roughly corresponding to the emission of the non-escaping closure — [29:15]

```cpp
struct puzzle_context {
  Int n;
};

Int puzzle(Int n) {
  struct puzzle_context context = { n };
  return sumTwice(&puzzle_closure, &context);
}

Int puzzle_closure(void *_context) {
  struct puzzle_context *context =
    (struct puzzle_context *) _context;
  return _context->n + 1;
}
```

### The function and its caller again, now taking an escaping function as its parameter — [29:34]

```swift
func sumTwice(f: @escaping () -> Int) -> Int {
  return f() + f()
}

func puzzle(n: Int) -> Int {
  return sumTwice { n + 1 }
}
```

### A closure that captures a local variable by reference — [29:53]

```swift
func sumTwice(f: () -> Int) -> Int {
  return f() + f()
}

func puzzle(n: Int) -> Int {
  var addend = 0
  return sumTwice {
    addend += 1
    return n + addend
  }
}
```

### Swift types roughly approximating how escaping variables and closures are handled — [30:30]

```swift
class Box<T> {
  let value: T
}

class puzzle_context {
  let n: Int
  let addend: Box<Int>
}
```

### A generic function that calls a protocol requirement — [30:40]

```swift
protocol DataModel {
    func update(from source: DataSource)
}

func updateAll<Model: DataModel>(models: [Model], from source: DataSource) {
    for model in models {
        model.update(from: source)
    }
}
```

### A C struct roughly approximating a protocol witness table — [31:03]

```cpp
struct DataModelWitnessTable {
    ConformanceDescriptor *identity;
    void (*update)(DataSource source,
                   TypeMetadata *Self);
};
```

### A C function signature roughly approximating how generic functions receive generic parameters — [31:20]

```cpp
void updateAll(Array<Model> models,
               DataSource source,
               TypeMetadata *Model,
               DataModelWitnessTable *Model_is_DataModel);
```

### A function that receives an array of values of protocol type — [31:36]

```swift
protocol DataModel {
    func update(from source: DataSource)
}

func updateAll(models: [any DataModel], from source: DataSource)
```

### A C struct roughly approximating the layout of the Swift type `any DataModel` — [31:49]

```swift
struct AnyDataModel {
    OpaqueValueStorage value;
    TypeMetadata *valueType;
    DataModelWitnessTable *value_is_DataModel;
};

struct OpaqueValueStorage {
    void *storage[3];
};
```

### A contrast of the two Swift function signatures from before — [31:50]

```swift
protocol DataModel {
    func update(from source: DataSource)
}

func updateAll<Model: DataModel>(models: [Model],
                            from source: DataSource) {
    for model in models {
        model.update(from: source)
    }
}

func updateAll(models: [any DataModel], from source: DataSource) {
    for model in models {
        model.update(from: source)
    }
}
```

### Specialization of a generic function for known type parameters — [32:57]

```swift
func updateAll<Model: DataModel>(models: [Model],
                            from source: DataSource) {
    for model in models {
        model.update(from: source)
    }
}

var myModels: [MyDataModel]
updateAll(models: myModels, from: source)

// Implicitly generated by the optimizer
func updateAll_specialized(models: [MyDataModel],
                           from source: DataSource) {
    for model in models {
        model.update(from: source)
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10217/5/8228D59A-1164-48DA-86CD-79F2191061DC/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2024/10217/5/8228D59A-1164-48DA-86CD-79F2191061DC/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2024/10217) — developer.apple.com. Indexed for agent consumption._
