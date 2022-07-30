from os.path import abspath, dirname


class Settings: 

    APP_NAME = "Real time object detection API"
    
    ROOT_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
    
    PROJECT_PATH = dirname(dirname(dirname(abspath(__file__))))

