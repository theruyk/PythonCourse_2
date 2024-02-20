from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:

    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FIELD = (
        By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")


class PostPageLocators:
    LOCATOR_CREATE_POST_BTN = (By.XPATH, "//*[@id='create-btn']")
    LOCATOR_TITLE_FIELD = (
        By.XPATH, "//*[@id='create-item']/div/div/div[1]/div/label/input")
    LOCATOR_DESCRIPTION_FIELD = (
        By.XPATH, "//*[@id='create-item']/div/div/div[2]/div/label/span/textarea")
    LOCATOR_CONTENT_FIELD = (
        By.XPATH, "//*[@id='create-item']/div/div/div[3]/div/label/span/textarea")
    LOCATOR_SAVE_BTN = (
        By.XPATH, "//*[@id='create-item']/div/div/div[7]/div/button/span")
    LOCATOR_TITLE_OF_CREATED_POST = (
        By.XPATH, "//*[@id='app']/main/div/div[1]/h1")
    LOCATOR_BLOG_LABEL = (By.XPATH, "//*[@id='app']/main/div/div[1]/h1")


class ContactUsPageLocators:
    LOCATOR_CONTACT_US_BTN = (
        By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_NAME_FIELD = (
        By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (
        By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_TO_US_FIELD = (
        By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN_2 = (
        By.XPATH, """//*[@id="contact"]/div[4]/button/span""")


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
        return self.enter_text_into_field(TestSearchLocators.LOCATOR_LOGIN_FIELD, word, description='login field')

    def enter_pass(self, word):
        return self.enter_text_into_field(TestSearchLocators.LOCATOR_PASS_FIELD, word, description='password field')

    def enter_title(self, word):
        return self.enter_text_into_field(PostPageLocators.LOCATOR_TITLE_FIELD, word, description='title field')

    def enter_description(self, word):
        return self.enter_text_into_field(PostPageLocators.LOCATOR_DESCRIPTION_FIELD, word, description='description field')

    def enter_content(self, word):
        return self.enter_text_into_field(PostPageLocators.LOCATOR_CONTENT_FIELD, word, description='content field')

    def enter_name(self, word):
        return self.enter_text_into_field(ContactUsPageLocators.LOCATOR_NAME_FIELD, word, description='name field')

    def enter_email(self, word):
        return self.enter_text_into_field(ContactUsPageLocators.LOCATOR_EMAIL_FIELD, word, description='email field')

    def enter_content_to_us(self, word):
        return self.enter_text_into_field(ContactUsPageLocators.LOCATOR_CONTENT_TO_US_FIELD, word, description='content to us field')


# CLICK

    def click_contact_us_button2(self):
        return self.click_button(
            ContactUsPageLocators.LOCATOR_CONTACT_US_BTN_2, 
            description='Contact us button 2'
        )

    def click_contact_us_button(self):
        return self.click_button(
            ContactUsPageLocators.LOCATOR_CONTACT_US_BTN, 
            description='Contact us button'
        )

    def click_save_button(self):
        return self.click_button(
            PostPageLocators.LOCATOR_SAVE_BTN, 
            description='Save button'
        )
    def click_login_button(self):
        return self.click_button(
            TestSearchLocators.LOCATOR_LOGIN_BTN, 
            description='Login button'
        )

# GET TEXT

    def get_alert_text(self):
        """Получает текст из алерта."""
        alert_text = self.find_alert().text
        logging.info(f"Alert text: '{alert_text}'")
        return alert_text

    def get_error_text(self):
        """Получает текст из поля ошибки."""
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, timeout=3)
        text = error_field.text
        logging.info(f"Error field text: '{text}' with locator '{TestSearchLocators.LOCATOR_ERROR_FIELD[1]}'")
        return text
