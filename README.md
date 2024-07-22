**E-Commerce Test Automation Project**

**Overview**

This repository contains an automated test suite for an e-commerce web application using Playwright with Python. The goal is to ensure the functionality of the application through automated tests.

**Requirements**

1. Install pytest plugin

   pip install pytest-playwright

2. Install the required browsers

   playwright install

**Features**

1. Automated UI tests using Playwright with Python
2. Reporting with Allure

**Usage**
**Test Structure**
- Test_Scripts/ - Contains all test cases
- pages/ Page Object Models for different pages
- conftest.py - Pytest fixtures for setup and teardown

**Running Tests**
 
 pytest .\Test_scripts\   --alluredir=allure-results

 **Generating allure reports**
 
 allure serve allure-results

![image](https://github.com/user-attachments/assets/d337c180-26ac-4593-9f46-3b94efb73e37)


