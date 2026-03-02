import pytest
import requests
import time
from selenium import webdriver

def test_google_firefox():
    driver = webdriver.Firefox()
    start = time.time()

    driver.get("https://www.firefox.com")
    assert "Firefox" in driver.title

    end = time.time()
    driver.quit()

    requests.post("http://localhost:8080/api/results", json={
        "test_name": "Firefox Title Test",
        "browser": "firefox",
        "status": "pass",
        "execution_time": end - start
    })