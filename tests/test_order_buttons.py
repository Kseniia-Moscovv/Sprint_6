import allure

from pages.main_page import MainPageYaScooter
from pages.order_page import OrderPageYaScooter
from constants.order_page_constants import OrderPageConstants


class TestOrderButtons:
    @allure.title('Header Order button test')
    @allure.description('Проверка кнопки "Заказать" в хэдере страницы')
    def test_check_header_order_button(self, driver):
        main_page = MainPageYaScooter(driver)
        order_page = OrderPageYaScooter(driver)

        main_page.click_on_header_order_button()
        order_page.wait_to_order_page_title_into_view()

        actual_title = order_page.get_order_title_text()
        assert actual_title == OrderPageConstants.ORDER_PAGE_TITLE

    @allure.title('Page Order button test')
    @allure.description('Проверка кнопки "Заказать" на странице под описанием оформления заказа')
    def test_check_page_order_button(self, driver):
        main_page = MainPageYaScooter(driver)
        order_page = OrderPageYaScooter(driver)

        main_page.scroll_to_page_order_button()
        main_page.wait_to_page_order_button_into_view()
        main_page.click_on_page_order_button()
        order_page.wait_to_order_page_title_into_view()

        actual_title = order_page.get_order_title_text()
        assert actual_title == OrderPageConstants.ORDER_PAGE_TITLE
