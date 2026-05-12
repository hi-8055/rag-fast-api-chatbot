from fastapi import APIRouter

from models.chat import ChatRequest

from services.embedding_service import (
    generate_embedding
)

from services.vector_service import (
    search_similar_chunks
)

from services.redis_service import (
    get_chat_history,
    save_message
)

from services.prompt_service import (
    build_prompt
)

from services.llm_service import (
    generate_response
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/")
async def chat(request: ChatRequest):

    # Step 1 — Get user query
    user_query = request.query

    # Step 2 — Convert query to embedding
    query_embedding = generate_embedding(
        user_query
    )

    # Step 3 — Search vector DB
    results = search_similar_chunks(
        query_embedding
    )

    # Step 4 — Extract retrieved chunks
    context_chunks = []

    for result in results:

        chunk_text = result.payload["text"]

        context_chunks.append(chunk_text)

    # Step 5 — Get chat history
    history = get_chat_history(
        request.session_id
    )

    # Step 6 — Build prompt
    prompt = build_prompt(
        context_chunks=context_chunks,
        chat_history=history,
        user_question=user_query
    )

    # Step 7 — Call LLM
    assistant_response = generate_response(
        prompt
    )

    # Step 8 — Save messages to Redis
    save_message(
        request.session_id,
        "user",
        user_query
    )

    save_message(
        request.session_id,
        "assistant",
        assistant_response
    )

    return {
        "response": assistant_response,
        "retrieved_chunks": context_chunks
    }