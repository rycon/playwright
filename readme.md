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
    - [VSCode Extensions](#vscode-extensions)
    - [VSCode Settings](#vscode-settings)
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

### VSCode Extensions
* 

### VSCode Settings

# Resources Used
Below are the resources used when investigating and setting up Playwright.
* [Getting Started - PlayWrigh Pyton and VS Code](https://playwright.dev/docs/getting-started-vscode)
* [LambdaTest - What is Playwright?](https://www.lambdatest.com/playwright)
* [Playwright Q&A](https://applitools.com/blog/top-playwright-questions-answered/)
* [PlayWright Playlist](https://www.youtube.com/watch?v=UC2wj3Bg3eM&list=PLqndseDs9rmIwtzB1i08UWkQjQhpmZhtH)