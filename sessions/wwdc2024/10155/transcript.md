---
id: "wwdc2024-10155"
event: "wwdc2024"
title: "Swift Charts: Vectorized and function plots"
url: "https://developer.apple.com/videos/play/wwdc2024/10155"
language: "eng"
words: 1472
---

# Swift Charts: Vectorized and function plots — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2024/10155) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:07]** Hi, I’m Apollo. Let me tell you about what's new in Swift Charts. Swift Charts enables the creation of informative, accessible, and delightful visualizations using SwiftUI. This release brings to you new charts to present weather trends, track your mood and vitals, and graph functions in Math Notes. That's right! Swift Charts now allows you to visualize things beyond data, by plotting mathematical functions in your apps. Swift Charts now also has vectorized plotting APIs

**[0:55]** that support visualizing larger data sets even more efficiently. I've plotted this video to teach you more about each of these exciting new capabilities of Swift Charts. Starting with function plots, which introduce two new APIs: LinePlot, for visualizing a single function, And AreaPlot, to fill in the area between two functions. Let me take you through how function plots can help me with data analysis. I’ve been researching Large-Scale Solar energy projects in the contiguous United States, using a dataset from US Geological Survey.

**[1:43]** I built a histogram to visualize the solar panels’ capacity densities with a ForEach over the data points, and a BarMark for each element. You know what? This histogram suggests that capacity density may be normally distributed. I’ll compare by plotting a normal distribution using the new function plot API. I've defined a function that calculates the points on a normal distribution curve and I can plot it using the new LinePlot API, which accepts a closure that takes a double and returns a double,

**[2:30]** so I can call my function with a precomputed mean and standard deviation. It's fundamental to Swift Charts that data visualizations are accessible to everyone. Swift Charts makes your chart accessible by default. I can use Voice Over to describe the chart. “The x axis is capacity density, The y axis is probability. There are two data series." Audio Graph works on a function plot, too.

**[3:16]** "Complete." Great! And just like in SwiftUI, you can use modifiers to customize how your functions look. Here, because the LinePlot has the same default color as the bars, it's a good idea to customize the color of my function plot with a different foregroundStyle. Much better now. But, to make it stand out just a little more, I would like to fill in the area below the curve. To do that, I can simply change the LinePlot to an AreaPlot. Then, to increase the contrast, I can further customize the AreaPlot

**[4:05]** with an opacity to make it more legible. So that's how to plot a simple math function. But Swift Charts makes it just as easy to build more advanced function plots. For example, not only can AreaPlot visualize the area under a curve, you can use it to visualize the area between two functions as well, by returning a tuple of yStart and yEnd for a given input x. Unlike visualizing data, a function can accept an unbounded range of x values.

**[4:51]** By default, Swift Charts automatically infers the domain by sampling the function. But I can customize the overall bounds of the chart by setting the X scale and the Y scale to include only parts of the function that I find interesting. I also have the ability to limit the domain of the function plot itself. By restricting AreaPlot’s sampling domain, the chart now includes only the middle part of this function. Swift Charts also supports plotting parametric functions.

**[5:36]** Here's a parametric function, where x and y are defined in terms of a 3rd variable, T. Let's plot it. You can graph parametric functions in Swift Charts by using the same LinePlot API, but return both x and y values given the value t. I love it! Next, let's talk about how to handle piece-wise functions. Sometimes, a piece-wise function doesn't have an output for certain values in it's domain. In those cases, you can return .nan to inform Swift Charts

**[6:23]** that there's not a number for that input value x. In other cases, your code might trap for certain x values, such as when evaluating 1 over x when x is equal to 0. Similarly, you should handle the special values by returning .nan. That's function plotting with Line Plot and Area Plot, where they treat an entire math function as a single entity. But the plot APIs are useful for more than just functions. They can make it more convenient and more efficient to visualize larger datasets.

**[7:09]** So we've added plot API variants for all the other mark types, too. These vectorized plot APIs can handle an entire collection in parallel to draw extensive data visualizations, such as a scatter plot for a classification model, or a heatmap visualizing self attention in a transformer language model. But before I let the plot thicken, let's review how you would declare a Chart using the Mark API. Marks are super flexible, allowing you to style each individual data point differently; from choosing which modifiers to apply, to even what kind of mark to use.

**[7:59]** However, most often you don't need this level of customization. It's common for an entire collection of data points to be styled homogeneously, using the same element properties for X, Y, foregroundStyle, and other visual attributes. In contrast, the new Vectorized Plot API, such as RectanglePlot, allows Swift Charts to process larger collections of data more efficiently. For an example of vectorized plots, let’s go back to our solar panel dataset. I want to add a visualization of ALL the solar panel installations to my app.

**[8:46]** For all the points in this chart, I'd like to customize them in the same way. The size will be determined by the capacity, and they'll be colored differently based on the panel's axis type. The dataset has raw GPS coordinates in longitude and latitudes, but I want to apply Albers projection to display the points on a flat surface. I could add computed properties in an extension to do this conversion on the fly, but to get the most out of vectorized plots, I'll add them as stored properties instead. Stored properties allows Swift Charts to access the x and y values

**[9:33]** for all data points with a constant memory offset instead of calling the getter for every data point. The new PointPlot API takes an entire collection of data to plot. For the x and y values of all the points in the plot, I can use the same .value syntax with a label, And a KeyPath to the stored properties x and y of the DataPoint structure. If you've used SwiftUI before, you might have already used KeyPaths. Using KeyPaths lets Swift Charts style all the points without iterating over the dataset.

**[10:21]** Modifiers for vectorized plots take keyPaths as well. With symbolSize, I make the size of each point represent its solar panel capacity. And similarly, I use a key path to the solar panel's axis type to customize the color of each point. All other modifiers that are often used for homogenous modification support a key path parameter, too. My app looks stunning in Apple Vision Pro with spatial computing. The vectorized plot on my left animates smoothly, and all the charts on my dashboard update simultaneously when I scrub through the bar chart.

**[11:09]** With pinch and drag, I can get a closer look at the vectorized plot we just added to learn more about each solar panel installation and glance over the normal distribution plot that we created earlier. That's vectorized plots. Now you might be wondering how Vectorized plots and Marks complement each other. Use Vectorized Plots for larger datasets where the entire plot is customized with the same modifiers and properties. Use the Mark API when you have fewer data points, but need to customize each element with individual mark types and modifiers,

**[11:55]** or if you need complex layering with zIndex. When using vectorized plots, you can help Swift Charts reduce the number of style alternation by grouping the collection of data by the style you'll use for them. Avoiding other computations during rendering can help too, such as by converting computed properties to stored properties. If you already know the few distinct styles you'll use, or the over all bounds of the chart, specifying them will render your Charts more efficiently. And lastly, it's common for some style customizations to be unnoticeable

**[12:42]** with larger amount of datapoints, so you can skip those entirely to make your chart even more performant. That's the new vectorized and function plots in Swift Charts. Try out these new features to take your visualizations to the next level. And download the Sample Project to check out more examples of function plots, including how you can add interactions to them. If you are new to Swift Charts, check out previous talks to get started. Thank you, and I look forward to what you'll plot next.
