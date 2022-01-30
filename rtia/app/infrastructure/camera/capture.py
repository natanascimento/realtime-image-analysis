from app.core.rtsp import RTSP
from app.core.config import settings
import cv2

class CameraCapture:

    def __init__(self) -> None:
        self.__cam_url = RTSP.get_rtsp_url(cam_ip=settings.CAM_IP, cam_port=settings.CAM_PORT, 
                                           cam_user=settings.CAM_USER, cam_pass=settings.CAM_PASS, 
                                           cam_channel=settings.CAM_CHANNEL)

    def run(self):
        cap = cv2.VideoCapture(self.__cam_url)

        while(True):
            ret, frame = cap.read()

            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()