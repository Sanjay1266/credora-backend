from fastapi import APIRouter, UploadFile, Form
from app.models.schemas import EvidenceResponse

router = APIRouter()

@router.post("/", response_model=EvidenceResponse)
async def upload_evidence(
    project_id: str = Form(...),
    latitude: float = Form(...),
    longitude: float = Form(...),
    timestamp: str = Form(...),
    image: UploadFile = Form(...)
):
    return {"message": "Evidence uploaded successfully"}
