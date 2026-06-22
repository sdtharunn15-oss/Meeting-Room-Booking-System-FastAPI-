from pydantic import BaseModel

class ParticipantCreate(BaseModel):
    employee_id: int