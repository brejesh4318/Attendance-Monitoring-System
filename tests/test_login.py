import re
from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_login(login_page: LoginPage):
    login_page.open()
    login_page.login()
    expect(login_page.page).to_have_url(re.compile(r"/dashboard"))

