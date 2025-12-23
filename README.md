# FarmX
# 🌱 FarmX – Autonomous AI-Based Precision Weed Control System

FarmX is an autonomous drone-based precision agriculture system that detects weeds at an early growth stage and applies targeted herbicide spraying using AI-driven computer vision.  
The system significantly reduces herbicide usage, manual labor, and crop damage compared to traditional blanket spraying methods.

---

## 🚜 Problem Statement

Weeds reduce global crop yields by **20–40%** annually and cost farmers billions in losses.  
Traditional solutions such as tractor-mounted sprayers or manual labor:
- Spray herbicides uniformly (including crops)
- Waste chemicals
- Increase soil and water contamination
- Require high labor costs

Early-stage weed detection is especially difficult, yet critical for maximizing yield.

---

## 💡 Solution Overview

FarmX introduces a **fully autonomous drone system** that:
- Uses AI (YOLO-based object detection) to identify weeds among crops
- Divides the field into small grids for precise targeting
- Sprays herbicide **only on detected weeds**
- Operates without continuous human control

This results in **chemical savings, higher yield, and lower operational cost**.

---

## 🤖 Key Features

- AI-based weed detection using YOLO
- Grid-level coordinate mapping (256×256 resolution)
- Targeted micro-spraying instead of blanket spraying
- Early-stage crop compatibility
- Modular design for different crops
- Scalable for large agricultural fields
- Future-ready cloud and analytics integration

---

## 🧠 AI & Technology Stack

### Machine Learning
- YOLO (You Only Look Once) for real-time weed detection
- Custom-trained maize (corn) + weed + soil dataset
- Python, OpenCV, Ultralytics YOLO

### Google & Cloud Technologies
- Google Colab – Model training
- Google Drive – Dataset storage
- Google Sheets – Experiment logging
- Firebase (planned) – Farmer dashboard & data sync
- Gemini API (planned) – Automated reports & insights

### Hardware (Planned / MVP)
- Autonomous quad/hexacopter drone
- High-resolution downward-facing camera
- 2-axis servo-controlled micro-sprayer
- GPS + IMU for navigation

---

## 📂 Project Folder Structure

FarmX/
│
├── Custom Maize Training Result/
│ └── Sample outputs and visual results from YOLO training
│
├── training_dataset/
│ ├── images/
│ │ ├── train/
│ │ └── val/
│ ├── labels/
│ │ ├── train/
│ │ └── val/
│ └── data.yaml
│
├── scripts/ (recommended)
│ ├── train.py
│ ├── inference.py
│ └── grid_generator.py
│
├── model/ (recommended)
│ └── trained_model.pt (ignored in git)
│
├── data_sample/ (recommended)
│ └── few demo images only
│
├── README.md
└── .gitignore

---

## 📊 Workflow

1. Farmer defines field boundary (future web interface)
2. Drone captures top-down images
3. AI model detects weed locations
4. Field divided into micro-grids
5. Coordinates sent to spray controller
6. Herbicide applied only where needed

---

## 📈 Impact & Benefits

| Metric | Traditional Spraying | FarmX |
|------|----------------------|-------|
| Herbicide Usage | High | ↓ up to 60% |
| Labor Cost | High | Minimal |
| Crop Damage | Possible | Near zero |
| Environmental Impact | High | Low |
| Precision | Low | Very High |

---

## 🔮 Future Enhancements

- Firebase-powered farmer dashboard
- Google Earth Engine field mapping
- Autonomous path planning
- Multi-crop model support
- Real-time analytics & yield prediction
- Full UAV flight autonomy

---

## 🧪 Status

🔧 **MVP / Research Prototype**  
📍 Actively under development

---

## 👨‍💻 Author

**Parth Vishwakarma**  
B.Tech CSD – MITS Gwalior  
AI | Computer Vision | Precision Agriculture

---

## 📜 License

This project is for academic, research, and prototype purposes.
