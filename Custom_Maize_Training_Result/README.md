🌱 FarmX – YOLOv Weed Detection Model

This repository contains a trained YOLO-based object detection model developed as part of FarmX, an autonomous drone-based precision agriculture system for weed detection and targeted herbicide spraying.

📌 Model Overview

Model Type: YOLO (You Only Look Once)

Task: Object Detection

Classes:

crop

weed

Training Objective:
Detect weeds accurately from top-down aerial images of farmland to enable precision spraying.

🧠 Use Case

The model is designed to be deployed on an autonomous agricultural drone equipped with:

A high-resolution downward-facing camera

Onboard or edge AI inference system

Detected weed coordinates are later mapped onto a 256×256 grid and passed to a precision spraying controller.

📁 Folder Structure
train/
├── weights/
│   ├── best.pt        # Best trained model
│   └── last.pt        # Last training checkpoint
├── args.yaml          # Training configuration
├── results.csv        # Training metrics per epoch
├── results.png        # Training performance graphs
├── confusion_matrix.png
├── labels.jpg
└── README.md

⚙️ Training Details

Framework: Ultralytics YOLO

Input Data: Annotated aerial images of crops and weeds

Image Perspective: Top-view (drone camera)

Optimization: Precision-focused to reduce false positives on crops

🚀 Inference Example
from ultralytics import YOLO

model = YOLO("weights/best.pt")
results = model("test.png", conf=0.5)
results[0].save("output.png")

🌍 Impact

Reduces herbicide usage

Protects healthy crops

Improves yield and sustainability

Minimizes manual labor

📌 Project Context

This model is a core component of FarmX, an AI-driven solution aimed at transforming traditional farming into smart, autonomous precision agriculture.

👤 Author

Parth Vishwakarma
B.Tech CSD | B.Sc AI & DS
FarmX Project
