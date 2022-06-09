import warnings
warnings.filterwarnings("ignore")

import cv2

from app.core.config import settings
from app.infrastructure.repositories.detector.models import CascadeDetectorModel


class HaarcascadeDetector(CascadeDetectorModel):

    def __init__(self) -> None:
        super().__init__()
        self.__cascade_full_body = self.load(settings.HAARCASCADE_FULL_BODY)
        self.__cascade_half_body = self.load(settings.HAARCASCADE_HALF_BODY)

    def run(self, source_image):
        gray_image = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)

        full_body = self.__cascade_full_body.detectMultiScale(gray_image, 1.1, 3)
        half_body = self.__cascade_half_body.detectMultiScale(gray_image, 1.3, 5)

        for (x, y, w, h) in full_body:
            cv2.rectangle(source_image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Haarcascade Detector", source_image)

    @staticmethod
    def stop():
        cv2.destroyAllWindows()
