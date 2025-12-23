
This approach allows:
- Persistent storage
- Easy dataset updates
- Team collaboration

---

## ⚙️ Training Workflow

1. Open Google Colab notebook
2. Enable GPU (Runtime → Change runtime type → GPU)
3. Mount Google Drive
4. Install required libraries
5. Train YOLO model
6. Save trained weights to Drive
7. Download or deploy model

---

## 🧪 Sample Training Commands

```python
!pip install ultralytics
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
model.train(
    data="/content/drive/MyDrive/FarmX/training_dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16
)
