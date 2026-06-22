from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String)
    capacity = Column(Integer)
    location = Column(String)
    is_available = Column(Boolean, default=True)