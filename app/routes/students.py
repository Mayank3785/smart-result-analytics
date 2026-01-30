from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Student
from app.schemas import StudentCreate

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(
        roll_no=student.roll_no,
        name=student.name,
        branch=student.branch,
        semester=student.semester
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"message": "Student added successfully", "id": new_student.id}
