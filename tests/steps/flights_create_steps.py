from behave import step


@step('I fill Flight Name field by "{value}" value on Add Flight page')
def step_impl(context, value):
    context.flight_page.fill_name_field(value)


@step('I fill Add Flight page fields with following values')
def step_impl(context):
    input_value_dict = {}
    for row in context.table:
        input_value_dict[row["input"]] = row["value"]
    context.flight_page.fill_all_fields(input_value_dict)


@step('I click [{button_name}] button on Add Flight page')
def step_impl(context, button_name):
    context.flight_page.click_button(button_name)


@step("[{button_name}] button is disabled on Add Flight page")
def step_impl(context, button_name):
    context.flight_page.assert_that_button_is_disabled(button_name)


@step('"{expected_message}" error message appears under "{input_name}" input on Add Flight page')
def step_impl(context, expected_message, input_name):
    context.flight_page.assert_that_validation_message_is_presented(input_name, expected_message)


@step('Following data presented in "{section_name}" section on Flight Overview page')
def step_impl(context, section_name):
    expected_values = []
    for row in context.table:
        expected_values.append(row["value"])
    context.flight_page.assert_that_section_contains_correct_data(section_name, expected_values)
