from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = "main_session"


class ChatResponse(BaseModel):
    response: str
