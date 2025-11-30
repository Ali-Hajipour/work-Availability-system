from sqlalchemy import Column, Integer, String
from app.db.db import Base
from pydantic import BaseModel, Field

class User(Base):
    __tablename__ = "user"

    id =Column(Integer, primary_key=True , index=True)
    personal_number = Column(Integer , unique=True , index=True , nullable=False)
    hashed_password = Column (String , nullable=False)
    role = Column(String, nullable=False)


class UserCreate(Base):
    personal_number: int = Field(..., ge=100000, le=999999)
    password: str
    role: str

