from pydantic import BaseModel

class JobCreate(BaseModel):
    pass  # no input needed for now

class JobResponse(BaseModel):
    id: int
    status: str
    result: str | None

    class Config:
        from_attributes = True