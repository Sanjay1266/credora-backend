from pydantic import BaseModel
from typing import Optional

class LoginRequest(BaseModel):
    email: str

class LoginResponse(BaseModel):
    token: str
    role: str

class Project(BaseModel):
    id: str
    name: str
    location: str

class EvidenceResponse(BaseModel):
    message: str
