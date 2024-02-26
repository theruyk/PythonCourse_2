from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

class TestSearchLocators:
    ids = dict()

    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)

    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])

class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description= None):
        if description:
          element_name = description
        else: 
          element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator: str, description: str = None):
        element_name = description if description else locator
        field = self.find_element(locator, time=3)

        if not field:
            return None

        try:
            text = field.text
        except Exception as e:
            logging.exception(f"Exception while getting text from {element_name}: {e}")
            return None

        logging.debug(f"Successfully retrieved text from the element: '{element_name}'. Found text: '{text}'.")
        return text

# ENTER TEXT
    def enter_login(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description='login field')

    def enter_pass(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description='password field')

# CLICK
    def click_login_button(self):
        return self.click_button(
            TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], 
            description='Login button'
        )

    def click_about_button(self):
        return self.click_button(
            TestSearchLocators.ids["LOCATOR_ABOUT_BTN"], 
            description='Login button'
        )     