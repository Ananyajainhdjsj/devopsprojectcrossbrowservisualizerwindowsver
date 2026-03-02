from flask import Blueprint, render_template, request, jsonify
from models import TestResult
from extensions import db

main = Blueprint('main', __name__)

@main.route("/")

def dashboard():
    results = TestResult.query.all()

    chrome_pass = len([r for r in results if r.browser == "chrome" and r.status == "pass"])
    firefox_pass = len([r for r in results if r.browser == "firefox" and r.status == "pass"])

    chrome_fail = len([r for r in results if r.browser == "chrome" and r.status == "fail"])
    firefox_fail = len([r for r in results if r.browser == "firefox" and r.status == "fail"])

    chrome_time = sum([r.execution_time for r in results if r.browser == "chrome"])
    firefox_time = sum([r.execution_time for r in results if r.browser == "firefox"])

    total_tests = len(results)

    return render_template(
        "dashboard.html",
        results=results,
        chrome_pass=chrome_pass,
        firefox_pass=firefox_pass,
        chrome_fail=chrome_fail,
        firefox_fail=firefox_fail,
        chrome_time=chrome_time,
        firefox_time=firefox_time,
        total_tests=total_tests
    )

@main.route("/api/results", methods=["POST"])
def upload_result():
    data = request.json

    result = TestResult(
        test_name=data["test_name"],
        browser=data["browser"],
        status=data["status"],
        execution_time=data["execution_time"]
    )

    db.session.add(result)
    db.session.commit()

    return jsonify({"message": "Result saved"}), 201