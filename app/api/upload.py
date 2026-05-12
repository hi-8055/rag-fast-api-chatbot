import uuid
from datetime import datetime

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)

from qdrant_client.models import PointStruct

from services.file_service import (
    save_file,
    extract_text_from_pdf,
    read_text_file
)

from services.chunk_service import chunk_text
from services.embedding_service import generate_embedding
from services.vector_service import store_vectors

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)

ALLOWED_EXTENSIONS = ["pdf", "txt"]

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    # Validate extension
    extension = file.filename.split(".")[-1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are allowed"
        )

    # Generate document id
    document_id = str(uuid.uuid4())

    # Save file
    file_path = await save_file(file)

     # Extract text
    if extension == "pdf":
        extracted_text = extract_text_from_pdf(file_path)

    else:
        extracted_text = read_text_file(file_path)

    # Chunking
    chunks = chunk_text(extracted_text)

    points = []

    for index, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk)

        point = PointStruct(
            id=index,
            vector=embedding,
            payload={
                "document_id": document_id,
                "filename": file.filename,
                "chunk_id": index,
                "text": chunk,
                "created_at": str(datetime.utcnow())
            }
        )

        points.append(point)

    # Store vectors
    store_vectors(points)

    return {
        "message": "Document processed successfully",
        "document_id": document_id,
        "total_chunks": len(chunks)
    }