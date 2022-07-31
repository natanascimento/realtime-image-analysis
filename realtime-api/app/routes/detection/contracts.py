from pydantic import BaseModel, Field


class DetectionConnectionRequest(BaseModel):
    location: str = Field(min_length=1, max_length=249)
    quantity: int
    detected_at: str = Field(min_length=1)

    class Config:
        allow_mutation = False
        schema_extra = {
            "example": {
                "location": "location-X",
                "quantity": 1,
                "detected_at": "30-07-2022 11:30:00.0011",
            }
        }
