from testpage import OperationsHelper, PostPageLocators, ContactUsPageLocators, TestSearchLocators
from selenium.webdriver.support.wait import WebDriverWait
import yaml
from selenium.webdriver.support import expected_conditions as EC
import time
import logging 

with open("/Users/the_ryuk/Desktop/PythonCurse_2/Selenium_crossbrowser/test_data.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    """Проверяет что ошибка при вводе невалидных данных при авторизации соответствует 401"""
    logging.info("Test 1 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    """Проверяет успешность авторизации при вводе валидных данных"""
    logging.info("Test 2 starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    
    # Ждём появления элемента с меткой "Home" и проверяем его текст
    blog_label = testpage.find_element(PostPageLocators.LOCATOR_BLOG_LABEL)
    assert blog_label.text == 'Blog'

def test_step3(browser):
    """Добавляет и проверяет наличие поста"""
    logging.info("Test 3 starting")
    testpage = OperationsHelper(browser)
    testpage.find_element(PostPageLocators.LOCATOR_CREATE_POST_BTN).click()

    WebDriverWait(testpage.driver, 10).until(
        EC.visibility_of_element_located(PostPageLocators.LOCATOR_TITLE_FIELD)
    )
    testpage.enter_title(testdata['post_title'])
    testpage.enter_description(testdata['post_description'])
    testpage.enter_content(testdata['post_content'])
    testpage.click_save_button()
    time.sleep(3)
    
    title_text = testpage.find_element(PostPageLocators.LOCATOR_TITLE_OF_CREATED_POST)
    assert title_text.text == testdata['post_title']

def test_step4(browser):
    """Проверяет механику работы формы Contact Us"""
    logging.info("Test 4 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.find_element(ContactUsPageLocators.LOCATOR_CONTACT_US_BTN).click()
    WebDriverWait(testpage.driver, 10).until(
        EC.visibility_of_element_located(ContactUsPageLocators.LOCATOR_NAME_FIELD)
    )
    testpage.enter_name(testdata['name_for_contact_us'])
    testpage.enter_email(testdata['email_for_contact_us'])
    testpage.enter_content_to_us(testdata['content_for_contact_us'])
    testpage.click_contact_us_button()
    WebDriverWait(testpage.driver, 10).until(EC.alert_is_present())
    # Получение текста алерта
    alert = testpage.find_alert()
    alert_text = alert.text
    # Закрытие алерта
    alert.accept()
    assert alert_text == 'Form successfully submitted'