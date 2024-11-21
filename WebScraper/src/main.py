import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def scrape_cbcb_products():
    # Paths to Chrome for Testing and ChromeDriver
    chrome_binary_path = 'ProjectFlower/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing'
    chromedriver_path = 'ProjectFlower/chromedriver-mac-arm64/chromedriver'

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_binary_path
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # Initialize WebDriver
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to the CBCB Berkeley shop page
    url = 'https://www.iheartjane.com/embed/stores/1172/menu/all'
    driver.get(url)

    # Function to dynamically handle the popup
    def handle_popup(driver):
        try:
            # Locate the "Close" button within the popup
            popup_close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Close']"))
            )
            popup_close_button.click()
            print("Popup closed.")
        except TimeoutException:
            print("No popup appeared.")
        except Exception as e:
            print(f"Unexpected error handling popup: {e}")

    # Call the popup handler
    handle_popup(driver)

    try:
        # Scroll to the bottom to load content
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Wait for content to load

        # Wait for product elements to be visible
        WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'ProductCard'))
        )
    except TimeoutException:
        print("Timed out waiting for page to load")
        print(driver.page_source)  # Debugging step to check loaded content
        driver.quit()
        return

    # Extract product details
    products = []
    product_cards = driver.find_elements(By.CLASS_NAME, 'ProductCard')
    for card in product_cards:
        try:
            name = card.find_element(By.CLASS_NAME, 'ProductCard__name').text
            price = card.find_element(By.CLASS_NAME, 'ProductCard__price').text
            description = card.find_element(By.CLASS_NAME, 'ProductCard__description').text
            products.append({
                'Name': name,
                'Price': price,
                'Description': description
            })
        except NoSuchElementException as e:
            print(f"Error extracting product details: Missing element - {e}")
        except Exception as e:
            print(f"Error extracting product details: {e}")

    # Close the WebDriver
    driver.quit()

    # Save to CSV
    if products:
        df = pd.DataFrame(products)
        df.to_csv('cbcb_products.csv', index=False)
        print(f"Scraped and saved {len(products)} products to 'cbcb_products.csv'")
    else:
        print("No products found or extracted.")

if __name__ == '__main__':
    scrape_cbcb_products()
