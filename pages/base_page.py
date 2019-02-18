from os import path

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    _IMPLICIT_TIMEOUT = 0
    _EXPLICIT_TIMEOUT = 30

    def __init__(self, browser, env):
        self.env = env
        self.browser = browser
        self.browser.implicitly_wait(BasePage._IMPLICIT_TIMEOUT)
        self.explicitly_wait = WebDriverWait(browser, BasePage._EXPLICIT_TIMEOUT)

    # element wait methods
    def _is_element_visible(self, locator):
        self.explicitly_wait.until(expected_conditions.visibility_of_element_located((By.XPATH, locator)),
                                   message=f"'{locator}' element doesn't appear on the page")

    def _is_element_not_visible(self, locator):
        self.explicitly_wait.until(expected_conditions.invisibility_of_element_located((By.XPATH, locator)),
                                   message=f"'{locator}' element doesn't disappear from the page")

    def _is_element_clickable(self, locator):
        self.explicitly_wait.until(expected_conditions.element_to_be_clickable((By.XPATH, locator)),
                                   message=f"'{locator}' element is not clickable on the page")

    # element status methods
    def if_element_visible(self, locator):
        self._is_element_visible(locator)

    def if_element_not_visible(self, locator):
        self._is_element_not_visible(locator)

    def if_element_displayed(self, locator):
        self._is_element_visible(locator)
        return self.browser.find_element_by_xpath(locator).is_displayed()

    def if_element_selected(self, locator):
        self._is_element_visible(locator)
        return self.browser.find_element_by_xpath(locator).is_selected()

    def if_element_enabled(self, locator):
        self._is_element_visible(locator)
        return self.browser.find_element_by_xpath(locator).is_enabled()

    # elements set actions methods
    def click(self, locator):
        self._is_element_clickable(locator)
        self.browser.find_element_by_xpath(locator).click()

    def clear(self, locator):
        self._is_element_visible(locator)
        self.browser.find_element_by_xpath(locator).clear()

    def fill(self, locator, value):
        self._is_element_visible(locator)
        self.browser.find_element_by_xpath(locator).clear()
        self.browser.find_element_by_xpath(locator).send_keys(value)

    def select(self, select_locator, value, value_text):
        self.fill(select_locator, value)
        self.click(value_text)

    def tab(self, locator):
        self._is_element_visible(locator)
        self.browser.find_element_by_xpath(locator).send_keys(Keys.TAB)

    # elements get actions method
    def get_text(self, locator):
        self._is_element_visible(locator)
        return self.browser.find_element_by_xpath(locator).text

    def get_text_from_all_elements(self, locator):
        self._is_element_visible(locator)
        elements = self.browser.find_elements_by_xpath(locator)
        elements_text = [i.text for i in elements]
        return elements_text

    def get_attribute_value(self, locator, attribute):
        self._is_element_visible(locator)
        return self.browser.find_element_by_xpath(locator).get_attribute(attribute)

    def get_attribute_from_all_elements(self, locator, attribute):
        self._is_element_visible(locator)
        elements = self.browser.find_elements_by_xpath(locator)
        elements_attribute_value = [i.get_attribute(attribute) for i in elements]
        return elements_attribute_value

    def get_css_property_value(self, locator, css_property):
        self._is_element_visible(locator)
        return self.browser.find_element_by_xpath(locator).value_of_css_property(css_property)

    # overall_steps browser actions
    def goto_url(self, url):
        self.browser.get(url)

    def scroll_up(self):
        self.browser.execute_script("window.scrollTo(0, 0);")

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def upload_file(self, locator, file_path):
        self.browser.find_element_by_xpath(locator).send_keys(file_path)

    def refresh_current_page(self):
        self.browser.refresh()

    def clean_browser_cookies_and_storage(self):
        self.browser.execute_script("window.localStorage.clear();")
        self.browser.delete_all_cookies()

    def take_screenshot(self, screenshot_title):
        self.browser.save_screenshot(path.join(path.dirname(path.dirname(path.realpath(__file__))))
                                     + '/artifacts/[' + screenshot_title + '].png')

    def quit(self):
        self.browser.quit()
