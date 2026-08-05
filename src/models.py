from pydantic import BaseModel


class PromptConfig(BaseModel):
    version: str
    timestamp: str
    system_prompt: str


class ClassificationResult(BaseModel):
    category: str
    summary: str

class ExpectedOutput(BaseModel):
    category: str
    summary: str


class GoldenTestCase(BaseModel):
    id: str
    input: str
    expected_output: ExpectedOutput
    expected_difficulty: str
    notes: str    

class EvaluationResult(BaseModel):
    test_case_id: str
    expected_category: str
    predicted_category: str
    expected_summary: str
    predicted_summary: str
