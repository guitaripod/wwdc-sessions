---
id: "wwdc2020-10197"
event: "wwdc2020"
year: 2020
title: "Broaden your reach with Siri Event Suggestions"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2020/10197"
topics: ["Developer Tools", "Maps & Location", "Safari & Web", "App Services"]
platforms: ["iOS", "iPadOS", "macOS", "watchOS"]
hasTranscript: true
---

# Broaden your reach with Siri Event Suggestions

**Event:** WWDC20 · **Topic:** App Services · **Platforms:** iOS, iPadOS, macOS, watchOS · **Published:** 2020-06-24 · **Session:** [wwdc2020-10197](https://developer.apple.com/videos/play/wwdc2020/10197)

Whether you’re hosting event information in your app, on the web, or in an email, Siri Event Suggestions can help people keep track of their commitments — without compromising their privacy. We’ll show you how to set up your reservations so that they automatically show up in the Calendar app and how to work with the Siri Event Suggestions APIs for iOS and Markup for web and email.

**Keywords:** `calendar`, `donations`, `email`, `events`, `intents`, `mail`, `safari`, `shortcuts`, `siri event suggestions`, `travel`, `web`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(4,652 words)

## Documentation & Resources

- [Register with Apple for Siri Event Suggestions Markup](https://developer.apple.com/contact/request/siri-events/) _guide_
  - Markdown (sosumi.ai): https://sosumi.ai/contact/request/siri-events/
- [Integrating Your App with Siri Event Suggestions](https://developer.apple.com/documentation/SiriKit/integrating-your-app-with-siri-event-suggestions) _samplecode_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/SiriKit/integrating-your-app-with-siri-event-suggestions
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/SiriKit/integrating-your-app-with-siri-event-suggestions.json

## Code Snippets

### JSON-LD — [6:31]

```json
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "FoodEstablishmentReservation",
  "reservationStatus": "http://schema.org/ReservationConfirmed",
  "reservationId": "IWDSCA",
  "partySize": "2",
  "reservationFor": {
    "@type": "FoodEstablishment",
    "name": "EPIC Steak",
    "startDate": "2020-06-26T19:30:00-07:00",
    "telephone": "(415)369-9955"
    "address": {
      "@type": "http://schema.org/PostalAddress",
      "streetAddress": "369 The Embarcadero",
      "addressLocality": "San Francisco"
      "addressRegion": "CA",
      "postalCode": "95105",
      "addressCountry": "USA"
    }
  }
}
</script>
```

### Microdata — [6:45]

```json
<div itemscope itemtype="FoodEstablishmentReservation"> 
  <link itemprop="reservationStatus" href="http://schema.org/ReservationConfirmed"/>
  <meta itemprop="reservationId" content="IWDSCA"/>
  <meta itemprop="partySize" content="2"/>
  <div itemprop="reservationFor" itemscope itemtype="FoodEstablishment">
    <meta itemprop="name" content="EPIC Steak"/>
    <meta itemprop="startDate" content="2020-06-26T19:30:00-07:00"/>
    <meta itemprop="telephone" content="(415)369-9955"/>
    <div itemprop="address" itemscope itemtype="PostalAddress">
      <meta itemprop="streetAddress" content="369 The Embarcadero"/>
      <meta itemprop="addressLocality" content="San Francisco"/>
      <meta itemprop="addressRegion" content="CA"/>
      <meta itemprop="postalCode" content="95105"/>
      <meta itemprop="addressCountry" content="USA"/>
    </div>
  </div>
</div>
```

### Modified Reservation JSON-LD — [6:58]

```json
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "FoodEstablishmentReservation",
  "reservationStatus": "http://schema.org/ReservationConfirmed",
  "reservationId": "IWDSCA",
  "partySize": "2",
  "reservationFor": {
    "@type": "FoodEstablishment",
    "name": "EPIC Steak",
    "startDate": "2020-06-26T18:30:00-07:00",
    "telephone": "(415)369-9955"
    "address": {
      "@type": "http://schema.org/PostalAddress",
      "streetAddress": "369 The Embarcadero",
      "addressLocality": "San Francisco"
      "addressRegion": "CA",
      "postalCode": "95105",
      "addressCountry": "USA"
    }
  }
}
</script>
```

### Cancelled Reservation JSON-LD — [7:21]

```json
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "FoodEstablishmentReservation",
  "reservationStatus": "http://schema.org/ReservationCancelled",
  "reservationId": "IWDSCA",
  "partySize": "2",
  "reservationFor": {
    "@type": "FoodEstablishment",
    "name": "EPIC Steak",
    "startDate": "2020-06-26T19:30:00-07:00",
    "telephone": "(415)369-9955"
    "address": {
      "@type": "http://schema.org/PostalAddress",
      "streetAddress": "369 The Embarcadero",
      "addressLocality": "San Francisco"
      "addressRegion": "CA",
      "postalCode": "95105",
      "addressCountry": "USA"
    }
  }
}
</script>
```

### SuggestionsAllowAnyDomainForMarkup default — [8:13]

```bash
defaults write com.apple.suggestions SuggestionsAllowAnyDomainForMarkup -bool true
```

### SuggestionsAllowUnverifiedSourceForMarkup default — [8:25]

```bash
defaults write com.apple.suggestions SuggestionsAllowUnverifiedSourceForMarkup -bool true
```

### SuggestionsAllowAnyDomainForMarkup default — [8:49]

```bash
defaults write com.apple.suggestions SuggestionsAllowAnyDomainForMarkup -bool true
```

### SuggestionsAllowUnverifiedSourceForMarkup default — [9:03]

```swift
defaults write com.apple.suggestions SuggestionsAllowUnverifiedSourceForMarkup -bool true
```

### Reservation Confirmation JSON-LD — [10:32]

```json
<script type='application/ld+json'>
{
  "@context": "http://schema.org",
  "@type": "http://schema.org/FoodEstablishmentReservation",
  "reservationId": "IWDSCA",
  "reservationStatus": "http://schema.org/ReservationConfirmed",
  "url": "http://localhost:3000/reservations/6",
  "underName": {
    "@type": "http://schema.org/Person",
    "name": "John Appleseed"
  },
  "broker": {
    "@type": "http://schema.org/Organization",
    "name": "Apple Reservations"
  },
  "startTime": "2020-06-26T19:30:00-07:00",
  "partySize": "2",
  "reservationFor": {
    "@type": "http://schema.org/FoodEstablishment",
    "name": "EPIC Steak",
    "telephone": "(415)369-9955",
    "address": {
      "@type": "http://schema.org/PostalAddress",
      "streetAddress": "369 The Embarcadero",
      "addressLocality": "San Francisco"
      "addressRegion": "CA",
      "postalCode": "95105",
      "addressCountry": "USA"
    }
  }
}
</script>
```

### Reservation Cancelled JSON-LD — [11:04]

```json
<script type='application/ld+json'>
{
  "@context": "http://schema.org",
  "@type": "http://schema.org/FoodEstablishmentReservation",
  "reservationId": "IWDSCA",
  "reservationStatus": "http://schema.org/ReservationCancelled",
  "url": "http://localhost:3000/reservations/6",
  "underName": {
    "@type": "http://schema.org/Person",
    "name": "John Appleseed"
  },
  "broker": {
    "@type": "http://schema.org/Organization",
    "name": "Apple Reservations"
  },
  "startTime": "2020-06-26T19:30:00-07:00",
  "partySize": "2",
  "reservationFor": {
    "@type": "http://schema.org/FoodEstablishment",
    "name": "EPIC Steak",
    "telephone": "(415)369-9955",
    "address": {
      "@type": "http://schema.org/PostalAddress",
      "streetAddress": "369 The Embarcadero",
      "addressLocality": "San Francisco"
      "addressRegion": "CA",
      "postalCode": "95105",
      "addressCountry": "USA"
    }
  }
}
</script>
```

### Registration URL — [13:10]

```bash
developer.apple.com/contact/request/siri-events
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2020/10197/4/FD55A473-26AA-4BE5-896E-D18F043D0EB4/master.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2020/10197) — developer.apple.com. Indexed for agent consumption._
