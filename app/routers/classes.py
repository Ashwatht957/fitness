from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import get_db
from app.routers.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.FitnessClass)
def create_class(class_in: schemas.FitnessClassCreate, db: Session = Depends(get_db), user: schemas.User = Depends(get_current_user)):
    fitness_class = models.FitnessClass(**class_in.dict())
    db.add(fitness_class)
    db.commit()
    db.refresh(fitness_class)
    return fitness_class

@router.get("/", response_model=list[schemas.FitnessClass])
def get_classes(db: Session = Depends(get_db)):
    return db.query(models.FitnessClass).all()