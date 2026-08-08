import yaml

from models import PromptConfig


def load_prompt(path: str) -> PromptConfig:
    """
    Load and validate a prompt configuration from a YAML file.
    """

    with open(
        path,
        "r",
        encoding="utf-8",
    ) as file:

        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(
            f"Prompt file '{path}' is empty or invalid."
        )

    return PromptConfig(**data)