# hudl_test
Exercise for hiring process

Built using venv, requirements.txt in the main folder is up to date

Runs only with Firefox driver (geckodriver-v0.36.0-win64.zip) for now, additional browsers should be easy to add but not within current scope

run single tests with following command from hudl_test folder
$   python3 -m unittest tests.login_tests.TestLogin.test_login_with_valid_user

run full suite with html report (with added date-time stamp in the name) resulting from the tests subfolder with the following command
$   pytest --html=./reports/report$(get-date -f yyyy-MM-dd-HHmmss).html login_tests.py