from fastapi import APIRouter
from app.models.schemas import LoginRequest, LoginResponse

router = APIRouter()

USERS = {
    "user@mail.com": "user",
    "verifier@mail.com": "verifier",
    "admin@mail.com": "admin",
}

@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    role = USERS.get(data.email)
    if not role:
        return {"token": "", "role": "invalid"}

    return {
        "token": "mock-jwt-token",
        "role": role,
    }
