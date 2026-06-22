# Meeting Room Booking System

## Project Description

Meeting Room Booking System is a FastAPI-based application used to manage employees, meeting rooms, bookings, and participants.

The system provides JWT authentication, room availability checking, booking conflict validation, pagination, background tasks, email reminders, database migrations, and API testing.

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Alembic
* JWT Authentication
* Pytest
* Docker

---

## Project Structure

```
meeting_room_booking/

app/
 ├── models/
 ├── schemas/
 ├── routers/
 ├── services/
 ├── utils/
 ├── database.py
 └── main.py

alembic/
tests/

Dockerfile
requirements.txt
README.md
```

---

## Installation

Clone the repository:

```
git clone <repository-url>
```

Move into project:

```
cd meeting_room_booking
```

Create virtual environment:

```
python -m venv venv
```

Activate:

Windows:

```
venv\Scripts\activate
```

Install requirements:

```
pip install -r requirements.txt
```

---

## Run Application

Start FastAPI server:

```
uvicorn app.main:app --reload
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# Authentication

Login API:

```
POST /auth/login
```

Example:

```
{
 "email":"admin123@gmail.com",
 "password":"admin123"
}
```

After login use the generated JWT token in Swagger Authorize.

---

# API Endpoints

## Employees

```
POST   /employees/
GET    /employees/
GET    /employees/{employee_id}
PUT    /employees/{employee_id}
```

## Rooms

```
POST   /rooms/
GET    /rooms/
GET    /rooms/{room_id}
PUT    /rooms/{room_id}
```

## Bookings

```
POST    /bookings/
GET     /bookings/
GET     /bookings/{booking_id}
DELETE  /bookings/{booking_id}
```

## Participants

```
POST /bookings/{booking_id}/participants

GET /bookings/{booking_id}/participants
```

---

# Features

## Employee Management

* Create employees
* Update employee details
* View employees

## Room Management

* Create meeting rooms
* Manage room details

## Booking System

* Create bookings
* Prevent room time conflicts
* Prevent employee meeting conflicts

## Authentication

* JWT based login
* Password hashing

## Bonus Features

* Pagination
* Background email reminders
* Alembic migrations
* Pytest API testing
* Docker support

---

# Testing

Run tests:

```
pytest
```

---

# Database

Database:

```
SQLite
```

Migration:

Create migration:

```
alembic revision --autogenerate -m "message"
```

Apply migration:

```
alembic upgrade head
```

---

# Docker

Build:

```
docker build -t meeting-room-booking .
```

Run:

```
docker run -p 8000:8000 meeting-room-booking
```
