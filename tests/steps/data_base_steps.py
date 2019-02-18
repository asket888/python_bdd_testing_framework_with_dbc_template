from behave import step
from hamcrest import assert_that, equal_to


# account table management DB steps
@step('I create new account with "{account_name}" name using DB')
def step_impl(context, account_name):
    context.db_connection.insert_account(account_name)


@step('Account with name "{account_name}" has following column values in DB')
def step_impl(context, account_name):
    actual_values = context.db_connection.select_account_by_name(account_name)
    expected_values = {}
    for row in context.table:
        expected_values[row["column"]] = row["value"]
    for key in expected_values:
        assert_that(str(actual_values[key]), equal_to(expected_values[key]))


# custom_targeting_group table management DB steps
@step('I create new "{list_type}" targeting list with "{targeting_list_name}" name using DB')
def step_impl(context, list_type, targeting_list_name):
    context.db_connection.insert_custom_targeting_list(list_type, targeting_list_name)


@step('I assign "{targeting_list_name}" targeting list to "{account_name}" account using DB')
def step_impl(context, targeting_list_name, account_name):
    context.db_connection.update_custom_targeting_list_set_account_id(targeting_list_name, account_name)


# project table management DB steps
@step('I create new "{project_name}" project for "{account_name}" account using DB')
def step_impl(context, project_name, account_name):
    context.db_connection.insert_project(project_name, account_name)


# flight table management DB steps
@step('I create new "{flight_name}" flight for "{project_name}" project using DB')
def step_impl(context, flight_name, project_name):
    context.db_connection.insert_flight(flight_name, project_name)


@step('Flight with name "{flight_name}" has following column values in DB')
def step_impl(context, flight_name):
    actual_values = context.db_connection.select_flight_by_name(flight_name)
    expected_values = {}
    for row in context.table:
        expected_values[row["column"]] = row["value"]
    for key in expected_values:
        assert_that(str(actual_values[key]), equal_to(expected_values[key]))
