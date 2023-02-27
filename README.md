This is a Python automation project that utilizes Selenium to test the website https://www.saucedemo.com/.

# Requirements
Python 3.6 or above
Chrome browser
ChromeDriver (version should match with the installed Chrome browser version)

# Installation
Clone the repository to your local machine using git clone https://github.com/your_username/saucedemo-automation.git
Navigate to the project directory in your terminal
Install the required packages by running the command pip install -r requirements.txt

# How to Run
Navigate to the project directory in your terminal
Run the command python test_saucedemo.py
The script will launch a Chrome browser and perform automated tests on the website. After the tests have finished running, the browser will close automatically.

# Tests
This automation script includes the following tests:

Login test: logs in to the website using valid credentials and verifies that the login is successful.
Cart test: adds a product to the cart, navigates to the cart page, removes the product from the cart, and verifies that the cart is empty.
FCP test : navigates to the website and measures the load time of the First Contentful Paint (LCP) element. 
LCP test: navigates to the website and measures the load time of the Largest Contentful Paint (LCP) element.

# Notes
Before running the script, make sure to update the username and password variables in the test_saucedemo.py file with valid credentials.
If you encounter any issues with the ChromeDriver, make sure that the version of the ChromeDriver matches the version of the installed Chrome browser.
You can adjust the speed of the script by changing the sleep times in the test_saucedemo.py file. However, be careful not to make the script too fast, as this may cause errors in the automated tests.