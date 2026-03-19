class Forms:
    first_name_input = '//input[@name="first_name"]'
    last_name_input = '//input[@name="last_name"]'
    email_input = '//input[@name="email"]'
    gender_male_radio_btn = '//input[@name="gender" and @value="Male"]'
    gender_female_radio_btn = '//input[@name="gender" and @value="Female"]'
    gender_other_radio_btn = '//input[@name="gender" and @value="Other"]'
    mobile_number_input = '//input[@name="mobile"]'
    date_of_birth_calendar_btn = '//button[@role="right-icon"]'
    subjects_type_to_search_input = '//input[@id="subjectsAutocomplete"]'
    selected_subject_tag = '//div[@id="subjectsTags"]'
    subjects_suggestions_dropdown = '//*[@id="subjectsSuggestions"]'
    checkbox_hobbies_sports = '//label[@for="hobbies_0"]'
    checkbox_hobbies_reading = '//label[@for="hobbies_1"]'
    checkbox_hobbies_music = '//label[@for="hobbies_2"]'
    picture_choose_file_picker = '//input[@type="file" and @name="picture"]'
    current_address_input = '//textarea[@name="current_address"]'
    select_state_dropdown = '//div[@id="div_id_state"]//div[contains(@class,"custom-dropdown-control")]'
    select_city_dropdown = '//div[@id="div_id_city"]//div[contains(@class,"custom-dropdown-control")]'
    state_option = '//div[@id="div_id_state"]//div[contains(@class,"custom-dropdown-option") and normalize-space()="{}"]'
    city_option = '//div[@id="div_id_city"]//div[contains(@class,"custom-dropdown-option") and normalize-space()="{}"]'
    submit_btn = '//*[@id="submit-id-submit"]'

    submit_result_title = '//*[@id="resultsModalLabel"]'
    submit_result_close_btn = '//*[@id="closeSmallModal-userForm"]'

    mobile_error_message = "//span[@id='error_1_id_mobile']"

