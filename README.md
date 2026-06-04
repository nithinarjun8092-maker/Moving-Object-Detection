# Real-Time Moving Object Detection | Python & OpenCV

## Overview
A real-time moving object detection system that uses a webcam 
to detect and highlight all moving objects instantly using 
Python and OpenCV.

## How It Works
1. Captures live video feed from webcam
2. Converts each frame to grayscale
3. Applies Gaussian blur to reduce noise
4. Compares current frame with the first frame to find differences
5. Uses contour detection to draw bounding boxes around moving objects
6. Displays "Moving Object Detected" text on screen in real time

## Features
- Real-time detection through live webcam feed
- Draws bounding boxes around every moving object
- Lightweight — works in just 41 lines of Python code
- No heavy ML framework required — pure OpenCV

## Tools & Libraries Used
- Python
- OpenCV (cv2)
- imutils

## How To Run
1. Install the required libraries:
   pip install opencv-python imutils

2. Run the script:
   python Moving_Object_Detection.py

3. Press 'q' to quit the program

## Use Cases
- Security and surveillance systems
- Traffic monitoring
- Motion triggered recording systems
- Robotics and automation
