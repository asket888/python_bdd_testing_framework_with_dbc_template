import time
import zipfile
from os import listdir, remove, path


def download_wait(path_to_downloads, expected_file_extension):
    seconds = 0
    wait = True
    while wait and seconds < 5:
        time.sleep(1)
        if [file_name for file_name in listdir(path_to_downloads) if file_name.endswith(expected_file_extension)]:
            wait = False
        seconds += 1
    if wait:
        raise TimeoutError("File wasn't downloaded successfully")


def get_files_from_directory(path_to_downloads, expected_file_extension):
    return [file_name for file_name in listdir(path_to_downloads) if file_name.endswith(expected_file_extension)]


def unzip_file(path_to_downloads, path_to_zip_file):
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(path_to_downloads)
    zip_ref.close()


def cleanup_directory(path_to_downloads):
    for file_name in listdir(path_to_downloads):
        if not file_name.endswith(".gitignore"):
            remove(path.join(path_to_downloads, file_name))
