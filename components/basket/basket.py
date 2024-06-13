import allure
from playwright.sync_api import Page
from page_factory.button import Button
import settings as s


class Basket:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.make_order_btn = Button(page, s.MAKE_ORDER_BTN, name="Оформить заказ")

    def basket_is_opened(self, url):
        self.make_order_btn.should_be_visible()
        with allure.step(f'Checking that "{self.page.url}" is equal to "{url}"'):
            assert self.page.url == url




