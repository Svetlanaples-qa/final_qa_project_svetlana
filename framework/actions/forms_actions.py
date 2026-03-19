from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.actions.base_actions import BaseActions
from framework.modules.forms import Forms


class FormsActions(BaseActions):
    PRACTICE_FORM_URL = "https://www.qa-practice.com/forms/practice-form"

    def open_practice_form_page(self):
        self.driver.get(self.PRACTICE_FORM_URL)

    def wait_for_subject_selected(self, subject_name, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            lambda d: subject_name in d.find_element(By.XPATH, Forms.selected_subject_tag).text
        )

    def fill_first_name(self, first_name):
        self.type(Forms.first_name_input, first_name)

    def fill_last_name(self, last_name):
        self.type(Forms.last_name_input, last_name)

    def fill_email(self, email):
        self.type(Forms.email_input, email)

    def select_gender(self, gender):
        if gender == "Male":
            self.click(Forms.gender_male_radio_btn)
        elif gender == "Female":
            self.click(Forms.gender_female_radio_btn)
        elif gender == "Other":
            self.click(Forms.gender_other_radio_btn)
        else:
            raise ValueError(f"Unsupported gender value: {gender}")

    def fill_mobile_number(self, mobile_number):
        self.type(Forms.mobile_number_input, mobile_number)

    def open_and_close_date_picker(self):
        self.click(Forms.date_of_birth_calendar_btn)
        self.click(Forms.date_of_birth_calendar_btn)

    def select_subject(self, subject_name):
        element = self.wait_for_element_visible(Forms.subjects_type_to_search_input)
        element.clear()
        element.send_keys(subject_name)

        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, Forms.subjects_suggestions_dropdown))
        )

        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)
        element.send_keys(Keys.TAB)

        self.wait.until(
            EC.invisibility_of_element_located((By.XPATH, Forms.subjects_suggestions_dropdown))
        )

        self.wait_for_subject_selected(subject_name)

    def select_hobbies(self, hobby):
        if hobby == "Sports":
            self.wait_until_visible(Forms.checkbox_hobbies_sports)
            self.click_with_js(Forms.checkbox_hobbies_sports)
        elif hobby == "Reading":
            self.wait_until_visible(Forms.checkbox_hobbies_reading)
            self.click_with_js(Forms.checkbox_hobbies_reading)
        elif hobby == "Music":
            self.wait_until_visible(Forms.checkbox_hobbies_music)
            self.click_with_js(Forms.checkbox_hobbies_music)
        else:
            raise ValueError(f"Unsupported hobby value: {hobby}")

    def upload_picture(self, file_path):
        element = self.wait_until_visible(Forms.picture_choose_file_picker)
        element.send_keys(file_path)

    def fill_current_address(self, address):
        self.type(Forms.current_address_input, address)

    def select_state(self, state_name):
        self.scroll_down(250)
        self.wait_until_visible(Forms.select_state_dropdown)
        self.click_with_js(Forms.select_state_dropdown)
        self.wait_until_visible(Forms.state_option.format(state_name))
        self.click_with_js(Forms.state_option.format(state_name))

    def select_city(self, city_name):
        self.wait_until_visible(Forms.select_city_dropdown)
        self.click_with_js(Forms.select_city_dropdown)
        self.wait_until_visible(Forms.city_option.format(city_name))
        self.click_with_js(Forms.city_option.format(city_name))

    def click_submit(self):
        self.scroll_down(250)
        self.wait_until_visible(Forms.submit_btn)
        self.click_with_js(Forms.submit_btn)

    def get_mobile_error_text(self):
        return self.get_text(Forms.mobile_error_message)

    def fill_required_fields(self, first_name, last_name, gender, mobile_number):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.select_gender(gender)
        self.fill_mobile_number(mobile_number)

    def fill_full_form(
        self,
        first_name,
        last_name,
        email,
        gender,
        mobile_number,
        subject,
        hobby,
        address,
        state,
        city,
        picture_path=None,
    ):
        print("STEP: fill_first_name")
        self.fill_first_name(first_name)

        print("STEP: fill_last_name")
        self.fill_last_name(last_name)

        print("STEP: fill_email")
        self.fill_email(email)

        print("STEP: select_gender")
        self.select_gender(gender)

        print("STEP: fill_mobile_number")
        self.fill_mobile_number(mobile_number)

        print("STEP: open_and_close_date_picker")
        self.open_and_close_date_picker()

        print("STEP: select_subject")
        self.select_subject(subject)

        print("STEP: scroll_down")
        self.scroll_down(650)

        print("STEP: select_hobbies")
        self.select_hobbies(hobby)

        if picture_path:
            print("STEP: upload_picture")
            self.upload_picture(picture_path)

        print("STEP: fill_current_address")
        self.fill_current_address(address)

        print("STEP: select_state")
        self.select_state(state)

        print("STEP: select_city")
        self.select_city(city)

    def close_submit_result_modal(self):
        self.click(Forms.submit_result_close_btn)

    def is_submit_result_visible(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, Forms.submit_result_title))
            )
            return True
        except TimeoutException:
            return False

    def get_submit_result_title_text(self):
        return self.get_text(Forms.submit_result_title)