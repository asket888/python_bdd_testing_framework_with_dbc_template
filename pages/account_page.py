from hamcrest import assert_that, equal_to, equal_to_ignoring_case

from pages.base_page import BasePage


class AccountCreatePage(BasePage):

    # dynamic xpath. depends from parameter in method signature ({} will be replaced by method parameter)
    _CREATE_ACCOUNT_BUTTON_TEMPLATE = "//div[@class='sd-modal-content']//button[text()='{button_name}']"
    _CREATE_ACCOUNT_INPUT_TEMPLATE = "//div[text()='{input_name}']/../following-sibling::div//input"
    _CREATE_ACCOUNT_SELECT_FIRST_VALUE_TEMPLATE = "//sd-option[1]//*[contains(text(),'{value}')]"
    _CREATE_ACCOUNT_ERROR_MESSAGE_TEMPLATE = "//div[text()='{input_name}']/../following-sibling::div//sd-error"
    _CREATE_ACCOUNT_MARGIN_CALC_BUTTON_TEMPLATE = "//span[contains(text(),'{button_name}')]/.."

    def __init__(self, context):
        super().__init__(context.browser, context.env)

    def click_button(self, button_name):
        self.click(self._CREATE_ACCOUNT_BUTTON_TEMPLATE.format(button_name=button_name))

    def fill_one_field(self, input_name, value):
        self.fill(self._CREATE_ACCOUNT_INPUT_TEMPLATE.format(input_name=input_name), value)
        self.tab(self._CREATE_ACCOUNT_INPUT_TEMPLATE.format(input_name=input_name))

    def fill_all_fields(self, data_dict):
        self.fill(self._CREATE_ACCOUNT_INPUT_TEMPLATE.format(input_name="Account Name"),
                  data_dict["Account Name"])
        self.select(self._CREATE_ACCOUNT_INPUT_TEMPLATE.format(input_name="Vertical"),
                    data_dict["Vertical"],
                    self._CREATE_ACCOUNT_SELECT_FIRST_VALUE_TEMPLATE.format(value=data_dict["Vertical"]))
        self.fill(self._CREATE_ACCOUNT_INPUT_TEMPLATE.format(input_name="Default Margin"),
                  data_dict["Default Margin"])
        self.click(self._CREATE_ACCOUNT_MARGIN_CALC_BUTTON_TEMPLATE.format(
            button_name=data_dict["Margin Calculation"]))

    def assert_that_account_with_title_not_exist(self, account_name):
        self.if_element_not_visible(self._CREATE_ACCOUNT_BUTTON_TEMPLATE.format(account_name=account_name))

    def assert_that_validation_message_is_presented(self, input_name, message):
        assert_that(self.get_text(
            self._CREATE_ACCOUNT_ERROR_MESSAGE_TEMPLATE.format(input_name=input_name)), equal_to_ignoring_case(message))

    def assert_that_button_is_disabled(self, button_name):
        assert_that(bool(self.if_element_enabled(self._CREATE_ACCOUNT_BUTTON_TEMPLATE.format(button_name=button_name))),
                    equal_to(False))
