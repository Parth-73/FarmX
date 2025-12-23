"""
FarmX - Servo Logic Module
Author: Parth Vishwakarma

Purpose:
- Convert 256x256 grid coordinates into servo angles
- Control 2-axis (Pan-Tilt) sprinkler system
- Enable precision herbicide spraying
"""

import time
from typing import Tuple, List

# =========================
# CONFIG
# =========================
GRID_SIZE = 256

PAN_SERVO_MIN = 0       # degrees
PAN_SERVO_MAX = 180

TILT_SERVO_MIN = 30     # degrees (to avoid hitting drone frame)
TILT_SERVO_MAX = 150

SPRAY_DURATION = 0.4   # seconds per weed

# =========================
# GRID → SERVO MAPPING
# =========================
def grid_to_servo_angles(grid_x: int, grid_y: int) -> Tuple[float, float]:
    """
    Convert grid coordinates (256x256) to servo angles.
    """

    pan_angle = PAN_SERVO_MIN + (
        (grid_x / (GRID_SIZE - 1)) * (PAN_SERVO_MAX - PAN_SERVO_MIN)
    )

    tilt_angle = TILT_SERVO_MIN + (
        (grid_y / (GRID_SIZE - 1)) * (TILT_SERVO_MAX - TILT_SERVO_MIN)
    )

    return round(pan_angle, 2), round(tilt_angle, 2)

# =========================
# SERVO CONTROL (PLACEHOLDER)
# =========================
def move_servo(pan: float, tilt: float):
    """
    Placeholder for real servo control.
    Replace with GPIO / PWM / Arduino / ESP32 logic.
    """
    print(f"[SERVO] Moving → Pan: {pan}°, Tilt: {tilt}°")
    time.sleep(0.2)

def spray_on():
    """
    Turn spray ON.
    """
    print("[SPRAY] ON")

def spray_off():
    """
    Turn spray OFF.
    """
    print("[SPRAY] OFF")

# =========================
# SINGLE TARGET SPRAY
# =========================
def spray_at_coordinate(grid_x: int, grid_y: int):
    """
    Complete spray sequence for one weed.
    """

    pan, tilt = grid_to_servo_angles(grid_x, grid_y)

    move_servo(pan, tilt)
    spray_on()
    time.sleep(SPRAY_DURATION)
    spray_off()

# =========================
# MULTIPLE TARGET HANDLER
# =========================
def spray_multiple_targets(targets: List[Tuple[int, int]]):
    """
    Spray multiple weed coordinates sequentially.
    """

    for idx, (x, y) in enumerate(targets):
        print(f"\n[TARGET {idx + 1}] Grid ({x}, {y})")
        spray_at_coordinate(x, y)

# =========================
# TEST RUN
# =========================
if __name__ == "__main__":
    print("[TEST] Servo Logic Running")

    test_targets = [(120, 80), (200, 140), (50, 220)]
    spray_multiple_targets(test_targets)

    print("\n[DONE] Servo logic test complete")
