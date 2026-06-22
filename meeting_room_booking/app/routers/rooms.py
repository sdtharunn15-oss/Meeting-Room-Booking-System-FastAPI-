from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from app.database import get_db
from app.dependencies import admin_required

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

SECRET_KEY = "meetingroomsecret"
ALGORITHM = "HS256"

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

from app.models.room import Room
from app.schemas.room import RoomCreate

router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)


@router.post("/")
def create_room(
    room: RoomCreate,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):
    

 @router.get("/")
 def get_rooms(
    capacity: int = None,
    db: Session = Depends(get_db)
):
    query = db.query(Room)

    if capacity:
        query = query.filter(
            Room.capacity >= capacity
        )

    return query.all()


@router.get("/{room_id}")
def get_room(room_id: int, db: Session = Depends(get_db)):
    return db.query(Room).filter(
        Room.id == room_id
    ).first()


@router.put("/{room_id}")
def update_room(
    room_id: int,
    room: RoomCreate,
    db: Session = Depends(get_db),
    user=Depends(admin_required)
):
    existing_room = db.query(Room).filter(
        Room.id == room_id
    ).first()

    if not existing_room:
        return {"message": "Room not found"}

    existing_room.room_name = room.room_name
    existing_room.capacity = room.capacity
    existing_room.location = room.location
    existing_room.is_available = room.is_available

    db.commit()
    db.refresh(existing_room)

    return existing_room


@router.get("/")
def get_rooms(
    capacity: int = None,
    db: Session = Depends(get_db)
):
    query = db.query(Room)

    if capacity:
        query = query.filter(
            Room.capacity >= capacity
        )

    return query.all()