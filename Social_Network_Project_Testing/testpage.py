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

    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


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

    def enter_title(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE_FIELD"], word, description='title field')

    def enter_description(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION_FIELD"], word, description='description field')

    def enter_content(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_FIELD"], word, description='content field')

    def enter_name(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NAME_FIELD"], word, description='name field')

    def enter_email(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_EMAIL_FIELD"], word, description='email field')

    def enter_content_to_us(self, word):
        return self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_TO_US_FIELD"], word, description='content to us field')


# CLICK

    def click_contact_us_button2(self):
        return self.click_button(
            TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN_2"], 
            description='Contact us button 2'
        )

    def click_contact_us_button(self):
        return self.click_button(
            TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], 
            description='Contact us button'
        )

    def click_save_button(self):
        return self.click_button(
            TestSearchLocators.ids["LOCATOR_SAVE_BTN"], 
            description='Save button'
        )
    def click_login_button(self):
        return self.click_button(
            TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], 
            description='Login button'
        )

# GET TEXT

    def get_alert_text(self):
        alert_text = self.find_alert().text
        logging.info(f"Alert text: '{alert_text}'")
        return alert_text

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], timeout=3)
        text = error_field.text
        logging.info(f"Error field text: '{text}' with locator '{TestSearchLocators.ids['LOCATOR_ERROR_FIELD'][1]}'")
        return text
