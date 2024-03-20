# Playwright

I created this branch to preserve the original attempt. I followed a really great, but out of date tutorial, that was more complex than what I'm used to. Main will become my second attempt to create something that works for me.

The intention is to learn Playwright. To get a new project setup from scratch, to get a PoC working, and document my process to learn from. I have no prior experience with Playwright, and I have little experience writing UI Automation.

All tests in this repository _should_ work from your local machine. I can't promise that breaking changes weren't made to the app or API under test.

I've included my Insomnia collection in the repo as well. I use a tool such as this when I'm initially investigating and testing an endpoint while writing the automated tests.

- [Playwright](#playwright)
- [About This Repository](#about-this-repository)
- [About Playwright](#about-playwright)
  - [Folder Structure](#folder-structure)
  - [Config.ini](#configini)
  - [Test Strategy](#test-strategy)
- [Setup and Required Tools](#setup-and-required-tools)
  - [Verify Setup](#verify-setup)
    - [Using requirements.txt to install modules](#using-requirementstxt-to-install-modules)
    - [VSCode Extensions](#vscode-extensions)
      - [Required](#required)
      - [Nice to Have](#nice-to-have)
    - [VSCode Settings](#vscode-settings)
- [Writing Tests](#writing-tests)
  - [Configuration](#configuration)
  - [UI Automation](#ui-automation)
  - [API Automation](#api-automation)
    - [GraphQL](#graphql)
    - [Testing the Endpoints](#testing-the-endpoints)
  - [Linters and Formatters](#linters-and-formatters)
- [Util and Helper Files... What do they?!](#util-and-helper-files-what-do-they)
  - [TestData -\> requests .py files](#testdata---requests-py-files)
  - [TestData -\> response .py files](#testdata---response-py-files)
  - [utils -\> faker.py](#utils---fakerpy)
  - [utils -\> user\_client.py](#utils---user_clientpy)
  - [utils -\> base\_client.py](#utils---base_clientpy)
- [Copilot](#copilot)
- [Resources Used](#resources-used)

# About This Repository
This repository is a place for me to learn more about PlayWright and UI automation in general. It will be rough to look at for people with programming experience, as everything I know was learned on the job. I will practice UI and API automation.

# About Playwright
Playwright is an opensource automation framework developed by Microsoft. Playwright is cross browser, cross platform, supports multiple programming languages, and support UI and API automation. For this PoC I've chosen Python as I have little programming experience and what I have was done in Python.

One of the benefits of Playwright over Selenium is Playwrights approach to making the tests more resilient. Playwright handles waits automatically removing the need to manually add and tweak.It handles dynamic pages which waits for the element to load, and then performs the assertion. It will also automatically retry a test assertion that has failed, before setting the error state.

Playwright also supports testing across browser processes, meaning across browser tabs, and browser profiles. Meaning, you could have one tab with the application, and another tab another application. Allowing you to enter data into one app, and seeing it replicated in another.

Playwright also has some built in tool as well, such as recording interaction and creating a test, and some tools to be investigate and debug failures.

Playwright also supports parallel test execution. This is handled by the test runner, such as Pytest or Jest.

Playwright supports UI and API automation, and my repo will cover both as I learn.

## Folder Structure
This section will need to be thought through and expanded upon as I learn more about PlayWright, and as I get more tests, utilities, and other files in place.

I know a few things for certain at this time. For UI automation I will follow the Page Object Model (POM), where I'll split the web page elements into their own file, and a separate test case file for each page. So there will be at least page and test folders.

Current thought on structure:


```
  \constants
  \pages (POM)
    \page1
  \endpoints
  \testdata
    \api
      \test_endpoint1
    \ui
      \test_page1
  \tests
    \ui
      \page1
    \api
      \endpoint1
  \utils
  ```

## Config.ini
The config.ini file will contain information that will be referenced by the test cases. Initially, it will have the API test url and endpoints. Over time, it may contain information such as ID's and other details that are shared across tests.

TODO see if I can get environment specific config files working, ideally while keeping the base config file in use. Having anything in the env specific file overwrite details from the base file.

TODO see if I can use a similar approach for a secrets file to contain login and other credentials. This file would be in the .gitignore to ensure it isn't uploaded to the repo.

## Test Strategy
Looking to setup tests in a way where the test code is made simple, and test scenarios are data driven. The idea would be to write one test, reference a data file, and have the test scenarios within the data. Each test execution would look through the test cases within these files.

# Setup and Required Tools
Playwright only needs a few tools installed to get started.

1. I prefer [VSCode](https://code.visualstudio.com/download), but any IDE will work.
2. [Download and install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). You can also download their desktop app to manage your repo. I prefer to learn and teach Git in the terminal.
3. [Download and install python](https://www.python.org/downloads/). Make sure select "add to PATH", this is _critical_
4. Create a new Python Virtual Environment, by typing `python -m venv venv` into you terminal in the folder you wish to use as your project
5. You will see a new folder called venv with a bunch of sub folders and files
6. Next, in your terminal type `.\venv\Scripts\activate`. You will see the terminal change to have (venv) at the beginning of your line.
7. Now we will install PlayWright using: `pip install pytest-playwright`
8. Then we'll install the PlayWright browsers using: `playwright install`
9. For API testing, I prefer [Insomnia](https://insomnia.rest/) as it has a clean interface, it runs well, it has extensions, and has great graphQL support. I will have a section dedicated to Insomnia.

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
#### Required
* PlayWright Test for VSCode
* PlayWright Runner
* PlayWright Snippers
* GraphQL
* YAML

#### Nice to Have
* Todo Tree, displays a list of places marked as to do within the code.
* Code Spell Checker
* Gitlense, adds more Git features to VSCode, including git blame
* Indent-rainbow, makes it easier to read and write indents, very useful for Python and YAML
* view-in-browser, right click on an html file to open in your web browser, great for viewing reports

### VSCode Settings
To come.. maybe.

# Writing Tests
My instance of PlayWright I installed above also includes Pytest, which will make writing tests much easier. When creating a new test file it's important to remember to prefix your file name with test_, this will inform PyTest that the file is to be included when gathering tests to run.

## Configuration
It's best to keep configuration details with one file, and in this case it's the config.ini file. The baseApiUrl, and endpoints as simple examples.

## UI Automation
I will be using the website https://www.automationexercise.com/ for my UI Automation. I have never used this site to test before, and it looks useful at first glance.

## API Automation
I will be using https://reqres.in for my API automation, they have a [swagger](https://reqres.in/api-docs/). A lot of the utils and structure I got from an excellent tutorial on [Medium](https://elixirautomation.medium.com/list/demystifying-api-testing-playwright-and-python-760ce307431b). The tutorial sets up a lot of utilities and useful functions, many of which I would have attempted to write on my own, from memory, based on what I've used during my years working. Plus this example uses some Python and PyTest functions I've never experienced.

A lot of the PlayWright functions have been expanded upon by these utilities, this will allow me to write smaller and easier to read test scripts.

The tutorial I followed has the endpoints in their own folder, I'm not sure how this would scale as the number of endpoints increases. Not something for me to worry about at this time, but I may write out my thoughts as they come to me.

### GraphQL
[The Awesome GraphQL repo](https://github.com/chentsulin/awesome-graphql) has a lot of great resources to learn from.
I really liked my experience writing GraphQL automation, I'll add some examples as well. I'll use this Github repo to pick a public set of endpoints

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


# Util and Helper Files... What do they?!
It's all well and good that I can read a tutorial and copy and paste their examples, it's another thing for me to understand what each file does. In this section I will document what each file from the tutorial does.

## TestData -> requests .py files
These files are used when constructing the request payloads. The .py files have the structure of the request payload, and values can be passed in from a utility such as Faker (to generate random values) or passed in from a data file.

I've never used this before, I have experience with the json payload being stored in a yaml file, and I could use .replace() to add data from another call, or from faker where needed.  

## TestData -> response .py files
These files are used to validate the response object has the correct fields and value type. For example, the id field in the data object is an integer. I have an example of a similar validation in my Karate repo. 

## utils -> faker.py
This utility will generate and return random values for a name, and a job. These names can then be used 

## utils -> user_client.py
This is the code to make the REST request, and supports any request method, PUT, PATCH, POST, GET, DELETE. It looks to use the logger util to dump the status to the console for observation, 

## utils -> base_client.py
Ths constructs the REST request, the user_client.py and other request files reference this file, and pass in the details.

# Copilot
I plan to explore copilot to see how it helps or hinders writing automation.

# Resources Used
Below are the resources used when investigating and setting up Playwright.
* [Getting Started - PlayWright Python and VS Code](https://playwright.dev/docs/getting-started-vscode)
* [LambdaTest - What is Playwright?](https://www.lambdatest.com/playwright)
* [Playwright Q&A](https://applitools.com/blog/top-playwright-questions-answered/)
* [PlayWright Playlist](https://www.youtube.com/watch?v=UC2wj3Bg3eM&list=PLqndseDs9rmIwtzB1i08UWkQjQhpmZhtH)
* [Testing API's with PlayWright](https://elixirautomation.medium.com/automated-api-testing-playwright-part-1-d8eea1ccf0aa)
* [API Testing Series on Medium](https://elixirautomation.medium.com/)