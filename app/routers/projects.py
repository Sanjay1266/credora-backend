from fastapi import APIRouter
from app.models.schemas import Project

router = APIRouter()

PROJECTS = [
    Project(id="p1", name="Palm Jaggery Sustainability", location="Ramanathapuram"),
    Project(id="p2", name="Agroforestry Carbon Project", location="Theni"),
]

@router.get("/", response_model=list[Project])
def get_projects():
    return PROJECTS
