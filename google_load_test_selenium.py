import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_google_loads():
    chrome_options = Options()

    # Detect if running in CI/CD (like GitHub Actions)
    if os.getenv("CI"):
        print("Running in CI/CD - Using headless mode")
        chrome_options.add_argument("--headless=new")  # Ensures compatibility
        chrome_options.add_argument("--no-sandbox")  # Required for CI environments
        chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
        chrome_options.add_argument("--remote-debugging-port=9222")  # Enable debugging
        chrome_options.add_argument("--disable-gpu")  # Fixes rendering issues
        chrome_options.add_argument("--window-size=1920,1080")  # Set fixed window size
    else:
        print("Running locally - Opening Chrome normally")

    # Set up ChromeDriver using webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open Google
    driver.get("https://www.google.com")
    
    # Wait for Google to load
    time.sleep(3)  

    # Check if the page loaded successfully
    assert "Google" in driver.title
    print("Google loaded successfully!")

    # Close browser
    driver.quit()

if __name__ == "__main__":
    test_google_loads()
