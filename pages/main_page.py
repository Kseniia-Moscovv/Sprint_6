import allure

from locators.main_page_locators import MainPageYaScooterLocators
from pages.base_page import BasePageYaScooter


class MainPageYaScooter(BasePageYaScooter):
    @allure.step('Скролл к разделу "Вопросы о важном"')
    def scroll_to_faq_section(self):
        element = self.find_element(MainPageYaScooterLocators.faq_section)
        self.scroll_into_view(element)

    @allure.step('Ожидание появления раздела "Вопросы о важном" в области видимости')
    def wait_to_faq_section_into_view(self):
        self.visibility_of_element_located(MainPageYaScooterLocators.faq_section)

    @allure.step('Ожидание появления ответа на вопрос в области видимости')
    def wait_to_answer_into_view(self, index):
        self.visibility_of_element_located(MainPageYaScooterLocators.get_faq_answer(index))

    @allure.step('Клик на вопрос в разделе "Вопросы о важном"')
    def click_on_question(self, question):
        self.click_on_element(MainPageYaScooterLocators.get_faq_question(question))

    @allure.step('Ожидание кликабельности элемента "вопрос" в разделе "Вопросы о важном"')
    def wait_for_question_to_be_clickable(self, question):
        self.element_to_be_clickable(MainPageYaScooterLocators.get_faq_question(question))

    @allure.step('Получение текста ответа на вопрос')
    def get_answer_text(self, answer):
        return self.get_element_text(MainPageYaScooterLocators.get_faq_answer(answer))

    @allure.step('Клик по кнопке "Заказать" в хэдере страницы')
    def click_on_header_order_button(self):
        self.click_on_element(MainPageYaScooterLocators.header_order_button)

    @allure.step('Скролл до кнопки "Заказать" под описанием оформления заказа')
    def scroll_to_page_order_button(self):
        element = self.find_element(MainPageYaScooterLocators.page_order_button)
        self.scroll_into_view(element)

    @allure.step('Ожидание появления кнопки "Заказать" в области видимости')
    def wait_to_page_order_button_into_view(self):
        self.visibility_of_element_located(MainPageYaScooterLocators.page_order_button)

    @allure.step('Клик по кнопке "Заказать" под описанием оформления заказа')
    def click_on_page_order_button(self):
        self.click_on_element(MainPageYaScooterLocators.page_order_button)

    @allure.step('Ожидание появления кнопки "Заказать" в области видимости')
    def wait_to_page_order_button(self):
        self.visibility_of_element_located(MainPageYaScooterLocators.page_order_button)

    @allure.step('Получение текста (названия) в кнопке "Заказать"')
    def get_main_page_order_button_text(self):
        return self.get_element_text(MainPageYaScooterLocators.page_order_button)
