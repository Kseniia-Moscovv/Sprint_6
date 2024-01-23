import allure
import pytest

from constants.faq_answers_constants import FaqAnswersConstants
from pages.main_page import MainPageYaScooter


class TestFaqAnswers:
    @pytest.mark.parametrize('index, answer', FaqAnswersConstants.FAQ_DATA)
    @allure.title('FAQ test')
    @allure.description('Проверка раздела с вопросами о главном и ответами на них с помощью параметризации')
    def test_check_answer_text(self, driver, index, answer):
        main_page = MainPageYaScooter(driver)

        main_page.scroll_to_faq_section()
        main_page.wait_to_faq_section_into_view()
        main_page.wait_for_question_to_be_clickable(index)
        main_page.click_on_question(index)
        main_page.wait_to_answer_into_view(index)

        actual_answer = main_page.get_answer_text(index)
        assert actual_answer == answer
