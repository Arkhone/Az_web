import allure

from playwright.sync_api import Page
from pages.base_page import BasePage
from page_factory.button import Button
import settings as s


class PlaywrightHomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.catalog_button = Button(page, s.CATALOG_BTN, name="Кнопку каталог")

    def open_catalog(self):
        self.catalog_button.click()

    def language_present(self, language: str):
        self.language_title.should_be_visible(language=language)
        self.language_title.should_have_text(
            language.capitalize(), language=language
        )
