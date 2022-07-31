from os.path import abspath, dirname
from os import environ
import dotenv


class Settings:

    dotenv.load_dotenv(dotenv.find_dotenv())

    APP_NAME = "Real time object detection API"
    
    ROOT_PATH = dirname(dirname(dirname(dirname(abspath(__file__)))))
    
    PROJECT_PATH = dirname(dirname(dirname(abspath(__file__))))

    DB_TYPE = environ.get('DB_TYPE')
    DB_USER = environ.get('DB_USER')
    DB_PASSWORD = environ.get('DB_PASSWORD')
    DB_CLUSTER = environ.get('DB_CLUSTER')
    DB_NAME = environ.get('DB_NAME')
