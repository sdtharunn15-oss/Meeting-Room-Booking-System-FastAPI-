from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    name: str
    email: str
    department: str
    role: str
    password: str


class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    department: str
    role: str

    class Config:
        from_attributes = True