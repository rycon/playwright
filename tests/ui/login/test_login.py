from playwright.sync_api import expect
from utils.config_parser import get_secrets
from pages.LoginPage import LoginPage


def test_login_standard_user(setup_tear_down) -> None:
    page = setup_tear_down
    username = get_secrets("Credentials", "standard_user_username")
    password = get_secrets("Credentials", "password")
    credentials = {'username': username, 'password': password}
    
    # Login with the above credentials
    LoginPage(page).site_login(credentials)

    # Verify Inventory page loads after login.
    # expect(products_page.product_header).to_have_text("Products") # I'm getting a recursion error with this, skipping
    product_header = page.locator("[data-test=\"title\"]")
    expect(product_header).to_have_text("Products")


# Negative Test Cases
def test_login_invalid_user(setup_tear_down) -> None:
    page = setup_tear_down
    password = get_secrets("Credentials", "password")
    credentials = {'username': "invalid_user", 'password': password}
    
    # Login with the above credentials
    LoginPage(page).site_login(credentials)

    # Verify error message for invalid username and password.
    expected_error_message = "Epic sadface: Username and password do not match any user in this service"

    # TODO I need to figure out how to use the POM for these.
    error_locator = page.locator("[data-test=\"error\"]")
    expect(error_locator).to_have_text(expected_error_message)
    #example with partial text matching
    expect(error_locator).to_contain_text("Username and password do not match")


def test_login_missing_password(setup_tear_down) -> None:
    page = setup_tear_down
    username = get_secrets("Credentials", "standard_user_username")
    credentials = {'username': username, 'password': ""}

    # Login with the above credentials
    LoginPage(page).site_login(credentials)

    # Verify error message for invalid username and password.
    expected_error_message = "Epic sadface: Password is required"
    error_locator = page.locator("[data-test=\"error\"]")
    expect(error_locator).to_have_text(expected_error_message)


def test_login_missing_username(setup_tear_down) -> None:
    page = setup_tear_down
    password = get_secrets("Credentials", "password")
    credentials = {'username': "", 'password': password}

    # Login with the above credentials
    LoginPage(page).site_login(credentials)

    # Verify error message for invalid username and password.
    expected_error_message = "Epic sadface: Username is required"
    error_locator = page.locator("[data-test=\"error\"]")
    expect(error_locator).to_have_text(expected_error_message)


def test_login_no_credentials(setup_tear_down) -> None:
    page = setup_tear_down
    credentials = {'username': "", 'password': ""}

    # Login with the above credentials
    LoginPage(page).site_login(credentials)

    # Verify error message for invalid username and password.
    expected_error_message = "Username is required"
    error_locator = page.locator("[data-test=\"error\"]")
    expect(error_locator).to_contain_text(expected_error_message)
