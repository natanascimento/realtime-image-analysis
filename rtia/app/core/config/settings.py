from os.path import abspath, dirname
from os import environ
from dotenv import load_dotenv, find_dotenv


class Settings: 

    def __init__(self) -> None:
        load_dotenv(find_dotenv())

    ROOT_PATH = dirname(dirname(abspath(__file__)))
    
    CAM_IP = environ['CAM_IP'].get()
    CAM_PORT = environ['CAM_PORT'].get()
    CAM_USER = environ['CAM_USER'].get()
    CAM_PASS = environ['CAM_PASS'].get()
    CAM_CHANNEL = environ['CAM_CHANNEL'].get()

    def get_rtsp_url(self) -> str:
        return f"rtsp://{self.CAM_IP}:{self.CAM_PORT}/user={self.CAM_USER}&password={self.CAM_PASS}&channel={self.CAM_CHANNEL}&stream=0.sdp?"