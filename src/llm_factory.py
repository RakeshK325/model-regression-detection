import os


def generate(
    system_prompt: str,
    user_prompt: str,
) -> str:
    """
    Select the LLM backend.

    Uses the mock backend when USE_MOCK_LLM=true.
    Otherwise uses the local Ollama backend.
    """

    use_mock = (
        os.getenv("USE_MOCK_LLM", "false").lower()
        == "true"
    )

    if use_mock:
        from mock_llm import generate as mock_generate

        return mock_generate(
            system_prompt,
            user_prompt,
        )

    from llm import generate as ollama_generate

    return ollama_generate(
        system_prompt,
        user_prompt,
    )