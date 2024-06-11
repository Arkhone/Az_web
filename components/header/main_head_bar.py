from playwright.sync_api import Page

from page_factory.button import Button
from components.catalog.catalog_bar import CatalogBar
import settings as s


class MainHeadBar:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.catalog_bar = CatalogBar(page)

        self.catalog_button = Button(page, s.CATALOG_BTN, name="Каталог button")

    def open_catalog(self):
        self.catalog_button.should_be_visible()

        self.catalog_button.hover()
        self.catalog_button.click()

        self.catalog_bar.catalog_is_opened()
