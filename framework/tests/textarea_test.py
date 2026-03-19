import allure
import random
import string

from pytest_check import check
from framework.actions.textarea_actions import TextAreaActions


@allure.feature("TextArea")
class TestTextArea:

    @allure.title("Submit textarea with text")
    def test_textarea_submit_with_text(self, driver):
        textarea_actions = TextAreaActions(driver)
        random_text = ''.join(random.choices(string.ascii_letters, k=10))
        with allure.step("Open textarea page"):
            textarea_actions.open_textarea_page()
        with allure.step(f"Enter text: {random_text}"):
            textarea_actions.enter_text(random_text)
        with allure.step("Click submit"):
            textarea_actions.click_submit()
        with allure.step("Verify result text"):
            actual_result = textarea_actions.get_result_text()
            expected_result = random_text
            with check:
                assert actual_result == expected_result, (
                    f"Expected '{expected_result}', but got '{actual_result}'"
                )

    @allure.title("Submit empty textarea and verify validation message")
    def test_textarea_submit_empty(self, driver):
        textarea_actions = TextAreaActions(driver)
        with allure.step("Open textarea page"):
            textarea_actions.open_textarea_page()
        with allure.step("Click submit without entering text"):
            textarea_actions.click_submit()
        with allure.step("Verify validation message"):
            actual_message = textarea_actions.get_validation_message()
            expected_message = "Please fill out this field."
            with check:
                assert actual_message == expected_message, (
                    f"Expected validation message '{expected_message}', but got '{actual_message}'"
                )