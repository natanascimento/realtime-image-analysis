from os.path import abspath, dirname
from os import environ
import dotenv


class Settings: 

    dotenv.load_dotenv(dotenv.find_dotenv())

    ROOT_PATH = dirname(dirname(abspath(__file__)))
    
    CAM_IP = environ.get('CAM_IP')
    CAM_PORT = environ.get('CAM_PORT')
    CAM_USER = environ.get('CAM_USER')
    CAM_PASS = environ.get('CAM_PASS')
    CAM_CHANNEL = environ.get('CAM_CHANNEL')