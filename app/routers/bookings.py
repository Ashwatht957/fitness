from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import get_db
from app.routers.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.Booking, status_code=status.HTTP_201_CREATED)
def book_class(
    booking_in: schemas.BookingCreate,
    db: Session = Depends(get_db),
    user: schemas.User = Depends(get_current_user)
):
    # Check if the class exists
    fitness_class = db.query(models.FitnessClass).filter(models.FitnessClass.id == booking_in.class_id).first()
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Fitness class not found")

    # Check available slots
    if fitness_class.availableSlots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    # Create booking
    booking = models.Booking(
        class_id=booking_in.class_id,
        user_id=user.id,
        client_name=booking_in.client_name,
        client_email=booking_in.client_email
    )

    # Deduct slot
    fitness_class.availableSlots -= 1

    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

@router.get("/", response_model=list[schemas.Booking])
def get_bookings(db: Session = Depends(get_db), user: schemas.User = Depends(get_current_user)):
    bookings = db.query(models.Booking).filter(models.Booking.user_id == user.id).all()
    return bookings
