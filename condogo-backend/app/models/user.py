from sqlalchemy import Column, String, Boolean, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
from datetime import datetime, timezone
import uuid
import enum

class UserRole(str, enum.Enum):
    admin = "admin"
    staff = "staff"
    owner = "owner"
    renter = "renter"

class UserStatus(str, enum.Enum):
    pending = "pending"
    verified = "verified"
    rejected = "rejected"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    status = Column(Enum(UserStatus), default=UserStatus.pending)
    unit_number = Column(String, nullable=True)
    is_blacklisted = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))