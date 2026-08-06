import json
import shutil
from datetime import datetime
from pathlib import Path

from models import EvaluationRun


def save_evaluation(
    evaluation: EvaluationRun,
    output_directory: str,
):

    output_directory = Path(output_directory)

    history_directory = output_directory / "history"

    history_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    history_file = (
        history_directory
        / f"evaluation_{timestamp}.json"
    )

    with open(
        history_file,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            evaluation.model_dump(),
            file,
            indent=4,
            ensure_ascii=False,
        )

    latest_file = output_directory / "latest.json"

    shutil.copy(
        history_file,
        latest_file,
    )

    baseline_file = output_directory / "baseline.json"

    if not baseline_file.exists():

        shutil.copy(
            history_file,
            baseline_file,
        )

    return history_file

def print_evaluation(evaluation):

    print("\n========================================")
    print("MODEL REGRESSION DETECTION SYSTEM")
    print("========================================")

    print(f"Prompt Version : {evaluation.prompt_version}")
    print(f"Total Cases    : {evaluation.total_cases}")

    print("\nEvaluation Results")
    print("----------------------------------------")

    for result in evaluation.results:

        print(f"\nTest Case : {result.test_case_id}")

        print(f"Expected Category : {result.expected_category}")
        print(f"Predicted Category: {result.predicted_category}")
        print(f"Correct           : {result.is_correct}")

        print("\nExpected Summary :")
        print(result.expected_summary)

        print("\nPredicted Summary :")
        print(result.predicted_summary)

        print("----------------------------------------")

def print_summary(evaluation):

    correct_predictions = sum(
        result.is_correct
        for result in evaluation.results
    )

    accuracy = (
        correct_predictions
        /
        evaluation.total_cases
    ) * 100

    print("\n========================================")
    print("Evaluation Summary")
    print("========================================")

    print(f"Correct Predictions   : {correct_predictions}")
    print(
        f"Incorrect Predictions : "
        f"{evaluation.total_cases - correct_predictions}"
    )
    print(f"Category Accuracy     : {accuracy:.2f}%")

    print("========================================")

def print_regression_report(comparison):

    print("\n========================================")
    print("Regression Report")
    print("========================================")

    print(f"Total Cases  : {comparison.total_cases}")
    print(f"Regressions  : {len(comparison.regressions)}")
    print(f"Improvements : {len(comparison.improvements)}")

    if comparison.regressions:

        print("\nRegressed Test Cases")
        print("--------------------")

        for case in comparison.regressions:

            print(f"Test Case : {case.test_case_id}")
            print(f"Previous  : {case.previous_correct}")
            print(f"Current   : {case.current_correct}")
            print(f"Status    : {case.status}")
            print()

    if comparison.improvements:

        print("\nImproved Test Cases")
        print("-------------------")

        for case in comparison.improvements:

            print(f"Test Case : {case.test_case_id}")
            print(f"Previous  : {case.previous_correct}")
            print(f"Current   : {case.current_correct}")
            print(f"Status    : {case.status}")
            print()            
