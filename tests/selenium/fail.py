import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_dashboard_fail():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        start = time.time()
        driver.get("http://localhost:8080")

        try:
            assert "THIS SHOULD FAIL" in driver.page_source
            status = "pass"  # This shouldn't happen
        except AssertionError:
            status = "fail"  # This is expected

        end = time.time()

        # Post the result (should be "fail")
        requests.post("http://localhost:8080/api/results", json={
            "test_name": "Intentional Failure Test",
            "browser": "chrome",
            "status": status,
            "execution_time": end - start,
        })


        # Assert failure detection
        assert status == "fail", "Test should have failed as expected"

    finally:
        driver.quit()