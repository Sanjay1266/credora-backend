from fastapi import APIRouter, UploadFile, Form, Depends, HTTPException
from app.models.schemas import EvidenceResponse
from app.core.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=EvidenceResponse)
async def upload_evidence(
    project_id: str = Form(...),
    latitude: float = Form(...),
    longitude: float = Form(...),
    timestamp: str = Form(...),
    image: UploadFile = Form(...),
    user=Depends(get_current_user),
):
    if user["role"] != "verifier":
        raise HTTPException(status_code=403, detail="Not authorized")

    return {"message": "Evidence uploaded successfully"}
