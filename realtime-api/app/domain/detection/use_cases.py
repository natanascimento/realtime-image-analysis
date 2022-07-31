from fastapi import Depends
from app.infrastructure.repositories.detection import PeopleDetection
from app.routes.detection.contracts import DetectionConnectionRequest


class CreatePeopleDetection:

    def __init__(self, repository: PeopleDetection = Depends()):
        self.__repository = repository

    def execute(self, request: DetectionConnectionRequest):
        return self.__repository.create(request)