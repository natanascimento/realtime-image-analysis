from app.routes.factory import RouterFactory
from app.routes.detection.contracts import PeopleDetectionRequest
from app.domain.detection.use_cases import CreatePeopleDetection, GetPeopleDetections, GetLastPeopleDetection
from fastapi import Depends

router = RouterFactory(version="v1", tag="detection").get


@router.post("/data/detection",
             response_description="Create a people detection",
             status_code=201)
def create_detection_data(detection_create_request: PeopleDetectionRequest,
                          detection_create: CreatePeopleDetection = Depends()):
    return detection_create.execute(detection_create_request).message


@router.get("/data/last_detection",
            response_description="Get last people detection",
            status_code=200)
def get_last_detection_data(last_detection: GetLastPeopleDetection = Depends()):
    return last_detection.execute().message


@router.get("/data/detections",
            response_description="Get people detections",
            status_code=200)
def get_detections_data(people_detections: GetPeopleDetections = Depends()):
    return people_detections.execute().response
