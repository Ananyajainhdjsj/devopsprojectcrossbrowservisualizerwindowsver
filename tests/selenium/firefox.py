import requests
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def test_dashboard_firefox():
    options = Options()
    options.add_argument("--headless")
    
    try:
        # Connect to Firefox running in Docker on port 4444
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )
        
        start = time.time()
        # Use host.docker.internal or localhost to access app from Docker container
        driver.get("http://host.docker.internal:8080")
        assert "Cross Browser Test Results" in driver.page_source
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