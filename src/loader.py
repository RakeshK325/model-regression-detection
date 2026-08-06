import json

from models import EvaluationRun


def load_evaluation(path: str) -> EvaluationRun:
    """
    Load a saved evaluation report from JSON
    and convert it into an EvaluationRun object.
    """

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return EvaluationRun(**data)