from ollama import chat


def generate(system_prompt: str, user_prompt: str) -> str:
    response = chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    )

    return response.message.content