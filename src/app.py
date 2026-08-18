from pathlib import Path

from flask import Flask, send_file


app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
REPORT_PATH = BASE_DIR.parent / "results" / "report.html"


@app.route("/")
def dashboard():
    if not REPORT_PATH.exists():
        return (
            "Report not found. Run 'python main.py' first.",
            404,
        )

    return send_file(REPORT_PATH)


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
    )