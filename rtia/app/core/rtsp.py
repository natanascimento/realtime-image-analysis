from app.core.config import settings

class RTSP:

    @staticmethod
    def get_rtsp_url() -> str:
        return f"rtsp://{settings.CAM_IP}:{settings.CAM_PORT}/user={settings.CAM_USER}&password={settings.CAM_PASS}&channel={settings.CAM_CHANNEL}&stream=0.sdp?"
