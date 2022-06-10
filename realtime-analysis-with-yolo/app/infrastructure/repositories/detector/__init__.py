import warnings
warnings.filterwarnings("ignore")

import cv2
import numpy as np

from app.core.config import settings
from app.infrastructure.repositories.detector.models import YoloModelLoader


class ObjectDetector(YoloModelLoader):

    def __init__(self) -> None:
        super().__init__()
        self.__net = self.load(type="accuracy")
        self.__font = cv2.FONT_HERSHEY_PLAIN
        self.__colors = np.random.uniform(0, 255, size=(100, 3))
        self.__classes = self.__get_classes()
        
    @staticmethod
    def __get_classes():
        classes = []
        
        with open(settings.COCO_CLASS_NAMES, "r") as class_names:
            classes = class_names.read().splitlines()
        
        return classes

    def run(self, source_image):

        height, width, _ = source_image.shape
        
        blob = cv2.dnn.blobFromImage(source_image, 1/255, (416,416), (0,0,0), swapRB=True, crop=False)
        
        self.__net.setInput(blob)
        
        output_layers_names = self.__net.getUnconnectedOutLayersNames()
        layers_outputs = self.__net.forward(output_layers_names)
        
        boxes = []
        confidences = []
        class_ids = []
        
        for output in layers_outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > float(settings.THRESHOLD_LEVEL):
                    center_x = int(detection[0]*width)
                    center_y = int(detection[1]*height)
                    w = int(detection[2]*width)
                    h = int(detection[3]*height)
                    
                    x = int(center_x - w/2)
                    y = int(center_y - h/2)
                    
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
                    
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)

        if len(indexes) > 0:
            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                label = str(self.__classes[class_ids[i]])
                confidence = str(round(confidences[i],2))
                color = self.__colors[i]
                cv2.rectangle(source_image, (x,y), (x+w, y+h), color, 2)
                cv2.putText(source_image, label + " " + confidence, (x, y+20), self.__font, 2, (255,255,255), 2)
      
        cv2.imshow(str(settings.APP_NAME), source_image)

    @staticmethod
    def stop():
        cv2.destroyAllWindows()
