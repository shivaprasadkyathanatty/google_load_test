from selenium import webdriver
from selenium.webdriver.common.by import By

def test_google_loads():
    driver = webdriver.Chrome()  # Use Firefox() if needed
    driver.get("https://www.google.com")  # Open Google

    assert "Google" in driver.title  # Check if "Google" is in the page title
    driver.quit()

if __name__ == "__main__":
    test_google_loads()
    print("Google loaded successfully!")
