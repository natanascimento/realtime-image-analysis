from typing import List, Dict
from dataclasses import dataclass, field


@dataclass
class DetectionCreationResponse:
    location: str
    message: str = field(init=False)

    def __post_init__(self):
        self.message = f"Event from {self.location} location was created"


@dataclass
class LastDetectionResponse:
    location: str
    quantity: str
    created_at: str
    message: dict = field(init=False)

    def __post_init__(self):
        self.message = {"location": self.location,
                        "quantity": self.quantity,
                        "created_at": self.created_at}


@dataclass
class DetectionsResponse:
    response: dict


@dataclass
class People:
    location: str
    quantity: str
    created_at: str
