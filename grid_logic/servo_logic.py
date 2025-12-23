"""
FarmX - Servo Logic Module
Author: Parth Vishwakarma

Purpose:
- Convert 256x256 grid coordinates to servo angles
- Control 2-axis (Pan-Tilt) sprinkler system
- Enable precision herbicide spraying
"""

from typing import Tuple
import time

# =========================
# CONFIG
# =========================
GRID_SIZE = 256

PAN_SERVO_MIN = 0      # degrees
PAN_SERVO_MAX = 180

TILT_SERVO_MIN = 30    # degrees (avoid hitting drone frame)
TILT_SERVO_MAX = 150

SPRAY_DURATION = 0.4  # seconds per weed

# =========================
# GRID → SERVO MAPPING
# =========================
def grid_to_servo_angles(
    grid_x: int,
    grid_y: int
) -> Tuple[float, float]:
    """
    Maps grid coordinate to servo angles.
    """

    pan_angle = PAN_SERVO_MIN + (
        (grid_x / (GRID_SIZE - 1)) * (PAN_SERVO_MAX - PAN_SERVO_MIN)
    )

    tilt_angle = TILT_SERVO_MIN + (
        (grid_y / (GRID_SIZE - 1)) * (TILT_SERVO_MAX - TILT_SERVO_MIN)
    )

    return round(pan_angle, 2), round(tilt_angle, 2)

# =========================
# SERVO PLACEHOLDER CONTROL
# =========================
def move_servo(pan: float, tilt: float):
    """
    Placeholder for real servo control.
    Replace with GPIO / PWM / Arduino interface.
    """
    print(f"[SERVO] Pan → {pan}°, Tilt → {tilt}°")
    time.sleep(0.2)

def spray_on():
    print("[SPRAY] ON")

def spray_off():
    print("[SPRAY] OFF")

# =========================
# MAIN SPRAY FUNCTION
# =========================
def spray_at_coordinate(grid_x: int, grid_y: int):
    """
    Complete spray action for one weed.
    """

    pan, tilt = grid_to_servo_angles(grid_x, grid_y)

    move_servo(pan, tilt)
    spray_on()
    time.sleep(SPRAY_DURATION)
    spray_off()

# =========================
# MULTI-WEED HANDLER
# =========================
def spray_multiple_targets(targets):
    """
    Spray all detected weed coordinates.
    """

    for idx, (x, y) in enumerate(targets):
        print(f"\n[TARGET {idx + 1}] Grid → ({x}, {y})")
        spray_at_coordinate(x, y)

# =========================
# TEST RUN
# =========================
if __name__ == "__main__":
    print("[TEST] Servo Logic")

    test_targets = [(120, 80), (200, 140), (50, 220)]
    spray_multiple_targets(test_targets)

    print("\n[DONE] Spraying complete")
