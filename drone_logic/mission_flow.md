📌 Objective

To autonomously detect and eliminate weeds in crop fields using an AI-powered drone that performs precision, coordinate-level herbicide spraying with minimal human intervention.

🧠 High-Level Mission Philosophy

FarmX follows a stop-and-act approach rather than continuous flight:

Ensures accurate weed detection

Reduces motion blur

Allows precise herbicide targeting

Makes the system reliable for early-stage crops

🔁 Complete Mission Flow
1️⃣ Mission Initialization

Farmer selects field boundary on web interface

Boundary coordinates and mission parameters are uploaded

Drone performs system checks:

Battery level

GPS lock

Camera availability

Sprayer readiness

2️⃣ Takeoff & Transit

Drone takes off from base station

Navigates to the start point of the selected field

Maintains safe altitude during transit

3️⃣ Hover Positioning

Drone descends to ~0.6 m (≈2 feet) above crop canopy

Enters stabilized hover mode

Ensures minimal vibration for image capture

4️⃣ Image Capture

High-resolution downward-facing camera captures field image

Image is stored locally for AI inference

Each image corresponds to a fixed ground coverage area

5️⃣ AI Weed Detection

Captured image is passed to the trained YOLO model

Model outputs:

Weed bounding boxes

Confidence scores

Only detections above threshold are considered valid

6️⃣ Grid Mapping & Coordinate Generation

Image is divided into a 256 × 256 grid

Weed bounding boxes are mapped to grid coordinates

Coordinates represent exact spray target points

7️⃣ Precision Spraying

Drone remains stationary during spraying

Sprinkler/servo system:

Aims at weed coordinates

Applies micro-dose herbicide

Wind compensation logic is applied if needed

8️⃣ Forward Movement

Drone moves forward by a fixed step distance

Overlapping coverage is avoided

Ensures complete field coverage

9️⃣ Loop Execution

Steps 3 → 8 repeat until:

Entire field area is covered

Or battery reaches safe return threshold

🔟 Mission Completion

Drone returns to base station

Mission data is logged:

Area covered

Number of weeds treated

Herbicide used

System enters standby mode

📊 Key Advantages of This Flow

✅ High detection accuracy

✅ Minimal chemical usage

✅ Safe for early-stage crops

✅ Fully autonomous after launch

🧩 File Mapping (Code Reference)
hover_capture.py        → Hover + image capture
run_inference.py       → YOLO weed detection
grid_generator.py      → 256×256 grid creation
coordinate_mapper.py   → Spray coordinate extraction
sprinkler_controller.py→ Herbicide spraying
mission_loop.py        → Full mission execution