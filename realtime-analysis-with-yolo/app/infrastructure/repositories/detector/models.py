from cv2 import dnn

from app.core.config import YoloSettings

class YoloModelLoader:

    @staticmethod
    def load(type:str):
        yolo_settings = YoloSettings(type=type)
        
        return dnn.readNet(yolo_settings.weights, 
                           yolo_settings.cfg)