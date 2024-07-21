from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


# cmd : "E:/chrome-win64/chrome.exe" --remote-debugging-port=9222 --user-data-dir="E:/chrome-win64/User Data"

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
driver.get('http://www.google.com')

linkedin_url = ""
time.sleep(100)
# Perform actions on the webpage
print(driver.title)

# Close the browser
driver.quit()
