

from pages.InventoryPage import InventoryPage


class LoginPage:

    def __init__(self, page):
        # Define the locators and other page elements to interact with
        self.page = page
        self._username = page.locator("[data-test=\"username\"]")
        self._password = page.locator("[data-test=\"password\"]")
        self._login_button = page.locator("[data-test=\"login-button\"]")
        self._error_message = page.locator("[data-test=\"error\"]")


    # Create methods to interact with the page
    def enter_username(self, username):
        self._username.clear()
        self._username.fill(username)


    def enter_password(self, password):
        self._password.clear()
        self._password.fill(password)


    def click_login_button(self):
        self._login_button.click()

    @ property
    def error_message(self):
        return self.error_message


    # Method to perform the login action, and returns the result to the InventoryPage class
    def site_login(self, credentials):
        self.enter_username(credentials["username"])
        self.enter_password(credentials["password"])
        self.click_login_button()
        return InventoryPage(self.page)
