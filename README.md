Facial Emotion Recognition with OpenCV & DeepFace

Real-time emotion detection via webcam using OpenCV for face detection and DeepFace’s pre-trained models for emotion recognition.

Overview

This project captures live video from your webcam, detects faces in each frame using Haar cascades, and identifies the emotion shown on each detected face using DeepFace’s emotion detection model. The recognized emotion is overlaid on the video feed in real time.

Key features:

Real-time webcam feed processing

Face detection via OpenCV

Emotion classification using DeepFace

Lightweight & minimal dependencies

Easy to run and extend

Why Use This

Simple, easy-to-follow implementation for real-time emotion recognition

Great starting point for building emotion-aware applications (e.g. mood detection, interactive UIs, analytics)

Demonstrates integration of classic CV (OpenCV face detection) + modern deep learning (DeepFace)

What’s Inside
File / Component	Purpose
emotion.py	Main script: captures video, detects faces, runs emotion prediction, renders results in real time
haarcascade_frontalface_default.xml	Pre-trained Haar cascade for face detection (OpenCV)
requirements.txt Python libraries needed to run the project
LICENSE	Project license

Setup & Usage

Follow these steps to get started:

Clone the repository

git clone https://github.com/darshan0703/Facial-Emotion-Recognition-using-cnn
cd Facial-Emotion-Recognition-using-cnn


Install dependencies

pip install -r requirements.txt


Or install manually:

pip install deepface opencv-python tf-keras


Download Haar Cascade file
Ensure haarcascade_frontalface_default.xml is available. (It’s included, but if not, you can get it from OpenCV’s GitHub.)

Run the application

python emotion.py


This opens your webcam window. As faces are detected, emotion labels will appear over them in real time. Press q to quit.

How It Works (Approach)

Capture video frames from webcam with OpenCV (VideoCapture)

Detect faces in each frame using Haar cascade classifier

For each detected face:

Extract ROI (Region of Interest)

Use DeepFace to preprocess and predict the emotion

Map the output to one of the emotion labels

Overlay the emotion label (e.g. “happy”, “sad”, “neutral”, etc.) on the video frame

Display the annotated frame

Exit the loop on a key press (e.g. q), then release resources

Tested On

OS: Windows / Linux / macOS

Python version: 3.x

Webcam support via OpenCV

Possible Extensions

Support video file input (instead of webcam)

Track multiple faces & maintain identity-based emotion history

Add logging or analytics (time spent in each emotion, average emotion over time)

UI overlay improvements (bounding boxes, colours, styling)

Integrate with web interface (Flask / Streamlit)

Trigger actions based on detected emotion (e.g. sound / alert / UI change)
