from pydantic import BaseModel
from typing import List, Optional


class ChatRequest(BaseModel):
    query: str
    top_k: Optional[int] = 3


class ChatResponse(BaseModel):
    answer: str
    context: Optional[List[str]] = []