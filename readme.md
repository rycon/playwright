# Playwright
The intention is to learn Playwright. To get a new project setup from scratch, to get a PoC working, and document best practices. I have no prior experience with Playwright, and I have little experience writing UI Automation.

- [Playwright](#playwright)
  - [About Playwright](#about-playwright)
  - [About This Repository](#about-this-repository)
    - [Folder Structure](#folder-structure)
    - [Test Strategy](#test-strategy)
  - [Install and Initial Setup](#install-and-initial-setup)
    - [New Project Setup](#new-project-setup)
    - [Existing Project - User Setup](#existing-project---user-setup)
      - [Tools](#tools)
      - [VSCode Extensions](#vscode-extensions)
      - [VSCode Settings](#vscode-settings)
  - [Resources Used](#resources-used)

## About Playwright
Playwright is an opensource automation framework developed by Microsoft. Playwright is cross browser, cross platform, supports multiple programming languages, and support UI and API automation. For this PoC I've chosen Typescript as that's seems to be the preffered language.

One of the benefits of Playwright over Selenium is Playwrights approach to making the tests mmore resiliant. Playwright handles waits automatically removing the need to manually add and tweak.It handles dynamic pages which waits for the element to load, and then performs the assertion. It will also automcatically retry a test assertion that has failed, before setting the error state.

Playwright also supports testing across browser processes, meaning across browser tabs, and browser profiles. Meaning, you could have one tab with the application, and another tab another application. Allowing you to enter data into one app, and seeing it replicated in another.

Playwright also has some built in tool as well, such as recodring interaction and creating a test, and some tools to be investigate and debug failures.

Playwright also supports parallel test execution. This is handled by the test runner, such as Pytest or Jest.

## About This Repository
This repository will function as a template and starting place for new Playwright projects. It will also contain a Proof of Concept to outline how Playwright works, and will contain training material, and a best practice guide. 

Ideally all projects within the organization that are using Playwright follow the same setup and coding styles. This will allow people to move across projexts with minimal ramp up time, allow easier understanding of the automation, and allow people from across projects to help one another.

Playwright can handle UI and API automation. I'm investigating to see if Playwright is a good fit for API automation, if so, does it make sense it keep them in the same repo, if so, how to best set that up. I suspect they will remain in the same repo, in different folders, and tags will be used to specify which tests to execute at run time.

### Folder Structure

### Test Strategy
Looking to setup tests in a way where the test code is made simple, and test scenarios are data driven. The idea would be to write one test, reference a data file, and have the test scenarios within the data...

## Install and Initial Setup
### New Project Setup
1. Starting a new project is simple, create a new Git repo for your project, and clone this repository into it. 
2. Next we will need to change the project name, and a few other configuration details
3.   

### Existing Project - User Setup
Playwright only needs a few tools installed to get started.

[Download and Install nodeJS LTS](https://nodejs.org/en/download) on your system. 64-bit is the mostly likely version you'll need. While installing on Windows, make sure the "Add to PATH" option is set to yes. On MacOS or Linux, you'll need to ensure that your PATH is updated. 

There is also an option to install additional tools, I selected this, and the latest version of python was installed, as well as a few dotnet fixes, and a few VSCode plugins. I'm uncertain if this was needed.

Next verify the install, open your terminal or powershell and type:

```bash
node -v
v20.9.0
```

```bash
npm -v
10.1.0
```

Next, [download and install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Depending on where the repo is stored, you can also download their desktop app to manage your repo.

#### Tools
* Visual Studio Code

#### VSCode Extensions


#### VSCode Settings

## Resources Used
Below are the resources used when investigating and setting up Playwright.
* [LambdaTest - What is Playwright?](https://www.lambdatest.com/playwright)
* [Playwright Q&A](https://applitools.com/blog/top-playwright-questions-answered/)