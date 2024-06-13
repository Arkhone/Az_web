import pytest

from pages.home_page import HomePage
from pages.playwright_languages_page import PlaywrightLanguagesPage
from settings import BASE_URL


class TestSearch:
    @pytest.mark.parametrize('keyword', ['python'])
    def test_search(
        self,
        keyword: str,
        home_page: HomePage,
        playwright_languages_page: PlaywrightLanguagesPage
    ):
        home_page.visit(BASE_URL)
        home_page.navbar.open_search()
        home_page.navbar.search_modal.find_result(
            keyword, result_number=0
        )

        playwright_languages_page.language_present(language=keyword)
