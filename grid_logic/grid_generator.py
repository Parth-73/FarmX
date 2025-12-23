"""
FarmX - Grid Generator
Author: Parth Vishwakarma

Purpose:
- Generate a 256x256 grid over an image
- Visualize spray target coordinates
- Assist in debugging and demo presentation
"""

import cv2
import os
from typing import List, Tuple

# =========================
# CONFIG
# =========================
GRID_SIZE = 256
GRID_COLOR = (200, 200, 200)     # light gray
TARGET_COLOR = (0, 0, 255)       # red
TARGET_RADIUS = 3

# =========================
# GRID OVERLAY FUNCTION
# =========================
def overlay_grid(image):
    """
    Draws 256x256 grid on the image.
    """

    height, width, _ = image.shape

    cell_w = width / GRID_SIZE
    cell_h = height / GRID_SIZE

    for i in range(1, GRID_SIZE):
        # Vertical lines
        x = int(i * cell_w)
        cv2.line(image, (x, 0), (x, height), GRID_COLOR, 1)

        # Horizontal lines
        y = int(i * cell_h)
        cv2.line(image, (0, y), (width, y), GRID_COLOR, 1)

    return image

# =========================
# TARGET VISUALIZATION
# =========================
def mark_targets(
    image,
    coordinates: List[Tuple[int, int]]
):
    """
    Marks spray target grid points on the image.
    """

    height, width, _ = image.shape
    cell_w = width / GRID_SIZE
    cell_h = height / GRID_SIZE

    for gx, gy in coordinates:
        px = int((gx + 0.5) * cell_w)
        py = int((gy + 0.5) * cell_h)

        cv2.circle(image, (px, py), TARGET_RADIUS, TARGET_COLOR, -1)

    return image

# =========================
# MAIN FUNCTION
# =========================
def generate_grid_visual(
    image_path: str,
    spray_coordinates: List[Tuple[int, int]],
    output_path: str = "ai_model/inference/grid_overlay.png"
):
    """
    Generates grid overlay image with spray targets.
    """

    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError("Image not found")

    image = overlay_grid(image)
    image = mark_targets(image, spray_coordinates)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, image)

    print(f"[INFO] Grid overlay saved to {output_path}")

# =========================
# TEST RUN
# =========================
if __name__ == "__main__":
    print("[TEST] Grid Generator")

    test_image = "ai_model/inference/test.png"
    test_coordinates = [(120, 80), (200, 140), (50, 220)]

    generate_grid_visual(
        image_path=test_image,
        spray_coordinates=test_coordinates
    )

    print("[DONE] Grid visualization complete")
