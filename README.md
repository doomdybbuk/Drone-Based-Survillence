# Drone-Based Surveillance for Mango Orchard Health Monitoring
## Overview
This project leverages drone technology and machine learning to monitor mango orchards in real-time. The system captures aerial footage using a drone-mounted camera, processes the video into individual frames, and then classifies the health of mango trees based on the detected diseases of their leaves. The project uses Python, OpenCV, and TensorFlow with EfficientNetB0 for the disease classification.

## Features
Drone-Based Video Surveillance: Real-time video capturing of mango orchards via drones.
Video Processing with OpenCV: Extracts frames from video footage for further analysis.
Mango Leaf Disease Detection: Trained a deep learning model on mango leaf disease dataset for classification of healthy and diseased trees.
Automated Tree Health Classification: Automates the process of classifying trees based on their health, significantly reducing manual intervention.
## Technologies Used
Programming Languages: Python
Libraries & Tools:
OpenCV (for video and image processing)
TensorFlow/Keras (for model training and classification)
EfficientNetB0 (pre-trained model for image classification)
Drone camera for footage capturing
Dataset: Mango Leaf Disease Dataset
## Project Structure
bash
Copy code
.
├── drone_surveillance.py         # Main script to process video and extract frames
├── frame_processing.py           # Script to classify extracted frames
├── models/                       # Folder containing the trained EfficientNetB0 model
├── video_frames/                 # Folder where extracted video frames are stored
└── README.md                     # This README file
