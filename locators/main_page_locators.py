from selenium.webdriver.common.by import By


class MainPageYaScooterLocators:
    cookie_button = [By.CLASS_NAME, 'App_CookieButton__3cvqF']
    faq_section = [By.CLASS_NAME, 'Home_FourPart__1uthg']
    main_page_title = [By.XPATH, './/div[@class="Home_Header__iJKdX"][contains(text(), "Самокат"][last()]']

    @staticmethod
    def get_faq_question(index):
        return By.ID, 'accordion__heading-' + index

    @staticmethod
    def get_faq_answer(index):
        return By.XPATH, './/div[@id="accordion__panel-' + index + '"]/p[1]'

    header_order_button = [By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[@class="Button_Button__ra12g"]']
    page_order_button = [By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']



