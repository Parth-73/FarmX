"""
FarmX - Wind Compensation Module
Author: Parth Vishwakarma

Purpose:
- Compensate spray target coordinates based on wind speed & direction
- Improve spraying accuracy under light wind conditions
"""

import math
from typing import Tuple

# =========================
# CONFIG
# =========================
GRID_SIZE = 256

# Tunable constant:
# Higher value = stronger compensation
COMPENSATION_FACTOR = 0.8

# =========================
# WIND MODEL
# =========================
def compensate_coordinates(
    grid_x: int,
    grid_y: int,
    wind_speed_mps: float,
    wind_direction_deg: float
) -> Tuple[int, int]:
    """
    Adjusts grid coordinates to counter wind drift.

    wind_direction_deg:
    - Direction FROM which wind is coming (meteorological standard)
    - 0° = North, 90° = East
    """

    # Convert direction to radians
    theta = math.radians(wind_direction_deg)

    # Calculate offset magnitude (scaled)
    offset = wind_speed_mps * COMPENSATION_FACTOR

    # Decompose into x & y components
    offset_x = offset * math.sin(theta)
    offset_y = offset * math.cos(theta)

    # Apply inverse offset (spray against wind)
    compensated_x = int(grid_x - offset_x)
    compensated_y = int(grid_y - offset_y)

    # Clamp to grid bounds
    compensated_x = max(0, min(GRID_SIZE - 1, compensated_x))
    compensated_y = max(0, min(GRID_SIZE - 1, compensated_y))

    return compensated_x, compensated_y

# =========================
# BATCH HANDLER
# =========================
def compensate_multiple_targets(
    targets,
    wind_speed_mps: float,
    wind_direction_deg: float
):
    """
    Applies wind compensation to multiple spray targets.
    """

    compensated_targets = []

    for x, y in targets:
        cx, cy = compensate_coordinates(
            x, y, wind_speed_mps, wind_direction_deg
        )
        compensated_targets.append((cx, cy))

    return compensated_targets

# =========================
# TEST RUN
# =========================
if __name__ == "__main__":
    print("[TEST] Wind Compensation")

    original_targets = [(120, 80), (200, 140), (50, 220)]
    wind_speed = 3.0       # m/s
    wind_direction = 90.0  # East wind

    compensated = compensate_multiple_targets(
        original_targets,
        wind_speed,
        wind_direction
    )

    print("Original Targets:     ", original_targets)
    print("Compensated Targets:  ", compensated)

    print("\n[DONE] Wind compensation test complete")
