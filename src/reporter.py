import json
import shutil
from datetime import datetime
from pathlib import Path

from models import EvaluationRun


def save_evaluation(
    evaluation: EvaluationRun,
    output_directory: str,
):
    """
    Save the evaluation result to history and update
    the latest and baseline reports.
    """

    output_directory = Path(
        output_directory
    )

    history_directory = (
        output_directory / "history"
    )

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

    latest_file = (
        output_directory / "latest.json"
    )

    shutil.copy(
        history_file,
        latest_file,
    )

    baseline_file = (
        output_directory / "baseline.json"
    )

    if not baseline_file.exists():
        shutil.copy(
            history_file,
            baseline_file,
        )

    return history_file


def print_evaluation(evaluation):

    print(
        "\n========================================"
    )

    print(
        "MODEL REGRESSION DETECTION SYSTEM"
    )

    print(
        "========================================"
    )

    print(
        f"Prompt Version : "
        f"{evaluation.prompt_version}"
    )

    print(
        f"Total Cases    : "
        f"{evaluation.total_cases}"
    )

    print("\nEvaluation Results")
    print("----------------------------------------")

    for result in evaluation.results:

        print(
            f"\nTest Case : "
            f"{result.test_case_id}"
        )

        print(
            f"Expected Category : "
            f"{result.expected_category}"
        )

        print(
            f"Predicted Category: "
            f"{result.predicted_category}"
        )

        print(
            f"Correct           : "
            f"{result.is_correct}"
        )

        print("\nExpected Summary :")
        print(result.expected_summary)

        print("\nPredicted Summary :")
        print(result.predicted_summary)

        print("----------------------------------------")


def print_summary(metrics):

    print(
        "\n========================================"
    )

    print("Evaluation Summary")

    print(
        "========================================"
    )

    print(
        f"Correct Predictions   : "
        f"{metrics.correct_predictions}"
    )

    print(
        f"Incorrect Predictions : "
        f"{metrics.incorrect_predictions}"
    )

    print(
        f"Accuracy              : "
        f"{metrics.accuracy:.2f}%"
    )

    print(
        f"Precision             : "
        f"{metrics.precision:.2f}%"
    )

    print(
        f"Recall                : "
        f"{metrics.recall:.2f}%"
    )

    print(
        f"F1 Score              : "
        f"{metrics.f1_score:.2f}%"
    )

    print(
        "========================================"
    )


def print_confusion_matrix(metrics):

    print(
        "\n========================================"
    )

    print("Confusion Matrix")

    print(
        "========================================"
    )

    for actual, predictions in (
        metrics.confusion_matrix.items()
    ):

        print(
            f"\nActual Category : "
            f"{actual}"
        )

        for predicted, count in (
            predictions.items()
        ):

            print(
                f"  Predicted as "
                f"{predicted:<12} : {count}"
            )


def print_category_metrics(metrics):

    print(
        "\n========================================"
    )

    print("Category Metrics")

    print(
        "========================================"
    )

    for category, values in (
        metrics.category_metrics.items()
    ):

        print(
            f"\nCategory : {category}"
        )

        print(
            f"Precision : "
            f"{values['precision']:.2f}%"
        )

        print(
            f"Recall    : "
            f"{values['recall']:.2f}%"
        )

        print(
            f"F1 Score  : "
            f"{values['f1']:.2f}%"
        )


def print_regression_report(comparison):

    print(
        "\n========================================"
    )

    print("Regression Report")

    print(
        "========================================"
    )

    print(
        f"Total Cases  : "
        f"{comparison.total_cases}"
    )

    print(
        f"Regressions  : "
        f"{len(comparison.regressions)}"
    )

    print(
        f"Improvements : "
        f"{len(comparison.improvements)}"
    )

    if comparison.regressions:

        print(
            "\nRegressed Test Cases"
        )

        print(
            "--------------------"
        )

        for case in comparison.regressions:

            print(
                f"Test Case : "
                f"{case.test_case_id}"
            )

            print(
                f"Previous  : "
                f"{case.previous_correct}"
            )

            print(
                f"Current   : "
                f"{case.current_correct}"
            )

            print(
                f"Status    : "
                f"{case.status}"
            )

            print()

    if comparison.improvements:

        print(
            "\nImproved Test Cases"
        )

        print(
            "-------------------"
        )

        for case in comparison.improvements:

            print(
                f"Test Case : "
                f"{case.test_case_id}"
            )

            print(
                f"Previous  : "
                f"{case.previous_correct}"
            )

            print(
                f"Current   : "
                f"{case.current_correct}"
            )

            print(
                f"Status    : "
                f"{case.status}"
            )

            print()