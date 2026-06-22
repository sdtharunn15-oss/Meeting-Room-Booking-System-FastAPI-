from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from datetime import date, timedelta

from app.utils.email import send_email
from app.database import get_db
from app.models.booking import Booking
from app.models.employee import Employee
from app.models.room import Room
from app.schemas.booking import BookingCreate


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.post("/")
def create_booking(
    booking: BookingCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):

    if booking.end_time <= booking.start_time:
        raise HTTPException(
            status_code=400,
            detail="End time must be greater than start time"
        )


    employee = db.query(Employee).filter(
        Employee.id == booking.employee_id
    ).first()


    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )


    room = db.query(Room).filter(
        Room.id == booking.room_id
    ).first()


    if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )


    room_conflict = db.query(Booking).filter(
        Booking.room_id == booking.room_id,
        Booking.start_time < booking.end_time,
        Booking.end_time > booking.start_time
    ).first()


    if room_conflict:
        raise HTTPException(
            status_code=400,
            detail="Room already booked for this time slot"
        )


    employee_conflict = db.query(Booking).filter(
        Booking.employee_id == booking.employee_id,
        Booking.start_time < booking.end_time,
        Booking.end_time > booking.start_time
    ).first()


    if employee_conflict:
        raise HTTPException(
            status_code=400,
            detail="Employee already has another meeting"
        )


    new_booking = Booking(**booking.dict())


    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)


    # Email reminder background task
    background_tasks.add_task(
        send_email,
        employee.email,
        "Meeting Reminder",
        f"Your meeting is scheduled from {booking.start_time} to {booking.end_time}"
    )


    return new_booking



@router.get("/")
def get_bookings(
    booking_date: date = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Booking)


    if booking_date:

        next_day = booking_date + timedelta(days=1)

        query = query.filter(
            Booking.start_time >= booking_date,
            Booking.start_time < next_day
        )


    return query.offset(skip).limit(limit).all()



@router.get("/{booking_id}")
def get_booking(
    booking_id: int,
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


    return booking



@router.delete("/{booking_id}")
def delete_booking(
    booking_id: int,
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


    db.delete(booking)
    db.commit()


    return {
        "message": "Booking deleted successfully"
    }