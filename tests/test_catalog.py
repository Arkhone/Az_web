from pages.playwright_home_page import PlaywrightHomePage
from settings import BASE_URL


class TestCatalog:
    def test_catalog(self, playwright_home_page: PlaywrightHomePage):
        playwright_home_page.visit(BASE_URL)
        playwright_home_page.main_head_bar.open_catalog()
        playwright_home_page.catalog_bar.catalog_is_opened()
gi