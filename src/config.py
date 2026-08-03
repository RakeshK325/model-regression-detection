import yaml

from models import PromptConfig

def load_prompt(path: str) -> PromptConfig:
    with open(path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)
    return PromptConfig(**data)