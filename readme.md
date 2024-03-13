# Playwright
The intention is to learn Playwright. To get a new project setup from scratch, to get a PoC working, and document best practices. I have no prior experience with Playwright, and I have little experience writing UI Automation.

- [Playwright](#playwright)
- [About This Repository](#about-this-repository)
- [About Playwright](#about-playwright)
  - [Folder Structure](#folder-structure)
  - [Test Strategy](#test-strategy)
- [Steps I took to Install and Complete the Initial Setup](#steps-i-took-to-install-and-complete-the-initial-setup)
- [Setup and Tools](#setup-and-tools)
  - [Verify Setup](#verify-setup)
    - [Using reqirements.txt to install modules](#using-reqirementstxt-to-install-modules)
    - [VSCode Extensions](#vscode-extensions)
    - [VSCode Settings](#vscode-settings)
- [Writing Tests](#writing-tests)
  - [Configuration](#configuration)
  - [UI Automation](#ui-automation)
  - [API Automation](#api-automation)
  - [Linters and Formatters](#linters-and-formatters)
- [Util Files... What do they?!](#util-files-what-do-they)
  - [](#)
- [Resources Used](#resources-used)

# About This Repository
This repository is a place for me to learn more about PlayWright and UI automation in general. It will be rough to look at for people with programming experience. I will cover UI and API automation.

# About Playwright
Playwright is an opensource automation framework developed by Microsoft. Playwright is cross browser, cross platform, supports multiple programming languages, and support UI and API automation. For this PoC I've chosen Python as I have little programming experience and what I have was done in Python.

One of the benefits of Playwright over Selenium is Playwrights approach to making the tests mmore resiliant. Playwright handles waits automatically removing the need to manually add and tweak.It handles dynamic pages which waits for the element to load, and then performs the assertion. It will also automcatically retry a test assertion that has failed, before setting the error state.

Playwright also supports testing across browser processes, meaning across browser tabs, and browser profiles. Meaning, you could have one tab with the application, and another tab another application. Allowing you to enter data into one app, and seeing it replicated in another.

Playwright also has some built in tool as well, such as recodring interaction and creating a test, and some tools to be investigate and debug failures.

Playwright also supports parallel test execution. This is handled by the test runner, such as Pytest or Jest.

Playwright supports UI and API automation, and my repo will cover both as I learn.

## Folder Structure

## Test Strategy
Looking to setup tests in a way where the test code is made simple, and test scenarios are data driven. The idea would be to write one test, reference a data file, and have the test scenarios within the data...

# Steps I took to Install and Complete the Initial Setup

1. Download and install VS Code
2. I'll be following the pypi instructions
3. 

# Setup and Tools
Playwright only needs a few tools installed to get started.

1. [Download and install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). You can also download their desktop app to manage your repo. I prefer to learn Git in the terminal.
2. [Download and install python](https://www.python.org/downloads/). Make sure select "add to PATH", this is _critical_
3. Create a new Python Virtual Environment, by typing `python -m venv venv` into you terminal in the folder you wish to use as your project
4. You will see a new folder called venv with a bunch of sub folders and files
5. Next, in your terminal type `.\venv\Scripts\activate`. You will see the terminal change to have (venv) at the beginning of your line.
6. Now we will install PlayWright using: `pip install pytest-playwright`
7. Then we'll install the PlayWright browsers using: `playwright install`
8. For API testing, I prefer [Insomnia](https://insomnia.rest/) as it has a clean interface, it runs well, it has extensions, and has great graphQL support.

## Verify Setup
To verify Python and pip are installed correctly type the following into your terminal:
```bash
python --version
```

```bash
pip --version
```

```bash
playwright --version
```

### Using reqirements.txt to install modules
An alternative way to install PlayWright and other python modules used in this repo, is my using a requirements.txt file and the command `pip install -r requirements.txt`.

You will first need to create the `requirements.txt` file in the root of your repo directory and fill it with:

```text
pytest-playwright
pytest
playwright
pydantic
assertpy
Faker
pytest-dependency
flake8
allure-pytest
```

### VSCode Extensions
* PlayWright Test for VSCode
* PlayWright Runner
* PlayWright Snippers

### VSCode Settings
To come.. maybe.

# Writing Tests
Our instance of PlayWright we installed above also includes Pytest, which will make writing tests much easier. When creating a new test file it's important to remember to prefix your file name with test_, this will inform PyTest that the file is to be included when searching for tests to run.

## Configuration
I was able to find an example where the author wrote a config parser, which allows me to keep add details such as the test url, endpoints, and more in one file for reference in tests. Having details such as this in one place makes adding new tests, and fixing broken test much easier.

## UI Automation
I will be using the website https://www.automationexercise.com/ for my UI Automation.

## API Automation
I will be using https://reqres.in for my API automation. A lot of the files and structure I got from an excellent source on [Medium](https://elixirautomation.medium.com/). A lot of what I wanted to add from a PyTest Framework I used at a past contract was already in here. I didn't need to hack together a solution from memory.

A lot of the PlayWright functions have been expanded upon by the utilities, this will allow me to write smaller and easier to read test scripts.

The tutorial I followed has the endpoints in their own folder, I'm not sure how this would scale as the number of endpoints increases. Not something for me to worry about at this time.

## Linters and Formatters


# Util Files... What do they?!
It's all well and good that I can read a tutorial and copy and paste their examples, it's another thing for me to understand what each file does. In this section I will document what each file from the tutorial does.

## 


# Resources Used
Below are the resources used when investigating and setting up Playwright.
* [Getting Started - PlayWrigh Pyton and VS Code](https://playwright.dev/docs/getting-started-vscode)
* [LambdaTest - What is Playwright?](https://www.lambdatest.com/playwright)
* [Playwright Q&A](https://applitools.com/blog/top-playwright-questions-answered/)
* [PlayWright Playlist](https://www.youtube.com/watch?v=UC2wj3Bg3eM&list=PLqndseDs9rmIwtzB1i08UWkQjQhpmZhtH)
* [Testing API's with PlayWright](https://elixirautomation.medium.com/automated-api-testing-playwright-part-1-d8eea1ccf0aa)
* [API Testing Series on Medium](https://elixirautomation.medium.com/)