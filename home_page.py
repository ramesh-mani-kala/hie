import re
import time
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from locators import home_locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Edit:
    """
    Class containing methods to handle login functionality using Selenium WebDriver.
    """

    def __init__(self, driver):
        """
        Initialize the Edit class with a WebDriver instance.

        :param driver: Selenium WebDriver instance to interact with the browser.
        """
        self.driver = driver
        # Define an explicit wait with a timeout of 60 seconds for all actions in this class.
        self.wait = WebDriverWait(self.driver, 60)

    def open_login_page(self):
        """
        Navigate to the login page by clicking the 'button_premium' button.
        Includes retries in case of intermittent issues locating the username field.
        """
        # Wait until the 'button_premium' button is clickable and click it.
        self.wait.until(EC.element_to_be_clickable((By.ID, 'button_premium'))).click()

        # Retry mechanism: attempt up to 3 times to locate the username field.
        for attempt in range(3):
            try:
                # Check if the username field is present.
                self.driver.find_element(home_locators.enter_username_locator)
                print("Username field located successfully.")
                break
            except Exception as e:
                print(f"Attempt {attempt + 1}: Username field not found. Retrying...")
                try:
                    # Retry clicking on 'button_premium' if the username field is not found.
                    self.driver.find_element(By.ID, 'button_premium').click()
                    print(f"Retrying click on 'button_premium' (Attempt {attempt + 1})...")
                    time.sleep(6)  # Wait before retrying.
                except Exception as retry_exception:
                    print(f"Retry click failed on attempt {attempt + 1}: {retry_exception}")

    def enter_username(self, username):
        """
        Enter the username into the username input field.

        :param username: The username to be entered.
        """
        # Wait until the username field is present and then send the username.
        self.wait.until(EC.presence_of_element_located(home_locators.enter_username_locator)).send_keys(username)

    def enter_password(self, password):
        """
        Enter the password into the password input field.

        :param password: The password to be entered.
        """
        # Wait until the password field is present and then send the password.
        self.wait.until(EC.presence_of_element_located(home_locators.enter_password_locator)).send_keys(password)

    def clicking_on_sign_in(self):
        """
        Click on the sign-in button to submit the login form.
        """
        # Wait until the login button is clickable and click it.
        self.wait.until(EC.element_to_be_clickable(home_locators.click_on_login_locator)).click()
        time.sleep(2)  # Small delay to ensure the action is complete before proceeding.
