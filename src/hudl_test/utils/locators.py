# utils/locator.py

from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    EMAIL_FIELD = (By.ID, 'username')
    EMAIL_FIELD_ERROR = (By.ID, 'error-element-username')
    #TODO: MISSING_USERNAME_FIELD_ERROR =''

    PASSWORD_FIELD = (By.ID, 'password')
    PASSWORD_FIELD_ERROR = (By.ID, 'error-element-password')
    FORGOT_PASSWORD_LINK = (By.PARTIAL_LINK_TEXT, 'Forgot Password')
    #TODO: MISSING_PASSWORD_FIELD_ERROR = ''

    CONTINUE_BUTTON = (By.NAME, 'action')


    CREATE_ACCOUNT_LINK = (By.PARTIAL_LINK_TEXT, 'Create Account')
    PRIVACY_POLICY_LINK = (By.PARTIAL_LINK_TEXT, 'Privacy Policy')
    #cheating here to avoid creating new page and associated objects but will allow explicit wait to check if above link navigates to the correct page
    PRIVACY_POLICY_POST_NAVIGATION_LINK = (By.PARTIAL_LINK_TEXT, 'Cookies Settings')

    TOS_LINK = (By.PARTIAL_LINK_TEXT, 'Terms of Service')
    #tried various locator strategies and XPATH seems to work for now
    GOOGLE_SSO_BUTTON = (By.XPATH, "//span[text()='Continue with Google']/..")
    #(By.PARTIAL_LINK_TEXT, 'Continue with Google')
    # (By.CLASS_NAME, 'ce1adcefd cad2d1f63 c05a3e248')
    
    FACEBOOK_SSO_BUTTON = (By.XPATH, "//span[text()='Continue with Facebook']/..")
    #(By.CLASS_NAME, 'ce1adcefd cad2d1f63 cdeec25e3')
    APPLE_SSO_BUTTON = (By.XPATH, "//span[text()='Continue with Apple']/..")