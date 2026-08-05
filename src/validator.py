import json

from models import GoldenTestCase


def load_golden_dataset(path: str) -> list[GoldenTestCase]:
    with open(path, "r", encoding="utf-8") as file:
        dataset = json.load(file)

    validated_cases = []

    for case in dataset:
        validated_cases.append(
            GoldenTestCase(**case)
        )

    return validated_cases