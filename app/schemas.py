from pydantic import BaseModel

class StudentCreate(BaseModel):
    roll_no: str
    name: str
    branch: str
    semester: int

class StudentResponse(StudentCreate):
    id: int

    class Config:
        orm_mode = True
