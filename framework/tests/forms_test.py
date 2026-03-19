import os
import allure
from pytest_check import check

from framework.actions.forms_actions import FormsActions


@allure.feature("Practice Form")
class TestPracticeForm:
    def test_submit_form_with_all_fields(self, driver):
        form = FormsActions(driver)

        with allure.step("Open Practice Form page"):
            form.open_practice_form_page()

        base_dir = os.path.dirname(os.path.dirname(__file__))
        picture_path = os.path.join(base_dir, "data", "1081458.jpg")

        print("PICTURE PATH:", picture_path)
        print("FILE EXISTS:", os.path.exists(picture_path))

        with allure.step("Fill all form fields"):
            form.fill_full_form(
                first_name="Svetlana",
                last_name="Ples",
                email="test@example.com",
                gender="Female",
                mobile_number="1234567890",
                subject="Hindi",
                hobby="Sports",
                address="Berlin, Germany",
                state="NCR",
                city="Delhi",
                picture_path=picture_path,
            )

        with allure.step("Submit the form"):
            form.click_submit()

        with allure.step("Check that submit result modal is displayed"):
            with check:
                assert form.is_submit_result_visible(timeout=5) is True, \
                    "Submit result modal was not displayed."

            with check:
                assert form.get_submit_result_title_text() == "Thanks for submitting the form", \
                    "Unexpected submit result title text."

        with allure.step("Close submit result modal"):
            form.close_submit_result_modal()

    def test_submit_form_with_required_fields(self, driver):
        form = FormsActions(driver)
        with allure.step("Open Practice Form page"):
            form.open_practice_form_page()
        with allure.step("Fill only required fields"):
            form.fill_required_fields(
                first_name="Svetlana",
                last_name="Ples",
                gender="Female",
                mobile_number="1234567890",
            )
        with allure.step("Submit the form"):
            form.scroll_down(800)
            form.click_submit()
        with allure.step("Check that submit result modal is displayed"):
            with check:
                assert form.is_submit_result_visible(timeout=5), \
                    "Submit result modal was not displayed."
        with allure.step("Check submit result title text"):
            with check:
                assert form.get_submit_result_title_text() == "Thanks for submitting the form", \
                    "Unexpected submit result title text."
        with allure.step("Close submit result modal"):
            form.close_submit_result_modal()

    def test_submit_form_with_invalid_mobile(self, driver):
        form = FormsActions(driver)

        with allure.step("Open Practice Form page"):
            form.open_practice_form_page()

        with allure.step("Fill required fields with invalid mobile number"):
            form.fill_required_fields(
                first_name="Svetlana",
                last_name="Ples",
                gender="Male",
                mobile_number="344444",
            )

        with allure.step("Submit the form"):
            form.scroll_down(300)
            form.click_submit()

        with allure.step("Check that mobile validation error appears"):
            with check:
                assert form.get_mobile_error_text() == "Mobile number must be exactly 10 digits", \
                    "Mobile validation error text is incorrect"