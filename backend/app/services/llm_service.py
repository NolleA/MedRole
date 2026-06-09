from openai import OpenAI
from app.config import settings

_client: OpenAI | None = None


def get_client() -> OpenAI:
    global _client
    if _client is None:
        if not settings.deepseek_api_key:
            raise RuntimeError("DEEPSEEK_API_KEY is not set. Please add it to backend/.env")
        _client = OpenAI(
            api_key=settings.deepseek_api_key,
            base_url=settings.deepseek_base_url,
        )
    return _client


def chat(system: str, messages: list[dict], max_tokens: int = 300, temperature: float = 0.8) -> str:
    client = get_client()
    full_messages = [{"role": "system", "content": system}] + messages
    response = client.chat.completions.create(
        model=settings.deepseek_model,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=full_messages,
    )
    return response.choices[0].message.content


def chat_json(system: str, messages: list[dict], max_tokens: int = 2000) -> str:
    client = get_client()
    full_messages = [{"role": "system", "content": system}] + messages
    response = client.chat.completions.create(
        model=settings.deepseek_model,
        max_tokens=max_tokens,
        temperature=0.2,
        messages=full_messages,
    )
    return response.choices[0].message.content
