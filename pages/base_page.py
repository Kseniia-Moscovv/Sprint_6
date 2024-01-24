from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from locators.base_page_locators import BasePageYaScooterLocators


class BasePageYaScooter:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.find_element(locator).click()

    def get_element_text(self, locator):
        return self.find_element(locator).text

    def type_input_text(self, locator, text):
        input_element = self.find_element(locator)
        input_element.click()
        input_element.send_keys(text)

    def press_enter(self, locator):
        element = self.find_element(locator)
        element.send_keys(Keys.ENTER)

    def visibility_of_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def element_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_window(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def click_on_yandex_logo(self):
        self.click_on_element(BasePageYaScooterLocators.yandex_logo)

    def click_on_scooter_logo(self):
        self.click_on_element(BasePageYaScooterLocators.scooter_logo)
