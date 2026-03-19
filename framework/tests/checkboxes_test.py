import allure
from pytest_check import check
from framework.actions.checkboxes_actions import CheckboxesActions


@allure.feature("Checkboxes")
class TestCheckboxes:
    @allure.title("Single checkbox: select checkbox and submit")
    def test_single_checkbox_submit(self, driver):
        checkboxes_actions = CheckboxesActions(driver)
        with allure.step("Open single checkbox page"):
            checkboxes_actions.open_single_checkbox_page()
        with allure.step("Select checkbox"):
            checkboxes_actions.select_single_checkbox()
        with allure.step("Click submit"):
            checkboxes_actions.click_submit()
        with allure.step("Verify result text"):
            actual_result = checkboxes_actions.get_checkbox_result_text()
            expected_result = "select me or not"
            with check:
                assert actual_result == expected_result, (
                    f"Expected result text to be '{expected_result}', but got '{actual_result}'"
                )

    @allure.title("Multiple checkboxes: select one checkbox and submit")
    def test_multiple_checkboxes_submit_one_checkbox(self, driver):
        checkboxes_actions = CheckboxesActions(driver)
        with allure.step("Open multiple checkboxes page"):
            checkboxes_actions.open_multiple_checkboxes_page()
        with allure.step("Select checkbox 'one'"):
            checkboxes_actions.select_checkbox_one()
        with allure.step("Click submit"):
            checkboxes_actions.click_submit()
        with allure.step("Verify result text"):
            actual_result = checkboxes_actions.get_checkbox_result_text()
            expected_result = "one"
            with check:
                assert actual_result == expected_result, (
                    f"Expected result text to be '{expected_result}', but got '{actual_result}'"
                )

    @allure.title("Multiple checkboxes: select all checkboxes and submit")
    def test_multiple_checkboxes_submit_all_checkboxes(self, driver):
        checkboxes_actions = CheckboxesActions(driver)
        with allure.step("Open multiple checkboxes page"):
            checkboxes_actions.open_multiple_checkboxes_page()
        with allure.step("Select checkboxes 'one', 'two', 'three'"):
            checkboxes_actions.select_multiple_checkboxes("one", "two", "three")
        with allure.step("Click submit"):
            checkboxes_actions.click_submit()
        with allure.step("Verify result text"):
            actual_result = checkboxes_actions.get_checkbox_result_text()
            expected_result = "one, two, ree"
            with check:
                assert actual_result == expected_result, (
                    f"Expected result text to be '{expected_result}', but got '{actual_result}'"
                )