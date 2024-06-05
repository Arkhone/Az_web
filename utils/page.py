from playwright.sync_api import Page
from utils.logger import logger

browser = Page()
class Page():

    def execute_script(self, script: str, *args) -> "Page":
        """Executes javascript in the current window or frame"""
        logger.info(
            "Page.execute_script() - Execute javascript `%s` into the Browser", script
        )

        self.webdriver.execute_script(script, *args)
        return self
