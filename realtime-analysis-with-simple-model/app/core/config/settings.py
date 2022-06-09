from os.path import abspath, dirname, join


class Settings: 

    ROOT_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
    
    PROJECT_PATH = dirname(dirname(dirname(abspath(__file__))))
    
    MODELS_PATH = join(PROJECT_PATH, "models")
    
    HAARCASCADE_FULL_BODY = join(MODELS_PATH, "haarcascade_fullbody.xml")
    HAARCASCADE_HALF_BODY = join(MODELS_PATH, "haarcascade_upperbody.xml")
