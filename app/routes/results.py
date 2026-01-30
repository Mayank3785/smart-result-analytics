from fastapi import APIRouter

router = APIRouter(prefix="/results", tags=["Results"])

@router.post("/upload")
def upload_results():
    return {"message": "CSV upload coming next"}
