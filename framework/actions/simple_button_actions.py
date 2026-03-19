from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.actions.base_actions import BaseActions
from framework.modules.simple_button import Button


class ButtonsActions(BaseActions):
    SIMPLE_BUTTON_URL = "https://www.qa-practice.com/elements/button/simple"

    def open_simple_button_page(self):
        self.driver.get(self.SIMPLE_BUTTON_URL)

    def click_button(self):
        self.click(Button.click_button)

    def get_result_text(self):
        return self.get_text(Button.submitted_result_text)

    def is_result_visible(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, Button.submitted_result_text))
            )
            return True
        except TimeoutException:
            return False