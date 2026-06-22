from fastapi import FastAPI

from app.database import Base, engine

from app.models.employee import Employee
from app.models.room import Room
from app.models.booking import Booking
from app.models.participant import Participant
from app.routers import rooms
from app.routers import employees
from app.routers import bookings
from app.routers import participants
from app.routers import auth
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(employees.router)
app.include_router(rooms.router)
app.include_router(bookings.router)
app.include_router(participants.router)
app.include_router(auth.router)



@app.get("/")
def root():
    return {"message": "Meeting Room Booking API"}