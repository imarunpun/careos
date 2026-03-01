from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.caregiver_model import Caregiver
from app.schemas.caregiver import CaregiverCreate, CaregiverResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/caregivers", response_model=CaregiverResponse)
def register_caregiver(
    caregiver: CaregiverCreate,
    db: Session = Depends(get_db)
):
    new_caregiver = Caregiver(**caregiver.dict())
    db.add(new_caregiver)
    db.commit()
    db.refresh(new_caregiver)

    return new_caregiver


@router.get("/caregivers", response_model=list[CaregiverResponse])
def get_caregivers(db: Session = Depends(get_db)):
    return db.query(Caregiver).all()