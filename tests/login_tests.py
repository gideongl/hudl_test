import sys
sys.path.append("..src")  # Add the parent directory to the system path
#Import base test class from base_tests module
from .base_tests import BaseTest
# Import the LoginPage class from the login_page module
from src.hudl_test.pages.login_page import LoginPage



# Define a test class named TestLogin that inherits from BaseTest.
class TestLogin(BaseTest):
    # Define the first test method, which tests login with valid user credentials.
    def test_login_with_valid_user(self):
        # Initialize a LoginPage object with the self.driver attribute
        login_page = LoginPage(self.driver)
        
        # Call the login_with_valid_user method on the login_page object
        login_page.login_with_valid_credentials()
        
        # Use self.assertIn to check if the string "logged-in-successfully"
        # is present in the current URL of the driver. If present, the test passes.
        self.assertIn("https://www.hudl.com/home", self.driver.current_url)
