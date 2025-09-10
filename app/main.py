from fastapi import FastAPI
from app.routers import auth, users, classes, bookings
from app.database import engine
from app import models

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Fitness Booking API 🚀")

# Root route
@app.get("/")
def root():
    return {"message": "Welcome to the Fitness Booking"}

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(classes.router, prefix="/classes", tags=["classes"])
app.include_router(bookings.router, prefix="/book", tags=["bookings"])