from hamcrest import assert_that, equal_to, equal_to_ignoring_case, has_item

from pages.base_page import BasePage


class ProjectCreatePage(BasePage):

    # static xpath. used as is
    CREATE_PROJECT_BUTTON = "//button[contains(text(),'Create Project') and @type='button']"

    # dynamic xpath. depends from parameter in method signature ({} will be replaced by method parameter)
    _CREATE_PROJECT_BUTTON_TEMPLATE = "//sd-card-title/h5[text()='{project_name}']"
    _CREATE_PROJECT_DATA_TEMPLATE = "//sd-card-title/h5[text()='{project_name}']/../../..//h5"
    _CREATE_PROJECT_INPUT_TEMPLATE = "//div[contains(text(),'{input_name}')]/../..//input"
    _CREATE_PROJECT_SELECT_FIRST_VALUE_TEMPLATE = "//sd-option[1]//*[contains(text(),'{value}')]"
    _CREATE_PROJECT_ERROR_MESSAGE_TEMPLATE = "//div[contains(text(),'{input_name}')]/../..//sd-error"

    def __init__(self, context):
        super().__init__(context.browser, context.env)

    def click_button(self, button_name):
        self.click(self._CREATE_PROJECT_BUTTON_TEMPLATE.format(button_name=button_name))

    def click_create_project_button(self):
        self.click(self.CREATE_PROJECT_BUTTON)

    def click_project_card(self, project_name):
        self.click(self._CREATE_PROJECT_BUTTON_TEMPLATE.format(project_name=project_name))

    def fill_one_field(self, input_name, value):
        self.fill(self._CREATE_PROJECT_INPUT_TEMPLATE.format(input_name=input_name), value)
        self.tab(self._CREATE_PROJECT_INPUT_TEMPLATE.format(input_name=input_name))

    def fill_all_fields(self, data_dict):
        self.fill(self._CREATE_PROJECT_INPUT_TEMPLATE.format(input_name="Project Name"), data_dict["Project Name"])
        self.select(self._CREATE_PROJECT_INPUT_TEMPLATE.format(input_name="Account"),
                    data_dict["Account"],
                    self._CREATE_PROJECT_SELECT_FIRST_VALUE_TEMPLATE.format(value=data_dict["Account"]))
        self.select(self._CREATE_PROJECT_INPUT_TEMPLATE.format(input_name="DV360 Advertiser"),
                    data_dict["DV360 Advertiser"],
                    self._CREATE_PROJECT_SELECT_FIRST_VALUE_TEMPLATE.format(value=data_dict["DV360 Advertiser"]))

    def assert_that_project_with_title_exist(self, project_name):
        self.if_element_visible(self._CREATE_PROJECT_BUTTON_TEMPLATE.format(project_name=project_name))

    def assert_that_project_with_title_not_exist(self, project_name):
        self.if_element_not_visible(self._CREATE_PROJECT_BUTTON_TEMPLATE.format(project_name=project_name))

    def assert_that_project_card_contains_correct_data(self, project_name, expected_values):
        actual_values = self.get_text_from_all_elements(self._CREATE_PROJECT_DATA_TEMPLATE
                                                        .format(project_name=project_name))
        for value in expected_values:
            assert_that(actual_values, has_item(value))

    def assert_that_button_is_disabled(self, button_name):
        assert_that(bool(self.if_element_enabled(self._CREATE_PROJECT_BUTTON_TEMPLATE.format(button_name=button_name))),
                    equal_to(False))

    def assert_that_validation_message_is_presented(self, input_name, message):
        assert_that(self.get_text(self._CREATE_PROJECT_ERROR_MESSAGE_TEMPLATE.format(input_name=input_name)),
                    equal_to_ignoring_case(message))
