from flask import Flask, render_template, jsonify
from tester.runner import run_tests
from storage import save_run, list_runs, init_db

app = Flask(__name__)

init_db()


@app.route("/run")
def run():

    result = run_tests()

    save_run(result)

    return jsonify(result)


@app.route("/dashboard")
def dashboard():

    runs = list_runs()

    return render_template("dashboard.html", runs=runs)


@app.route("/health")
def health():

    return {"status": "ok"}