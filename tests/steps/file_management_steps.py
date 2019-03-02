from behave import step


@step("Clean up downloads directory")
def step_impl(context):
    context.file_manager.cleanup_downloads_directory()


@step('"{file_name}" file was downloaded successfully')
def step_impl(context, file_name):
    context.file_manager.assert_that_csv_file_was_downloaded_successfully(file_name)


@step("Following files were downloaded successfully")
def step_impl(context):
    file_names = []
    for row in context.table:
        file_names.append(row["file_name"])
    context.file_manager.assert_that_sdf_files_were_downloaded_successfully(file_names)


@step('Downloaded "{file_name}" file contains "{row_num}" row(s)')
def step_impl(context, file_name, row_num):
    context.file_manager.assert_that_csv_file_contains_row_num(file_name, row_num)


@step('"{flight_type}" Flight "{sdf_file_name}" file contains same data like reference file')
def step_impl(context, flight_type, sdf_file_name):
    context.file_manager.assert_that_downloaded_csv_equals_to_reference(flight_type, sdf_file_name)
