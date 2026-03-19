import allure
from pytest_check import check

from framework.actions.alerts_actions import AlertsActions


@allure.feature("Alerts")
class TestAlerts:

    @allure.title("Confirmation box: accept alert")
    def test_confirmation_box_accept(self, driver):
        alerts_actions = AlertsActions(driver)
        with allure.step("Open confirmation box page"):
            alerts_actions.open_confirmation_box_page()
        with allure.step("Click confirmation box button"):
            alerts_actions.click_confirmation_box_button()
        with allure.step("Verify alert text"):
            actual_alert_text = alerts_actions.get_alert_text()
            expected_alert_text = "Select Ok or Cancel"
            with check:
                assert actual_alert_text == expected_alert_text, (
                    f"Expected alert text to be '{expected_alert_text}', but got '{actual_alert_text}'"
                )
        with allure.step("Accept alert"):
            alerts_actions.accept_alert()
        with allure.step("Verify result text after accepting alert"):
            actual_result = alerts_actions.get_confirmation_result_text()
            expected_result = "Ok"
            with check:
                assert actual_result == expected_result, (
                    f"Expected result text to be '{expected_result}', but got '{actual_result}'"
                )

    @allure.title("Confirmation box: dismiss alert")
    def test_confirmation_box_dismiss(self, driver):
        alerts_actions = AlertsActions(driver)
        with allure.step("Open confirmation box page"):
            alerts_actions.open_confirmation_box_page()
        with allure.step("Click confirmation box button"):
            alerts_actions.click_confirmation_box_button()
        with allure.step("Verify alert text"):
            actual_alert_text = alerts_actions.get_alert_text()
            expected_alert_text = "Select Ok or Cancel"
            with check:
                assert actual_alert_text == expected_alert_text, (
                    f"Expected alert text to be '{expected_alert_text}', but got '{actual_alert_text}'"
                )
        with allure.step("Dismiss alert"):
            alerts_actions.dismiss_alert()
        with allure.step("Verify result text after dismissing alert"):
            actual_result = alerts_actions.get_confirmation_result_text()
            expected_result = "Cancel"
            with check:
                assert actual_result == expected_result, (
                    f"Expected result text to be '{expected_result}', but got '{actual_result}'"
                )