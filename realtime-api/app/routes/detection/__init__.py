from app.routes.factory import RouterFactory
from app.routes.detection.contracts import DetectionConnectionRequest
from app.domain.detection.use_cases import CreatePeopleDetection
from fastapi import Depends

router = RouterFactory(version="v1", tag="detection").get


@router.post("/data/detection",
             response_description="Create a people detection",
             status_code=201)
def create_topic(sink_create_request: DetectionConnectionRequest, sink_create: CreatePeopleDetection = Depends()):
    return sink_create.execute(sink_create_request).message
