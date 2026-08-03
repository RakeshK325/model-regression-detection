import json

from llm import generate
from models import PromptConfig, ClassificationResult


def classify_email(
    email_text: str,
    prompt_config: PromptConfig
) -> ClassificationResult:
    """
    Classifies a customer support email using the configured LLM prompt.
    """

    result = generate(
        prompt_config.system_prompt,
        email_text
    )

    try:
        data = json.loads(result)
    except json.JSONDecodeError:
        raise ValueError(
            f"Model returned invalid JSON:\n\n{result}"
        )

    return ClassificationResult(**data)