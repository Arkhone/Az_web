from pages.home_page import HomePage
from settings import BASE_URL


class TestBasket:
    def test_open_basket(self, home_page: HomePage):
        home_page.visit(BASE_URL)
        home_page.main_head_bar.open_basket()
        home_page.basket.basket_is_opened()
