from classifier import classify_email

from models import (
    PromptConfig,
    GoldenTestCase,
    EvaluationResult,
    EvaluationRun,
)


def evaluate(
    prompt: PromptConfig,
    dataset: list[GoldenTestCase],
) -> EvaluationRun:

    results = []

    for test_case in dataset:

        prediction = classify_email(
            test_case.input,
            prompt
        )

        results.append(
    EvaluationResult(
        test_case_id=test_case.id,

        expected_category=test_case.expected_output.category,
        predicted_category=prediction.category,

        expected_summary=test_case.expected_output.summary,
        predicted_summary=prediction.summary,

        is_correct=(
            test_case.expected_output.category.lower()
            ==
            prediction.category.lower()
        )
    )
)

    return EvaluationRun(
        prompt_version=prompt.version,
        total_cases=len(dataset),
        results=results,
    )