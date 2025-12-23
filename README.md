Hand Gesture Controlled Robot using MediaPipe & Raspberry Pi

Control a robot using hand gestures only, without Arduino.
The Raspberry Pi processes video, detects hand gestures using MediaPipe, and directly controls motors through GPIO pins.

📌 Project Overview

This project demonstrates AI + Robotics + Embedded Linux by implementing a touchless robot control system using computer vision.

Real-time hand tracking using MediaPipe

Gesture recognition using finger landmark logic

Direct motor control via Raspberry Pi GPIO

No microcontroller required

🎯 Key Features

✔ No Arduino required
✔ Direct GPIO motor control
✔ Real-time gesture detection
✔ Low latency response
✔ AIoT / Industry 4.0 ready

🛠️ Tech Stack
Software

Raspberry Pi OS

Python 3

OpenCV

MediaPipe

RPi.GPIO

Hardware

Raspberry Pi 3 / 4

USB Camera / Pi Camera

L298N / L293D Motor Driver

DC Motors

Robot Chassis

Power Supply

📐 System Architecture
Hand Gesture
   ↓
USB Camera
   ↓
MediaPipe (Python)
   ↓
Gesture Logic
   ↓
RPi GPIO
   ↓
Motor Driver
   ↓
Robot Movement

✋ Gesture Mapping
Fingers	Gesture	Action
0	✊ Fist	STOP
1	☝	FORWARD
2	✌	BACKWARD
3	🤟	LEFT
4	🖐	RIGHT
📂 Folder Structure (GitHub)
hand-gesture-robot-rpi/
│
├── src/
│   └── hand_gesture_robot.py
│
├── requirements.txt
├── README.md
└── demo.mp4 (optional)

🧠 Working Principle

Camera captures live video

MediaPipe detects 21 hand landmarks

Fingers are counted using landmark positions

Gesture mapped to robot command

Raspberry Pi GPIO controls motors

🐍 Python Code (MediaPipe + GPIO)
