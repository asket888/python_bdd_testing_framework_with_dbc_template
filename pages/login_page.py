from hamcrest import assert_that, equal_to, equal_to_ignoring_case

from pages.base_page import BasePage


class LoginPage(BasePage):

    _LOGIN_PAGE_BLOCK = "//h4[text()='Please fill in the fields below to sign in:']/.."
    _LOGIN_ENTER_EMAIL_INPUT = "//input[@id='inputEmail']"
    _LOGIN_ENTER_PASS_INPUT = "//input[@id='inputPassword']"
    _LOGIN_SIGN_IN_BUTTON = "//button[@type='submit']"
    _LOGIN_ERROR_MESSAGE = "//span[@class='error-text']"

    def __init__(self, context):
        super().__init__(context.browser, context.env)
        self.env = context.env

    def goto_app_and_login_with_correct_credentials(self):
        try:
            self.goto_url(self.env["app_url"])
            self.assert_that_login_page_is_presented()
            self.fill(self._LOGIN_ENTER_EMAIL_INPUT, self.env["app_user"])
            self.fill(self._LOGIN_ENTER_PASS_INPUT, self.env["app_pwd"])
            self.click(self._LOGIN_SIGN_IN_BUTTON)
        except Exception:
            self.take_screenshot('before_all_setup')
            raise PermissionError('Can not login to application. Please check the screenshot in ./artifacts dir')

    def login_with_correct_credentials(self):
        self.fill(self._LOGIN_ENTER_EMAIL_INPUT, self.env["app_user"])
        self.fill(self._LOGIN_ENTER_PASS_INPUT, self.env["app_pwd"])
        self.click(self._LOGIN_SIGN_IN_BUTTON)

    def login_with_specific_credentials(self, login, password):
        self.fill(self._LOGIN_ENTER_EMAIL_INPUT, login)
        self.fill(self._LOGIN_ENTER_PASS_INPUT, password)

    def click_sing_in_button(self):
        self.click(self._LOGIN_SIGN_IN_BUTTON)

    def assert_that_login_page_is_presented(self):
        assert_that(self.if_element_displayed(self._LOGIN_PAGE_BLOCK), equal_to(True))

    def assert_that_error_message_is_presented(self, message):
        assert_that(self.get_text(self._LOGIN_ERROR_MESSAGE), equal_to_ignoring_case(message))

    def assert_that_sign_in_button_enabled(self):
        assert_that(bool(self.if_element_enabled(self._LOGIN_SIGN_IN_BUTTON)), equal_to(True))
