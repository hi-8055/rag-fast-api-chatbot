import json
import redis

redis_client = redis.Redis(
    host = "localhost",
    port = 6379,
    decode_responses = True
)

def save_message(
    session_id: str,
    role: str,
    content: str
):
    history = redis_client.get(session_id)

    if history:
        history = json.loads(history)
    else:
        history = []

    history.append({
        "role": role,
        "content": content
    })

    redis_client.set(
        session_id,
        json.dumps(history)
    )


def get_chat_history(session_id: str):

    history = redis_client.get(session_id)

    if history:
        return json.loads(history)

    return []