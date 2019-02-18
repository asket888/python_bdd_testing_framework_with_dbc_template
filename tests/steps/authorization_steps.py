from behave import step


@step('Login page appears')
def step_impl(context):
    context.login_page.assert_that_login_page_is_presented()


@step('I login with correct credentials')
def step_impl(context):
    context.login_page.login_with_correct_credentials()


@step('I login with following "{login}" and "{password}"')
def step_impl(context, login, password):
    context.login_page.login_with_specific_credentials(login, password)


@step('[Sign In] button is enabled')
def step_impl(context):
    context.login_page.assert_that_sign_in_button_enabled()


@step('I click [Sign In] button')
def step_impl(context):
    context.login_page.click_sing_in_button()


@step('"{expected_message}" error message appears on Login page')
def step_impl(context, expected_message):
    context.login_page.assert_that_error_message_is_presented(expected_message)
