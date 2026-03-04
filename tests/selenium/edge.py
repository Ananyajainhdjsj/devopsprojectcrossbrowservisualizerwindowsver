import requests
import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options

def test_dashboard_edge():
    
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    
    try:
        driver = webdriver.Remote(
            command_executor="http://localhost:4445/wd/hub",
            options=options
        )

        start = time.time()
        driver.get("http://172.17.0.1:8080")
        assert "Cross Browser" in driver.page_source
        end = time.time()

        # Post success result
        requests.post("http://localhost:8080/api/results", json={
            "test_name": "Dashboard Load Test",
            "browser": "edge",
            "status": "pass",
            "execution_time": end - start,
        })
        
    except Exception as e:
        # Post failure result
        try:
            requests.post("http://localhost:8080/api/results", json={
                "test_name": "Dashboard Load Test",
                "browser": "edge",
                "status": "fail",
                "execution_time": 0,
            })
        except:
            pass  # If API call fails, don't crash the test
        raise e
        
    finally:
        if 'driver' in locals():
            driver.quit()