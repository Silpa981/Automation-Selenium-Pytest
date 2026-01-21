
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_google_search():
    # Setup Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Open Google
    driver.get("https://www.google.com")

    # Search keyword
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.submit()

    # Wait for results
    time.sleep(3)

    # Validate page title
    assert "Selenium" in driver.title

    # Take screenshot
    driver.save_screenshot("google_search_result.png")

    driver.quit()


if __name__ == "__main__":
    test_google_search()
