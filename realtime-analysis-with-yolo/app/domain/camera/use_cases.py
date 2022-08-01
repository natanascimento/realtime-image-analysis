from app.infrastructure.repositories import CameraCapture, ObjectDetector


class CreateObjectDetection:
  
    def __init__(self, location: str) -> None:
        self._repository = CameraCapture(detector=ObjectDetector(location=location))
        
    def execute(self):
        return self._repository.run()
