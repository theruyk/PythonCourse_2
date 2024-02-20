from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:

  LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
  LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
  LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
  LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")


class PostPageLocators:
    LOCATOR_CREATE_POST_BTN = (By.XPATH, "//*[@id='create-btn']")
    LOCATOR_TITLE_FIELD = (By.XPATH, "//*[@id='create-item']/div/div/div[1]/div/label/input")
    LOCATOR_DESCRIPTION_FIELD = (By.XPATH, "//*[@id='create-item']/div/div/div[2]/div/label/span/textarea")
    LOCATOR_CONTENT_FIELD = (By.XPATH, "//*[@id='create-item']/div/div/div[3]/div/label/span/textarea")  # Предположим, что путь к полю 'content' отличается
    LOCATOR_SAVE_BTN = (By.XPATH, "//*[@id='create-item']/div/div/div[7]/div/button/span")
    LOCATOR_TITLE_OF_CREATED_POST = (By.XPATH, "//*[@id='app']/main/div/div[1]/h1")
    LOCATOR_BLOG_LABEL = (By.XPATH, "//*[@id='app']/main/div/div[1]/h1")

class ContactUsPageLocators:
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH,"""//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_TO_US_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN_2 = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")

class OperationsHelper(BasePage):

# ENTER TEXT
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def enter_title(self, word):
        logging.info(f"Sending '{word}' to title field {PostPageLocators.LOCATOR_TITLE_FIELD[1]}")
        title_field = self.find_element(PostPageLocators.LOCATOR_TITLE_FIELD)
        title_field.clear()
        title_field.send_keys(word)

    def enter_description(self, word):
        logging.info(f"Sending '{word}' to description field {PostPageLocators.LOCATOR_DESCRIPTION_FIELD[1]}")
        description_field = self.find_element(PostPageLocators.LOCATOR_DESCRIPTION_FIELD)
        description_field.clear()
        description_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Sending '{word}' to content field {PostPageLocators.LOCATOR_CONTENT_FIELD[1]}")
        content_field = self.find_element(PostPageLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(word)

    def enter_name(self, word):
        logging.info(f"Sending '{word}' to name field {ContactUsPageLocators.LOCATOR_NAME_FIELD[1]}")
        name_field = self.find_element(ContactUsPageLocators.LOCATOR_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(word)

    def enter_email(self, word):
        logging.info(f"Sending '{word}' to email field {ContactUsPageLocators.LOCATOR_EMAIL_FIELD[1]}")
        email_field = self.find_element(ContactUsPageLocators.LOCATOR_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(word)

    def enter_content_to_us(self, word):
        logging.info(f"Sending '{word}' to email field {ContactUsPageLocators.LOCATOR_CONTENT_TO_US_FIELD[1]}")
        ontent_to_us = self.find_element(ContactUsPageLocators.LOCATOR_CONTENT_TO_US_FIELD)
        ontent_to_us.clear()
        ontent_to_us.send_keys(word)


# CLICK

    def click_contact_us_button2(self):
        logging.info(f"Clicking Contact us button {ContactUsPageLocators.LOCATOR_CONTACT_US_BTN[1]}")
        contact_us_button2 = self.find_element(ContactUsPageLocators.LOCATOR_CONTACT_US_BTN_2)
        contact_us_button2.click()
    
    def click_contact_us_button(self):
        logging.info(f"Clicking Contact us button {ContactUsPageLocators.LOCATOR_CONTACT_US_BTN[1]}")
        contact_us_button = self.find_element(ContactUsPageLocators.LOCATOR_CONTACT_US_BTN)
        contact_us_button.click()

    def click_save_button(self):
        logging.info(f"Clicking save button {PostPageLocators.LOCATOR_SAVE_BTN[1]}")
        save_button = self.find_element(PostPageLocators.LOCATOR_SAVE_BTN)
        save_button.click()


# GET TEXT 
    def get_alert_text(self):
        """Получает текст из алерта."""
        alert = self.find_alert()
        alert_text = alert.text
        logging.info(f"Alert text: {alert_text}")
        return alert_text

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, timeout=3)
        text = error_field.text
        logging.info(f"Found text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text