from config import load_prompt
from validator import load_golden_dataset


def main():
    # Load prompt configuration
    prompt = load_prompt("../prompts/v1.yaml")

    # Load golden dataset
    dataset = load_golden_dataset("../datasets/golden_dataset_v1.json")

    print("========================================")
    print("Model Regression Detection System")
    print("========================================")
    print(f"Prompt Version : {prompt.version}")
    print(f"Dataset Size   : {len(dataset)} test cases")
    print("System Status  : Ready")
    print("========================================")


if __name__ == "__main__":
    main()