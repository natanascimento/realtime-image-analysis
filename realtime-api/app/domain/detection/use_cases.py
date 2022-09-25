from fastapi import Depends
from app.infrastructure.repositories.detection import PeopleDetection
from app.routes.detection.contracts import PeopleDetectionRequest


class CreatePeopleDetection:

    def __init__(self, repository: PeopleDetection = Depends()):
        self.__repository = repository

    def execute(self, request: PeopleDetectionRequest):
        return self.__repository.create(request)


class GetPeopleDetections:

    def __init__(self, repository: PeopleDetection = Depends()):
        self.__repository = repository

    def execute(self):
        return self.__repository.get()


class GetLastPeopleDetection:

    def __init__(self, repository: PeopleDetection = Depends()):
        self.__repository = repository

    def execute(self):
        return self.__repository.get_last_detection()
