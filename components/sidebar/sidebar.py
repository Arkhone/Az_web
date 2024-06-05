from playwright.sync_api import Page

from components.modal.search_modal import SearchModal
from page_factory.link import Link


class Sidebar:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.search_modal = SearchModal(page)

        self.welcome_link = Link(page, locator="//a[text()='Welcome']", name='Welcome')
        self.ambassadors_link = Link(page,  locator="//a[text()='Ambassadors']", name='Ambassadors')

    def visit_welcome(self):
        self.welcome_link.click()

    def visit_ambassadors(self):
        self.ambassadors_link.click()
