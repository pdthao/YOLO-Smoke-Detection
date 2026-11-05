from ultralytics import YOLO
# https://learnopencv.com/train-yolov8-on-custom-dataset/
 
def main(): 
    # Load the model.
    model = YOLO('yolov8s.pt')
 
    # Training.
    # results = model.train(data='data_custom.yaml', imgsz=1280, epochs=30000, batch=1, name='yolov8m', patience=0)
    # model.train(data='data_custom.yaml', imgsz=1312, epochs=3000000, batch=1, name='yolov8m', patience=0)
    model.train(data='data_custom.yaml', imgsz=640, epochs=300000, batch=1, name='yolov8s', patience=0)

if __name__ == "__main__":
    main()