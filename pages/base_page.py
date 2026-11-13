from playwright.sync_api import Page
from config import settings


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(settings.TIMEOUT_MS)

    def goto(self, url: str):
        self.page.goto(url)
