import unittest
from selenium import webdriver

# Define a test class named BaseTest that inherits from unittest.TestCase.
class BaseTest(unittest.TestCase):

    # This method is called before each test case.
    def setUp(self):
        # Create a Chrome WebDriver instance.
        self.driver = webdriver.Firefox()
        # Navigate to the specified URL.
        self.driver.get("https://identity.hudl.com/u/login/identifier?state=hKFo2SBqNVpGSzQ4VmRLNlhsQlRmSmdjSDBEcE9uMVhjM0lTbKFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIG5aejN2czJFUkRvU1dhOVQ3RWhTVHp3MGkxbWU2T1h2o2NpZNkgbjEzUmZrSHpLb3phTnhXQzVkWlFvYmVXR2Y0V2pTbjU")
    # This method is called after each test case.
    def tearDown(self):
        # Close the WebDriver, terminating the browser session.
        self.driver.close()

# Check if this script is the main module to be executed.
if __name__ == "__main__":
   # Run the test cases defined in this module
   unittest.main(verbosity=1)