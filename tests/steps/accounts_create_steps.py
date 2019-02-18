from behave import step


@step('I fill Create Account popup fields with following values')
def step_impl(context):
    input_value_dict = {}
    for row in context.table:
        input_value_dict[row["input"]] = row["value"]
    context.account_page.fill_all_fields(input_value_dict)


@step('I fill "{input_name}" field by "{value}" value on Create Account popup')
def step_impl(context, input_name, value):
    context.account_page.fill_one_field(input_name, value)


@step('I click [{button_name}] button on Create Account popup')
def step_impl(context, button_name):
    context.account_page.click_button(button_name)


@step('"{expected_message}" error message appears under "{input_name}" input on Create Account popup')
def step_impl(context, expected_message, input_name):
    context.account_page.assert_that_validation_message_is_presented(input_name, expected_message)


@step('[{button_name}] button is disabled on Create Account popup')
def step_impl(context, button_name):
    context.account_page.assert_that_button_is_disabled(button_name)


@step('"{account_name}" is not presented on Accounts page')
def step_impl(context, account_name):
    context.account_page.assert_that_account_with_title_not_exist(account_name)


@step('I click [Create Account] button on Accounts page')
def step_impl(context):
    context.account_page.click_create_account_button()
