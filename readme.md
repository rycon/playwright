# Playwright
The intention is to learn Playwright. To get a new project setup from scratch, to get a PoC working, and document best practices. I have no prior experience with Playwright, and I have little experience writing UI Automation.

The is my second attempt. My initial attempt in on a branch called old-framework. I was running into pytest and python errors when I ran those tests. I was able to fix a few, but the project is over my head, and I wanted to try again.

I created these tests by looking at the PlayWright Python documentation, and then wrote the utils to suite how I would approach the framework with my current knowledge.

- [Playwright](#playwright)
- [About This Repository](#about-this-repository)
- [About Playwright](#about-playwright)
  - [Folder Structure](#folder-structure)
  - [Test Strategy](#test-strategy)
- [Steps I took to Install and Complete the Initial Setup](#steps-i-took-to-install-and-complete-the-initial-setup)
- [Setup and Tools](#setup-and-tools)
  - [Verify Setup](#verify-setup)
    - [Using requirements.txt to install modules](#using-requirementstxt-to-install-modules)
    - [VSCode Extensions](#vscode-extensions)
    - [VSCode Settings](#vscode-settings)
- [Writing Tests](#writing-tests)
  - [Configuration](#configuration)
  - [UI Automation](#ui-automation)
  - [API Automation](#api-automation)
    - [GraphQL](#graphql)
    - [Testing the Endpoints](#testing-the-endpoints)
  - [Linters and Formatters](#linters-and-formatters)
  - [Utilities](#utilities)
- [Copilot](#copilot)
- [Todo](#todo)
- [Resources Used](#resources-used)

# About This Repository
This repository is a place for me to learn more about PlayWright and UI automation in general. It will be rough to look at for people with programming experience. I will cover UI and API automation.

# About Playwright
Playwright is an opensource automation framework developed by Microsoft. Playwright is cross browser, cross platform, supports multiple programming languages, and support UI and API automation. For this PoC I've chosen Python as I have little programming experience and what I have was done in Python.

One of the benefits of Playwright over Selenium is Playwrights approach to making the tests more resilient. Playwright handles waits automatically removing the need to manually add and tweak.It handles dynamic pages which waits for the element to load, and then performs the assertion. It will also automatically retry a test assertion that has failed, before setting the error state.

Playwright also supports testing across browser processes, meaning across browser tabs, and browser profiles. Meaning, you could have one tab with the application, and another tab another application. Allowing you to enter data into one app, and seeing it replicated in another.

Playwright also has some built in tool as well, such as recording interaction and creating a test, and some tools to be investigate and debug failures.

Playwright also supports parallel test execution. This is handled by the test runner, such as Pytest or Jest.

Playwright supports UI and API automation, and my repo will cover both as I learn.

## Folder Structure
Right now I only have API tests, and the folder structure is quite simple. tests, testdata, and utils. I will need to rethink once I start learning the UI portion.

## Test Strategy
Looking to setup tests in a way where the test code is made simple, and test scenarios are data driven. The idea would be to write one test, reference a data file, and have the test scenarios within the data...

# Steps I took to Install and Complete the Initial Setup

1. Download and install VS Code
2. I'll be following the pypi instructions

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

### Using requirements.txt to install modules
The best way to get everything installed is to install PlayWright and the other python modules used in this repo, by using the requirements.txt file and the command `pip install -r requirements.txt`.

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
pytest-asyncio
jsonschema
pyyaml
```

### VSCode Extensions
* PlayWright Test for VSCode
* PlayWright Runner
* PlayWright Snippers

### VSCode Settings
To come.. maybe.

# Writing Tests
My instance of PlayWright I installed above also includes Pytest, which will make writing tests much easier. When creating a new test file it's important to remember to prefix your file name with test_, this will inform PyTest that the file is to be included when gathering tests to run.

## Configuration
It's best to keep configuration details with one file, and in this case it's the config.ini file. I've borrowed a config loader from a tutorial I found, and it works how I envisioned.

## UI Automation
I will be using the website https://www.automationexercise.com/ for my UI Automation. I have never used this site to test before, and it looks useful at first glance.

## API Automation
I will be using restful-api.dev for my API automation, I got the idea for my utils from a framework I've used in the past, and wrote them from memory or by googling.

A lot of the PlayWright functions have been expanded upon by these utilities, this will allow me to write smaller and easier to read test scripts.

### GraphQL
[The Awesome GraphQL repo](https://github.com/chentsulin/awesome-graphql) has a lot of great resources to learn from.
I really liked my experience writing GraphQL automation, I'll add some examples as well. I'll use this Github repo to pick a public set of endpoints

I've picked the [Anilist Resolver](hhttps://anilist.co/graphiql) to write tests against.

To start with, I'm going to just the resolvers like you would for REST, a test per operator
### Testing the Endpoints
Prior to writing any API automation, I will first add the new endpoint to a tool such as [Insomnia](https://www.insomnia.rest). I will then do my manual API testing at this time, once I'm satisfied there are no defects, I will then write the automation scripts based on the user story acceptance criteria.

While at ATB working as an API Automation QA, this would be my typical workflow:

1. Developer picks up the ticket and creates/updates the swagger file.
2. Once the swagger is ready, the dev informs me, and I review. I ask any questions, provide feedback, etc.
3. Developer starts their work on the endpoint proper.
4. I'll create a new branch from main (I forget if I pull from main or wait for the developers branch, dev branch would be cleaner)
5. I'll use the swagger to start mapping out my test scenarios, get the base code and test data ready, etc.
6. Once the developer is ready for code review or wants testing prior to the code review, I merge their branch into mine, and run the endpoint from my machine.
7. I use Insomnia to test the endpoint, run through my scenarios, and log defects or provide feedback to the developer.
8. I use linters and other tools to ensure the code matches our coding styles.
9. Once my testing is complete, and the test cases and test data are written, I merge my branch into the developers branch.
10. The developer raises a PR, their unit tests are executed, then my automation is executed, and when those pass, the other developers can review.
11. Once the PR is approved, it's merged to main, and the update goes straight to production.
12. A similar process is done by the Front End QA.

With the above, we needed to be certain that breaking changes to the API were handled correctly, either by creating a new version of the endpoint, or by ensuring the UI and API were released at the same time. 

You can find my Insomnia export in the root of this repo. I have examples for REST and GraphQL endpoints.

## Linters and Formatters

## Utilities
I've written several utilities to make my life easier, and to make the code (hopefully) cleaner to read. I have a yaml and config parser, and I'm trying to get a single function written to send requests. I'm new to PlayWright and its not clear to me yet how to do that without breaking the tests. 


# Copilot
I plan to explore copilot to see how it helps or hinders writing automation.

# Todo
* Learn more Python!
* Look at data classes, and see if I can use that for test data.
* Add a logger to see steps, and request and response data for API test debugging
* Add utilities and other helpers
* Investigate Faker and use it in tests
* Look into adding loops for API tests, to allow multiple test cases in test data, and 1 test function

# Resources Used
Below are the resources used when investigating and setting up Playwright.
* [YouTube channel with general Python tips](https://www.youtube.com/@ArjanCodes)
* [PlayWright Python API Documentation](https://playwright.dev/python/docs/api-testing)
* [PlayWright Python Documentation](https://playwright.dev/python/docs/intro)
* [LambdaTest - What is Playwright?](https://www.lambdatest.com/playwright)
* [Playwright Q&A](https://applitools.com/blog/top-playwright-questions-answered/)
* [PlayWright Playlist - UI Automation](https://www.youtube.com/watch?v=UC2wj3Bg3eM&list=PLqndseDs9rmIwtzB1i08UWkQjQhpmZhtH)
* [This repo helped me figure out the make_call() function](https://github.com/AutomationPanda/playwright-python-tutorial/blob/main/tests/conftest.py)