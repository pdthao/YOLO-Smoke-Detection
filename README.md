# YOLO Smoke Detection

**Custom object detection training for smoke monitoring using Python and Ultralytics YOLO.**

This project explores training a YOLO model to recognize smoke in images. The source includes scripts for dataset preparation, converting annotations, training a custom detector, and resuming training from a checkpoint.

> **Repository scope:** This is a source-code portfolio version of the project. The original dataset, trained weights, and generated training runs are not included. Training results and accuracy metrics have not been independently verified here.

## Project overview

| Item | Details |
| --- | --- |
| Task | Smoke object detection |
| Language | Python |
| Framework | Ultralytics YOLO (YOLOv8s in the supplied training script) |
| Annotation formats | Pascal VOC XML → YOLO TXT |
| Classes | `smoke` (1 class) |
| Development environment | Python; Windows batch launchers are also provided |

## Main functionality

- **Dataset preparation:** Create a YOLO dataset configuration from a list of object classes.
- **Annotation conversion:** Convert Pascal VOC bounding boxes to normalized YOLO labels (`class x_center y_center width height`).
- **Custom model training:** Fine-tune YOLOv8s on an annotated smoke dataset.
- **Resume training:** Continue from an existing `last.pt` checkpoint.
- **Training artifacts:** Ultralytics can generate checkpoints and training logs in `runs/` during execution; these outputs are not committed to this repository.

## Repository structure

```text
YOLO-Smoke-Detection/
├── create_data_custom.py       # Generate a dataset YAML file
├── create_txt.py               # Convert XML annotations to YOLO TXT
├── data_custom.yaml            # One-class smoke dataset config
├── train.py                    # Start YOLOv8s training
├── train_resume.py             # Resume training from a checkpoint
├── run.bat                     # Windows launcher for training
├── run_resume.bat              # Windows launcher for resume
├── size.txt                    # Original project note
├── labelApp/
│   └── data/
│       └── predefined_classes.txt  # Smoke class name
├── .gitignore
└── README.md
```

## Requirements

- Python 3 and a compatible environment for Ultralytics YOLO
- Python packages: `ultralytics`, `Pillow`, `PyYAML`
- A labeled smoke dataset
- A YOLOv8s pretrained weight file (such as `yolov8s.pt`) or an accessible compatible model
- For resuming: an existing training checkpoint (`last.pt`)

Install Python dependencies:

```bash
python -m pip install ultralytics pillow pyyaml
```

## How to run

### 1. Prepare the dataset

The original archive contains images and YOLO text labels under `label/train` and `label/val`, but these are **not included** in this source-only repository. Provide a dataset you are authorized to use and arrange it to match the requirements of your installed Ultralytics version.

For example, a conventional layout is:

```text
dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

If starting from Pascal VOC XML annotations, adapt the paths in `create_txt.py`, then run it to produce YOLO-format `.txt` labels. Review the converted bounding boxes before training.

### 2. Update dataset paths

Edit `data_custom.yaml` for your machine, for example:

```yaml
path: ./dataset
train: images/train
val: images/val
nc: 1
names:
  - smoke
```

**Note:** The checked-in YAML currently uses a local `C:/waferData/smoke/...` path. The preparation scripts also contain `D:/waferData/degas/...` paths inherited from another dataset. Replace those hard-coded paths and verify that class names and labels refer to the smoke dataset before running them.

### 3. Start training

```bash
python train.py
```

The supplied script loads `yolov8s.pt` and sets `imgsz=640`, `batch=1`, and a very high maximum epoch count (`300000`) with `patience=0`. **Review and reduce these settings as needed** before launching a long training run. Training requires the corresponding model weights and dataset to be available.

### 4. Resume training (optional)

```bash
python train_resume.py
```

Update the hard-coded checkpoint path in `train_resume.py` first. The supplied script points to `C:/waferData/smoke/runs/detect/yolov8s/weights/last.pt`.

The supplied Windows `run.bat` and `run_resume.bat` use an absolute Anaconda Python path; update that path or run the Python commands directly.

## Important notes

- GitHub displays the code but does **not** run YOLO training in the browser.
- The project is not a turnkey downloadable smoke detector: dataset files, pretrained weights, and compatible local paths are required.
- The archive includes generated outputs and weights, but they are excluded from this public source snapshot to keep it lightweight.
- Do not upload captured images or third-party model weights without verifying permissions and applicable licenses.
- No detection accuracy, mAP, precision, recall, or deployed real-time monitoring performance is claimed without recorded evaluation results.

## Future improvements

- Replace absolute paths with configurable project-relative paths.
- Add a documented inference script for smoke detection on images or video.
- Include reproducible training settings and evaluation results.
- Provide example predictions using appropriately licensed sample images.

## Project type

Computer vision / custom object detection training / Python machine learning project.
