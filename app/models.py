from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    bookings = relationship("Booking", back_populates="user")  # <-- Add this line
    

# ...existing User model...

class FitnessClass(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    dateTime = Column(DateTime, nullable=False)
    instructor = Column(String, nullable=False)
    availableSlots = Column(Integer, nullable=False)
    bookings = relationship("Booking", back_populates="fitness_class")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    client_name = Column(String, nullable=False)
    client_email = Column(String, nullable=False)
    fitness_class = relationship("FitnessClass", back_populates="bookings")
    user = relationship("User", back_populates="bookings")
