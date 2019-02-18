from behave import step


@step('I refresh browser page')
def step_impl(context):
    context.main_menu_page.refresh_page()


@step('I delete all browser cookies')
def step_impl(context):
    context.main_menu_page.clean_browser_cookies()


@step('I go to "{page_name}" url page')
def step_impl(context, page_name):
    context.main_menu_page.goto_url_page_link(page_name)


@step('"{expected_tab_name}" tab is active in Main Menu')
def step_impl(context, expected_tab_name):
    context.main_menu_page.assert_that_tab_is_active(expected_tab_name)


@step('"{expected_title}" title appears on the page')
def step_impl(context, expected_title):
    context.main_menu_page.assert_that_title_displays(expected_title)


@step('"{popup_name}" popup appears on the page')
def step_impl(context, popup_name):
    context.main_menu_page.assert_that_popup_displays(popup_name)


@step('"{file_name}" file was downloaded successfully')
def step_impl(context, file_name):
    context.main_menu_page.assert_that_csv_file_was_downloaded_successfully(file_name)


@step('"{file_name}" file contains "{row_num}" row(s)')
def step_impl(context, file_name, row_num):
    context.main_menu_page.assert_that_csv_file_contains_row_num(file_name, row_num)


@step("Clean up downloads directory")
def step_impl(context):
    context.main_menu_page.cleanup_downloads_directory()


@step('All Main Menu elements display on the page')
def step_impl(context):
    context.main_menu_page.assert_that_all_main_menu_elements_are_presented()


@step('I click "{page_name}" tab in Main Menu')
def step_impl(context, page_name):
    context.main_menu_page.click_page_tab_button(page_name)
