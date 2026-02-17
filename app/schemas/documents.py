from pydantic import BaseModel
from typing import Dict, Any, Optional


class Document(BaseModel):
    id: Optional[str] = None
    content: str
    metadata: Dict[str, Any] = {}