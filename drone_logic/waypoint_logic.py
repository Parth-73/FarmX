"""
FarmX - Waypoint Logic Module
Author: Parth Vishwakarma

Purpose:
- Generate waypoints for full field coverage
- Move drone step-by-step between hover points
- Support stop-and-act spraying strategy
"""

import time
from typing import List, Tuple

# =========================
# CONFIG
# =========================
STEP_DISTANCE_METERS = 1.0      # forward movement after each spray
HOVER_ALTITUDE = 0.6            # meters (~2 feet)
MOVE_DELAY = 1.5                # seconds between moves

# =========================
# WAYPOINT GENERATION
# =========================
def generate_waypoints(
    start_lat: float,
    start_lon: float,
    field_length: int,
    field_width: int
) -> List[Tuple[float, float]]:
    """
    Generates a simple grid of waypoints.
    (For MVP: assumes rectangular field & flat terrain)
    """

    waypoints = []
    lat, lon = start_lat, start_lon

    for row in range(field_length):
        for col in range(field_width):
            waypoints.append((lat, lon))
            lon += 0.00001  # mock longitude step
        lat += 0.00001      # mock latitude step
        lon = start_lon

    return waypoints

# =========================
# DRONE MOVEMENT PLACEHOLDER
# =========================
def move_to_waypoint(lat: float, lon: float, altitude: float):
    """
    Placeholder for drone navigation command.
    Replace with MAVLink / DroneKit later.
    """
    print(f"[MOVE] Flying to waypoint ({lat}, {lon}) at {altitude} m")
    time.sleep(MOVE_DELAY)

def hover():
    """
    Simulated hover.
    """
    print(f"[HOVER] Holding position at {HOVER_ALTITUDE} m")
    time.sleep(1)

# =========================
# WAYPOINT EXECUTION
# =========================
def execute_waypoints(waypoints: List[Tuple[float, float]]):
    """
    Main execution loop for waypoint-based mission.
    """

    print(f"[INFO] Total waypoints: {len(waypoints)}")

    for index, (lat, lon) in enumerate(waypoints):
        print(f"\n[WAYPOINT {index + 1}]")
        move_to_waypoint(lat, lon, HOVER_ALTITUDE)
        hover()

        # At this point:
        # → hover_capture.py is called
        # → YOLO inference runs
        # → Sprinkler acts

# =========================
# TEST RUN
# =========================
if __name__ == "__main__":
    print("[START] Waypoint Logic Test")

    start_latitude = 26.2183   # example
    start_longitude = 78.1828  # example

    waypoints = generate_waypoints(
        start_lat=start_latitude,
        start_lon=start_longitude,
        field_length=3,
        field_width=3
    )

    execute_waypoints(waypoints)

    print("\n[DONE] Waypoint mission completed")
