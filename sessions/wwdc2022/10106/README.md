---
id: "wwdc2022-10106"
event: "wwdc2022"
year: 2022
title: "Profile and optimize your game's memory"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10106"
topics: ["Graphics & Games"]
platforms: ["iOS", "iPadOS", "macOS", "tvOS"]
hasTranscript: true
---

# Profile and optimize your game's memory

**Event:** WWDC22 · **Topic:** Graphics & Games · **Platforms:** iOS, iPadOS, macOS, tvOS · **Published:** 2022-06-10 · **Session:** [wwdc2022-10106](https://developer.apple.com/videos/play/wwdc2022/10106)

Learn how Apple platforms calculate and allocate memory for your game. We'll show you how to use Instruments and the Game Memory template to profile your game, take a memory graph to monitor current memory use, and analyze it using Xcode Memory Debugger and command line tools. We'll also explore Metal resources in Metal Debugger and provide tips and tricks to further help you optimize memory usage.

**Keywords:** `game dev`, `game developer`, `games`, `instruments`, `memory`, `memory graph`, `metal 3`, `profile guided optimization`, `xcode`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(5,479 words)

## Code Snippets

### Available memory for the process — [6:53]

```objectivec
#import <os/proc.h>

API_UNAVAILABLE(macos) API_AVAILABLE(ios(13.0), tvos(13.0), watchos(6.0))
size_t os_proc_available_memory(void);
```

### Current and peak footprint — [7:07]

```objectivec
#if __has_include(<libproc.h>)
#include <libproc.h> // On macOS.
#else
#include <sys/resource.h> // On iOS, iPadOS and tvOS.
int proc_pid_rusage(int pid, int flavor, rusage_info_t *buffer)  
    __OSX_AVAILABLE_STARTING(__MAC_10_9, __IPHONE_7_0);
#endif

rusage_info_current rusage_payload;

int ret = proc_pid_rusage(getpid(),
                          RUSAGE_INFO_CURRENT, // I.e., new RUSAGE_INFO_V6 this year.
                          (rusage_info_t *)&rusage_payload);
NSCAssert(ret == 0, @"Could not get rusage: %i.", errno); // Look up in `man errno`.

uint64_t footprint       = rusage_payload.ri_phys_footprint;
uint64_t footprint_peak  = rusage_payload.ri_lifetime_max_phys_footprint;
```

### Record an Instruments trace — [10:04]

```bash
xctrace record --template "Game Memory" \
--attach ModernRenderer \
--output ModernRenderer.trace \
--time-limit 30s
```

### Record an Instruments trace, on a selected device — [10:14]

```bash
xctrace record --device-name "Seth's iPhone" \
						   --template "Game Memory" \
               --attach ModernRenderer \
               --output ModernRenderer.trace \
               --time-limit 30s
```

### MallocStackLogging — [16:52]

```bash
# See `man malloc`.
MallocStackLogging=lite # Live allocations only.
MallocStackLogging=1    # All allocation and free history.
```

### Capture a memory graph — [18:07]

```bash
leaks $PID     --outputGraph foo.memgraph
# or
leaks GameName --outputGraph foo.memgraph
```

### Tag mapped anonymous memory — [20:12]

```objectivec
size_t length;

int tag = VM_MAKE_TAG(VM_MEMORY_APPLICATION_SPECIFIC_1); // Check out `man mmap`.

void * reservation = mmap(NULL,
                          length,
                          PROT_READ | PROT_WRITE,
                          MAP_ANONYMOUS | MAP_PRIVATE,
                          tag, // Instead of using default `-1`.
                          0);

if (reservation == MAP_FAILED) {
    @throw [[NSError alloc] initWithDomain:NSPOSIXErrorDomain
                                      code:errno
                                  userInfo:nil];    
}

return reservation;
```

### Tag anonymous memory — [20:30]

```objectivec
size_t page_count;

mach_vm_size_t allocation_size = page_count * PAGE_SIZE;
mach_vm_address_t vm_address;
kern_return_t kr;

kr = mach_vm_allocate(mach_task_self(),
                      &vm_address,
                      allocation_size,
                      VM_FLAGS_ANYWHERE | VM_MAKE_TAG(VM_MEMORY_APPLICATION_SPECIFIC_1));

if (kr != KERN_SUCCESS) { // Refer to mach/kern_return.h.
    @throw [[NSError alloc] initWithDomain:NSMachErrorDomain
                                      code:kr
                                  userInfo:nil];
}

return vm_address;
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10106/5/56A1A2BE-7EF5-4AA0-AE93-1F93BD885019/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10106/5/56A1A2BE-7EF5-4AA0-AE93-1F93BD885019/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10106) — developer.apple.com. Indexed for agent consumption._