from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.participant import Participant
from app.models.booking import Booking
from app.models.employee import Employee
from app.models.room import Room
from app.schemas.participant import ParticipantCreate

router = APIRouter(
    prefix="/bookings",
    tags=["Participants"]
)


@router.post("/{booking_id}/participants")
def add_participant(
    booking_id: int,
    participant: ParticipantCreate,
    db: Session = Depends(get_db)
):

    booking = db.query(Booking).filter(
        Booking.id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    employee = db.query(Employee).filter(
        Employee.id == participant.employee_id
    ).first()

    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    room = db.query(Room).filter(
        Room.id == booking.room_id
    ).first()

    participant_count = db.query(Participant).filter(
        Participant.booking_id == booking_id
    ).count()

    if participant_count >= room.capacity:
        raise HTTPException(
            status_code=400,
            detail="Room capacity exceeded"
        )

    new_participant = Participant(
        booking_id=booking_id,
        employee_id=participant.employee_id
    )

    db.add(new_participant)
    db.commit()
    db.refresh(new_participant)

    return new_participant


@router.get("/{booking_id}/participants")
def get_participants(
    booking_id: int,
    db: Session = Depends(get_db)
):
    return db.query(Participant).filter(
        Participant.booking_id == booking_id
    ).all()


