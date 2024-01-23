import allure

from constants.main_page_constants import MainPageConstants
from constants.ya_dzen_constants import YaDzenPageConstants
from pages.base_page import BasePageYaScooter
from pages.dzen_page import DzenPageYaScooter
from pages.main_page import MainPageYaScooter
from pages.order_page import OrderPageYaScooter


class TestYaLogo:
    @allure.title('Yandex Logo button test')
    @allure.description('Проверка открытия страницы Яндекс Дзен при клике на логотип Яндекс в сервисе Яндекс Самокат')
    def test_check_header_ya_logo(self, driver):
        base_page = BasePageYaScooter(driver)
        dzen_page = DzenPageYaScooter(driver)

        base_page.click_on_yandex_logo()
        base_page.switch_to_window(1)
        dzen_page.wait_to_load_dzen_page()

        actual_name_button = dzen_page.get_news_button_name()
        assert actual_name_button == YaDzenPageConstants.YANDEX_DZEN_NEWS_BUTTON

    @allure.title('Scooter Logo button test')
    @allure.description('Проверка открытия главной страницы Яндекс Самокат при клике на логотип Самокат в хэдере')
    def test_check_header_scooter_logo(self, driver):
        base_page = BasePageYaScooter(driver)
        main_page = MainPageYaScooter(driver)
        order_page = OrderPageYaScooter(driver)

        main_page.click_on_header_order_button()
        order_page.wait_to_order_page_title_into_view()
        base_page.click_on_scooter_logo()
        main_page.scroll_to_page_order_button()
        main_page.wait_to_page_order_button_into_view()

        actual_button_name = main_page.get_main_page_order_button_text()
        assert actual_button_name == MainPageConstants.MAIN_PAGE_ORDER_BUTTON_NAME
