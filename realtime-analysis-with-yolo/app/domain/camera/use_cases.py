from app.infrastructure.repositories import CameraCapture, ObjectDetector


class CreateObjectDetection:
  
    def __init__(self) -> None:
        self._repository = CameraCapture(detector=ObjectDetector())
        
    def execute(self):
        return self._repository.run()