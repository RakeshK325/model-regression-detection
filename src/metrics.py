from collections import defaultdict

from models import (
    EvaluationRun,
    Metrics,
)


def calculate_metrics(
    evaluation: EvaluationRun,
) -> Metrics:

    # -------------------------------
    # Basic Metrics
    # -------------------------------

    correct_predictions = sum(
        result.is_correct
        for result in evaluation.results
    )

    incorrect_predictions = (
        evaluation.total_cases
        - correct_predictions
    )

    accuracy = (
        correct_predictions
        / evaluation.total_cases
    ) * 100

    # -------------------------------
    # Build Confusion Matrix
    # -------------------------------

    confusion_matrix = defaultdict(
        lambda: defaultdict(int)
    )

    for result in evaluation.results:

        actual = result.expected_category
        predicted = result.predicted_category

        confusion_matrix[actual][predicted] += 1

    # Convert to normal dictionary
    confusion_matrix = {
        actual: dict(predictions)
        for actual, predictions in confusion_matrix.items()
    }

    # -------------------------------
    # Collect all categories
    # -------------------------------

    categories = set()

    for result in evaluation.results:
        categories.add(result.expected_category)
        categories.add(result.predicted_category)

    # -------------------------------
    # Calculate Precision, Recall, F1
    # -------------------------------

    category_metrics = {}

    precision_sum = 0.0
    recall_sum = 0.0
    f1_sum = 0.0

    for category in categories:

        # True Positives
        tp = (
            confusion_matrix
            .get(category, {})
            .get(category, 0)
        )

        # False Positives
        fp = 0

        for actual in categories:

            if actual == category:
                continue

            fp += (
                confusion_matrix
                .get(actual, {})
                .get(category, 0)
            )

        # False Negatives
        fn = 0

        for predicted in categories:

            if predicted == category:
                continue

            fn += (
                confusion_matrix
                .get(category, {})
                .get(predicted, 0)
            )

        # Precision
        precision = (
            tp / (tp + fp)
            if (tp + fp) > 0
            else 0.0
        )

        # Recall
        recall = (
            tp / (tp + fn)
            if (tp + fn) > 0
            else 0.0
        )

        # F1 Score
        f1 = (
            2 * precision * recall
            / (precision + recall)
            if (precision + recall) > 0
            else 0.0
        )

        category_metrics[category] = {
            "precision": precision * 100,
            "recall": recall * 100,
            "f1": f1 * 100,
        }

        precision_sum += precision
        recall_sum += recall
        f1_sum += f1

    # -------------------------------
    # Macro Average
    # -------------------------------

    total_categories = len(categories)

    precision = (
        precision_sum
        / total_categories
    ) * 100

    recall = (
        recall_sum
        / total_categories
    ) * 100

    f1_score = (
        f1_sum
        / total_categories
    ) * 100

    # -------------------------------
    # Return Metrics
    # -------------------------------

    return Metrics(
        accuracy=accuracy,
        correct_predictions=correct_predictions,
        incorrect_predictions=incorrect_predictions,
        precision=precision,
        recall=recall,
        f1_score=f1_score,
        confusion_matrix=confusion_matrix,
        category_metrics=category_metrics,
    )