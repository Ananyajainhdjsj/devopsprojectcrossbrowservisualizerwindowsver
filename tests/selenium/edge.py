import pytest
import requests
import time
from selenium import webdriver

def test_google_edge():
    driver = webdriver.Edge()
    start = time.time()

    driver.get("https://www.edge.com")
    assert "Edge" in driver.title

    end = time.time()
    driver.quit()

    requests.post("http://localhost:8080/api/results", json={
        "test_name": "edge Title Test",
        "browser": "edge",
        "status": "pass",
        "execution_time": end - start
    })