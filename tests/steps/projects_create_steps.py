from behave import step


@step('I click [{button_name}] button in Create Project popup')
def step_impl(context, button_name):
    context.project_page.click_button(button_name)


@step("I fill Create Project popup fields with following values")
def step_impl(context):
    input_value_dict = {}
    for row in context.table:
        input_value_dict[row["input"]] = row["value"]
    context.project_page.fill_all_fields(input_value_dict)


@step('I fill "{input_name}" field by "{value}" value in Create Project popup')
def step_impl(context, input_name, value):
    context.project_page.fill_one_field(input_name, value)


@step('"{expected_message}" error message appears under "{input_name}" input in Create Project popup')
def step_impl(context, expected_message, input_name):
    context.project_page.assert_that_validation_message_is_presented(input_name, expected_message)


@step("[{button_name}] button is disabled in Create Project popup")
def step_impl(context, button_name):
    context.project_page.assert_that_button_is_disabled(button_name)


@step('I click [Add Flight] button on Project Card page')
def step_impl(context):
    context.project_page.click_add_flight_button()


@step('I click [{button_name}] button in "{section_name}" section on Project Card page')
def step_impl(context, button_name, section_name):
    context.project_page.click_button_on_project_card_page(button_name, section_name)


@step('Add Flight message presented in Flight section on Project Card page')
def step_impl(context):
    context.project_page.assert_that_flight_section_is_empty()


@step('"{project_name}" is not presented on Projects page')
def step_impl(context, project_name):
    context.project_page.assert_that_project_with_title_not_exist(project_name)


@step('I click [Create Project] button on Projects page')
def step_impl(context):
    context.project_page.click_create_project_button()


@step('I click on "{project_name}" card Projects page')
def step_impl(context, project_name):
    context.project_page.assert_that_project_with_title_exist(project_name)
    context.project_page.click_project_card(project_name)


@step('"{project_name}" project card presented on the page and contains following data')
def step_impl(context, project_name):
    expected_values = []
    for row in context.table:
        expected_values.append(row["value"])
    context.project_page.assert_that_project_card_contains_correct_data(project_name, expected_values)
