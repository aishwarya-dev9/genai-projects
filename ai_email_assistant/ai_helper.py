import ollama
from prompts import get_system_prompt

MODEL = "llama3"


def generate_email(notes, tone):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": get_system_prompt(tone)
            },
            {
                "role": "user",
                "content": notes.strip()
            }
        ]
    )

    return response["message"]["content"]