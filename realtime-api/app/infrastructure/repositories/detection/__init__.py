from app.domain.detection.entities import DetectionCreationResponse, LastDetectionResponse, DetectionsResponse
from app.infrastructure.repositories.database import DatabaseConnection, DataProducer, DataConsumer


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

    @staticmethod
    def get_last_detection():
        try:
            consumer = DataConsumer(connection=DatabaseConnection()).consume_last_insert()
            return LastDetectionResponse(location=consumer.get("location"),
                                         quantity=consumer.get("quantity"),
                                         created_at=consumer.get("detected_at"))
        except Exception as exception:
            return f"[ERROR] {exception}"

    @staticmethod
    def get():
        try:
            return DetectionsResponse(response=DataConsumer(connection=DatabaseConnection()).consume())
        except Exception as exception:
            return f"[ERROR] {exception}"
