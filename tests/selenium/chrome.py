import requests
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager


def test_dashboard_chrome():

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())

    try:
        driver = webdriver.Chrome(service=service, options=options)

        start = time.time()

        driver.get("http://localhost:8080")

        assert "Cross Browser Test Results" in driver.page_source

        end = time.time()

        # Post success result
        requests.post(
            "http://localhost:8080/api/results",
            json={
                "test_name": "Dashboard Load Test",
                "browser": "chrome",
                "status": "pass",
                "execution_time": end - start,
            },
        )

    except Exception as e:
        # Post failure result
        try:
            requests.post(
                "http://localhost:8080/api/results",
                json={
                    "test_name": "Dashboard Load Test",
                    "browser": "chrome",
                    "status": "fail",
                    "execution_time": 0,
                },
            )
        except:
            pass
        raise e

    finally:
        if 'driver' in locals():
            driver.quit()