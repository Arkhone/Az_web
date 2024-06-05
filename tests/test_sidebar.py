import pytest

from pages.playwright_home_page import PlaywrightHomePage
from pages.playwright_languages_page import PlaywrightLanguagesPage
from settings import BASE_URL


class TestSidebar:
    @pytest.mark.parametrize('keyword', ['Ambassadors'])
    def test_search(
        self,
        keyword: str,
        playwright_languages_page: PlaywrightLanguagesPage
    ):
        playwright_languages_page.visit(BASE_URL)
        playwright_languages_page.navbar.open_search()
        playwright_languages_page.navbar.search_modal.find_result(
            'Python', result_number=0
        )
        playwright_languages_page.sidebar.visit_ambassadors()
        playwright_languages_page.language_present(language=keyword)
