from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from app.models.user import UserRole, UserStatus

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: UserRole
    unit_number: str | None = None

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: str
    role: UserRole
    status: UserStatus
    unit_number: str | None
    created_at: datetime

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse