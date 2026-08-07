from datetime import datetime
from pathlib import Path


def generate_html_report(evaluation, output_path):
    correct_predictions = sum(
        result.is_correct for result in evaluation.results
    )

    incorrect_predictions = (
        evaluation.total_cases - correct_predictions
    )

    accuracy = (
        correct_predictions / evaluation.total_cases
    ) * 100

    generated_time = datetime.now().strftime(
        "%d %b %Y %H:%M:%S"
    )

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

<title>Model Regression Detection Report</title>

<style>

body {{
    font-family: Arial, Helvetica, sans-serif;
    background:#f5f7fb;
    margin:40px;
}}

.container {{
    max-width:1200px;
    margin:auto;
}}

h1 {{
    color:#2563eb;
}}

.cards {{
    display:flex;
    gap:20px;
    margin:30px 0;
}}

.card {{
    flex:1;
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0 2px 8px rgba(0,0,0,0.08);
    text-align:center;
}}

.metric {{
    font-size:32px;
    font-weight:bold;
    color:#2563eb;
}}

.label {{
    color:#666;
    margin-top:10px;
}}

table {{
    width:100%;
    border-collapse:collapse;
    background:white;
    box-shadow:0 2px 8px rgba(0,0,0,0.08);
}}

th {{
    background:#2563eb;
    color:white;
    padding:14px;
}}

td {{
    padding:12px;
    border-bottom:1px solid #ddd;
    text-align:center;
}}

tr:hover {{
    background:#f3f8ff;
}}

.success {{
    color:green;
    font-weight:bold;
}}

.failure {{
    color:red;
    font-weight:bold;
}}

.footer {{
    margin-top:30px;
    color:#777;
}}

</style>

</head>

<body>

<div class="container">

<h1>Model Regression Detection Dashboard</h1>

<p>
Prompt Version:
<b>{evaluation.prompt_version}</b>
</p>

<div class="cards">

<div class="card">
<div class="metric">{accuracy:.2f}%</div>
<div class="label">Accuracy</div>
</div>

<div class="card">
<div class="metric">{evaluation.total_cases}</div>
<div class="label">Total Cases</div>
</div>

<div class="card">
<div class="metric">{correct_predictions}</div>
<div class="label">Correct</div>
</div>

<div class="card">
<div class="metric">{incorrect_predictions}</div>
<div class="label">Incorrect</div>
</div>

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

<div class="footer">
Generated on: {generated_time}
</div>

</div>

</body>

</html>
"""

    Path(output_path).write_text(
        html,
        encoding="utf-8"
    )
    