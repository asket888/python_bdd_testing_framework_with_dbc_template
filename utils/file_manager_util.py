import time
import zipfile
from os import listdir, remove, path
from hamcrest import assert_that, equal_to
from pandas import read_csv


def cleanup_directory(path_to_downloads):
    for file_name in listdir(path_to_downloads):
        if not file_name.endswith(".gitignore"):
            remove(path.join(path_to_downloads, file_name))


def download_wait(path_to_downloads, file_extension):
    seconds = 0
    wait = True
    while wait and seconds < 5:
        time.sleep(1)
        if get_files_with_extension_from_directory(path_to_downloads, file_extension):
            wait = False
        seconds += 1
    if wait:
        raise TimeoutError("File wasn't downloaded successfully")


def unzip_file(path_to_downloads, path_to_zip_file):
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(path_to_downloads)
    zip_ref.close()


def read_csv_file_data_without_columns(path_to_file, excluded_columns):
    actual_data = read_csv(path_to_file)
    return actual_data.drop(excluded_columns, axis=1)


def get_files_with_extension_from_directory(path_to_downloads, file_extension):
    return [file_name for file_name in listdir(path_to_downloads) if file_name.endswith(file_extension)]


def get_file_fullname_by_substring(path_to_downloads, substring, file_extension):
    actual_file_name = ""
    downloaded_files = get_files_with_extension_from_directory(path_to_downloads, file_extension)
    for file_name in downloaded_files:
        if substring in file_name:
            actual_file_name = file_name
    return actual_file_name


def assert_that_csv_files_are_equal(expected_file_name, expected_data, actual_data):
    for row in range(actual_data.shape[0]):
        actual_row = actual_data.iloc[row].tolist()
        expected_row = expected_data.iloc[row].tolist()
        for row_id, _ in enumerate(actual_row):
            assert_that(str(actual_row[row_id]), equal_to(str(expected_row[row_id])), "Mismatch in " +
                        expected_file_name + " file. Incorrect '" + expected_data.columns.values[row_id] + "' value " +
                        "in row #" + str(row))
