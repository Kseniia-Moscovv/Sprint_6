from selenium.webdriver.common.by import By


class OrderPageYaScooterLocators:
    order_page_title = [By.XPATH, './/div[@class="Order_Header__BZXOb"][text()="Для кого самокат"]']
    name_input = [By.XPATH, './/div[@class="Input_InputContainer__3NykH"]/input[@placeholder="* Имя"]']
    surname_input = [By.XPATH, './/div[@class="Input_InputContainer__3NykH"]/input[@placeholder="* Фамилия"]']
    address_input = [By.XPATH, './/div[@class="Input_InputContainer__3NykH"]/input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_station_input = [By.CLASS_NAME, 'select-search__input']
    phone_input = [By.XPATH, './/div[@class="Input_InputContainer__3NykH"]/input[@placeholder="* Телефон: на него позвонит курьер"]']
    next_button = [By.CLASS_NAME, 'Button_Middle__1CSJM']
    rent_form_tittle = [By.XPATH, './/div[@class="Order_Header__BZXOb"][text()="Про аренду"]']
    delivery_date = [By.XPATH, './/div[@class="react-datepicker__input-container"]/input[@placeholder="* Когда привезти самокат"]']
    rent_time_dropdown = [By.CLASS_NAME, 'Dropdown-root']
    black_colour_scooter_checkbox = [By.ID, 'black']
    grey_colour_scooter_checkbox = [By.ID, 'grey']
    comment_input = [By.XPATH, './/div[@class="Input_InputContainer__3NykH"]/input[@placeholder="Комментарий для курьера"]']
    order_button = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']
    approve_order_modal = [By.XPATH, './/div[@class="Order_ModalHeader__3FDaJ"][text()="Хотите оформить заказ?"]']
    confirm_order_button = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Да"]']
    approved_order_modal = [By.XPATH, './/div[@class="Order_ModalHeader__3FDaJ"][text()="Заказ оформлен"]']

    @staticmethod
    def get_metro_station_option(index):
        return [By.XPATH, './/ul[@class="select-search__options"]/li[@data-index=' + index + ']']

    @staticmethod
    def get_rent_time(rent_time):
        return [By.XPATH, './/div[@class="Dropdown-option"][text()="' + rent_time + '"]']

    @staticmethod
    def choose_scooter_colour(colour_id):
        return [By.ID, colour_id]
