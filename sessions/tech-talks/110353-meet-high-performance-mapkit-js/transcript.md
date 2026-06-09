---
id: "tech-talks-110353"
event: "tech-talks"
title: "Meet high-performance MapKit JS"
url: "https://developer.apple.com/videos/play/tech-talks/110353"
language: "eng"
words: 1112
---

# Meet high-performance MapKit JS — Transcript

[Session page](https://developer.apple.com/videos/play/tech-talks/110353) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:00]** Hello, my name is Tim Chien. I'm an engineer on the MapKit team here at Apple, working on MapKit JS. Today I'm going to talk about several exciting new features you can use to deliver the best possible experience when integrating MapKit JS with your web application. Since the introduction of MapKit JS in 2018, we have worked tirelessly adding new features every year. With that, MapKit JS has become an indispensable part of Apple's web offering, integrated into many websites like in our own Find My servers on icloud.com, and third-party websites like DuckDuckGo,

**[0:48]** and a property search website in Greece. You'll notice this website is taking advantage of MapKit JS's ability to localize the map features. We made it super easy to adopt MapKit JS in any web application with a simple include and initialization. However, we want to provide you the flexibility to adopt MapKit JS in the manner that optimizes the performance of your application. So starting this year, we have turned our eyes to performance and looked at how we could make your pages more responsive, faster to load, and in a manner designed to give you more control,

**[1:35]** enabling you to include only the functionalities you need when you need them. Today, I'm happy to introduce three new features that will just do that, including a new markup for high-performance MapKit JS loading, the ability to load additional MapKit JS libraries on demand, and finally, a new way for an application to signal the desired map features to present to the user. Now to demonstrate how these new features can improve your web application, let's say you're building an interactive treasure map for your fellow pirates. You have adopted the default implementation of MapKit JS.

**[2:20]** However, when viewing this page over the lousy pirate ship Wi-Fi it takes too long to load and the user has to wait too long for the map to appear, making your shipmates impatient. So to prevent a mutiny, you can use the new high-performance MapKit JS loading markup. It swaps the default implementation for an expanded markup with additional properties you'll use to tune your web app. First, MapKit JS now offers a new JavaScript bundle, market.core.js, that contains only the minimum amount of code to get yourself started. Next, we want to let MapKit JS know the subset of features

**[3:06]** we will need. Here, we specify just the map library, which is the minimum feature set to show an interactive map. We will prevent MapKit JS from blocking the page load by using the async attribute and invoke a callback specified by data callback attribute when it finishes loading. Since MapKit JS no longer blocks the page from loading, your web app should assert its readiness before assessing its interfaces for the first time. As an example, here is an async function that will resolve to the MapKit interface when MapKit JS is ready. As always, MapKit JS is available on the global window object as soon as it has been loaded.

**[3:55]** If the MapKit object is undefined, that means MapKit JS has not been loaded yet. Additionally, we want to check if the initial libraries have been loaded. Recall that we asked for the map library in the markup using the data library's attribute. Failing either of the two tests means the callback set using the data callback attribute has not been invoked. Here we convert a callback into a promise for our async function and clean up the callback right after promise resolution. With that, we have guaranteed that MapKit JS is ready to roll when this feature returns. Now, back to the syntax.

**[4:40]** There are some other useful attributes in our high-performance markup, including the crossorigin attribute that allows the browser to reuse a single HTTP/2 connection for all the requests going to the MapKit JS CDN. We would also like MapKit JS to initialize itself as soon as it has the opportunity to do so. We can achieve that by setting an initial token in the markup. Piece it together and we will make our page load even faster, but we are not there yet. Since we only asked for the map library, we would need to load the annotations library to be able to put our pirate ship and treasures back on the map.

**[5:30]** And that's where our second optimization comes in handy. A new method is offered just for that MapKit download. It loads additional libraries asynchronously on demand. And if any library you load requires another, it will be handled automatically. And here it is in action. Simply call MapKit download method to load the annotations library. Add a listener for the load event, then add your annotation when it is called. And of course, you can load more than annotations. For example, services encompass all services APIs

**[6:17]** like search and geocoder. Full map loads all the features available on the MapKit map class. And that includes basic map, overlays, annotations, and user location display. And GeoJSON loads the GeoJSON importer. Now, this is a good loading experience, but we can do even better than this. This is the third feature we are going to introduce today: prioritized map start-up. With the new load priority property,

**[7:04]** we can instruct MapKit JS to show points of interest sooner to give feral pirates a better head start. When setting the load priority, you should cater to the best experience that your user needs. There are three load priority options available. Points of Interest instructs MapKit map to show the map labels and points of interest sooner, even before your annotations. Land Cover, on the other hand, will service just the land cover, roads, and borders. As these options will interfere with some map behaviors during start-up, like rotation or precise map region of the viewport,

**[7:49]** you can turn off load priority altogether by setting it to none. And here is what it looks like in action. Simply use load priority in the map constructor option to specify the desired priority. Here we ask MapKit map to show the points of interest first. Now that's an even better loading experience. Today, we introduced three new features designed to improve the map load experience of your application. We believe that you can integrate MapKit JS while ensuring that the overall user experience remains seamless and unimpaired.

**[8:36]** For your existing application, feel free to adopt these new features gradually, as each will bring its own benefit. Be sure to check out the detailed documentation and the Maps Server API session shown below. We look forward to seeing how you take advantage of these new features. Thank you.
