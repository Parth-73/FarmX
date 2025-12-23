import cv2
import numpy as np
import os
from ultralytics import YOLO
from sprinkler.sprinkler_controller import send_to_sprinkler

# ==========================
# CONFIG
# ==========================
IMAGE_DIR = "images"          # Folder with input images
MODEL_PATH = "my_model.pt"
GRID_SIZE = 256
CONF_THRESHOLD = 0.58

OUTPUT_DIR = "output"
GRID_DIR = os.path.join(OUTPUT_DIR, "grids")
COORD_DIR = os.path.join(OUTPUT_DIR, "coords")

# ==========================
# SETUP
# ==========================
os.makedirs(GRID_DIR, exist_ok=True)
os.makedirs(COORD_DIR, exist_ok=True)

# ==========================
# LOAD MODEL
# ==========================
model = YOLO(MODEL_PATH)

# ==========================
# PROCESS EACH IMAGE
# ==========================
for img_name in os.listdir(IMAGE_DIR):

    if not img_name.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    image_path = os.path.join(IMAGE_DIR, img_name)
    image = cv2.imread(image_path)

    if image is None:
        print(f"❌ Skipping {img_name} (cannot read)")
        continue

    h, w, _ = image.shape
    cell_w = w // GRID_SIZE
    cell_h = h // GRID_SIZE

    print(f"\n🔍 Processing: {img_name}")

    # ==========================
    # YOLO INFERENCE
    # ==========================
    results = model(image, conf=CONF_THRESHOLD)[0]
    weed_boxes = []

    for box in results.boxes:
        cls = int(box.cls[0])
        if cls == 0:  # class 0 = weed
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            weed_boxes.append((x1, y1, x2, y2))

    # ==========================
    # GRID MAPPING
    # ==========================
    weed_cells = set()

    for (x1, y1, x2, y2) in weed_boxes:
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        gx = min(cx // cell_w, GRID_SIZE - 1)
        gy = min(cy // cell_h, GRID_SIZE - 1)

        weed_cells.add((gx, gy))

    # ==========================
    # GRID ON ORIGINAL IMAGE
    # ==========================
    grid_on_image = image.copy()

    for i in range(GRID_SIZE):
        cv2.line(grid_on_image, (i * cell_w, 0), (i * cell_w, h), (180, 180, 180), 1)
        cv2.line(grid_on_image, (0, i * cell_h), (w, i * cell_h), (180, 180, 180), 1)

    for (gx, gy) in weed_cells:
        x = gx * cell_w
        y = gy * cell_h
        cv2.rectangle(
            grid_on_image,
            (x, y),
            (x + cell_w, y + cell_h),
            (0, 0, 255),  # red cell border
            2
        )

    # ==========================
    # BLANK GRID WITH RED DOT + COORDS
    # ==========================
    blank_canvas = np.ones((h, w, 3), dtype=np.uint8) * 255

    # grid lines
    for i in range(GRID_SIZE):
        cv2.line(blank_canvas, (i * cell_w, 0), (i * cell_w, h), (200, 200, 200), 1)
        cv2.line(blank_canvas, (0, i * cell_h), (w, i * cell_h), (200, 200, 200), 1)

    # red dot + coordinate text
    for (gx, gy) in weed_cells:
        cx = gx * cell_w + cell_w // 2
        cy = gy * cell_h + cell_h // 2

        # red dot
        cv2.circle(blank_canvas, (cx, cy), 5, (0, 0, 255), -1)

        # coordinates text
        label = f"({gx},{gy})"
        cv2.putText(
            blank_canvas,
            label,
            (cx + 6, cy - 6),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.35,
            (0, 0, 0),
            1,
            cv2.LINE_AA
        )

    # ==========================
    # SAVE OUTPUTS
    # ==========================
    base_name = os.path.splitext(img_name)[0]

    grid_img_path = os.path.join(GRID_DIR, f"{base_name}_grid_on_image.png")
    grid_blank_path = os.path.join(GRID_DIR, f"{base_name}_grid_blank_with_coords.png")
    coord_path = os.path.join(COORD_DIR, f"{base_name}_coords.txt")

    cv2.imwrite(grid_img_path, grid_on_image)
    cv2.imwrite(grid_blank_path, blank_canvas)

    with open(coord_path, "w") as f:
        for gx, gy in sorted(weed_cells):
            f.write(f"{gx},{gy}\n")

    # ==========================
    # SEND TO SPRINKLER
    # ==========================
    send_to_sprinkler(sorted(weed_cells))

    print(f"✅ Done: {img_name}")
    print(f"   🖼 Grid on Image: {grid_img_path}")
    print(f"   🧾 Grid w/ Coords: {grid_blank_path}")
    print(f"   📍 Weed Cells: {len(weed_cells)}")

print("\n🚜 FarmX Batch Processing Complete")
