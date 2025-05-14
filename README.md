# hudl_test
Project Title: Hudle Test

Description: Exercise for hiring process

Installation Instructions: 
Built using venv, requirements.txt in the main folder is up to date
Runs only with Firefox driver (geckodriver-v0.36.0-win64.zip) for now, additional browsers should be easy to add but not within current scope

License Information: Published Under MIT license because I needed something but I cannot imagine this being of interest to anyone else.

Contribution Guidelines: Sorry, folks, need to do this one on my own.

Contact Information: ggluckman@gmail.com

To try it out...

Make sure to update your credential information on the page file, .src/hudl_test/pages/login_page.py up at the top or tests will fail...

Run single tests with following command from hudl_test folder
$   python3 -m unittest tests.login_tests.TestLogin.test_login_with_valid_user

Run the full suite with html report (with added date-time stamp in the name) resulting from the tests subfolder with the following command
$   pytest --html=./reports/report$(get-date -f yyyy-MM-dd-HHmmss).html login_tests.py