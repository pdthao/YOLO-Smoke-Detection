from ultralytics import YOLO
import multiprocessing

def main():
    # Load the last checkpoint or best model
    model = YOLO("C:/waferData/smoke/runs/detect/yolov8s/weights/last.pt")

    # Resume training using your dataset configuration
    model.train(data="data_custom.yaml", epochs=30000, imgsz=640, batch=4, resume=True)

if __name__ == "__main__":
    multiprocessing.freeze_support()  # This is optional, useful if freezing your code into an executable
    main()