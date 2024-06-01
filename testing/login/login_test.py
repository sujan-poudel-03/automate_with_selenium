from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

class Login:

    def __init__(self):
        self.username = "learningsujan@gmail.com"
        self.password = "freeschema"
        self.login_url = "https://boomconsole.com/login"
        self.success_url = "https://boomconsole.com/captures/boomgpt"
        self.driver = webdriver.Chrome(options=options)

    def login_web(self):
        print("Login Testing started from WEB")

        self.driver.get(self.login_url)
        sleep(3)

        print("Navigated to login page")

        try:
            # Find the username input field and enter the username
            username_field = self.driver.find_element(By.XPATH, '//input[@formcontrolname="email"]')
            username_field.send_keys(self.username)

            # Find the password input field and enter the password
            password_field = self.driver.find_element(By.XPATH, '//input[@formcontrolname="password"]')
            password_field.send_keys(self.password)

            # Find the login button and click it
            login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
            login_button.click()

            # wait for the next page to load and check for a successful login
            WebDriverWait(self.driver, 10).until(EC.url_changes(self.success_url))
            sleep(3)

            print("Login successful, current URL:", self.driver.current_url)

            # Extract access tokens from local storage
            profile_data = self.extract_tokens_from_local_storage()
            

        except Exception as e:
            print("An error occurred:", e)  

        finally:
            # Close the browser
            self.driver.quit()
            print("Testing completed")


    def extract_tokens_from_local_storage(self):
        try:
            # Execute JavaScript to retrieve the access token from local storage
            profile = self.driver.execute_script("return localStorage.getItem('profile');")  # Adjust key as needed
            return profile
        except Exception as e:
            print("An error occurred while extracting tokens:", e)


login_test_instance = Login()
login_test_instance.login_web()