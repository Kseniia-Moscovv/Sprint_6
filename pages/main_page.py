from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageYaScooterLocators


class MainPageYaScooter:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_faq_section(self):
        element = self.driver.find_element(*MainPageYaScooterLocators.faq_section)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_to_faq_section_into_view(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageYaScooterLocators.faq_section))

    def wait_to_answer_into_view(self, index):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageYaScooterLocators.get_faq_answer(index)))

    def click_on_question(self, question):
        self.driver.find_element(*MainPageYaScooterLocators.get_faq_question(question)).click()

    def wait_for_question_to_be_clickable(self, question):
        (WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(MainPageYaScooterLocators.get_faq_question(question))))

    def get_answer_text(self, answer):
        return self.driver.find_element(*MainPageYaScooterLocators.get_faq_answer(answer)).text

    def click_on_header_order_button(self):
        self.driver.find_element(*MainPageYaScooterLocators.header_order_button).click()

    def scroll_to_page_order_button(self):
        element = self.driver.find_element(*MainPageYaScooterLocators.page_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_to_page_order_button_into_view(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageYaScooterLocators.page_order_button))

    def click_on_page_order_button(self):
        self.driver.find_element(*MainPageYaScooterLocators.page_order_button).click()

    def wait_to_page_order_button(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageYaScooterLocators.page_order_button))

    def get_main_page_order_button_text(self):
        return self.driver.find_element(*MainPageYaScooterLocators.page_order_button).text


