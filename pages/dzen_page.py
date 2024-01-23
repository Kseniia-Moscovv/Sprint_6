import allure

from locators.yandex_dzen_page_locators import YaDzenLocators
from pages.base_page import BasePageYaScooter


class DzenPageYaScooter(BasePageYaScooter):
    @allure.step('Ожидание появления кнопки "Новости" на странице Yandex Dzen')
    def wait_to_load_dzen_page(self):
        self.visibility_of_element_located(YaDzenLocators.YANDEX_DZEN_NEWS_BUTTON)

    @allure.step('Получение текста (названия) в кнопке "Новости" на странице Yandex Dzen')
    def get_news_button_name(self):
        return self.get_element_text(YaDzenLocators.YANDEX_DZEN_NEWS_BUTTON)
