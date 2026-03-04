import requests
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

def test_dashboard_edge():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Edge(options=options)

        start = time.time()
        driver.get("http://localhost:8080")

        assert "Cross Browser Test Results" in driver.page_source

        end = time.time()

        requests.post("http://localhost:8080/api/results", json={
            "test_name": "Dashboard Load Test",
            "browser": "edge",
            "status": "pass",
            "execution_time": end - start,
        })

    except Exception as e:
        try:
            requests.post("http://localhost:8080/api/results", json={
                "test_name": "Dashboard Load Test",
                "browser": "edge",
                "status": "fail",
                "execution_time": 0,
            })
        except:
            pass

        raise e

    finally:
        if 'driver' in locals():
            driver.quit()