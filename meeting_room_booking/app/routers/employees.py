from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate
from app.database import get_db

from app.utils.jwt import hash_password
router = APIRouter(prefix="/employees", tags=["Employees"])


@router.post("/")
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    employee_data = employee.dict()

    employee_data["password"] = hash_password(
        employee.password
    )

    new_employee = Employee(**employee_data)

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee

@router.get("/")
def get_employees(
    department: str = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(Employee)

    if department:
        query = query.filter(
            Employee.department == department
        )

    return query.offset(skip).limit(limit).all()
@router.get("/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    return db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

@router.put("/{employee_id}")
def update_employee(
    employee_id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    emp = db.query(Employee).filter(
        Employee.id == employee_id
    ).first()

    if not emp:
        return {"message": "Employee not found"}

    emp.name = employee.name
    emp.email = employee.email
    emp.department = employee.department
    emp.role = employee.role

    db.commit()
    db.refresh(emp)

    return emp


