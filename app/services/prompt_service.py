def build_prompt(
    context_chunks,
    chat_history,
    user_question
):

    context_text = "\n\n".join(context_chunks)

    history_text = ""

    for item in chat_history:

        history_text += (
            f"{item['role']}: "
            f"{item['content']}\n"
        )

    prompt = f"""
You are a helpful AI assistant.

Context:
{context_text}

Chat History:
{history_text}

Question:
{user_question}

Answer:
"""

    return prompt