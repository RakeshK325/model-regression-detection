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

    is_correct: bool


class EvaluationRun(BaseModel):
    prompt_version: str
    total_cases: int
    results: list[EvaluationResult]


class RegressionCase(BaseModel):
    test_case_id: str
    previous_correct: bool
    current_correct: bool
    status: str


class RegressionReport(BaseModel):
    total_cases: int
    regressions: list[RegressionCase]
    improvements: list[RegressionCase]


class Metrics(BaseModel):
    accuracy: float

    correct_predictions: int
    incorrect_predictions: int

    precision: float
    recall: float
    f1_score: float

    confusion_matrix: dict[str, dict[str, int]]

    category_metrics: dict[str, dict[str, float]]