import allure
import pytest

from constants.order_page_constants import OrderPageConstants
from pages.main_page import MainPageYaScooter
from pages.order_page import OrderPageYaScooter


class TestCreateOrder:
    @allure.title('Order creation test')
    @allure.description('Проверка создания заказа с разными наборами данных с помощью параметризации')
    @pytest.mark.parametrize('name, surname, address, metro_station, phone, delivery_date, rent_time, scooter_colour, comment', OrderPageConstants.CLIENT_DATA)
    def test_check_to_create_order(self, driver, name, surname, address, metro_station, phone, delivery_date, rent_time, scooter_colour, comment):
        main_page = MainPageYaScooter(driver)
        order_page = OrderPageYaScooter(driver)

        main_page.click_on_header_order_button()
        order_page.wait_to_order_page_title_into_view()
        order_page.fill_in_client_form(name, surname, address, metro_station, phone)
        order_page.fill_in_rent_form(delivery_date, rent_time, scooter_colour, comment)
        order_page.approve_order()
        actual_approved_order_title = order_page.get_approved_order_title_text()

        assert OrderPageConstants.APPROVED_ORDER_MODAL_TITLE in actual_approved_order_title
