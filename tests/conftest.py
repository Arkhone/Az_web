import pytest
from playwright.sync_api import Page, sync_playwright

from pages.home_page import HomePage
from pages.playwright_languages_page import PlaywrightLanguagesPage


@pytest.fixture(scope='function')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        yield chromium.new_page()


@pytest.fixture(scope='function')
def home_page(chromium_page: Page) -> HomePage:
    return HomePage(chromium_page)


@pytest.fixture(scope='function')
def playwright_languages_page(chromium_page: Page) -> PlaywrightLanguagesPage:
    return PlaywrightLanguagesPage(chromium_page)
