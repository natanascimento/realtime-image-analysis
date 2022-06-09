import time
from datetime import datetime

from imutils import resize
from imutils.video import VideoStream
from imutils.video import FPS
import cv2
from tqdm import tqdm

from app.core.config import settings
from app.infrastructure.repositories.camera.connection import CameraConnection
from app.infrastructure.repositories.camera.detector import CameraDetector
from app.infrastructure.repositories.database import DatabaseConnection, DataProducer

class CameraCapture:

    def __init__(self, detector: CameraDetector, connection: CameraConnection) -> None:
        self.__cam_url = connection.get_connection_url(cam_ip=settings.CAM_IP, cam_port=settings.CAM_PORT, 
                                                            cam_user=settings.CAM_USER, cam_pass=settings.CAM_PASS, 
                                                            cam_channel=settings.CAM_CHANNEL, protocol="rtsp")
        self.__detector = detector
        self.__model_threshold = settings.MODEL_THRESHOLD

    @staticmethod
    def __loading():
        for i in tqdm(range(int(100)), ncols=100):
            time.sleep(0.02)


    def run(self):
        print("[INFO] Reading camera image")
        video = VideoStream(src=0).start()
        self.__loading()
        print("[INFO] Starting FPS Counter")
        fps = FPS().start()
        
        while True:
            frame = video.read()
            image = resize(frame, width=720)
            boxes, scores, classes, num = self.__detector.run(image=image)

            object_counted = 0
            for item in range(len(boxes)):
                if classes[item] == 1 and scores[item] > float(self.__model_threshold):
                    box = boxes[item]
                    
                    object_counted += 1

                    cv2.rectangle(image, (box[1],box[0]),
                                    (box[3],box[2]),(134,235,52),2)
                    cv2.rectangle(image, (box[1],box[0]-30),
                                    (box[1]+125,box[0]),(134,235,52), 
                                    thickness=cv2.FILLED)
                    cv2.putText(image, f' Person {round(scores[item], 2)}', 
                                    (box[1],box[0]-10), cv2.FONT_HERSHEY_SIMPLEX, 
                                    0.5, (225,255,225), 1)

            output = {"persons": object_counted, 
                    "elapsed_time": f"{self.__detector.elapsed_time:.2f}",
                    "created_at": datetime.now()}
            
            DataProducer(DatabaseConnection()).produce(body=output)
            
            print("[INFO] Elapsed Time: {} | Persons in the Image: {}".format(output["elapsed_time"],
                                                                              output["persons"]))

            cv2.imshow("Image Captured", image)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("[INFO] Detector was been paused!")
                break
                    
        fps.stop()
        cv2.destroyAllWindows()

        print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))