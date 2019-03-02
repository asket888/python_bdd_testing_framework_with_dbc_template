import re

from os import path
from hamcrest import assert_that, equal_to, has_item

from pages.base_page import BasePage
from utils import file_manager_util


class MainMenuPage(BasePage):

    # static xpath. used as is
    _PATH_TO_DOWNLOADS_FOLDER = path.join(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))),
                                          'resources/downloads/')

    # dynamic xpath. depends from parameter in method signature ({} will be replaced by method parameter)
    _PAGE_TITLE_TEMPLATE = "//h3[text()='{expected_title}']"
    _PAGE_TAB_TEMPLATE = "//a[contains(text(),'{page_name}')]"
    _PAGE_POPUP_TITLE_TEMPLATE = "//h3/sd-modal-header[text()='{popup_title}']"
    _PAGE_ACTIVE_TAB_TEMPLATE = "//sd-nav-left//a[contains(text(),'{expected_title}') and @class='active']"

    def __init__(self, context):
        super().__init__(context.browser, context.env)

    def refresh_page(self):
        self.refresh_current_page()

    def clean_browser_cookies(self):
        self.clean_browser_cookies_and_storage()

    def goto_url_page_link(self, page_link):
        self.goto_url("".join([self.env["app_url"], page_link.lower()]))

    def click_page_tab_button(self, page_link):
        self.click(self._PAGE_TAB_TEMPLATE.format(page_name=page_link))

    def assert_that_tab_is_active(self, expected_title):
        self.if_element_visible(self._PAGE_ACTIVE_TAB_TEMPLATE.format(expected_title=expected_title))

    def assert_that_title_displays(self, expected_title):
        self.if_element_visible(self._PAGE_TITLE_TEMPLATE.format(expected_title=expected_title))

    def assert_that_popup_displays(self, expected_title):
        self.if_element_visible(self._PAGE_POPUP_TITLE_TEMPLATE.format(popup_title=expected_title))

    def assert_that_csv_file_was_downloaded_successfully(self, expected_file_name):
        file_manager_util.download_wait(self._PATH_TO_DOWNLOADS_FOLDER, ".csv")
        downloaded_files = file_manager_util.get_files_with_extension_from_directory(self._PATH_TO_DOWNLOADS_FOLDER,
                                                                                     ".csv")
        downloaded_files = [re.sub('[-].*', '', x) for x in downloaded_files]

        assert_that(downloaded_files, has_item(expected_file_name))

    def assert_that_csv_file_contains_row_num(self, expected_file_name, expected_row_num):
        actual_file_name = ""
        downloaded_files = file_manager_util.get_files_with_extension_from_directory(self._PATH_TO_DOWNLOADS_FOLDER,
                                                                                     ".csv")
        for file_name in downloaded_files:
            if expected_file_name in file_name:
                actual_file_name = file_name
        with open(''.join([self._PATH_TO_DOWNLOADS_FOLDER, actual_file_name])) as file:
            assert_that(sum(1 for line in file), equal_to(int(expected_row_num)))

    def cleanup_downloads_directory(self):
        file_manager_util.cleanup_directory(self._PATH_TO_DOWNLOADS_FOLDER)
