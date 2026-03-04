import requests
import time
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def test_dashboard_firefox():
    options = Options()
    options.add_argument("--headless")
    
    # Try different Firefox binary paths for snap installation
    firefox_paths = [
        "/snap/firefox/current/usr/lib/firefox/firefox",  # Snap path
        "/usr/bin/firefox",  # Regular installation
        "/usr/lib/firefox/firefox",  # Alternative path
    ]
    
    firefox_binary = None
    for path in firefox_paths:
        if os.path.exists(path):
            firefox_binary = path
            break
    
    if firefox_binary:
        options.binary_location = firefox_binary
    
    try:
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        
        start = time.time()
        driver.get("http://localhost:8080")
        assert "Cross Browser" in driver.page_source
        end = time.time()

        # Post success result
        requests.post("http://localhost:8080/api/results", json={
            "test_name": "Dashboard Load Test",
            "browser": "firefox",
            "status": "pass",
            "execution_time": end - start,
        })
        
    except Exception as e:
        # Post failure result
        try:
            requests.post("http://localhost:8080/api/results", json={
                "test_name": "Dashboard Load Test",
                "browser": "firefox",
                "status": "fail",
                "execution_time": 0,
            })
        except:
            pass  # If API call fails, don't crash the test
        raise e
        
    finally:
        if 'driver' in locals():
            driver.quit()