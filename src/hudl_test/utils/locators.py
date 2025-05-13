# utils/locator.py

from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    EMAIL_FIELD = (By.ID, 'username')
    EMAIL_FIELD_ERROR = (By.ID, 'error-element-password')

    PASSWORD_FIELD = (By.ID, 'password')
    PASSWORD_FIELD_ERROR = (By.ID, 'error-element-password')
    FORGOT_PASSWORD_LINK = (By.PARTIAL_LINK_TEXT, 'Forgot Password')

    CONTINUE_BUTTON = (By.NAME, 'action')


    CREATE_ACCOUNT_LINK = (By.PARTIAL_LINK_TEXT, 'Create Account')
    PRIVACY_POLICY_LINK = (By.PARTIAL_LINK_TEXT, 'Privacy Policy')
    TOS_LINK = (By.PARTIAL_LINK_TEXT, 'Terms of Service')

    GOOGLE_SSO_BUTTON = (By.CLASS_NAME, 'ce1adcefd cad2d1f63 c05a3e248')
    FACEBOOK_SSO_BUTTON = (By.CLASS_NAME,'ce1adcefd cad2d1f63 cdeec25e3')
    APPLE_SSO_BUTTON = (By.CLASS_NAME, 'ce1adcefd cad2d1f63 c2fe1899b')