from datetime import datetime
from pathlib import Path


def generate_html_report(
    evaluation,
    metrics,
    comparison,
    output_path,
):
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

<title>Model Regression Detection Dashboard</title>

<style>

body {{
    margin:0;
    padding:40px;
    background:#f5f7fb;
    font-family:Arial, Helvetica, sans-serif;
}}

.container {{
    max-width:1300px;
    margin:auto;
}}

h1 {{
    color:#2563eb;
    margin-bottom:10px;
}}

.subtitle {{
    color:#666;
    margin-bottom:30px;
}}

.cards {{
    display:flex;
    gap:20px;
    margin-bottom:25px;
}}

.card {{
    flex:1;
    background:white;
    padding:24px;
    border-radius:16px;
    box-shadow:0 8px 20px rgba(0,0,0,0.08);
    text-align:center;
    transition:transform .2s ease;
}}

.card:hover {{
    transform:translateY(-5px);
}}

.metric {{
    font-size:36px;
    font-weight:bold;
    color:#2563eb;
}}

.label {{
    margin-top:12px;
    color:#555;
    font-size:18px;
}}

.section-title {{
    margin-top:40px;
    margin-bottom:15px;
    color:#2563eb;
}}

table {{
    width:100%;
    border-collapse:collapse;
    background:white;
    box-shadow:0 8px 20px rgba(0,0,0,0.08);
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
    background:#eef5ff;
}}

.success {{
    color:#16a34a;
    font-weight:bold;
}}

.failure {{
    color:#dc2626;
    font-weight:bold;
}}

.footer {{
    margin-top:40px;
    color:#777;
}}

</style>

</head>

<body>

<div class="container">

<h1>Model Regression Detection Dashboard</h1>

<div class="subtitle">
Prompt Version :
<strong>{evaluation.prompt_version}</strong>
</div>

<div class="cards">

<div class="card">
<div class="metric">{metrics.accuracy:.2f}%</div>
<div class="label">Accuracy</div>
</div>

<div class="card">
<div class="metric">{metrics.precision:.2f}%</div>
<div class="label">Precision</div>
</div>

<div class="card">
<div class="metric">{metrics.recall:.2f}%</div>
<div class="label">Recall</div>
</div>

<div class="card">
<div class="metric">{metrics.f1_score:.2f}%</div>
<div class="label">F1 Score</div>
</div>

</div>

<div class="cards">

<div class="card">
<div class="metric">{metrics.correct_predictions}</div>
<div class="label">Correct</div>
</div>

<div class="card">
<div class="metric">{metrics.incorrect_predictions}</div>
<div class="label">Incorrect</div>
</div>

<div class="card">
<div class="metric">{len(comparison.regressions)}</div>
<div class="label">Regressions</div>
</div>

<div class="card">
<div class="metric">{len(comparison.improvements)}</div>
<div class="label">Improvements</div>
</div>

</div>

<h2 class="section-title">
Evaluation Results
</h2>

<table>

<tr>

<th>Test Case</th>

<th>Expected Category</th>

<th>Predicted Category</th>

<th>Status</th>

</tr>

{rows}

</table>

<div class="footer">

<strong>Total Test Cases :</strong>
{evaluation.total_cases}

<br><br>

<strong>Generated :</strong>
{generated_time}

</div>

</div>

</body>

</html>
"""

    Path(output_path).write_text(
        html,
        encoding="utf-8",
    )