from config import load_prompt
from validator import load_golden_dataset
from evaluator import evaluate
from reporter import (
    save_evaluation,
    print_evaluation,
    print_summary,
    print_regression_report,
)
from loader import load_evaluation
from comparator import compare_runs
from html_report import generate_html_report


def main():

    # Load configuration
    prompt = load_prompt("../prompts/v1.yaml")

    # Load dataset
    dataset = load_golden_dataset(
        "../datasets/golden_dataset_v1.json"
    )

    # Run evaluation
    evaluation = evaluate(
        prompt,
        dataset
    )

    # Save evaluation
    report_path = save_evaluation(
        evaluation,
        "../results"
    )

    # Load reports
    baseline = load_evaluation("../results/baseline.json")
    latest = load_evaluation("../results/latest.json")

    # Compare
    comparison = compare_runs(
        baseline,
        latest
    )

    # Console output
    print_evaluation(evaluation)

    print_summary(evaluation)

    print("\nEvaluation report saved successfully!")
    print(f"Location: {report_path}")

    print_regression_report(comparison)
    generate_html_report(
    evaluation,
    "../results/report.html"
    )

    print("\nHTML report generated successfully!")
    print("Location: ../results/report.html")


if __name__ == "__main__":
    main()