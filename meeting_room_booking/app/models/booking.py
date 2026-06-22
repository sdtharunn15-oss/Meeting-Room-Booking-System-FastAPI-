from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.database import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))
    meeting_title = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)