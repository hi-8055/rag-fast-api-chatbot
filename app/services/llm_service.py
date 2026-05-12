import os
import requests

from dotenv import load_dotenv

load_dotenv()

EURI_API_KEY = os.getenv("EURI_API_KEY")

EURI_URL = (
    "https://api.euron.one/api/v1/euri/chat/completions"
)


def generate_response(prompt: str):

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {EURI_API_KEY}"
    }

    payload = {
        "model": "gpt-4.1-mini",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 1000,
        "temperature": 0.7
    }

    response = requests.post(
        EURI_URL,
        headers=headers,
        json=payload
    )

    # Debug print
    print("STATUS CODE:", response.status_code)
    print("RAW RESPONSE:", response.text)

    data = response.json()

    # Safe validation
    if "choices" not in data:

        return f"LLM API Error: {data}"

    return data["choices"][0]["message"]["content"]