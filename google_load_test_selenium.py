import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_google_loads():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Run in headless mode (needed for GitHub Actions)
    chrome_options.add_argument("--no-sandbox")  # Bypass OS-level security restrictions
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
    chrome_options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging
    chrome_options.add_argument("--disable-gpu")  # Disable GPU for better stability
    chrome_options.add_argument("--window-size=1920,1080")  # Set fixed window size

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.google.com")

    time.sleep(3)  # Wait for Google to load
    assert "Google" in driver.title  # Validate the title
    print("Google loaded successfully!")

    driver.quit()

if __name__ == "__main__":
    test_google_loads()
