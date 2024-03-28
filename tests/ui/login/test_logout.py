from playwright.sync_api import Page, expect


def test_login_logout_standard_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.click("[data-test=\"login-button\"]")

    # Open the hamburger menu and logout
    page.click("#react-burger-menu-btn")
    page.click("[data-test=\"logout-sidebar-link\"]")
    login_button = page.locator("[data-test=\"login-button\"]")
    expect(login_button).to_be_visible()
