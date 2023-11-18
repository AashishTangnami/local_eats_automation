from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
# Add other browser options as needed

class DriverFactory:
    @staticmethod
    def get_driver(browser_name, options=None):
        if browser_name.lower() == "chrome":
            return DriverFactory.get_chrome_driver(options)
        elif browser_name.lower() == "firefox":
            return DriverFactory.get_firefox_driver(options)
        else:
            raise ValueError(f"Browser '{browser_name}' not supported")

    @staticmethod
    def get_chrome_driver(options=None):
        if not isinstance(options, ChromeOptions):
            options = ChromeOptions()
        return webdriver.Chrome(options=options)

    @staticmethod
    def get_firefox_driver(options=None):
        if options is None:
            options = FirefoxOptions()
        return webdriver.Firefox(options=options)
    
    @staticmethod
    def get_safari_driver(options=None):
        if options is None:
            options = SafariOptions()
        return webdriver.Safari(options=options)

    @staticmethod
    def get_edge_driver(options=None):
        if options is None:
            options = EdgeOptions()
        return webdriver.Edge(options=options)
# Path: FareEats/utils/fareats_bot.py