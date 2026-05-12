from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams
)

client = QdrantClient(
    host="localhost",
    port=6333
)

COLLECTION_NAME = "documents"


# Create collection if not exists
collections = client.get_collections().collections

collection_names = [
    c.name for c in collections
]

if COLLECTION_NAME not in collection_names:

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE
        )
    )


def store_vectors(points):

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )


def search_similar_chunks(
    query_embedding,
    limit: int = 3
):

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_embedding,
        limit=limit
    ).points

    return results