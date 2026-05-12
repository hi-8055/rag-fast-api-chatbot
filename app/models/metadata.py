from datetime import datetime
from pydantic import BaseModel


class ChunkMetadata(BaseModel):
    document_id: str
    filename: str
    chunk_id: int
    created_at: datetime