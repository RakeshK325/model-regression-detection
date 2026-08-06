from models import (
    EvaluationRun,
    RegressionCase,
    RegressionReport,
)


def compare_runs(
    previous_run: EvaluationRun,
    current_run: EvaluationRun,
) -> RegressionReport:

    previous_lookup = {
        result.test_case_id: result
        for result in previous_run.results
    }

    regressions = []
    improvements = []

    for current in current_run.results:

        previous = previous_lookup.get(current.test_case_id)

        if previous is None:
            continue

        # Regression: Correct → Incorrect
        if previous.is_correct and not current.is_correct:
            regressions.append(
                RegressionCase(
                    test_case_id=current.test_case_id,
                    previous_correct=True,
                    current_correct=False,
                    status="REGRESSION",
                )
            )

        # Improvement: Incorrect → Correct
        elif (not previous.is_correct) and current.is_correct:
            improvements.append(
                RegressionCase(
                    test_case_id=current.test_case_id,
                    previous_correct=False,
                    current_correct=True,
                    status="IMPROVEMENT",
                )
            )

    return RegressionReport(
        total_cases=current_run.total_cases,
        regressions=regressions,
        improvements=improvements,
    )