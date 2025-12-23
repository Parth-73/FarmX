# 🔧 Servo Control Logic – FarmX Project

This document describes the control logic used for the **2-axis servo-based herbicide spraying system** in the FarmX autonomous drone.

The servo mechanism enables precise, coordinate-level spraying based on AI-detected weed locations.

---

## 🎯 Objective

To accurately align the spray nozzle with detected weed coordinates and apply herbicide only at the target location, minimizing chemical waste and crop damage.

---

## 🧠 Inputs to the Servo System

The servo controller receives the following inputs:

- Weed detection coordinates from AI model (YOLO)
- Grid resolution (256 × 256)
- Drone altitude from ground
- Wind speed and direction (optional, future enhancement)
- Servo angle limits

---

## 🧩 Coordinate System

- The camera frame is divided into a **256 × 256 grid**
- Each grid cell represents a physical ground area
- Weed detection outputs `(x, y)` pixel coordinates
- Coordinates are normalized and mapped to servo angles

---
Camera Image
↓
AI Weed Detection (YOLO)
↓
Grid Mapping (256×256)
↓
Coordinate Normalization
↓
Servo Angle Calculation
↓
Spray Actuation

## 🔄 Control Logic Flow


---

## ⚙️ Servo Architecture

- **X-axis servo** → Horizontal movement
- **Y-axis servo** → Vertical movement
- **Spray solenoid / pump** → ON/OFF control

Each servo operates independently but synchronously.

---

## 📐 Angle Mapping Logic

Let:
- `x, y` = detected weed coordinates
- `W, H` = image width and height
- `θx, θy` = servo angles

Mapping:

θx = map(x, 0 → W, minX → maxX)
θy = map(y, 0 → H, minY → maxY)

Where:
- `minX, maxX` and `minY, maxY` are servo mechanical limits

---

## 💧 Spray Decision Logic

IF confidence ≥ threshold
AND grid cell not sprayed
THEN
    move servos to target angle
    activate spray for t milliseconds
    mark grid cell as sprayed
ELSE
    skip target

