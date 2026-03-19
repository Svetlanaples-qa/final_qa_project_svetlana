from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.actions.base_actions import BaseActions
from framework.modules.inputs import Input


class InputsActions(BaseActions):
    TEXT_INPUT_URL = "https://www.qa-practice.com/elements/input/simple"

    def open_simple_input_page(self):
        self.driver.get(self.TEXT_INPUT_URL)

    def press_enter(self, locator):
        element = self.wait_for_element_visible(locator)
        element.send_keys(Keys.ENTER)

    def type_text_string(self, text):
        self.type(Input.submit_me_input, text)

    def submit_text_string_with_enter(self):
        self.press_enter(Input.submit_me_input)

    def get_result_title_text(self):
        return self.get_text(Input.result_title)

    def get_result_text(self):
        return self.get_text(Input.result_text)

    def get_text_string_error_message(self):
        return self.get_text(Input.text_string_error_message)

    def is_result_box_visible(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, Input.your_input_was_box))
            )
            return True
        except TimeoutException:
            return False

    def is_text_string_error_visible(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, Input.text_string_error_message))
            )
            return True
        except TimeoutException:
            return False