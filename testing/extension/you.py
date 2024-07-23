from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# Path to your ChromeDriver executable
CHROMEDRIVER_PATH = "E:/chromedriver-win64/chromedriver.exe"

# Path to your Chrome binary
CHROME_PATH = "E:/chrome-win64/chrome.exe"

# Set up Chrome options to use the specified binary
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.binary_location = CHROME_PATH
chrome_options.add_argument('--no-sandbox')

# Set up ChromeDriver service
service = Service(CHROMEDRIVER_PATH)

# Create a new instance of the Chrome driver with the specified options and service
driver = webdriver.Chrome(service=service, options=chrome_options)

# Go to the desired website
driver.get('https://www.you.com')

time.sleep(3)
# Perform actions on the webpage
print(driver.title)

# Find the textarea element by its ID
textarea = driver.find_element(By.ID, 'search-input-textarea')

# Type the question into the textarea
question = "hello"
textarea.send_keys(question)

# Simulate pressing the RETURN key to submit the query
textarea.send_keys(Keys.RETURN)

time.sleep(4)

text_to_find = "Hello! How can I assist you today?"
items = driver.find_element(By.CSS_SELECTOR, ".sc-3e1a6f84-4")
print(items.text)

time.sleep(4)
# Find elements containing the text
elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{text_to_find}')]")

# Extract and print the text content of each matching element
for element in elements:
    print("HTML:", element.get_attribute('outerHTML'))
    print("Class:", element.get_attribute('class'))
    print(element.text)

    time.sleep(5)
    # Find the parent element
    parent_element = element.find_element(By.XPATH, "..")
    
    # Extract and print the text content, HTML, and class attribute of the parent element
    print("Parent HTML:", parent_element.get_attribute('outerHTML'))
    print("Parent Class:", parent_element.get_attribute('class'))
    print("Parent Text:", parent_element.text)

    time.sleep(5)

    # Find the grandparent element
    grandparent_element = element.find_element(By.XPATH, "../..")
    
    # Extract and print the text content, HTML, and class attribute of the grandparent element
    print("Grandparent HTML:", grandparent_element.get_attribute('outerHTML'))
    print("Grandparent Class:", grandparent_element.get_attribute('class'))
    print("Grandparent Text:", grandparent_element.text)

time.sleep(4)

# Close the browser
driver.quit()
