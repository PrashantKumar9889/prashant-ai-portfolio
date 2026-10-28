
import os

import requests
from dotenv import load_dotenv

from backend.services.retrieval_service import search_knowledge_base

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openrouter/free")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def generate_answer(
    question: str,
    top_k: int = 4,
    history: list[dict[str, str]] | None = None,
) -> str:
    """Generate an evidence-grounded answer using OpenRouter and RAG."""

    if not question.strip():
        return "Please enter a question."

    if not OPENROUTER_API_KEY:
        raise RuntimeError(
            "OPENROUTER_API_KEY is missing. Check your root .env file."
        )

    # Retrieve relevant evidence from your existing ChromaDB.
    history = (history or [])[-10:]
    previous_user_message = next(
        (
            message["content"]
            for message in reversed(history)
            if message["role"] == "user"
        ),
        "",
    )
    retrieval_query = "\n".join(
        part
        for part in (previous_user_message, question)
        if part
    )
    results = search_knowledge_base(retrieval_query, top_k=top_k)

    if not results:
        return "I couldn't find relevant information in my portfolio knowledge base."

    context_parts = []

    for result in results:
        metadata = result["metadata"]

        context_parts.append(
            f"Source: {metadata.get('source_name', 'Unknown')}\n"
            f"Title: {metadata.get('title', 'Untitled')}\n"
            f"Content:\n{result['content']}"
        )

    context = "\n\n---\n\n".join(context_parts)

    system_prompt = """
You are the AI portfolio assistant for Prashant Kumar.

Answer questions using only the portfolio evidence provided.
Do not invent skills, work experience, achievements, project details,
education, or personal information.

Use conversation history only to understand references in the latest
question. Previous assistant messages are not evidence and may be incorrect.
Do not repeat or rely on factual claims from conversation history unless
they are supported by the portfolio evidence provided for this answer.

If the evidence does not contain enough information, clearly say so.
Distinguish internship experience from full-time employment.
Answer naturally, professionally, and concisely.
"""

    messages = [
        {"role": "system", "content": system_prompt},
        *history,
        {
            "role": "user",
            "content": (
                f"Portfolio evidence:\n\n{context}\n\n"
                f"Question: {question}"
            ),
        },
    ]

    response = requests.post(
        OPENROUTER_URL,
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "X-OpenRouter-Title": "Prashant AI Portfolio",
        },
        json={
            "model": OPENROUTER_MODEL,
            "messages": messages,
            "temperature": 0.2,
            "max_tokens": 600,
        },
        timeout=60,
    )

    if not response.ok:
        raise RuntimeError(
            f"OpenRouter API error ({response.status_code}): "
            f"{response.text[:500]}"
        )

    data = response.json()

    print("\nDEBUG - OpenRouter response:")
    print(data)

    choices = data.get("choices", [])

    if not choices:
        raise RuntimeError(
            f"No answer returned by OpenRouter: {data}"
        )

    message = choices[0].get("message", {})
    answer = message.get("content")

    if isinstance(answer, list):
        answer = "\n".join(
            item.get("text", "")
            for item in answer
            if isinstance(item, dict)
        )

    if not isinstance(answer, str) or not answer.strip():
        raise RuntimeError(
            f"OpenRouter returned no text content: {data}"
        )

    return answer.strip()

    if not answer or not answer.strip():
        return "The model returned an empty answer. Please try again."

    return answer.strip()


if __name__ == "__main__":
    question = input("Ask your portfolio chatbot: ")

    try:
        print("\nAnswer:\n")
        print(generate_answer(question))
    except (requests.RequestException, RuntimeError, KeyError, IndexError) as exc:
        print(f"\nChatbot error: {exc}")