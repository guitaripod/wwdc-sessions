---
id: "wwdc2021-10296"
event: "wwdc2021"
title: "Diagnose unreliable code with test repetitions"
url: "https://developer.apple.com/videos/play/wwdc2021/10296"
language: "eng"
words: 1084
---

# Diagnose unreliable code with test repetitions — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2021/10296) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:09]** Hello and welcome to WWDC 2021. I'm Suzy, and I work on XCTest in Xcode. In this session, we're gonna learn about how to diagnose unreliable code with test repetitions, a tool to repeat your tests. In the process of running tests that exercise your app, your tests may occasionally fail when running unreliable code. You may run into this type of inconsistency when dealing with race conditions, environment assumptions, global state, or communication with external services. These are hard bugs to track down because they're challenging to reproduce. One way to diagnose these types of failures

**[0:54]** is to run your tests repeatedly. Test repetition, added in Xcode 13, allows you to repeat a test up to a specified number of iterations with a stopping condition. Xcode supports three test repetition modes. The first mode is Fixed iterations. Fixed iterations will repeat your tests a fixed number of times regardless of the status. Fixed iterations is great for understanding the reliability of your test suite and helping keep it reliable as new tests are introduced over time. The second is Until failure. Until failure will continue to repeat a test until it fails. I love using this tool to reproduce a nondeterministic test failure to catch it in the debugger.

**[1:41]** Lastly is Retry on failure. Retry on failure will retry your test until it succeeds up to a specified maximum. This is useful to identify unreliable tests which fail initially but eventually succeed on reattempt. If a test in CI is exhibiting this behavior, you could enable Retry on failure in your test plan temporarily and gather additional data to fix the issue. It's important to remember retrying failures can hide problems in the actual product. Some functionality fails initially before eventually succeeding, so it's best to use this mode temporarily to diagnose the failures. Let's get a better understanding of how this works in practice.

**[2:26]** I created an app called IceCreamTruckCountdown that tells me how long until the ice cream truck drives by my home. I love when the truck has cookies and cream, and so I wrote a test called testFlavors to ensure that the truck has all the flavors. testFlavors has a truck that I get from the truckDepot. I call prepareFlavors and, lastly, assert that the truck has all 33 flavors. Recently, I've noticed testFlavors sometimes fails on the main branch in Xcode Cloud. To gather more information, I temporarily configured my test plan, enabling Test Repetition Mode to Retry on failure. Let's take a look at the report navigator

**[3:11]** and check our cloud reports. My tests are inconsistently failing, so let's check this last one for more information. If I expand the first device open, there is an iteration label here letting us know it was the first iteration of this test. Huh. And when I expand all the other rows, the assertion failures are all the same, and this last test passed. I expected all the tests to pass consistently, not just on one device. I'm gonna try to reproduce this failure locally. Let's go to our file that has testFlavors.

**[3:59]** I'll Control-click on the test diamond for our test. In the menu, I'll select Run "testFlavors()" Repeatedly… to bring up the test repetition dialog. Here you can select the stopping condition of your repetitions, set Maximum Repetitions, and other options like Pause on Failure. I want to try to reproduce the issue that happened in our cloud report, so I'm setting my stopping condition to go through maximum repetitions and keep it at 100. Now I'll run my test. Oh, yay! The test failed locally. When I click on the failure annotation, it displays the same error that happened in Xcode Cloud,

**[4:45]** and it failed 4 out of 100 times. Great! I can now debug this issue. I'll Control-click again on the test diamond for testFlavors, selecting Run "testFlavors()" Repeatedly… but this time, I'm gonna use stop on failure so I can debug the issue when it happens. Thankfully, Xcode automatically selects Pause on Failure for me, so I can catch the error in the debugger. All right, we have caught the issue. And I know we're looking at inconsistencies with the flavors on the truck, so I'll take a look at our truck object in the debugger.

**[5:30]** It seems strange that flavors is 0 when it should be 33 because we already called prepareFlavors. I wonder if we've made it inside this completionHandler. I'll add a breakpoint and click Continue. Hmm, that seems wrong. Oh, the fulfill is called in the outer completionHandler and not the inner prepareFlavors completionHandler. This is a fairly simple bug caused by asynchronous events with multiple completionHandlers and the expectation not being fulfilled in the correct place.

**[6:15]** XCTest's support for Swift 5.5's async/await lets me simplify this test so it won't happen again. To transform this test to use async/await, I'll add “async throws” to the method header. I'll use the “await” version of getting the iceCreamTruck from the truckDepot. I'll use the "await" version of prepareFlavors.

**[7:07]** I'll keep the same assert, but the truck is no longer optional. Let's run this test one more time to make sure that it is fixed. I'll Control-click and select Run "testFlavors()" Repeatedly… and once again select Maximum Repetitions as the stop condition. Yay! The test passed 100 times. I'm now confident that this is fixed, and I'm ready to remove Retry on failure from the test plan and commit my change. So we just got a better understanding of how to use this at desk and one way to run your test repeatedly in CI

**[7:52]** by configuring it in your test plan. Let's talk about another way to run your tests with repetition, like in the demo, using the CLI. When running xcodebuild directly, you can add xcodebuild flags which override any test plan setting. Pass -test-iterations with a number to run a test a fixed number of times or combine it with -retry-tests-on-failure or -run-tests-until-failure to use it with one of the other stopping conditions. To run your test the same as in the demo with xcodebuild, you start with the base xcodebuild command used to run your tests and add the flags -test-iterations set to 100 and -run-tests-until-failure. In summary, use test repetitions as a tool

**[8:38]** to help diagnose unreliable code. For more information about handling inconsistent tests, watch "Embrace expected failures in XCTest." To learn more about Swift async, check out "Meet async/await in Swift." Thanks for watching. [percussive music]
