from fastapi import APIRouter, Depends
from app.models.schemas import Project
from app.core.deps import get_current_user

router = APIRouter()

PROJECTS = [
    Project(id="p1", name="Palm Jaggery Sustainability", location="Ramanathapuram"),
    Project(id="p2", name="Agroforestry Carbon Project", location="Theni"),
]

@router.get("/", response_model=list[Project])
def get_projects(user=Depends(get_current_user)):
    return PROJECTS
