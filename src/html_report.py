from pathlib import Path
from datetime import datetime


def generate_html_report(evaluation, output_path):
    generated_time = datetime.now().strftime(
    "%d %b %Y %H:%M:%S"
    )
    correct_predictions = sum(
        result.is_correct for result in evaluation.results
    )

    accuracy = (
        correct_predictions / evaluation.total_cases
    ) * 100

    rows = ""

    for result in evaluation.results:

        status = (
    '<span class="success">Correct</span>'
    if result.is_correct
    else
    '<span class="failure">Incorrect</span>'
)

        rows += f"""
        <tr>
            <td>{result.test_case_id}</td>
            <td>{result.expected_category}</td>
            <td>{result.predicted_category}</td>
            <td>{status}</td>
        </tr>
        """

    html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<title>Evaluation Report</title>

<style>

body {{
    font-family: Arial, sans-serif;
    margin:40px;
}}

table {{
    border-collapse: collapse;
    width:100%;
}}

th,td {{
    border:1px solid #ccc;
    padding:10px;
}}

th {{
    background:#1f2937;
    color:white;
}}

h1 {{
    color:#2563eb;
}}

.summary {{
    margin-bottom:30px;
}}

</style>

</head>

<body>

<h1>Model Regression Detection Report</h1>

<div class="summary">

<p><strong>Prompt Version:</strong> {evaluation.prompt_version}</p>

<p><strong>Total Cases:</strong> {evaluation.total_cases}</p>

<p><strong>Accuracy:</strong> {accuracy:.2f}%</p>

</div>

<table>

<tr>

<th>Test Case</th>

<th>Expected</th>

<th>Predicted</th>

<th>Status</th>

</tr>

{rows}

</table>

</body>

</html>
"""

    Path(output_path).write_text(
        html,
        encoding="utf-8"
    )