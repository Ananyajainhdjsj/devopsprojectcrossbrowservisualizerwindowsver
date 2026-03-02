import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_dashboard_chrome():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    start = time.time()
    driver.get("http://localhost:8080")

    assert "Cross Browser" in driver.page_source

    end = time.time()
    driver.quit()

    requests.post("http://localhost:8080/api/results", json={
        "test_name": "Dashboard Load Test",
        "browser": "chrome",
        "status": "pass",
        "execution_time": end - start
    })