from pydantic import BaseModel, Field


class DetectionConnectionRequest(BaseModel):
    quantity: str = Field(min_length=1, max_length=249)

    class Config:
        allow_mutation = False
        schema_extra = {
            "example": {
                "table_name": "table-X",
            }
        }