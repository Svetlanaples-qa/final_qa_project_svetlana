from framework.actions.base_actions import BaseActions
from framework.modules.checkboxes import Checkboxes


class CheckboxesActions(BaseActions):
    SINGLE_CHECKBOX_URL = "https://www.qa-practice.com/elements/checkbox/single_checkbox"
    MULTIPLE_CHECKBOXES_URL = "https://www.qa-practice.com/elements/checkbox/mult_checkbox"

    def open_single_checkbox_page(self):
        self.open_page(self.SINGLE_CHECKBOX_URL)

    def open_multiple_checkboxes_page(self):
        self.open_page(self.MULTIPLE_CHECKBOXES_URL)

    def select_single_checkbox(self):
        self.click_with_js(Checkboxes.single_checkbox_input)

    def click_submit(self):
        self.click_with_js(Checkboxes.submit_btn)

    def get_checkbox_result_text(self):
        return self.get_text(Checkboxes.result_text)

    def select_checkbox_one(self):
        self.click_with_js(Checkboxes.checkbox_one)

    def select_checkbox_two(self):
        self.click_with_js(Checkboxes.checkbox_two)

    def select_checkbox_three(self):
        self.click_with_js(Checkboxes.checkbox_three)

    def select_multiple_checkboxes(self, *checkboxes):
        for checkbox in checkboxes:
            if checkbox == "one":
                self.select_checkbox_one()
            elif checkbox == "two":
                self.select_checkbox_two()
            elif checkbox == "three":
                self.select_checkbox_three()
            else:
                raise ValueError(f"Unsupported checkbox value: {checkbox}")