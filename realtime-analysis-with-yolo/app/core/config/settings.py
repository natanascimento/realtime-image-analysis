from os.path import abspath, dirname, join


class Settings: 

    APP_NAME = "Object Detector"
    
    ROOT_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
    
    PROJECT_PATH = dirname(dirname(dirname(abspath(__file__))))
    
    MODELS_PATH = join(PROJECT_PATH, "models")
    
    IMAGES_PATH = join(PROJECT_PATH, "images")
    
    TEST_IMAGE = join(IMAGES_PATH, "peoples-on-street.jpg")
    
    YOLOV3_PATH = join(MODELS_PATH, "yolov3")
    
    COCO_CLASS_NAMES = join(YOLOV3_PATH, "coco.names")

    THRESHOLD_LEVEL = 0.3
    

class YoloSettings(Settings):

    def __init__(self, type:str) -> None:
        super().__init__()
        if type == "performance":
            self.__YOLOV3_PATH = join(self.YOLOV3_PATH, "yolov3-tiny")
        if type == "accuracy":
            self.__YOLOV3_PATH = join(self.YOLOV3_PATH, "yolov3-608")
        
    @property 
    def weights(self):
        return join(self.__YOLOV3_PATH, "yolov3.weights")
    
    @property 
    def cfg(self):
        return join(self.__YOLOV3_PATH, "yolov3.cfg")
