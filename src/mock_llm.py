import json


def generate(
    system_prompt: str,
    user_prompt: str,
) -> str:
    """
    Deterministic mock classifier used by CI.

    This avoids requiring Ollama during automated tests.
    """

    text = user_prompt.lower()

    if any(
        keyword in text
        for keyword in [
            "charged",
            "charge",
            "billed",
            "billing",
            "invoice",
            "payment",
            "refund",
            "subscription",
        ]
    ):
        category = "billing"

    elif any(
        keyword in text
        for keyword in [
            "crash",
            "crashing",
            "freeze",
            "freezes",
            "server error",
            "application",
            "app",
            "upload",
        ]
    ):
        category = "technical"

    elif any(
        keyword in text
        for keyword in [
            "password",
            "account",
            "email address",
            "login",
            "reset",
        ]
    ):
        category = "account"

    else:
        category = "general"

    response = {
        "category": category,
        "summary": "Mock classification generated for CI testing.",
    }

    return json.dumps(response)