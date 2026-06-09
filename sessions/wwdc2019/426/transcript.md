---
id: "wwdc2019-426"
event: "wwdc2019"
title: "Building Activity Classification Models in Create ML"
url: "https://developer.apple.com/videos/play/wwdc2019/426"
language: "eng"
words: 1517
---

# Building Activity Classification Models in Create ML — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2019/426) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:12]** I am Yuxin from Core ML. Today I'm very excited to introduce a brand-new model in Create ML this year, Activity Classification. We do lots of activities with our devices every day such as playing games, doing sports. And our mobile devices have been equipped with a very rich set of sensors. Such as for motion, Accelerometer and Gyroscope are very commonly used. And they can help us to detect your device's three-dimensional acceleration, rotation rate or

**[0:59]** device orientation. And we could just use such sensor data to represent our activities. For example, if you are jogging, your activity data may look very different when you are standing still. Similarly, if you have different gestures, gaming controls, or different sports movement. Your activity data could also be distinctive enough to be recognized. So what is Activity Classification? It is a task that allows you to recognize your pre-defined set

**[1:45]** of physical actions that you do with your devices. Then what if you have a different set of activities to recognize or your app may have a different need. We think it will be really great if you could customize your own model for your own purpose and that's exactly what we are introducing this year, Activity Classification in Create ML. Perhaps, let's start with an example. I really love to go out and play ultimate frisbee with my family

**[2:30]** and friends. So after a whole game, I'm also very interested to see how well I might have performed such as what they types of throwing techniques and how many of them. So I trained a Frisbee Motion Classifier to recognize my moves and I use it on my watch. I think it's going to be fine. Let's see a live demo first. So this is the screen of my phone which is paired with my watch. So my model is going to run on my watch. You can see a Start button here.

**[3:15]** So once I hit a Start button, my watch is going to start streaming the sensor data. And then my model is going to make continuous predictions. So let's get started. Now it asks me to try a frisbee move which means it predicts a no activity class which is true for now. Let me try something simple first. Forehand. And next, Backhand.

**[4:01]** And this is my favorite one. Chicken Wing. I also have a fancier and secret one to show. Bowling. It's called Bowler but as if I'm playing bowling. Let me try that again. Bowler. Yeah, it's machine learning models. Now, let me hit the Stop button and see my results. Looks like pretty okay to me. For certain classes like Bowler,

**[4:48]** I know I can always go back and collect more data. So I'm pretty fine with this. Very good exercise for today. Now, let's come back and I know you as developers may have lots of other more creative ideas to explore. So now let's see how could we truly set your model in Create ML. Just the three steps. First, collect some data for your own activities. Train the model using Create ML.

**[5:35]** And finally, deploy the model to your app. Let's get some data first. The easiest way to access sensor data is to use Core Motion. For more information, please refer to our previous sessions as well as Apple Developers Documentation. But from a high-level point of view your app could simply access a list of the sensors. So Core Motion Framework. You can also manipulate the Start, Stop, or Set Update Intervals from your app for your recordings.

**[6:20]** And you can also use exactly the same mechanism for both your training data collection as well as your later on device inference. And here is how my data look like. This is one of my Forehand recordings, which is in a CSV format. There's one column of Time Stamps and several other columns of the sensor features. I actually used both User Acceleration and Rotation Grade for my frisbee motion example. But here for simplicity only three are listed.

**[7:06]** And if they would like to take one step further to look into the data, this is how the activity patterns may look like. My Forehand recording has three back to back moves in the same class. And later during training, the deep learning model is going to use a sliding window to move through this time series data. And in this way, it could extract both your spatial and temporal patterns of the activities. Now we have the files ready. You could simply organize your data in such a hierarchy of data source, where each folder's name

**[7:53]** is a Label name. And all the files under this folder belongs to the same activity. We support CSV,JSON , and text formats. You could choose either one of them or if you like, you can mix and match. There's a data ready. Now let's start printing. Simply select Activity Class from our template from the Create ML app. And now this is a standard info screen where you could drag and drop your training data into the window. For Activity, you can see a

**[8:39]** preview of how many files and how many samples in your recordings. The one special step above the Activity is that you have to tell Create ML what are the sensor features you'd like to try out. Simply select one or a few from this list. And all these sensor features actually come from your own files, the headers of your CSV files. Optionally, you could choose to adjust the parameters as well such as this Prediction Window Size based on how fast and slow of your activities. For my frisbee motion example, I

**[9:27]** actually used the two second window, which is 100 samples. So I put 100 here and that's because my data was initially sampled at a 50 hertz frequency. Now, let's hit the Train button and we can start training from here. I'm sure you have seen this whole process several times during the week. I'm going to skip this because the whole workflow from here is exactly the same as other models in Create ML. If you are satisfied with your accuracies, you could move on and try some new data to

**[10:13]** evaluate the performance of this model. This is a standard testing tab. Just supply your testing data the same way you just did. And after the evaluation, you would see a table of your per class matrix in terms of precision and recall. For my frisbee motion example, you can see here, Bowler and Hammer, these certain classes are not that perfect. So this perhaps means I need to go back and collect more data for these classes. And iterate again, so we

**[10:58]** can improve the performance. And finally, we get a train model and from this point, you could choose either save the model and deploy it to our app or you can do batch predictions in Create ML app on your Mac directly here. Simply add some new unseen and unlabeled the data into the window and you will see immediate prediction results in terms of Label Name, Confidence, and also a preview of your Activity Data so you could have a better understanding of your activities.

**[11:46]** And finally, this is my Core ML model. My Frisbee Motion Example is a Neural Network classifier. With only 1.1 megabyte which is pretty small and very simple for mobile devices. In addition, you could also see a complete list of all the sensor features you have used in training, as well as a Prediction Window size. So later for your own device inference, you could simply use the same data, same size to keep consistent. And this is Create ML app.

**[12:32]** We also have the framework in macOS. So you could automate this whole process by using Xcode Playground, Swift Script, or Command Line Tools. Like this. The one special step above Activity is that you have to specify the selectedSensors. And other than this, the rest of the workflow is standard and is the same with other models we have, where each training evaluation and model saving is just a one line of code for each.

**[13:17]** And this is how we view an activity classifier in Create ML. But additionally, I'd also love to share a few better practices for this model. Understand your activities. Use the relevant sensors, such as Accelerometer and Gyroscope, are very common for motion-based tasks. It will be also helpful to collect some data for additional no activity or other class. This is especially helpful for your runtime performance.

**[14:03]** Providing balanced classes is also good practice. For activity, this is in terms of both number of recording files and the recording length for each class. And finally, Core Motion provides both raw sensor data and processed device motion data. Device motion is a sensor fusion under Core Motion Framework, and it provides some additional normalization, time alignment, or bias removal. So sometimes it could be really helpful for you to process the data.
