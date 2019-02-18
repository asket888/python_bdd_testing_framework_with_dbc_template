import allure

from db.db_connection import DbConnection
from pages.login_page import LoginPage
from pages.main_menu_page import MainMenuPage
from pages.flight_page import FlightCreatePage
from pages.account_page import AccountCreatePage
from pages.project_page import ProjectCreatePage

from utils.config_util import get_env, get_browser


def before_all(context):
    # setup global variables
    context.env = get_env(context.config.userdata['env'])
    context.browser = get_browser(context.config.userdata['browser'])
    # setup page_objects
    context.db_connection = DbConnection(context)
    context.main_menu_page = MainMenuPage(context)
    context.login_page = LoginPage(context)
    context.flight_page = FlightCreatePage(context)
    context.account_page = AccountCreatePage(context)
    context.project_page = ProjectCreatePage(context)

    # login to application
    context.login_page.goto_app_and_login_with_correct_credentials()


def before_scenario(context, scenario):
    context.db_connection.cleanup_test_data_from_db()


def after_scenario(context, scenario):
    if scenario.status == 'failed':
        allure.attach(context.browser.get_screenshot_as_png(),
                      attachment_type=allure.attachment_type.PNG)


def after_all(context):
    context.db_connection.cleanup_test_data_from_db()
    context.db_connection.close_conn()
    context.browser.quit()
