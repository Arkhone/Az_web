import allure
from playwright.sync_api import Page, Response

from components.navigation.navbar import Navbar
from components.sidebar.sidebar import Sidebar


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.navbar = Navbar(page)
        self.sidebar = Sidebar(page)

    def visit(self, url: str) -> Response | None:
        with allure.step(f'Opening the url "{url}"'):
            return self.page.goto(url, wait_until='networkidle')

    def reload(self) -> Response | None:
        with allure.step(f'Reloading page with url "{self.page.url}"'):
            return self.page.reload(wait_until='domcontentloaded')
