from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_page_locators import OrderPageYaScooterLocators
from selenium.webdriver.common.keys import Keys


class OrderPageYaScooter:
    def __init__(self, driver):
        self.driver = driver

    def wait_to_order_page_title_into_view(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(OrderPageYaScooterLocators.order_page_title))

    def get_order_title_text(self):
        return self.driver.find_element(*OrderPageYaScooterLocators.order_page_title).text

    def input_name(self, name):
        name_input = self.driver.find_element(*OrderPageYaScooterLocators.name_input)
        name_input.click()
        name_input.send_keys(name)

    def input_surname(self, surname):
        surname_input = self.driver.find_element(*OrderPageYaScooterLocators.surname_input)
        surname_input.click()
        surname_input.send_keys(surname)

    def input_address(self, address):
        address_input = self.driver.find_element(*OrderPageYaScooterLocators.address_input)
        address_input.click()
        address_input.send_keys(address)

    def click_on_metro_station(self, index):
        self.driver.find_element(*OrderPageYaScooterLocators.metro_station_input).click()
        metro_station = self.driver.find_element(*OrderPageYaScooterLocators.get_metro_station_option(index))
        self.driver.execute_script("arguments[0].scrollIntoView();", metro_station)
        metro_station.click()

    def input_phone(self, phone):
        phone_input = self.driver.find_element(*OrderPageYaScooterLocators.phone_input)
        phone_input.click()
        phone_input.send_keys(phone)

    def click_on_next_button(self):
        self.driver.find_element(*OrderPageYaScooterLocators.next_button).click()

    def wait_to_rent_title_into_view(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(OrderPageYaScooterLocators.rent_form_tittle))

    def input_delivery_date(self, date):
        delivery_date = self.driver.find_element(*OrderPageYaScooterLocators.delivery_date)
        delivery_date.click()
        delivery_date.send_keys(date)
        delivery_date.send_keys(Keys.ENTER)

    def input_rent_time(self, rent_time):
        self.driver.find_element(*OrderPageYaScooterLocators.rent_time_dropdown).click()
        self.driver.find_element(*OrderPageYaScooterLocators.get_rent_time(rent_time)).click()

    def choose_scooter_colour(self, colour_id):
        self.driver.find_element(*OrderPageYaScooterLocators.choose_scooter_colour(colour_id)).click()

    def input_comment(self, comment_text):
        comment = self.driver.find_element(*OrderPageYaScooterLocators.comment_input)
        comment.click()
        comment.send_keys(comment_text)

    def click_on_order_button(self):
        self.driver.find_element(*OrderPageYaScooterLocators.order_button).click()

    def wait_to_approve_order_modal(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(OrderPageYaScooterLocators.approve_order_modal))

    def click_on_confirm_order_button(self):
        self.driver.find_element(*OrderPageYaScooterLocators.confirm_order_button).click()

    def wait_to_approved_order_modal(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(OrderPageYaScooterLocators.approved_order_modal))

    def get_approved_order_title_text(self):
        return self.driver.find_element(*OrderPageYaScooterLocators.approved_order_modal).text

    def fill_in_client_form(self, name, surname, address, metro_station, phone):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.click_on_metro_station(metro_station)
        self.input_phone(phone)
        self.click_on_next_button()
        self.wait_to_rent_title_into_view()

    def fill_in_rent_form(self, date, rent_time, colour_id, comment_text):
        self.input_delivery_date(date)
        self.input_rent_time(rent_time)
        self.choose_scooter_colour(colour_id)
        self.input_comment(comment_text)
        self.click_on_order_button()
        self.wait_to_approve_order_modal()

    def approve_order(self):
        self.click_on_confirm_order_button()
        self.wait_to_approved_order_modal()

















