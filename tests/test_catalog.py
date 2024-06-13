from pages.home_page import HomePage
from settings import BASE_URL


class TestCatalog:
    def test_open_catalog(self, home_page: HomePage):
        home_page.visit(BASE_URL)
        home_page.main_head_bar.open_catalog()
        home_page.catalog_bar.catalog_is_opened()

