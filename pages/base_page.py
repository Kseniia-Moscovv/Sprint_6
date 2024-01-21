from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageYaScooterLocators
from selenium.webdriver.support import expected_conditions as EC

from locators.yandex_dzen_page_locators import YaDzenLocators


class BasePageYaScooter:
    def __init__(self, driver):
        self.driver = driver

    def click_on_yandex_logo(self):
        self.driver.find_element(*BasePageYaScooterLocators.yandex_logo).click()

    def wait_to_load_dzen_page(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(YaDzenLocators.YANDEX_DZEN_NEWS_BUTTON))

    def get_news_button_name(self):
        return self.driver.find_element(*YaDzenLocators.YANDEX_DZEN_NEWS_BUTTON).text

    def click_on_scooter_logo(self):
        self.driver.find_element(*BasePageYaScooterLocators.scooter_logo).click()
