from selenium.webdriver.support.ui import WebDriverWait

from framework.actions.base_actions import BaseActions
from framework.modules.alerts import Alerts


class AlertsActions(BaseActions):

    def open_confirmation_box_page(self):
        self.open_page(Alerts.CONFIRMATION_BOX_URL)

    def click_confirmation_box_button(self):
        self.click_with_js(Alerts.alerts_click_btn)

    def wait_for_alert(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until(lambda d: d.switch_to.alert)

    def get_alert_text(self, timeout=5):
        alert = self.wait_for_alert(timeout)
        return alert.text

    def accept_alert(self, timeout=5):
        alert = self.wait_for_alert(timeout)
        alert.accept()

    def dismiss_alert(self, timeout=5):
        alert = self.wait_for_alert(timeout)
        alert.dismiss()

    def get_confirmation_result_text(self):
        return self.get_text(Alerts.alerts_result_text)