# Discover container machines

**Topic:** Developer Tools · **Platforms:** macOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-389](https://developer.apple.com/videos/play/wwdc2026/389)

Meet container machines, a new tool included in Container that offers a lightweight persistent Linux environment on Mac. Explore how container machines work and how the design of Containerization allows for a performant and seamless experience when developing for Linux on macOS.

## Transcript

[Read the full transcript](transcript.md)

## Documentation & Resources

- [Container](https://github.com/apple/container) _guide_
- [Containerization](https://github.com/apple/containerization) _guide_

## Code Snippets

### Viewing container machine commands — [4:41]

```bash
container machine
```

### Creating a new container machine — [5:00]

```bash
container machine create --name demo --set-default alpine
```

### Echo hi — [5:39]

```bash
container machine run echo hi
```

### Running uname — [5:57]

```bash
container machine run uname
```

### Start interactive shell — [6:28]

```bash
container machine run
```

### List container machines — [8:01]

```bash
container machine list
```

### Start interactive shell — [8:22]

```bash
container machine run
```

### Run the application — [9:13]

```bash
swift run
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/389/4/8dd035e7-0481-4028-b4bd-e91ba3634198/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/389/4/8dd035e7-0481-4028-b4bd-e91ba3634198/cmaf-download.m3u8

---

_Source: Apple Inc. — developer.apple.com. Indexed for agent consumption._