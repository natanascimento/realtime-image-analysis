from app.infrastructure.repositories.camera.connection import CameraConnection
from app.infrastructure.repositories.camera.detector import CameraDetector
from app.infrastructure.repositories.camera.capture import CameraCapture

class CreateCameraAnalysis:

    def __init__(self) -> None:
        self._repository = CameraCapture(detector=CameraDetector(),
                                         connection=CameraConnection())

    def execute(self):
        return self._repository.run()