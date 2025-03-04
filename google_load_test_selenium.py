import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_google_loads():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")  # Helps in CI environments
    chrome_options.add_argument("--headless")  # Run in headless mode (no UI)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevents memory issues
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")  # Set a unique user-data directory

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    driver.get("https://www.google.com")

    time.sleep(2)  # Give time for the page to load
    assert "Google" in driver.title  # Validate the page title
    
    driver.quit()

if __name__ == "__main__":
    test_google_loads()
    print("Google loaded successfully!")
