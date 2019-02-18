from hamcrest import assert_that, equal_to, equal_to_ignoring_case, contains_string, has_item

from pages.base_page import BasePage


class FlightCreatePage(BasePage):

    # static xpath. used as is
    _CREATE_FLIGHT_FLIGHT_NAME_INPUT = "//input[@data-test-id='flightName']"
    _CREATE_FLIGHT_BULK_UPLOAD_ERROR_MESSAGE = "//div[@class='error']/h5"

    # dynamic xpath. depends from parameter in method signature ({} will be replaced by method parameter)
    _CREATE_FLIGHT_BUTTON_TEMPLATE = "//button[contains(text(),'{button_name}')] | "
    _CREATE_FLIGHT_CARD_SECTION_TEMPLATE = "//h3[text()='{section_name}']/../../../..//h5/.."
    _CREATE_FLIGHT_INPUT_ERROR_MESSAGE_TEMPLATE = "//div[text()=' {input_name} ']/../..//sd-error"

    def __init__(self, context):
        super().__init__(context.browser, context.env)

    def click_button(self, button_name):
        self.click(self._CREATE_FLIGHT_BUTTON_TEMPLATE.format(button_name=button_name))

    def fill_name_field(self, value):
        self.fill(self._CREATE_FLIGHT_FLIGHT_NAME_INPUT, value)
        self.tab(self._CREATE_FLIGHT_FLIGHT_NAME_INPUT)

    def fill_all_fields(self, data_dict):
        self.fill(self._CREATE_FLIGHT_FLIGHT_NAME_INPUT, data_dict["Flight Name"])
        self.click(self._CREATE_FLIGHT_BUTTON_TEMPLATE.format(button_name=data_dict["Location"]))
        self.click(self._CREATE_FLIGHT_BUTTON_TEMPLATE.format(button_name=data_dict["Language"]))
        self.click(self._CREATE_FLIGHT_BUTTON_TEMPLATE.format(button_name=data_dict["Ad Format"]))

    def assert_that_section_contains_correct_data(self, section_name, expected_values):
        actual_values = self.get_text_from_all_elements(self._CREATE_FLIGHT_CARD_SECTION_TEMPLATE
                                                        .format(section_name=section_name))
        for value in expected_values:
            assert_that(actual_values, has_item(value))

    def assert_that_button_is_disabled(self, button_name):
        assert_that(bool(self.if_element_enabled(self._CREATE_FLIGHT_BUTTON_TEMPLATE.format(button_name=button_name))),
                    equal_to(False))

    def assert_that_validation_message_is_presented(self, input_name, message):
        assert_that(self.get_text(self._CREATE_FLIGHT_INPUT_ERROR_MESSAGE_TEMPLATE.format(input_name=input_name)),
                    equal_to_ignoring_case(message))

    def assert_that_error_message_is_presented(self, message):
        assert_that(self.get_text(self._CREATE_FLIGHT_BULK_UPLOAD_ERROR_MESSAGE), contains_string(message))
