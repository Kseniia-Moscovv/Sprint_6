import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

from constants.constants import Constants
from locators.main_page_locators import MainPageYaScooterLocators


@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(Constants.MAIN_PAGE_URL)
    driver.find_element(*MainPageYaScooterLocators.cookie_button).click()
    yield driver
    driver.quit()
