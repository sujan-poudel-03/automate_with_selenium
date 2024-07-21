from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

class LinkedIn:

    def __init__(self):
        self.linkedin_login_url = "https://www.linkedin.com/login"
        self.success_url = "https://www.linkedin.com/in/saugatsingh/"
        self.driver = webdriver.Chrome(options=options)

    def linkedin_login_with_google(self):
        print("Login Testing started from Google")

        self.driver.get(self.linkedin_login_url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'alternate-signin__btn--google')))

        print("Navigated to login page")

        try:
            # Find the Google sign-in button and click it
            google_signup_area = self.driver.find_element(By.CLASS_NAME, 'alternate-signin__btn--google')
            google_signup_area.click()
            WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))  # Wait until a new window opens
    
            print("Google login page opened")

            # Switch to the Google login window
            self.driver.switch_to.window(self.driver.window_handles[-1])    

            # # Enter Google email
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'identifierId')))
            # email_input = self.driver.find_element(By.ID, 'identifierId')
            # email_input.send_keys('your_google_email')  # Update this
            # email_input.send_keys(Keys.RETURN)
            # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))

            # # Enter Google password
            # password_input = self.driver.find_element(By.NAME, 'password')
            # password_input.send_keys('your_google_password')  # Update this
            # password_input.send_keys(Keys.RETURN)
            # WebDriverWait(self.driver, 10).until(EC.url_contains("linkedin.com"))  # Wait until LinkedIn redirects back

            # # Switch back to the original window
            # self.driver.switch_to.window(self.driver.window_handles[0])

            print("Logged into LinkedIn using Google")

        except Exception as e:
            print(f"An error occurred: {e}")


    # def linkedin_login_with_google(self):
    #     print("Login Testing started from Google")

    #     self.driver.get(self.linkedin_login_url)

    #     print("Navigated to login page")
    #      # Find the Google sign-in button and click it
    #     google_signup_area = self.driver.find_element(By.CLASS_NAME, 'alternate-signin__btn--google')
    #     google_signup_area.click()
    #     WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))  # Wait until a new window opens0
    #     print("Google login page opened")


    #     # try:
    #     #     # Find the username input field and enter the username
    #     #     google_signup_area = self.driver.find_element(By.CLASS_NAME, 'nsm7Bb-HzV7m-LgbsSe-MJoBVe')
    #     #     google_signup_area.click()

    #     #     # username_field.send_keys(self.username)


    #     #     # wait for the next page to load and check for a successful login
    #     #     # WebDriverWait(self.driver, 10).until(EC.url_changes(self.success_url))
    #     #     # sleep(3)

    #     #     # print("Login successful, current URL:", self.driver.current_url)
            

    #     # except Exception as e:
    #     #     print("An error occurred:", e)  

    #     # finally:
    #     #     # Close the browser
    #     #     self.driver.quit()
    #     #     print("Testing completed")


    def linkedin_login(self):
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



login_test_instance = LinkedIn()
login_test_instance.linkedin_login_with_google()