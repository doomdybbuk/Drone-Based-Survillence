Drone-Based Surveillance for Mango Orchard Health Monitoring
Overview
This project leverages drone technology and machine learning to monitor mango orchards in real-time. The system captures aerial footage using a drone-mounted camera, processes the video into individual frames, and then classifies the health of mango trees based on the detected diseases of their leaves. The project uses Python, OpenCV, and TensorFlow with EfficientNetB0 for the disease classification.

Features
Drone-Based Video Surveillance: Real-time video capturing of mango orchards via drones.
Video Processing with OpenCV: Extracts frames from video footage for further analysis.
Mango Leaf Disease Detection: Trained a deep learning model on mango leaf disease dataset for classification of healthy and diseased trees.
Automated Tree Health Classification: Automates the process of classifying trees based on their health, significantly reducing manual intervention.
Technologies Used
Programming Languages: Python
Libraries & Tools:
OpenCV (for video and image processing)
TensorFlow/Keras (for model training and classification)
EfficientNetB0 (pre-trained model for image classification)
Drone camera for footage capturing
Dataset: Mango Leaf Disease Dataset
Project Structure
bash
Copy code
.
├── drone_surveillance.py         # Main script to process video and extract frames
├── frame_processing.py           # Script to classify extracted frames
├── models/                       # Folder containing the trained EfficientNetB0 model
├── video_frames/                 # Folder where extracted video frames are stored
└── README.md                     # This README file
Installation
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/drone-based-surveillance.git
cd drone-based-surveillance
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Download the Mango Leaf Disease Dataset and place it in the dataset/ folder.

Usage
Frame Extraction from Video: Use the drone_surveillance.py script to capture video footage and extract frames:

python
Copy code
import cv2
import os

videocap = cv2.VideoCapture("path_to_your_video.mp4")
count = 0
while videocap.isOpened():
    success, image = videocap.read()
    if not success:
        break
    cv2.imwrite(f"video_frames/frame_{count}.png", image)
    count += 1
videocap.release()
Train or Load Model: Train a classifier model using EfficientNetB0 on the provided dataset or load the pre-trained model from the models/ folder:

python
Copy code
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.models import load_model

# Load pre-trained model
model = load_model('models/mango_disease_classifier.h5')
Classify Frames: After extracting frames, classify them to detect mango leaf diseases:

python
Copy code
from frame_processing import classify_frame

# Example classification for one frame
result = classify_frame("video_frames/frame_1.png")
print(f"Health status: {result}")
Dataset
The dataset used in this project can be found on Kaggle:
Mango Leaf Disease Dataset
It contains 4000 images (240x320 resolution) of mango leaves, categorized into 8 classes (7 diseases + healthy leaves).

Model and Classifier
We use EfficientNetB0 for the classification task. The model is pre-trained and fine-tuned to detect the following diseases:

Anthracnose
Bacterial Canker
Cutting Weevil
Die Back
Gall Midge
Powdery Mildew
Sooty Mould
Healthy Leaves
