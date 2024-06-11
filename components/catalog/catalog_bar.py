from playwright.sync_api import Page

from page_factory.title import Title
import settings as s


class CatalogBar:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.catalog_header = Title(page, locator=s.CATALOG_HDR, name="Каталог title")

    def catalog_is_opened(self):
        self.catalog_header.should_be_visible()
