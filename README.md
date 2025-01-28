# Selenium_SQM
Selenium WebDriver Project for LMS Login Automation
Project Overview
This project demonstrates how to automate login functionality using Selenium WebDriver for the LMS (Learning Management System) at https://lms.aps.rjt.ac.lk/login. It includes code to handle both successful and unsuccessful login attempts based on the credentials provided.

Prerequisites
Before you run this script, make sure you have the following installed:

Python 3.8 or higher
Selenium library
WebDriver Manager

Installation

git clone https://github.com/Sreesangeethan/Selenium_SQM

cd Selenium_SQM

Set Up Python Virtual Environment

python -m venv .venv

Activate Virtual Environment

.\.venv\Scripts\activate

pip install selenium webdriver_manager

Usage
To run the script, ensure that your virtual environment is activated and execute the following command:
python main.py

The script performs the following actions:

Opens a Chrome browser and navigates to the LMS login page.
Attempts to log in using provided credentials.
Outputs whether the login was successful based on the presence of a specific page element.
Modifying Credentials
To test different credentials, modify the username and password values in the main.py script under the section where credentials are entered:

username_input.send_keys("your_username")
password_input.send_keys("your_password")
Handling Different Outcomes
The script checks for a successful login by searching for an element identified by its ID "welcomeMessage". If the element is not found, it prints "Login failed!".

Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your enhancements.

License
This project is licensed under the MIT License - see the LICENSE file for details.
