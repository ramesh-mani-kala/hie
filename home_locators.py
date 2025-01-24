from selenium.webdriver.common.by import By

# Locator for the username input field
# This identifies the HTML element with ID 'mat-input-0' where the username should be entered.
enter_username_locator = By.ID, 'mat-input-0'

# Locator for the password input field
# This identifies the HTML element with ID 'mat-input-1' where the password should be entered.
enter_password_locator = By.ID, 'mat-input-1'

# Locator for the login button
# This identifies the HTML element with ID 'Login-btn' that should be clicked to log in.
click_on_login_locator = By.ID, 'Login-btn'
