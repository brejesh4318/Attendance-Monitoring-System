import pytest
from config import settings
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {**browser_type_launch_args, "headless": settings.HEADLESS, "slow_mo": settings.SLOW_MO}


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)
