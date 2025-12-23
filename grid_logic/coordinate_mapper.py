"""
FarmX - Coordinate Mapper
Author: Parth Vishwakarma

Purpose:
- Convert YOLO bounding boxes into precise spray coordinates
- Map image pixels to a 256x256 grid
- Output weed target points for sprinkler control
"""

from typing import List, Tuple

# =========================
# CONFIG
# =========================
GRID_SIZE = 256   # 256x256 grid

# =========================
# DATA FORMAT EXPECTED
# =========================
# YOLO bounding box format (pixel-based):
# (x_center, y_center, width, height)
# Image size: (img_width, img_height)

# =========================
# CORE LOGIC
# =========================
def map_bbox_to_grid(
    bbox: Tuple[int, int, int, int],
    img_width: int,
    img_height: int
) -> Tuple[int, int]:
    """
    Maps YOLO bounding box center to grid coordinates.
    """

    x_center, y_center, _, _ = bbox

    grid_x = int((x_center / img_width) * GRID_SIZE)
    grid_y = int((y_center / img_height) * GRID_SIZE)

    # Clamp values within grid
    grid_x = min(max(grid_x, 0), GRID_SIZE - 1)
    grid_y = min(max(grid_y, 0), GRID_SIZE - 1)

    return grid_x, grid_y


def extract_spray_coordinates(
    detections: List[Tuple[int, int, int, int]],
    img_width: int,
    img_height: int
) -> List[Tuple[int, int]]:
    """
    Converts all weed detections into spray coordinates.
    """

    spray_points = []

    for bbox in detections:
        grid_coord = map_bbox_to_grid(bbox, img_width, img_height)
        spray_points.append(grid_coord)

    return spray_points


# =========================
# FILE OUTPUT (OPTIONAL)
# =========================
def save_coordinates(
    coordinates: List[Tuple[int, int]],
    filepath: str = "ai_model/inference/weed_coordinates.txt"
):
    """
    Saves spray coordinates to file.
    """

    with open(filepath, "w") as f:
        for x, y in coordinates:
            f.write(f"{x},{y}\n")

    print(f"[INFO] Spray coordinates saved to {filepath}")


# =========================
# TEST RUN
# =========================
if __name__ == "__main__":
    print("[TEST] Coordinate Mapper")

    # Example YOLO detections (x_center, y_center, w, h)
    detections = [
        (320, 240, 50, 60),
        (100, 180, 40, 40),
        (500, 300, 70, 80)
    ]

    image_width = 640
    image_height = 480

    spray_coords = extract_spray_coordinates(
        detections,
        image_width,
        image_height
    )

    print("[RESULT] Spray Coordinates:")
    for coord in spray_coords:
        print(coord)

    save_coordinates(spray_coords)
