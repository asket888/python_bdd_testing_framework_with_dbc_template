import re
from os import path

from hamcrest import assert_that, equal_to, has_item

from utils.file_manager_util import cleanup_directory, download_wait, unzip_file, read_csv_file_data_without_columns,\
    get_files_with_extension_from_directory, get_file_fullname_by_substring, assert_that_csv_files_are_equal


class FileManager:
    # static xpath. used as is
    _PATH_TO_DOWNLOADS_FOLDER = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'resources/downloads/')
    _PATH_TO_SDF_REFERENCE_FOLDER = path.join(path.dirname(path.dirname(path.abspath(__file__))), 'resources/csv/sdf/')
    _CSV_COLUMNS_TO_EXCLUDE = ['Line Item Id', 'Io Id', 'Name', 'Start Date', 'End Date', 'Details']

    def __init__(self, context):
        self.env = context.env

    def cleanup_downloads_directory(self):
        cleanup_directory(self._PATH_TO_DOWNLOADS_FOLDER)

    def assert_that_csv_file_was_downloaded_successfully(self, expected_file_name):
        download_wait(self._PATH_TO_DOWNLOADS_FOLDER, ".csv")
        downloaded_files = get_files_with_extension_from_directory(self._PATH_TO_DOWNLOADS_FOLDER, ".csv")
        downloaded_files = [re.sub('[-].*', '', x) for x in downloaded_files]

        assert_that(downloaded_files, has_item(expected_file_name))

    def assert_that_sdf_files_were_downloaded_successfully(self, expected_files):
        download_wait(self._PATH_TO_DOWNLOADS_FOLDER, ".zip")
        zip_file_fullname = get_file_fullname_by_substring(self._PATH_TO_DOWNLOADS_FOLDER, ".zip", ".zip")
        unzip_file(self._PATH_TO_DOWNLOADS_FOLDER, '/'.join([self._PATH_TO_DOWNLOADS_FOLDER, zip_file_fullname]))

        downloaded_files = get_files_with_extension_from_directory(self._PATH_TO_DOWNLOADS_FOLDER, ".csv")
        downloaded_files = [re.sub('^([^_]+)_', '', x) for x in downloaded_files]

        for file in expected_files:
            assert_that(downloaded_files, has_item(file))

    def assert_that_csv_file_contains_row_num(self, expected_file_name, expected_row_num):
        actual_file_name = get_file_fullname_by_substring(self._PATH_TO_DOWNLOADS_FOLDER, expected_file_name, ".csv")

        with open(''.join([self._PATH_TO_DOWNLOADS_FOLDER, actual_file_name])) as file:
            assert_that(sum(1 for line in file), equal_to(int(expected_row_num)))

    def assert_that_downloaded_csv_equals_to_reference(self, expected_file_name):
        expected_file_path = self._PATH_TO_DOWNLOADS_FOLDER + expected_file_name
        expected_data = read_csv_file_data_without_columns(expected_file_path, self._CSV_COLUMNS_TO_EXCLUDE)

        actual_file_path = self._PATH_TO_DOWNLOADS_FOLDER + get_file_fullname_by_substring(
            self._PATH_TO_DOWNLOADS_FOLDER, expected_file_name, ".csv")
        actual_data = read_csv_file_data_without_columns(actual_file_path, self._CSV_COLUMNS_TO_EXCLUDE)
        assert_that_csv_files_are_equal(expected_file_name, expected_data, actual_data)
