import allure
from pytest_check import check

from framework.actions.inputs_actions import InputsActions


@allure.feature("Simple Input")
class TestSimpleInput:
    def test_submit_valid_text_input(self, driver):
        input_page = InputsActions(driver)
        valid_text = "qa_test_sveta_input_123"
        with allure.step("Open Simple Input page"):
            input_page.open_simple_input_page()
        with allure.step("Enter valid text string"):
            input_page.type_text_string(valid_text)
        with allure.step("Submit text string by pressing Enter"):
            input_page.submit_text_string_with_enter()
        with allure.step("Check that result box is displayed"):
            with check:
                assert input_page.is_result_box_visible(timeout=5), \
                    "Result box was not displayed."
        with allure.step("Check result title text"):
            with check:
                assert input_page.get_result_title_text() == "Your input was:", \
                    "Result title text is incorrect."
        with allure.step("Check submitted text in result box"):
            with check:
                assert input_page.get_result_text() == valid_text, \
                    "Submitted text in result box is incorrect."

    def test_submit_one_character(self, driver):
        input_page = InputsActions(driver)
        invalid_text = "n"
        with allure.step("Open Simple Input page"):
            input_page.open_simple_input_page()
        with allure.step("Enter one character into text input"):
            input_page.type_text_string(invalid_text)
        with allure.step("Submit text string by pressing Enter"):
            input_page.submit_text_string_with_enter()
        with allure.step("Check that validation error is displayed"):
            with check:
                assert input_page.is_text_string_error_visible(timeout=5), \
                    "Validation error message was not displayed."
        with allure.step("Check validation error text"):
            with check:
                assert input_page.get_text_string_error_message() == "Please enter 2 or more characters", \
                    "Validation error text is incorrect."

    def test_submit_26_characters(self, driver):
        input_page = InputsActions(driver)
        invalid_text = "qa_test_s_1234567890AB"
        with allure.step("Open Simple Input page"):
            input_page.open_simple_input_page()
        with allure.step("Enter text longer than 25 characters"):
            input_page.type_text_string(invalid_text)
        with allure.step("Submit text string by pressing Enter"):
            input_page.submit_text_string_with_enter()
        with allure.step("Check that max length validation error is displayed"):
            with check:
                assert input_page.is_text_string_error_visible(timeout=5), \
                    "Validation error for max length was not displayed."
        with allure.step("Check max length validation error text"):
            with check:
                assert input_page.get_text_string_error_message() == "Please enter no more than 25 characters", \
                    "Max length validation error text is incorrect."