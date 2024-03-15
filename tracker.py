from ultralytics import YOLO
import threading
import Choosers
import math
import cv2

def clamp(value, min, max):
    if value < min: return min
    elif value > max: return max
    else: return value

def findKey(value: int, dict: dict):
    keys: list = list(dict.keys())
    vals: list = list(dict.values())
    pos = vals.index(value)
    return keys[pos]

def runTrackerInThread(source: int, model: YOLO, fps: int, confidence: float):
    video = cv2.VideoCapture(source)
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 1920) 
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    video.set(cv2.CAP_PROP_FPS, fps)

    while True:
        ret, frame = video.read()

        if not ret:
            break

        results = model.track(frame, persist=True, conf=confidence)
        res_plotted = results[0].plot()
        cv2.namedWindow("[LIVE] Robot & Note AI Detection", cv2.WINDOW_NORMAL)
        cv2.imshow("[LIVE] Robot & Note AI Detection", res_plotted)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    video.release()

source :int = Choosers.intChooser('Enter an integer that represents the source of the model\'s input: ')
modelOptions: dict = {
    'nano_robo_v1': 0,
    'medium_robo_v3': 1
}
modelChoice :int = Choosers.optionChooser('Choose a YOLOv8 model type: ', modelOptions)
fps :int = Choosers.intChooser('Enter an FPS to run the tracker on (can be bottle necked by the model speed): ')
conf :float = clamp(Choosers.floatChooser('Enter a confidence level up to which a model\'s predictions should be thrown out: '), 0.0, 1.0)

print(f'\nSource: {source}\nModel: {findKey(modelChoice, modelOptions)}.pt\nFPS: {fps}\nConfidence: {conf}\n\nPress \'q\' on your keyboard to stop the model predictions.')

model = YOLO(f'{findKey(modelChoice, modelOptions)}.pt')
tracker_thread1 = threading.Thread(target=runTrackerInThread, args=(source, model, fps, conf), daemon=True)
tracker_thread1.start()
tracker_thread1.join()
cv2.destroyAllWindows()
    
    