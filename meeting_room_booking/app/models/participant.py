from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))