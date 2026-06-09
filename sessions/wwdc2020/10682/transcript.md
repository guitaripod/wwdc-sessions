---
id: "wwdc2020-10682"
event: "wwdc2020"
title: "Swan's Quest, Chapter 2: A time for tones"
url: "https://developer.apple.com/videos/play/wwdc2020/10682"
language: "eng"
words: 799
---

# Swan's Quest, Chapter 2: A time for tones — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2020/10682) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:03]** Hello, and welcome to WWDC. Hello, and welcome back to Swan's Quest. I'm Rob, your host as we go inside the second chapter of our journey. We hope you had a fun time with the first challenge, and learned a little bit about accessible interfaces. In the second chapter, you returned to the Lizard, who helps you uncover the mystery of the Swan's scroll. I don't want to spoil it for you, but I can tell you that to pass this challenge, you need to play a series of musical notes for the Swan. In order to play notes, we're gonna show you two pieces of API: ToneOutput and Timer. We'll cover both of them in enough detail for you to impress our magnificent regent. Finally, we'll end with a side quest

**[0:49]** for those of you in search of more adventure. First, let's talk about how to play tones. For that, we're gonna use the ToneOutput type. We introduced ToneOutput in Sonic Workshop, and included it in Sonic Create, so you could use it in your own projects. Let's take a closer look at ToneOutput. Our ToneOutput type has a straightforward API for playing generated signals from a tone value. It produces 44,100 samples a second. That's so your ears hear continuous sound instead of discrete pulses. The primary instance method, play(tone:) is what you call to create a signal. The definition for tone is equally straightforward.

**[1:34]** A pitch, which is a Double representation of a frequency, and a volume, also described as a Double. And this is what it looks like in use. In this example, we create an instance of ToneOutput, then pass it a 440 Hz frequency, or middle A. Run this code in your Playground and you should hear a tone reminiscent of the Emergency Broadcast System. If you don't stop running your Playground code, that tone's gonna play forever. Let's check in with Stephen to see how to play more than one note. Thanks, Rob. As he mentioned, the ToneOutput sample will play continuously unless it is stopped. To stop the ToneOutput instance, we need to call stopTones as highlighted here.

**[2:21]** We can accomplish this in our example by calling Dispatch_async_After, which calls stopTones after 400 milliseconds. The note will play for a short period of time and then stop. This approach won't work if you want to play more than one note. We recommend using a timer. It's a more straightforward API and it's easy to repeat a loop over a predetermined time interval. Let's update our example to play multiple notes. Here, we have supplied the frequencies for middle A, middle B and middle C. To play them consecutively after one another, we use a timer. We iterate over our array of tones, playing the next one every 400 milliseconds. When we get to the end of our array, we call stopTones on our ToneOutput

**[3:10]** and invalidate our timer so it'll stop repeating. Finally, you need to make a call to endPerformance, so that you get credit for your work. You'll use this same call on all of your remaining challenges to signal to the Swan that you've finished performing. And that's how you can use a timer to play multiple different notes one after the other. Thanks, Stephen. Before we go any further, I want to warn you. This side quest will contain spoilers for this chapter's challenge. If you want to complete the challenge first, hit pause on this video and come back after you've completed the challenge. Good luck. Okay, are you ready to do this side quest?

**[3:56]** The Swan's challenge was to play a C-major scale, and they provided all of the frequencies for you. Let's see if you can adapt that code to play an F-major scale. If you think about it, you already have many of the frequencies you need. First, the F-major scale starts at F4. You already have that note from the Swan. Second, you should be able to reuse your code from your C-major scale. Finally, if you need to go up an octave, just double the frequency. That means to get an A5 from an A4, you need to multiply 440 Hz by two to get 880 Hz. Right. You're gonna need the frequency for B-flat too. During this episode,

**[4:41]** we gave you tips for completing the second challenge in Swan's Quest. We introduced you to ToneOutput and how to use Swift Playgrounds to play tuned pitches by frequency. Then we discussed how to use timers to change notes for a certain duration. Tomorrow, we'll be back with a "note-able" challenge. You're not gonna wanna miss it. Good luck, have fun, and join us in the forums to share your solutions for the side quest. We'd love to hear how you did.
