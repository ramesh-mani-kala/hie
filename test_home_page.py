import pytest
from pages.home_page import Edit
@pytest.mark.usefixtures("setup")
class TestEdit:
    def test_to_verify_the_two_step_verification(self):
        # Initialize Edit class
        edit_driver = Edit(self.driver)

        # Open login page
        edit_driver.open_login_page()

        # Use the dynamically passed username and password
        edit_driver.enter_username(self.username)
        edit_driver.enter_password(self.password)

        # Click on the sign-in button
        edit_driver.clicking_on_sign_in()

     def test_to_verify_the_two_step_verification(self):
       