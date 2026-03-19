import allure
from pytest_check import check

from framework.actions.simple_button_actions import ButtonsActions


@allure.feature("Buttons")
class TestButtons:
    def test_click_simple_button(self, driver):
        button_page = ButtonsActions(driver)
        with allure.step("Open Simple Button page"):
            button_page.open_simple_button_page()
        with allure.step("Click the button"):
            button_page.click_button()
        with allure.step("Check that result is displayed"):
            with check:
                assert button_page.is_result_visible(timeout=5), \
                    "Result text was not displayed."
        with allure.step("Check result text"):
            with check:
                assert button_page.get_result_text() == "Submitted", \
                    "Result text is incorrect."