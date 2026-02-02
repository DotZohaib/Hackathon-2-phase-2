from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "pending"

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class TodoRead(TodoBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True
