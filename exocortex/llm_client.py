from typing import Optional
from openai import OpenAI
import os

# Make sure you set: export OPENAI_API_KEY="your key"
client = OpenAI()

def call_llm(system_prompt: str, user_prompt: str, model: Optional[str] = "gpt-4o") -> str:
    """
    Real LLM call using OpenAI.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"[LLM ERROR] {e}"
