from pydantic import BaseModel

class CaregiverCreate(BaseModel):
    name: str
    email: str
    phone: str
    location: str
    role: str

class CaregiverResponse(CaregiverCreate):
    id: int

    class Config:
        from_attributes = True