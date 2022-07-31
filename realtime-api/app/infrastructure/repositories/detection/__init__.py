from app.domain.detection.entities import DetectionCreationResponse
from app.infrastructure.repositories.database import DatabaseConnection, DataProducer


class PeopleDetection:

    @staticmethod
    def create(request):

        body = {"location": request.location,
                "quantity": request.quantity,
                "detected_at": request.detected_at}

        try:
            DataProducer(connection=DatabaseConnection()).produce(body=body)
            return DetectionCreationResponse(location=request.location)
        except Exception as exception:
            return f"[ERROR] {exception}"
