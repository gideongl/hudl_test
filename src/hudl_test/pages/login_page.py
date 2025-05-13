from ..utils.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

VALID_USERNAME = 'ggluckman@gmail.com'
VALID_EMAIL_NONUSERNAME = 'test123@testing.test.com'
INVALID_EMAIL = '2test@2.test.2'
VALID_PASSWORD = 'LetsTest123!'
INVALID_PASSWORD = '123'


#login page class for POM
class LoginPage (object):
    def __init__(self, driver):
        #initialize the webdriver, using firefox in this case
        self.driver = driver
        #import the locators from the locators file
        self.locator = LoginPageLocators

    # golbal wait for elelements to become accessible with max wait of 10 seconds
    def wait_for_element(self, element):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(element)
        )

    # Method to fill out the username/email field
    def fill_username(self, username):
        #wait for the element to be present
        self.wait_for_element(self.locator.EMAIL_FIELD)
        #find the element and send the username to it
        self.driver.find_element(*self.locator.EMAIL_FIELD).send_keys(username)

    # Method to fill out the password field
    def fill_password(self, password):
        #wait for the element to be present
        self.wait_for_element(self.locator.PASSWORD_FIELD)
        #find the element and send the password to it
        self.driver.find_element(*self.locator.PASSWORD_FIELD).send_keys(password)

    #Method to click the continue button
    def click_continue_button(self):
        #wait for the element to be present
        self.wait_for_element(self.locator.CONTINUE_BUTTON)
        #find the element and click it
        self.driver.find_element(*self.locator.CONTINUE_BUTTON).click()

    # Method to attempt login
    def login(self, username, password):
        #fill out the username
        self.fill_username(username)
        #click the continue button
        self.click_continue_button()
        #fill out the password field
        self.fill_password(password)
        #click the continue button
        self.click_continue_button()

    #Method to login with valid credentials
    def login_with_valid_credentials(self):
        self.login(VALID_USERNAME, VALID_PASSWORD)

    # Method to get the email address validation error message for the username field
    def get_username_error_message(self):
        #fill out the username with an invalid email address
        self.fill_username(INVALID_EMAIL)
        #click the continue button
        self.click_continue_button()
        #wait for the element to be present
        self.wait_for_element(self.locator.EMAIL_FIELD_ERROR)
        #find the element and return the text
        return self.driver.find_element(*self.locator.EMAIL_FIELD_ERROR).text
    
        # Method to get the invalid username/password error because of a non-existent username
    def get_username_error_message(self):
        #fill out the username with an invalid email address
        self.fill_username(VALID_EMAIL_NONUSERNAME)
       #click the continue button
        self.click_continue_button()
        #fill resulting password field with an invalid password
        self.fill_password(VALID_PASSWORD)
        #click the continue button
        self.click_continue_button()
        #wait for the element to be present
        self.wait_for_element(self.locator.PASSWORD_FIELD_ERROR)
        #find the element and return the text
        return self.driver.find_element(*self.locator.PASSWORD_FIELD_ERROR).text
    
    # Method to get the invalid username/password error because of an incorrect password
    def get_username_error_message(self):
        #fill out the username with an invalid email address
        self.fill_username(VALID_USERNAME) 
        #click the continue button
        self.click_continue_button()
        #fill resulting password field with an invalid password
        self.fill_password(INVALID_PASSWORD)
        #click the continue button
        self.click_continue_button()
        #wait for the element to be present
        self.wait_for_element(self.locator.PASSWORD_FIELD_ERROR)
        #find the element and return the text
        return self.driver.find_element(*self.locator.PASSWORD_FIELD_ERROR).text
    
    
    # Method to get the error message for the password field
    def get_password_error_message(self):
        #fill out the username with an invalid email address
        self.fill_username(VALID_EMAIL_NONUSERNAME)
        #click the continue button
        self.click_continue_button()
        #fill resulting password field with an invalid password
        self.fill_password(INVALID_PASSWORD)
        #click the continue button
        self.click_continue_button()
        #wait for the element to be present
        self.wait_for_element(self.locator.EMAIL_FIELD_ERROR)
        #find the element and return the text
        return self.driver.find_element(*self.locator.PASSWORD_FIELD_ERROR).text
    

    # Method to click the create account link
    def click_create_account(self):
        #wait for the element to be present
        self.wait_for_element(self.locator.CREATE_ACCOUNT_LINK)
        #find the element and click it
        self.driver.find_element(*self.locator.CREATE_ACCOUNT_LINK).click()

    # Method to click the forgot password link
    def click_forgot_password(self):
        #wait for the element to be present
        self.wait_for_element(self.locator.FORGOT_PASSWORD_LINK)
        #find the element and click it
        self.driver.find_element(*self.locator.FORGOT_PASSWORD_LINK).click()

    # Method to click the privacy policy link (https://www.hudl.com/privacy)
    def click_privacy_policy(self):
        #wait for the element to be present
        self.wait_for_element(self.locator.PRIVACY_POLICY_LINK)
        #find the element and click it
        self.driver.find_element(*self.locator.PRIVACY_POLICY_LINK).click()

    # Method to click the terms of service link (https://www.hudl.com/terms)
    def click_terms_of_service(self):
        #wait for the element to be present
        self.wait_for_element(self.locator.TOS_LINK)
        #find the element and click it
        self.driver.find_element(*self.locator.TOS_LINK).click()

    # Method to click the google sign in button
    def click_google_sign_in(self):
        #wait for the element to be present
        self.wait_for_element(self.locator.GOOGLE_SSO_BUTTON)
        #find the element and click it
        self.driver.find_element(*self.locator.GOOGLE_SSO_BUTTON).click()

    # Method to click the facebook sign in button
    def click_facebook_sign_in(self):
        #wait for the element to be present
        self.wait_for_element(self.locator.FACEBOOK_SSO_BUTTON)
        #find the element and click it
        self.driver.find_element(*self.locator.FACEBOOK_SSO_BUTTON).click() 
    
    # Method to click the apple sign in button
    def click_apple_sign_in(self):
        #wait for the element to be present
        self.wait_for_element(self.locator.APPLE_SSO_BUTTON)
        #find the element and click it
        self.driver.find_element(*self.locator.APPLE_SSO_BUTTON).click()
    

