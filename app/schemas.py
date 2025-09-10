from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    full_name: str | None = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

class FitnessClassCreate(BaseModel):
    name: str
    dateTime: datetime
    instructor: str
    availableSlots: int

class FitnessClass(BaseModel):
    id: int
    name: str
    dateTime: datetime
    instructor: str
    availableSlots: int

    class Config:
        from_attributes = True

class BookingCreate(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class Booking(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: EmailStr

    class Config:
        from_attributes = True