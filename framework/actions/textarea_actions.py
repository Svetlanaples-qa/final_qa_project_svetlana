from framework.actions.base_actions import BaseActions
from framework.modules.textarea import TextArea


class TextAreaActions(BaseActions):

    def open_textarea_page(self):
        self.open_page(TextArea.TEXTAREA_URL)

    def enter_text(self, text):
        self.type(TextArea.textarea_input, text)

    def click_submit(self):
        self.click_with_js(TextArea.submit_btn)

    def get_result_text(self):
        return self.get_text(TextArea.result_text)

    def get_validation_message(self):
        element = self.wait_for_element_visible(TextArea.textarea_input)
        return element.get_attribute("validationMessage")