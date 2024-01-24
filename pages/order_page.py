import allure

from pages.base_page import BasePageYaScooter
from locators.order_page_locators import OrderPageYaScooterLocators


class OrderPageYaScooter(BasePageYaScooter):
    @allure.step('Ожидание заголовка страницы с формой заказа')
    def wait_to_order_page_title_into_view(self):
        self.visibility_of_element_located(OrderPageYaScooterLocators.order_page_title)

    @allure.step('Получение текста заголовка страницы с формой заказа')
    def get_order_title_text(self):
        return self.get_element_text(OrderPageYaScooterLocators.order_page_title)

    @allure.step('Ввод значения в поле "Имя"')
    def input_name(self, name):
        self.type_input_text(OrderPageYaScooterLocators.name_input, name)

    @allure.step('Ввод значения в поле "Фамилия"')
    def input_surname(self, surname):
        self.type_input_text(OrderPageYaScooterLocators.surname_input, surname)

    @allure.step('Ввод значения в поле "Адрес"')
    def input_address(self, address):
        self.type_input_text(OrderPageYaScooterLocators.address_input, address)

    @allure.step('Выбор станции метро')
    def click_on_metro_station(self, index):
        self.click_on_element(OrderPageYaScooterLocators.metro_station_input)
        metro_station = self.find_element(OrderPageYaScooterLocators.get_metro_station_option(index))
        self.scroll_into_view(metro_station)
        metro_station.click()

    @allure.step('Ввод значения в поле "Телефон"')
    def input_phone(self, phone):
        self.type_input_text(OrderPageYaScooterLocators.phone_input, phone)

    @allure.step('Клик по кнопке "Далее" под формой заказа')
    def click_on_next_button(self):
        self.click_on_element(OrderPageYaScooterLocators.next_button)

    @allure.step('Ожидание заголовка страницы с формой "Про аренду"')
    def wait_to_rent_title_into_view(self):
        self.visibility_of_element_located(OrderPageYaScooterLocators.rent_form_tittle)

    @allure.step('Выбор даты начала аренды')
    def input_delivery_date(self, date):
        self.type_input_text(OrderPageYaScooterLocators.delivery_date, date)
        self.press_enter(OrderPageYaScooterLocators.delivery_date)

    @allure.step('Выбор срока аренды')
    def input_rent_time(self, rent_time):
        self.click_on_element(OrderPageYaScooterLocators.rent_time_dropdown)
        self.click_on_element(OrderPageYaScooterLocators.get_rent_time(rent_time))

    @allure.step('Выбор цвета самоката')
    def choose_scooter_colour(self, colour_id):
        self.click_on_element(OrderPageYaScooterLocators.choose_scooter_colour(colour_id))

    @allure.step('Ввод значения в поле "Комментарий для курьера"')
    def input_comment(self, comment_text):
        self.type_input_text(OrderPageYaScooterLocators.comment_input, comment_text)

    @allure.step('Клик по кнопке "Заказать" под формой "Про аренду"')
    def click_on_order_button(self):
        self.click_on_element(OrderPageYaScooterLocators.order_button)

    @allure.step('Ожидание модального окна подтверждения заказа')
    def wait_to_approve_order_modal(self):
        self.visibility_of_element_located(OrderPageYaScooterLocators.approve_order_modal)

    @allure.step('Клик по кнопке "Да" в модальном окне подтверждения заказа')
    def click_on_confirm_order_button(self):
        self.click_on_element(OrderPageYaScooterLocators.confirm_order_button)

    @allure.step('Ожидание модального окна с подтверждением оформления заказа')
    def wait_to_approved_order_modal(self):
        self.visibility_of_element_located(OrderPageYaScooterLocators.approved_order_modal)

    @allure.step('Получение заголовка модального окна с подтверждением оформления заказа')
    def get_approved_order_title_text(self):
        return self.get_element_text(OrderPageYaScooterLocators.approved_order_modal)

    @allure.step('Заполнение формы "Для кого самокат"')
    def fill_in_client_form(self, name, surname, address, metro_station, phone):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.click_on_metro_station(metro_station)
        self.input_phone(phone)
        self.click_on_next_button()
        self.wait_to_rent_title_into_view()

    @allure.step('Заполнение формы "Про аренду"')
    def fill_in_rent_form(self, date, rent_time, colour_id, comment_text):
        self.input_delivery_date(date)
        self.input_rent_time(rent_time)
        self.choose_scooter_colour(colour_id)
        self.input_comment(comment_text)
        self.click_on_order_button()
        self.wait_to_approve_order_modal()

    @allure.step('Подтверждение заказа')
    def approve_order(self):
        self.click_on_confirm_order_button()
        self.wait_to_approved_order_modal()
