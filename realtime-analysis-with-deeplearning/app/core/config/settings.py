from os.path import abspath, dirname, join
from os import environ
import dotenv


class Settings: 

    dotenv.load_dotenv(dotenv.find_dotenv())

    ROOT_PATH = dirname(dirname(dirname(abspath(__file__))))
    
    CAM_IP = environ.get('CAM_IP')
    CAM_PORT = environ.get('CAM_PORT')
    CAM_USER = environ.get('CAM_USER')
    CAM_PASS = environ.get('CAM_PASS')
    CAM_CHANNEL = environ.get('CAM_CHANNEL')

    MODEL_PATH = join(ROOT_PATH, "model", "mobilenet_ssd.pb")
    MODEL_THRESHOLD = 0.7


    DB_TYPE = environ.get('DB_TYPE')
    DB_USER = environ.get('DB_USER')
    DB_PASSWORD = environ.get('DB_PASSWORD')
    DB_CLUSTER = environ.get('DB_CLUSTER')
    DB_NAME = environ.get('DB_NAME')