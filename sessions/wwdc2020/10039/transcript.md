---
id: "wwdc2020-10039"
event: "wwdc2020"
title: "Build document-based apps in SwiftUI"
url: "https://developer.apple.com/videos/play/wwdc2020/10039"
language: "eng"
words: 1389
---

# Build document-based apps in SwiftUI — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2020/10039) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:03]** Hello and welcome to WWDC. Hi, everyone. My name's Tina. I work on SwiftUI. Today I'm going to talk about building apps supporting documents with SwiftUI. First off, what is a document? People have been managing their files with the Finder and Files app on macOS, iPadOS and iOS. They can use features like tags, cloud file providers and external storage devices to organize their projects as they need. They expect to be able to use apps that allow them to seamlessly open these files in place, view and edit them. This includes being able to make changes on the original document, where the change is accessible to all apps that support opening files in place.

**[0:50]** This is in contrast to apps that import those files into some database that is then managed by the app. When you edit an imported document, you're editing a copy of the original document, and the original is unchanged. Professional apps like Pixelmator not only allows users to do openInPlace file management, but also enable powerful editing capabilities, including opening multiple files at once. Almost all of the functionality in apps like Pixelmator, Keynote and Final Cut Pro is focused on allowing users to do this management of documents. We often call these "document-based apps" as an indication of that behavior. But opening documents is a feature your app can support

**[1:35]** without being entirely document-based. Apps like Xcode have additional UI and features outside of its document support. And apps like Mail and Console primarily present a non-document-based appearance, but support opening additional documents, like EML files or crash reports. A SwiftUI application is composed of apps, scenes and views. Adding support for documents is done compositionally using another scene type, called DocumentGroup. A simple text-editing app looks like this. When you use DocumentGroup in your app, you're declaring that your app supports opening and managing this type of document in place. As shown in the "App Essentials in SwiftUI" talk,

**[2:21]** the structure of our code matches the hierarchy of ownership of an app. In this case, our app contains a single DocumentGroup scene, able to open multiple windows of that document content. And of course, as a compositional element, it could support multiple DocumentGroups for different types, or a WindowGroup and a DocumentGroup. You can compose these scenes into your app, and SwiftUI automatically gives your app the expected platform behaviors for those scenes. That includes standard UI elements specific to document apps. State Tracking and Handoff on Mac, and Document Browser and the Navigation Bar with search field and sharing functionality on iOS.

**[3:08]** You get all these with very minimal code. Now let's build something using DocumentGroup API. So I was prototyping a drawing app with SwiftUI on my iPad Playground. I currently have a canvas where I can add shapes of different colors and change their shapes. I think it's working quite well, so I want to make it into an app where I can save and manage my drawings. Let's see how to do this. Let's open Xcode and create a document-based app. I want to have it run on both macOS and iOS, so I'm going to choose the multi-platform template. I'm going to call it "ShapeEdit."

**[3:58]** This already comes with some templates. Let's try building and running this. We now have a text-editing app that has all the document-supporting features we mentioned before. Now, before we dive in, let's have a look at the project settings. I'm going to focus on the macOS target for now, but the configuration we're going to use applies to both the iOS and macOS targets. Let's take a look at the Info.plist.

**[4:43]** Xcode adds the "Document Type" section for document-based apps. The value in this identifier field is a uniform type identifier. The system uses this identifier to associate files with your app, so it knows to open this type of document in your app when it sees one on the system. This identifier is declared as an imported type down here. It's imported because the plain text type was declared by another party, and we import this type declaration to tell the system that the app knows about it.

**[5:28]** For our app, we're going to declare a type of our own, so let's come back here... and create one. Since it's a type we invented, we need to export the type declaration to tell the system that we are the authoritative owner of this type. We do this by filling out the "Exported Type Identifier" section. Let's give it a description. We're going to store the drawing app's binary data, so make it conform to public data...

**[6:14]** and public content. I'm also going to assign it an extension. So this is all we need to change here. Let's have a look at the main function. Our document type ShapeEditDocument is declared for us already. Both the type of document and the base document to use when creating new documents are passed to DocumentGroup. The document property of the closure's argument is a binding that provides us with read-write access to the underlying data model, which is the text in this text-editing app.

**[7:00]** DocumentGroup supports opening place, and the binding lets SwiftUI know when the text is updated so it takes care of registering undo and dirtying the document state. Let's take a look at ContentView, which is the default view for presenting the document. It consists of a TextEditor. Since we're going to do a shape-drawing app, we're going to replace it with a canvas where users can draw. But we'll come back to that later. Let's have a look at a ShapeEditDocument. It is a value type that conforms to the file document protocol,

**[7:45]** which is the representation of a document on disk. First, we are going to define readableContentTypes. It's an array of UTType, the uniform type identifier. SwiftUI uses this to identify the type of a document that your user wants to open, and only those defined here are allowed. exampleText is defined here. This should match what we put in the "Document Types" section of the target's Info.plist earlier, so let's change this. Notice the difference between the two declarations. Here, we're using the exportedAs constructor,

**[8:31]** while previously we were using the importedAs constructor. The imported type is a computed variable because it's imported. That means its value can change over time as apps are installed or uninstalled. Here, we're using an exported type, so it can be declared a constant. For more information, see the documentation for UTType on the Developer website. Now let's change this... to our own type. Next, let's implement initializing our document, giving the FileWrapper and the contentType.

**[9:17]** We don't need this code, so I'm going to remove them. The contentType argument is always the type supported by the app. And there are a few ways to do this. Here, we're going to use a JSONDecoder. And to use a JSONDecoder, the type needs to conform to "Codable." We also need to implement writing out the document to a file for our specified type. We don't need these either, so I'm also going to remove them. FileWrapper is the destination of the serialization. It's an inout argument, and we can either create the new FileWrapper or update it.

**[10:04]** Again, there are a few ways to do this, and we'll use a JSONEncoder. So that's all we need to do to conform to the file document protocol. Notice that we are working with a value type here. This means that you get all the benefits of working with this struct, including copy-on-write behavior, and that the app can start saving while the user is still drawing. Now, with document support in place, let's add our prototype canvas code into the project. We have a graphic type that defines the attributes of the shapes

**[10:51]** and a Canvas View to display the shapes. Let's change the data type in the document from text to our graphic type. Let's also add some initial shapes. Let's also swap out the TextEditor with our canvas. And we're all set. Let's run it.

**[11:41]** We have a drawing app that supports documents. I can save the drawings and revisit them later. So, this is how easy it is to add document support to your app in SwiftUI. Thank you.
