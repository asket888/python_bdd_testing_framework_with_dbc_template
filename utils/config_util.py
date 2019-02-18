import json
from os import path

from selenium import webdriver
from selenium.webdriver import chrome, firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

_PATH_TO_DOWNLOADS = path.join(path.dirname(path.dirname(path.abspath(__file__))), "resources/downloads")


def _read_config(file, tag):
    with open(file) as json_file:
        as_dict = json.load(json_file)[tag]
        return as_dict


def get_browser(browser):
    if browser.upper() == "CH":
        options = chrome.options.Options()
        options.add_experimental_option('prefs', {'download.default_directory': _PATH_TO_DOWNLOADS})
        return webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                chrome_options=options)
    elif browser.upper() == "CH_HL":
        options = chrome.options.Options()
        options.add_argument("--window-size=1600x900")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.headless = True
        return webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                                chrome_options=options)
    elif browser.upper() == "FF":
        options = firefox.options.Options()
        return webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                 firefox_options=options)
    elif browser.upper() == "FF_HL":
        options = firefox.options.Options()
        options.add_argument("--window-size=1600x900")
        options.headless = True
        return webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                                 firefox_options=options)
    else:
        raise TypeError("Unexpected Browser. Check your behave.ini file variables")


def get_env(env):
    if env.upper() == "DEV":
        return _read_config("config.json", "DEV")
    elif env.upper() == "UAT":
        return _read_config("config.json", "UAT")
    elif env.upper() == "LOCALHOST":
        return _read_config("config.json", "LOCALHOST")
    else:
        raise TypeError("Unexpected Env. Check your behave.ini file variables")
