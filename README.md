# Fitness Booking API 🚀

A simple **Booking API** for a fictional **fitness studio**, built using **Python + FastAPI**.  
Users can sign up, log in, view classes, create new classes, and book fitness classes.

---

## 📌 Features

- User authentication (Sign Up & Login) using JWT tokens
- Create and list fitness classes
- Book fitness classes with slot validation
- View your own bookings
- Protected endpoints: only authenticated users can create classes or make bookings
- SQLite database for development (can be swapped for PostgreSQL or others)

---

## 🛠 Tech Stack

- **Language:** Python 3.11+
- **Framework:** FastAPI
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Authentication:** JWT Token-based
- **Docs:** Swagger UI (`/docs`)  

---

## 📁 Project Structure
fitness-booking-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                  # Entry point for the FastAPI app
│   ├── models.py                # SQLAlchemy models (User, FitnessClass, Booking)
│   ├── schemas.py               # Pydantic schemas for request/response validation
│   ├── database.py              # Database connection and session management
│   └── routers/
│       ├── auth.py              # Signup/login routes and JWT authentication
│       ├── users.py             # User-related routes (optional additional endpoints)
│       ├── classes.py           # CRUD operations for fitness classes
│       └── bookings.py          # Booking operations (create/view bookings)
├── requirements.txt             # Python dependencies
└── README.md                     # Project documentation


