---
id: "wwdc2020-10021"
event: "wwdc2020"
title: "Build Metal-based Core Image kernels with Xcode"
url: "https://developer.apple.com/videos/play/wwdc2020/10021"
language: "eng"
words: 846
---

# Build Metal-based Core Image kernels with Xcode — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2020/10021) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:03]** Hello and welcome to WWDC. Welcome, everyone. My name is David Hayward, and I'm an engineer on the Core Image team. I'll be giving a short presentation today that will show you everything you need to do to build Metal-Based Core Image kernels in Xcode. First off, why do you want to write custom CIKernels in Metal? In addition to the usual features of CIKernels, such as automatic tiling and concatenation, by writing them in Metal, you will reduce runtime compile times by shifting that work to when your app is built, give your kernels access to high-performance features such as gather-reads, group-writes, and half-float math, and make your life easier as a developer by syntax highlighting as you type

**[0:50]** and syntax checking when you build. So now that you know these benefits, let me show you step-by-step how to add Metal Core Image kernels to your application. There are five simple steps. First, add custom build rules to your project, then add .ci.metal sources to your project, write your kernel, initialize your CIKernel objects, and apply your kernel to create a new CIImage. Unlike conventional Metal compute and graphics shaders, Core Image Metal code needs to be compiled and linked with special flags. I recommend adding two custom build rules to your project targets that will make using these flags automatic.

**[1:35]** First we'll go to the project's target settings and add a build rule for files that end in .ci.metal. For files with this extension, we will run a one-line script that calls the Metal compiler with the required -fcikernel flag. This build rule will produce an output binary that will end in .ci.air. Next, we will add a second rule for files that end in .ci.air. For files with this extension, we will run another one-line script that calls the Metal linker with the required -cikernel flag. This build rule will produce an output in your apps resources directory that will end in .ci.metallib.

**[2:22]** Now that we have added the custom build rules, all we need to do is add a .ci.metal source to your project. To do that, all you need to do is go to the file menu and select New, File, and select that you want to add a Metal file, and then create a file name that ends in .ci so that the new file in your project will end in .ci.metal. For today's session, I will demonstrate this with a kernel that is shown in another great presentation on Edit and Playback HDR Video With AVFoundation. The kernel from that presentation applies an animated zebra-stripe effect that highlights the bright, extended range portions of an HDR video.

**[3:08]** To write a custom CIKernel for this effect is really easy. First, at the top of the source, you will include CoreImage.h header so that you get access to all the normal Metal classes as well as the additional classes that Core Image provides. Next you will declare the function for the kernel, which must be extern "C". The example is a CIColorKernel, so the function must return a float4 pixel and take some arguments. Here, the first argument is a Core Image sample_t that represents a pixel from an input image. This pixel is a linear premultiplied RGBA float4, which is suitable for either SDR or HDR images.

**[3:55]** The last argument is a Core Image destination that provides the coordinate of the pixel to return. In the implementation of this kernel, we use the dest.coord x and y values to determine which diagonal line we are on. Then we use some simple math to calculate if we should be on a zebra stripe or not. If we are on a zebra stripe, and the current pixel sample is brighter than the normal Standard Dynamic Range white of 1, then we will return a bright red pixel. Otherwise we return the input sample unchanged. For detailed documentation on Metal Shader Language for Core Image kernels, I recommend you go to developer.apple.com and download this reference PDF.

**[4:42]** It documents the Metal Core Image kernel classes and also describes more advanced features like gather-reads and group-writes. The final steps I will describe today are in the Swift code that loads your kernel and applies it to create a new image. Kernels are typically used by CIFilter subclasses which will have input properties such inputImage and other parameters. We recommend that your filter instantiate its CIKernel object using a static property. This way, the work of loading the compiled metallib resource is done only once when it is first needed. Lastly, CIFilter subclass must override the output image property. In this getter, you will take the kernel from the static property

**[5:29]** and use its apply method to create a new image. So that concludes my step-by-step description on how to build Metal Core Image kernels in Xcode. I have shown you how to add custom build rules to your project, how to write a kernel and add it to your project, and how to initialize and apply your kernel object to create a new image.
