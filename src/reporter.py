import json
from datetime import datetime
from pathlib import Path

from models import EvaluationRun


def save_evaluation(
    evaluation: EvaluationRun,
    output_directory: str,
):

    # Create the directory if it doesn't exist
    Path(output_directory).mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"evaluation_{timestamp}.json"

    output_path = (
        Path(output_directory)
        / filename
    )

    with open(
        output_path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            evaluation.model_dump(),
            file,
            indent=4,
            ensure_ascii=False,
        )

    return output_path