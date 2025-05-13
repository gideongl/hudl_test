import sys
sys.path.append("..src")  # Add the parent directory to the system path
#Import base test class from base_tests module
from .base_tests import BaseTest
# Import the LoginPage class from the login_page module
from src.hudl_test.pages.login_page import LoginPage



# Define a test class named TestLogin that inherits from BaseTest.
class TestLogin(BaseTest):


    # Test for login with valid user credentials.
    def test_login_with_valid_user(self):
        # Initialize a LoginPage object with the self.driver attribute
        login_page = LoginPage(self.driver)
        
        # Call the login_with_valid_user method on the login_page object
        login_page.login_with_valid_credentials()
        
        # Use self.assertIn to check if the string "logged-in-successfully"
        # is present in the current URL of the driver. If present, the test passes.
        self.assertIn("https://identity.hudl.com/authorize/resume?", self.driver.current_url)


    #   Test login atttempt with an invalid username that is not a correctly formatted email address.
    def test_login_with_invalid_username(self):
        # Initialize a LoginPage object with the self.driver attribute.
        login_page = LoginPage(self.driver)
        
        # Call the get_email_validation_error_message method on the login_page object.
        # Assign the result to the variable result (error message).
        result = login_page.get_email_validation_error_message()
        
        # Use self.assertIn to check if the string "Enter a valid email." is
        # present in the result. If present, the test passes.
        self.assertIn("Enter a valid email.", result)

    #   Test login atttempt with an invalid username that is not an actual registered user.
    def test_login_with_nonexistent_username(self):
        # Initialize a LoginPage object with the self.driver attribute.
        login_page = LoginPage(self.driver)
        
        # Call the get_email_validation_error_message method on the login_page object.
        # Assign the result to the variable result (error message).
        result = login_page.get_nonexistent_username_error_message()
        
        # Use self.assertIn to check if the string "Enter a valid email." is
        # present in the result. If present, the test passes.
        self.assertIn("Incorrect username or password.", result)

    #Test login atttempt with an incorrect password that is not for the registered user.
    def test_login_with_incorrect_password(self):
        # Initialize a LoginPage object with the self.driver attribute.
        login_page = LoginPage(self.driver)
        
        # Call the get_email_validation_error_message method on the login_page object.
        # Assign the result to the variable result (error message).
        result = login_page.get_incorrect_password_error_message()
        
        # Use self.assertIn to check if the string "Enter a valid email." is
        # present in the result. If present, the test passes.
        self.assertIn("Your email or password is incorrect. Try again.", result)

    # Test for login attempt with empty username field. TODO: Implement error message check, instead of just checking that no navigation occurs.
    def test_login_with_empty_username(self):
        # Initialize a LoginPage object with the self.driver attribute
        login_page = LoginPage(self.driver)
        
        # Call the login_with_valid_user method on the login_page object
        login_page.empty_username_field_error()
        
        # Use self.assertIn to check if the string "logged-in-successfully"
        # is present in the current URL of the driver. If present, the test passes.
        self.assertIn("https://identity.hudl.com/u/login/identifier?", self.driver.current_url)

    # Test for login attempt with empty password field. TODO: Implement error message check, instead of just checking that no navigation occurs.
    def test_login_with_empty_password(self):
        # Initialize a LoginPage object with the self.driver attribute
        login_page = LoginPage(self.driver)
        
        # Call the login_with_valid_user method on the login_page object
        login_page.empty_password_field_error()
        
        # Use self.assertIn to check if the string "logged-in-successfully"
        # is present in the current URL of the driver. If present, the test passes.
        self.assertIn("https://identity.hudl.com/u/login/password?", self.driver.current_url)

    # Test the Create Account link on the login page.
    def test_create_account_link(self):
        # Initialize a LoginPage object with the self.driver attribute
        login_page = LoginPage(self.driver)
        
        # Call the click_create_account_link method on the login_page object
        login_page.click_create_account_link()
        
        # Use self.assertIn to check if the expected URL is present in the current URL of the driver.
        # If present, the test passes.
        self.assertIn("https://identity.hudl.com/u/signup/identifier?", self.driver.current_url)

    # Test the forgot password link on the login page
    def test_forgot_password_link(self):
        # Initialize a LoginPage object with the self.driver attribute
        login_page = LoginPage(self.driver)
        
        # Call the click_create_account_link method on the login_page object
        login_page.click_forgot_password_link()
        
        # Use self.assertIn to check if the expected is present in the current URL of the driver.
        # If present, the test passes.
        self.assertIn("https://identity.hudl.com/u/reset-password/request/prod-hudl-users-terraform?", self.driver.current_url)

    # Test the Privacy Policy link on the login page
    def test_privacy_policy_link(self):
        # Initialize a LoginPage object with the self.driver attribute
        login_page = LoginPage(self.driver)
        
        # Call the click_create_account_link method on the login_page object
        login_page.click_privacy_policy_link()
        #No assertion as it is implicit in the login page function (login_page.click_privacy_policy_link) which checks page load and title from link

    # Test the Terms of Service link on the login page
    def test_TOS_link(self):
        # Initialize a LoginPage object with the self.driver attribute
        login_page = LoginPage(self.driver)
        
        # Call the click_create_account_link method on the login_page object
        login_page.click_terms_of_service_link()
        #No assertion as it is implicit in the login page function (login_page.click_terms_of_service_link) which checks page load and title from link


    # Test the Google SSO button on the login page, checks only the navigation of the button, judged SSO functionality outside current exercise scope
    def test_google_sso_button(self):
        # Initialize a LoginPage object with the self.driver attribute
        login_page = LoginPage(self.driver)
        
        # Call the click_create_account_link method on the login_page object
        login_page.click_google_sign_in_button()
        
        # Use self.assertIn to check if the resulting navigation is to the expected SSO login page.
        # If present, the test passes.
        self.assertIn("https://accounts.google.com/v3/signin", self.driver.current_url)

    # Test the Facebook SSO button on the login page, checks only the navigation of the button, judged SSO functionality outside current exercise scope
    def test_facebook_sso_button(self):
        # Initialize a LoginPage object with the self.driver attribute
        login_page = LoginPage(self.driver)
        
        # Call the click_create_account_link method on the login_page object
        login_page.click_facebook_sign_in_button()
        
        # Use self.assertIn to check if the resulting navigation is to the expected SSO login page.
        # If present, the test passes.
        self.assertIn("https://www.facebook.com/login.php", self.driver.current_url)

    # Test the Apple SSO button on the login page, checks only the navigation of the button, judged SSO functionality outside current exercise scope
    def test_apple_sso_button(self):
        # Initialize a LoginPage object with the self.driver attribute
        login_page = LoginPage(self.driver)
        
        # Call the click_create_account_link method on the login_page object
        login_page.click_apple_sign_in_button()
        
        # Use self.assertIn to check if the resulting navigation is to the expected SSO login page.
        # If present, the test passes.
        self.assertIn("https://appleid.apple.com/auth/authorize?", self.driver.current_url)