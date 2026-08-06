from config import load_prompt
from validator import load_golden_dataset
from evaluator import evaluate
from reporter import save_evaluation


def main():

    # Load prompt configuration
    prompt = load_prompt("../prompts/v1.yaml")

    # Load golden dataset
    dataset = load_golden_dataset(
        "../datasets/golden_dataset_v1.json"
    )

    # Run evaluation
    evaluation = evaluate(
        prompt,
        dataset
    )

    # Save evaluation results
    report_path = save_evaluation(
    evaluation,
    "../results"
)

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

    # Calculate category accuracy
    correct_predictions = sum(
        result.is_correct
        for result in evaluation.results
    )

    accuracy = (
        correct_predictions
        / evaluation.total_cases
    ) * 100

    print("\n========================================")
    print("Evaluation Summary")
    print("========================================")
    print(f"Correct Predictions   : {correct_predictions}")
    print(f"Incorrect Predictions : {evaluation.total_cases - correct_predictions}")
    print(f"Category Accuracy     : {accuracy:.2f}%")
    print("========================================")

    print("\nEvaluation report saved successfully!")
    print(f"Location: {report_path}")


if __name__ == "__main__":
    main()