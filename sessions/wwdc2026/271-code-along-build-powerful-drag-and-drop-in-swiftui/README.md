---
id: "wwdc2026-271"
event: "wwdc2026"
year: 2026
title: "Code-along: Build powerful drag and drop in SwiftUI"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2026/271"
topics: ["App Services", "SwiftUI & UI Frameworks"]
platforms: ["iOS", "iPadOS", "macOS", "visionOS"]
hasTranscript: true
---

# Code-along: Build powerful drag and drop in SwiftUI

**Event:** WWDC26 · **Topic:** SwiftUI & UI Frameworks · **Platforms:** iOS, iPadOS, macOS, visionOS · **Published:** 2026-06-08 · **Session:** [wwdc2026-271](https://developer.apple.com/videos/play/wwdc2026/271)

Follow along as we build a game of Solitaire to explore the latest drag-and-drop capabilities in SwiftUI. We’ll show you how to use the new reordering API to let people arrange content, implement drag containers to move multiple items at once, and customize the drag-and-drop lifecycle to fit your app’s rules. To get the most out of this session, watch “Meet Transferable” from WWDC22.

**Keywords:** `screenshots`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(2,288 words)

## Documentation & Resources

- [Making a card game with drag, drop, and reordering in SwiftUI](https://developer.apple.com/documentation/SwiftUI/Making-a-card-game-with-drag-drop-and-reordering-in-swiftui) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SwiftUI/Making-a-card-game-with-drag-drop-and-reordering-in-swiftui
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SwiftUI/Making-a-card-game-with-drag-drop-and-reordering-in-swiftui.json
- [Drag and drop](https://developer.apple.com/documentation/UIKit/drag-and-drop) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/UIKit/drag-and-drop
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/UIKit/drag-and-drop.json

## Code Snippets

### Add reorderable to the preview — [3:40]

```swift
#Preview {
    @Previewable @State var cards = [
        CardValue(rank: .ace, suit: .clubs),
        CardValue(rank: .ace, suit: .diamonds),
        CardValue(rank: .ace, suit: .hearts),
        CardValue(rank: .ace, suit: .spades)
    ]

    HStack {
        ForEach(cards) { card in
            CardFaceView(card: card)
        }
        .reorderable()
    }
    .frame(maxWidth: .infinity, maxHeight: .infinity)
    .reorderContainer(for: CardValue.self) { difference in
        cards.apply(difference: difference)
    }
    .padding()
    .background(.green.gradient)
}
```

### Add reorder container to the GameView — [4:40]

```swift
struct GameView: View {
    var game: Game

    var body: some View {
        GeometryReader { proxy in
            let spacing: CGFloat = 10
            let cardWidth = (proxy.size.width - 6 * spacing) / 7
            VStack {
                HStack(alignment: .top, spacing: spacing) {
                    Group {
                        RemainderView(game: game)
                        CardBackView()
                            .hidden()
                        ForEach(CardValue.Suit.allCases) { suit in
                            DestinationView(game: game, suit: suit)
                        }
                    }
                    .frame(width: cardWidth)
                }
                .padding(.bottom, 20)
                HStack(alignment: .top, spacing: spacing) {
                    ForEach(0..<7) { index in
                        PileView(game: game, index: index)
                            .frame(width: cardWidth)
                    }
                }
                .frame(maxHeight: .infinity, alignment: .top)
              	// Add the reorder container modifier.
                .reorderContainer(for: CardValue.self, in: Card.Group.self) { difference in
                    game.moveCards(difference: difference)
                }
            }
        }
        .padding()
    }
}
```

### Add reorderable to PileView — [5:58]

```swift
struct PileView: View {
    var game: Game
    var index: Int
    @Query var cards: [Card]

    var body: some View {
        ZStack(alignment: .topLeading) {
            CardPlaceholderView()
            PileLayout {
                let index = firstFaceUpIndex
              	// Iterates over the face down cards.
                ForEach(cards[..<index]) { card in
                    CardView(card: card)
                }
                // Iterates over the face up cards.
                ForEach(cards[index...], id: \.value) { card in
                    CardView(card: card)
                }
                .reorderable(collectionID: Card.Group.pile(index))
            }
        }
    }

    var firstFaceUpIndex: Int {
        cards.firstIndex { !$0.isFaceDown } ?? cards.endIndex
    }
}
```

### Add dragContainer to customize the reorderContainer modifier. — [7:50]

```swift
struct GameView: View {
    var game: Game

    var body: some View {
        GeometryReader { proxy in
            let spacing: CGFloat = 10
            let cardWidth = (proxy.size.width - 6 * spacing) / 7
            VStack {
                HStack(alignment: .top, spacing: spacing) {
                    Group {
                        RemainderView(game: game)
                        CardBackView()
                            .hidden()
                        ForEach(CardValue.Suit.allCases) { suit in
                            DestinationView(game: game, suit: suit)
                        }
                    }
                    .frame(width: cardWidth)
                }
                .padding(.bottom, 20)
                HStack(alignment: .top, spacing: spacing) {
                    ForEach(0..<7) { index in
                        PileView(game: game, index: index)
                            .frame(width: cardWidth)
                    }
                }
                .frame(maxHeight: .infinity, alignment: .top)
                .reorderContainer(for: CardValue.self, in: Card.Group.self) { difference in
                    game.moveCards(difference: difference)
                }
                // Add dragContainer to customize reorderContainer.
                .dragContainer(for: CardValue.self) { cardID in
                    game.cardStack(startingAt: cardID)
                }
            }
        }
        .padding()
    }
}
```

### Add dragPreviewsFormation to customize how the dragged cards appear — [8:45]

```swift
struct GameView: View {
    var game: Game

    var body: some View {
        GeometryReader { proxy in
            let spacing: CGFloat = 10
            let cardWidth = (proxy.size.width - 6 * spacing) / 7
            VStack {
                HStack(alignment: .top, spacing: spacing) {
                    Group {
                        RemainderView(game: game)
                        CardBackView()
                            .hidden()
                        ForEach(CardValue.Suit.allCases) { suit in
                            DestinationView(game: game, suit: suit)
                        }
                    }
                    .frame(width: cardWidth)
                }
                .padding(.bottom, 20)
                HStack(alignment: .top, spacing: spacing) {
                    ForEach(0..<7) { index in
                        PileView(game: game, index: index)
                            .frame(width: cardWidth)
                    }
                }
                .frame(maxHeight: .infinity, alignment: .top)
                .reorderContainer(for: CardValue.self, in: Card.Group.self) { difference in
                    game.moveCards(difference: difference)
                }
                .dragContainer(for: CardValue.self) { cardID in
                    game.cardStack(startingAt: cardID)
                }
              	// Have dragged cards appear as a stack.
                .dragPreviewsFormation(.stack)
            }
        }
        .padding()
    }
}
```

### Add dropPreviewsFormation to customize how dragged cards appear over a destination — [9:14]

```swift
struct GameView: View {
    var game: Game

    var body: some View {
        GeometryReader { proxy in
            let spacing: CGFloat = 10
            let cardWidth = (proxy.size.width - 6 * spacing) / 7
            VStack {
                HStack(alignment: .top, spacing: spacing) {
                    Group {
                        RemainderView(game: game)
                        CardBackView()
                            .hidden()
                        ForEach(CardValue.Suit.allCases) { suit in
                            DestinationView(game: game, suit: suit)
                        }
                    }
                    .frame(width: cardWidth)
                }
                .padding(.bottom, 20)
                HStack(alignment: .top, spacing: spacing) {
                    ForEach(0..<7) { index in
                        PileView(game: game, index: index)
                            .frame(width: cardWidth)
                    }
                }
                .frame(maxHeight: .infinity, alignment: .top)
                .reorderContainer(for: CardValue.self, in: Card.Group.self) { difference in
                    game.moveCards(difference: difference)
                }
                .dragContainer(for: CardValue.self) { cardID in
                    game.cardStack(startingAt: cardID)
                }
                .dragPreviewsFormation(.stack)
            }
            // Have a consistent appearance over drop destinations.
            .dropPreviewsFormation(.stack)
        }
        .padding()
    }
}
```

### Add a drag configuration to allow move. — [11:40]

```swift
struct RemainderView: View {
    @Query var cards: [Card]
    var game: Game

    var body: some View {
        Button {
            incrementCardIndex()
        } label: {
            ZStack {
                CardPlaceholderView()
                CardBackView()
                    .opacity(cards.isEmpty ? 0 : 1)
            }
        }
        .buttonStyle(.plain)
        .disabled(cards.isEmpty)
        ZStack {
            CardPlaceholderView()
            if let currentCard {
                CardFaceView(card: currentCard.value)
                    .draggable(containerItemID: currentCard.value)
                    .opacity(currentCard.value == hiddenCard ? 0 : 1)
            }
        }
        .dragContainer(for: CardValue.self) { cardID in
            [cardID]
        }
        // Add the drag configuration to allow me.
        .dragConfiguration(DragConfiguration(allowMove: true))
    }
}
```

### Add a drop destination modifier and configure it — [12:05]

```swift
struct GameView: View {
    var game: Game

    var body: some View {
        GeometryReader { proxy in
            let spacing: CGFloat = 10
            let cardWidth = (proxy.size.width - 6 * spacing) / 7
            VStack {
                HStack(alignment: .top, spacing: spacing) {
                    Group {
                        RemainderView(game: game)
                        CardBackView()
                            .hidden()
                        ForEach(CardValue.Suit.allCases) { suit in
                            DestinationView(game: game, suit: suit)
                        }
                    }
                    .frame(width: cardWidth)
                }
                .padding(.bottom, 20)
                HStack(alignment: .top, spacing: spacing) {
                    ForEach(0..<7) { index in
                        PileView(game: game, index: index)
                            .frame(width: cardWidth)
                    }
                }
                .frame(maxHeight: .infinity, alignment: .top)
                .reorderContainer(for: CardValue.self, in: Card.Group.self) { difference in
                    game.moveCards(difference: difference)
                }
                .dragContainer(for: CardValue.self) { cardID in
                    game.cardStack(startingAt: cardID)
                }
                .dragPreviewsFormation(.stack)
                .dragConfiguration(DragConfiguration(allowMove: true))
                // Add a drop destination to accept inserts
                .dropDestination(for: CardValue.self) { newCards, session in
                    if let destination = session.reorderDestination(
                        for: CardValue.self, in: Card.Group.self) {
                        game.insertCards(newCards, to: destination)
                    }
                }
                // Configure where cards will go when reordering,
                // and accept them by move.
                .dropConfiguration { session in
                    // Calculate which pile is being dragged over.
                    let alignedX = session.location.x - 0.5 * spacing
                    let pile = Int(alignedX / (cardWidth + spacing))
                    let destination = ReorderDifference<CardValue, Card.Group>
                        .Destination(position: .end, collectionID: .pile(pile))
                    // Check if the move is allowed.
                    let allowed = session.suggestedOperations.contains(.move)
                    && game.validateMove(session: session, destination: destination)
                    let operation: DropOperation = allowed ? .move : .forbidden
                    return DropConfiguration(operation: operation, destination: destination)
                }
            }
            .dropPreviewsFormation(.stack)
        }
        .padding()
    }
}
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2026/271/5/07f08d32-e28e-476f-8ebe-a3600b2e917c/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2026/271/5/07f08d32-e28e-476f-8ebe-a3600b2e917c/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2026/271) — developer.apple.com. Indexed for agent consumption._
