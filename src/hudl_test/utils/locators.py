# utils/locator.py

from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    EMAIL_FIELD = (By.ID, 'username')
    EMAIL_FIELD_ERROR = (By.ID, 'error-element-username')

    PASSWORD_FIELD = (By.ID, 'password')
    PASSWORD_FIELD_ERROR = (By.ID, 'error-element-password')
    FORGOT_PASSWORD_LINK = (By.PARTIAL_LINK_TEXT, 'Forgot Password')
    EDIT_EMAIL_LINK = (By.PARTIAL_LINK_TEXT, 'Edit')

    CONTINUE_BUTTON = (By.NAME, 'action')
    # The following locators are for the non-login links within the login pag
    CREATE_ACCOUNT_LINK = (By.PARTIAL_LINK_TEXT, 'Create Account')
    PRIVACY_POLICY_LINK = (By.PARTIAL_LINK_TEXT, 'Privacy Policy')
    TOS_LINK = (By.PARTIAL_LINK_TEXT, 'Terms of Service')

    # The following locators are for the SSO buttons on the login page.
    #tried various locator strategies and XPATH seems to work for now for the SSO stuff
    GOOGLE_SSO_BUTTON = (By.XPATH, "//span[text()='Continue with Google']/..")
    FACEBOOK_SSO_BUTTON = (By.XPATH, "//span[text()='Continue with Facebook']/..")
    APPLE_SSO_BUTTON = (By.XPATH, "//span[text()='Continue with Apple']/..")