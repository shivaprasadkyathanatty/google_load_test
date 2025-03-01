from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_google_loads():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")

    assert "Google" in driver.title  # Check if "Google" is in the page title
    driver.quit()

if __name__ == "__main__":
    test_google_loads()
    print("Google loaded successfully!")
