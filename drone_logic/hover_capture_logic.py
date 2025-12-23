"""
FarmX - Hover Capture Module
Author: Parth Vishwakarma

Function:
- Drone hovers at a fixed altitude
- Waits for stabilization
- Captures an image
- Saves image for AI weed detection
"""

import time
import cv2
from datetime import datetime

# =========================
# CONFIG
# =========================
HOVER_HEIGHT_METERS = 0.6        # ~2 feet above ground
STABILIZATION_TIME = 2.0         # seconds
CAMERA_INDEX = 0                # USB camera / drone camera
IMAGE_SAVE_PATH = "ai_model/inference/"
IMAGE_PREFIX = "hover_capture"

# =========================
# DRONE PLACEHOLDER LOGIC
# =========================
def hover_drone(height):
    """
    Placeholder for drone hover command.
    In real drone: MAVLink / PX4 / ArduPilot command.
    """
    print(f"[INFO] Hovering drone at {height} meters...")
    time.sleep(1)

def stabilize_drone():
    """
    Allow drone to stabilize before image capture.
    """
    print("[INFO] Stabilizing drone...")
    time.sleep(STABILIZATION_TIME)

# =========================
# IMAGE CAPTURE
# =========================
def capture_image():
    """
    Captures image from camera and saves it.
    """
    cap = cv2.VideoCapture(CAMERA_INDEX)

    if not cap.isOpened():
        raise RuntimeError("Camera not accessible")

    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise RuntimeError("Failed to capture image")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{IMAGE_PREFIX}_{timestamp}.png"
    filepath = IMAGE_SAVE_PATH + filename

    cv2.imwrite(filepath, frame)
    print(f"[INFO] Image captured: {filepath}")

    return filepath

# =========================
# MAIN FUNCTION
# =========================
def hover_and_capture():
    """
    Complete hover → stabilize → capture pipeline
    """
    hover_drone(HOVER_HEIGHT_METERS)
    stabilize_drone()
    image_path = capture_image()
    return image_path

# =========================
# TEST RUN
# =========================
if __name__ == "__main__":
    print("[START] Hover Capture Test")
    img = hover_and_capture()
    print(f"[DONE] Captured image saved at: {img}")
