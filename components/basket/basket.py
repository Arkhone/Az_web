from playwright.sync_api import Page

from page_factory.button import Button
import settings as s


class Basket:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.make_order_btn = Button(page, s.MAKE_ORDER_BTN, name="Оформить заказ")

    def basket_is_opened(self):
        self.make_order_btn.should_be_visible()
