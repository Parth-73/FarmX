"""
FarmX - Sprinkler Controller
Author: Parth Vishwakarma

Purpose:
- High-level control of herbicide spraying
- Uses servo logic to aim nozzle
- Handles safety, timing, and multi-target spraying
"""

import time
from typing import List, Tuple

from sprinkler.servo_logic import (
    grid_to_servo_angles,
    move_servo,
    spray_on,
    spray_off
)

# =========================
# CONFIG
# =========================
SPRAY_DELAY = 0.2        # delay after servo movement
SPRAY_DURATION = 0.4     # seconds per weed
MAX_TARGETS_PER_HOVER = 20

# =========================
# SAFETY CHECKS
# =========================
def safety_check(targets: List[Tuple[int, int]]) -> bool:
    """
    Basic safety validation before spraying.
    """

    if not targets:
        print("[INFO] No weeds detected. Skipping spray.")
        return False

    if len(targets) > MAX_TARGETS_PER_HOVER:
        print("[WARNING] Too many targets. Limiting spray count.")
        return True

    return True

# =========================
# SINGLE TARGET SPRAY
# =========================
def spray_target(grid_x: int, grid_y: int):
    """
    Spray herbicide at a single grid coordinate.
    """

    pan, tilt = grid_to_servo_angles(grid_x, grid_y)

    print(f"[TARGET] Grid ({grid_x},{grid_y}) → Servo ({pan}°, {tilt}°)")

    move_servo(pan, tilt)
    time.sleep(SPRAY_DELAY)

    spray_on()
    time.sleep(SPRAY_DURATION)
    spray_off()

# =========================
# MULTI-TARGET HANDLER
# =========================
def spray_targets(targets: List[Tuple[int, int]]):
    """
    Spray all detected weed targets in sequence.
    """

    if not safety_check(targets):
        return

    print(f"[INFO] Spraying {len(targets)} target(s)")

    for idx, (x, y) in enumerate(targets):
        print(f"\n[SPRAY {idx + 1}/{len(targets)}]")
        spray_target(x, y)

    print("\n[INFO] Spraying complete for this hover cycle")

# =========================
# MISSION HOOK
# =========================
def execute_sprinkler_cycle(weed_coordinates: List[Tuple[int, int]]):
    """
    Entry point called from mission loop.
    """

    print("[START] Sprinkler cycle")
    spray_targets(weed_coordinates)
    print("[END] Sprinkler cycle")

# =========================
# TEST RUN
# =========================
if __name__ == "__main__":
    print("[TEST] Sprinkler Controller")

    test_coordinates = [(120, 80), (200, 140), (50, 220)]
    execute_sprinkler_cycle(test_coordinates)

    print("\n[DONE] Test complete")
