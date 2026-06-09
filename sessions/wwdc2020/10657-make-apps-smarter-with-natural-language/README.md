---
id: "wwdc2020-10657"
event: "wwdc2020"
year: 2020
title: "Make apps smarter with Natural Language"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10657"
topics: ["AI & Machine Learning"]
platforms: ["iOS", "iPadOS", "macOS"]
hasTranscript: true
---

# Make apps smarter with Natural Language

**Event:** WWDC20 · **Topic:** AI & Machine Learning · **Platforms:** iOS, iPadOS, macOS · **Published:** 2020-06-25 · **Session:** [wwdc2020-10657](https://developer.apple.com/videos/play/wwdc2020/10657)

Explore how you can leverage the Natural Language framework to better analyze and understand text. Learn how to draw meaning from text using the framework's built-in word and sentence embeddings, and how to create your own custom embeddings for specific needs. We’ll show you how to use samples to train a custom text classifier or word tagger to extract important pieces of information out of text— all powered by the transfer learning algorithms in Natural Language. Find out how you can create apps that can answer user questions, recognize similarities in text, and find relevant documents, images, and more. To get the most out of this session, you should have a basic understanding of the Natural Language framework. For an overview, watch “Introducing Natural Language Framework” and “Advances in Natural Language Framework.” You can also brush up on model training using Create ML through “Introducing the Create ML App.”

**Keywords:** `core ml`, `create ml`, `custom models`, `embeddings`, `machine learning`, `natural language`, `nlp`, `sentence embedding`, `text analysis`, `text processing`, `word embedding`, `word tagging`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(6,695 words)

## Code Snippets

### Confidence Scores: tagHypotheses — [3:53]

```swift
import NaturalLanguage 

let tagger = NLTagger(tagSchemes: [.nameType])
let str = "Tim Cook is very popular in Spain."
let strRange = Range(uncheckedBounds: (str.startIndex, str.endIndex))
tagger.string = str
tagger.setLanguage(.english, range: strRange)

tagger.enumerateTags(in: str.startIndex..<str.endIndex, unit: .word, scheme: .nameType, options: .omitWhitespace) { (tag, tokenRange) -> Bool in
    let (hypotheses, _) = tagger.tagHypotheses(at: tokenRange.lowerBound, unit: .word, 
                                               scheme: .nameType, maximumCount: 1)
    print(hypotheses)
    return true
}
```

### Word Embedding — [12:19]

```swift
import NaturalLanguage

if let embedding = NLEmbedding.wordEmbedding(for: .english) {
    let word = "bicycle"

    if let vector = embedding.vector(for: word) {
        print(vector)
    }

    let dist = embedding.distance(between:word, and: "motorcycle")
    print(dist)

    embedding.enumerateNeighbors(for: word, maximumCount: 5) { neighbor, distance in
        print("\(neighbor): \(distance.description)")
        return true
    }
}
```

### Sentence Embedding — [16:32]

```swift
import NaturalLanguage

if let embedding = NLEmbedding.sentenceEmbedding(for: .english) {
    let sentence = "This is a sentence."

    if let vector = sentenceEmbedding.vector(for: sentence) {
        print(vector)
    }

    let dist = sentenceEmbedding.distance(between: sentence, and: "That is a sentence.")
    print(dist)
}
```

### Finding nearest neighbor with sentence embedding — [18:36]

```swift
func answerKey(for string: String) -> String? {
        guard let embedding = NLEmbedding.sentenceEmbedding(for: .english) else { return nil }
        guard let queryVector = embedding.vector(for: string) else { return nil }

        var answerKey: String? = nil
        var answerDistance = 2.0

        for (key, vectors) in self.faqEmbeddings {
            for (vector) in vectors {
                let distance = self.cosineDistance(vector, queryVector)
                if (distance < answerDistance) {
                    answerDistance = distance
                    answerKey = key
                }
            }
        }

        return answerKey
    }
```

### Sentence embedding compressed as custom embedding — [22:19]

```swift
import NaturalLanguage
import CreateML


let embedding = try MLWordEmbedding(dictionary: sentenceVectors)

try embedding.write(to: URL(fileURLWithPath: "/tmp/Verse.mlmodel"))
```

### Finding nearest neighbor with sentence embedding and custom embedding — [22:47]

```swift
func answerKeyCustom(for string: String) -> String? {
        guard let embedding = NLEmbedding.sentenceEmbedding(for: .english) else { return nil }
        guard let queryVector = embedding.vector(for: string) else { return nil }

        guard let (nearestLineKey, _) = self.customEmbedding.neighbors(for: queryVector, maximumCount: 1).first else { return nil }

        return self.poemKeyFromLineKey(nearestLineKey)
    }
```

### WordTagger — [33:29]

```swift
import CreateML

let modelParameters = MLWordTagger.ModelParameters(algorithm: .crf(revision: 1))
```

### Using custom word tagger — [36:46]

```swift
func findTags(for string: String) {
        let model = try! NLModel(contentsOf: Bundle.main.url(forResource: "Nosh", withExtension: "mlmodelc")!)
        let tagger = NLTagger(tagSchemes: [NoshTags])

        tagger.setModels([model], forTagScheme: NoshTags)
        tagger.string = string

        tagger.enumerateTags(in: string.startIndex..<string.endIndex, unit: .word, scheme: NoshTags, options: .omitWhitespace) { (tag, tokenRange) -> Bool in

            let name = String(string[tokenRange])

            switch tag {
                case NoshTagRestaurant:
                    self.noteRestaurant(name)
                case NoshTagFood:
                    self.noteFood(name)
                case NoshTagFromCity:
                    self.noteFromCity(name)
                case NoshTagToCity:
                    self.noteToCity(name)
                default:
                    break
            }
            return true
        }
    }
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10657/6/2C0D8310-7D45-4FD5-B49E-91B0F6D2B511/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10657) — developer.apple.com. Indexed for agent consumption._
