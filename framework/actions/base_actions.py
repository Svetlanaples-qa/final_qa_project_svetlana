from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseActions:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_page(self, url):
        self.driver.get(url)

    def wait_for_element_visible(self, locator, timeout=None):
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def wait_for_element_clickable(self, locator, timeout=None):
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable((By.XPATH, locator)))

    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )

    def wait_for_page_stable(self, timeout=3):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def scroll_down(self, pixels=700):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        self.wait_for_page_stable()

    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    def click_with_js(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_element_visible(locator).text

    def get_attribute(self, locator, attribute_name):
        return self.wait_for_element_visible(locator).get_attribute(attribute_name)