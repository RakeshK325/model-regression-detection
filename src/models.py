from pydantic import BaseModel


class PromptConfig(BaseModel):
    version: str
    timestamp: str
    system_prompt: str


class ClassificationResult(BaseModel):
    category: str
    summary: str