"""Log in and leave the browser open so you can see / use the page.

Run:  python run.py        (close the browser window or press Ctrl+C to finish)
"""
from playwright.sync_api import sync_playwright

from config import settings
from pages.login_page import LoginPage


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=settings.SLOW_MO)
        page = browser.new_page(no_viewport=True)
        login = LoginPage(page)
        login.open()
        login.login()
        print("Logged in:", page.url)
        # TODO: add your automation steps here

        try:
            page.wait_for_event("close", timeout=0)  # wait until the window is closed
        except KeyboardInterrupt:
            pass
        browser.close()


if __name__ == "__main__":
    main()
