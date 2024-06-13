from playwright.sync_api import Page

from page_factory.button import Button
from components.catalog.catalog_bar import CatalogBar
import settings as s


class MainHeadBar:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.catalog_bar = CatalogBar(page)

        self.catalog_btn = Button(page, s.CATALOG_BTN, name="Каталог")
        self.coin_btn = Button(page, s.COIN_BTN, name="Коины")
        self.orders_btn = Button(page, s.ORDERS_BTN, name="Заказы")
        self.favorites_btn = Button(page, s.FAVORITES_BTN, name="Избранное")
        self.basket_btn = Button(page, s.BASKET_BTN, name="Корзина")
        self.entrance_btn = Button(page, s.ENTRANCE_BTN, name="Вход")

    def open_catalog(self):
        self.catalog_btn.should_be_visible()

        self.catalog_btn.hover()
        self.catalog_btn.click()

        self.catalog_bar.catalog_is_opened()

    def open_basket(self):
        self.basket_btn.should_be_visible()
        self.basket_btn.hover()
        self.basket_btn.click()
