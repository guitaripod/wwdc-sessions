---
id: "wwdc2024-10087"
event: "wwdc2024"
title: "Create custom environments for your immersive apps in visionOS"
url: "https://developer.apple.com/videos/play/wwdc2024/10087"
language: "eng"
words: 1224
---

# Create custom environments for your immersive apps in visionOS — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2024/10087) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:07]** Hello.  My name is Daniel, and I'm a RealityKit UX Designer at Apple. Today, I would like to talk about creating impactful custom app environments for Vision Pro. In this session, we will discuss design considerations for your environment which contribute to the success of the final product. We will share guidelines for keeping 3D assets as light and efficient as possible. We will review the export workflow, including the role of lighting and texture baking in your custom app environment. This is to help reduce the complexity and the computational load of your scene Finally, we will bring the pieces from Blender to Reality Composer Pro. When you begin designing your custom app environment,

**[0:52]** there are some questions you should consider about its function. Is it to create a warm, welcoming ambiance for an immersive experience... or perhaps to help your viewer feel more creative? Is it to help someone feel calm and relaxed... or is it for reviewing work in optimal lighting conditions? In our example, we are creating a viewing environment for the Destination Video app. It is a large, open space with a clear central view to our focus - the screen. Let’s jump in to creating an environment. First, you can begin blocking out using your digital content creation tool

**[1:38]** (also known as DCC), such as Maya and Blender, with simple primitives likes boxes and planes to create a quick first iteration. As environments are built to real-world scale, human figures are helpful to give an accurate sense of size. As you build out your environment, be aware that your perception of scale in headset is different to what is viewed on a 2D screen. Going between the two as you tweak the overall size and the scale of individual elements is important. Be aware when including a viewing screen in your environment that placing assets in front of the screen may produce undesirable depth conflicts.

**[2:23]** This environment and its screen are designed as a seated experience from an optimal location, set within a viewing area as represented by this circle on the ground. The default view is towards the screen but the viewer will be able to look around the studio and be able to move within the system safety bounds. Note that it’s not necessary to create geometry for areas that are not visible from the viewing area. We will now discuss guidelines for keeping geometry as light and efficient as possible in your custom app environment. The assets in your scene can be hand-modeled, a scan from the real world using Object Capture

**[3:08]** or maybe purchased from a 3D library. In our scene, we include part of a tree which was created using Object Capture. The asset was then decimated in Blender, the DCC tool used in this example. Geometry should be as complex as necessary to communicate the asset with enough detail. As the tree asset is located at the back of the scene, and it requires less detail, so in this case, the tree asset can be decimated. Next, let’s discuss textures. In our scene, there are various textures such as the matte black steel of the structure,

**[3:53]** the oak treads of the stairs and the concrete floor. Let’s take a closer look. The concrete floor covers a significant area of the space. To create this texture, we use a mix of procedural maps generated in Adobe Substance Designer and real photography. The initial layer was generated procedurally to create high-frequency detail and to allow us to tile the texture without losing definition. The second layer was composed of real photographic elements. We then overlaid two more textures to add variation and break up the repetition to land on the final texture applied across the floor.

**[4:41]** Next, let’s look at lighting. Lighting can be a powerful tool that influences the viewer's perception of the space and can direct their attention to specific elements. This scene is lit by spotlights which evenly illuminate the art on the walls and the floor. A daytime HDRI brings in light through the roof light. Your environment can have multiple lighting set-ups to give the viewer the choice of how to experience the space. This space has 2 modes: light and dark. In dark mode, we switch to a nighttime HDRI, and the spotlight intensity is increased.

**[5:27]** As you test the lighting, it is important to note that how you perceive light varies between monitor and headset. Next, let’s discuss part of the workflow, Texture Baking, which captures all surface characteristics of 3D objects into a single image. This image can then be reapplied to the objects, making them look realistic and detailed without additional raytracing. This technique combines all surface data into a single UV Map and greatly decreases the total number of textures in the scene. In our scene, we repacked the UVs of the entire scene into six groups: Mid section,

**[6:12]** Ceiling, Floor, Front section, Rear section and Props. Once you have simplified the scene into 6 UV maps and 6 textures, the scene should be light and simple to manipulate. We can now export a usdc file to Reality Composer Pro. For this simple process, you can use any DCC that can save out USD files such as Maya, Houdini or Blender, which I will use. With my 3D scene ready in Blender, I will go to the File menu, and I will select the Export option. Here, you can see the option for a file name called "Universal Scene Description",

**[6:57]** which I will use as a final format for the final export. I will leave all the parameters as they are by default, and the only thing I will change is the Root Prim name. This is important as this name will carry to Reality Composer Pro. Now, in Reality Composer Pro I just need to import the usdc file into a new project. When I import the file, you can see that because I named my objects and materials in Blender, now it’s easy to modify the materials for each piece.

**[7:42]** I have baked the lighting, so the only thing I need to do in Reality Composer Pro is to change the original material to "unlit". I have previously loaded the maps for this scene, so I will connect each map to the corresponding material. Lastly, I'm going to disable "Apply Post Process" tone map to be sure the look is exactly the same as I developed it in Blender. I'm going to repeat this process for the rest of the materials in my scene. To add the final touches, I will select the elements that should look like glass and assign them a physically-based material.

**[8:29]** I will adjust the "Roughness" and "Opacity" attributes to achieve the desired effect. By now, I should have in Reality Composer Pro a 3D scene that represents the final look for my project. At this point, you might need to add some other interesting elements to your 3D scene, like video components. In this session, we looked at how to design, create and optimize an environment to run on VisionOS. We shared a case study of a studio designed for watching media, and we shared tips when going between DCCs and Reality Composer Pro.

**[9:14]** We can’t wait to see the environments and experiences that you will create!
