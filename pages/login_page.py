from playwright.sync_api import expect

from config import settings
from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = page.locator("input[formcontrolname='email']")
        self.password_input = page.locator("input[formcontrolname='password']")
        # "Forgot Password" is also a submit button, so match by name
        self.login_button = page.get_by_role("button", name="Login", exact=True)

    def open(self):
        self.goto(settings.LOGIN_URL)
        expect(self.username_input).to_be_visible()

    def login(self, username: str = settings.USERNAME, password: str = settings.PASSWORD):
        # the form is pre-filled with demo values, so fill() overwrites them
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        self.page.wait_for_url("**/dashboard**")
