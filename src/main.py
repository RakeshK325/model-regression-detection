from config import load_prompt
from validator import load_golden_dataset
from evaluator import evaluate
from metrics import calculate_metrics
from reporter import (
    save_evaluation,
    print_evaluation,
    print_summary,
    print_confusion_matrix,
    print_category_metrics,
    print_regression_report,
)
from loader import load_evaluation
from comparator import compare_runs
from html_report import generate_html_report


def main():

    # Load prompt
    prompt = load_prompt("../prompts/v1.yaml")

    # Load dataset
    dataset = load_golden_dataset(
        "../datasets/golden_dataset_v1.json"
    )

    # Evaluate
    evaluation = evaluate(
        prompt,
        dataset
    )

    # Calculate metrics
    metrics = calculate_metrics(
        evaluation
    )

    # Save evaluation
    report_path = save_evaluation(
        evaluation,
        "../results"
    )

    # Generate HTML report
    generate_html_report(
        evaluation,
        "../results/report.html"
    )

    # Load reports
    baseline = load_evaluation(
        "../results/baseline.json"
    )

    latest = load_evaluation(
        "../results/latest.json"
    )

    # Compare runs
    comparison = compare_runs(
        baseline,
        latest
    )

    # Console Output
    print_evaluation(evaluation)

    print_summary(metrics)

    print_confusion_matrix(metrics)
    
    print_category_metrics(metrics)

    print("\nEvaluation report saved successfully!")
    print(f"Location: {report_path}")

    print("\nHTML report generated successfully!")
    print("Location: ../results/report.html")

    print_regression_report(comparison)


if __name__ == "__main__":
    main()