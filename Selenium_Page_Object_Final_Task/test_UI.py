from testpage import OperationsHelper, TestSearchLocators
from selenium.webdriver.support.wait import WebDriverWait
import yaml
from selenium.webdriver.support import expected_conditions as EC
import time
from BaseApp import BasePage

with open("/Users/the_ryuk/Desktop/PythonCurse_2/Selenium_Page_Object_Final_Task/test_data.yaml") as f:
    testdata = yaml.safe_load(f)

def test_autorization(browser):
    """Проверяет успешность авторизации при вводе валидных данных"""
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    blog_label = testpage.find_element(TestSearchLocators.ids['LOCATOR_BLOG_LABEL'])
    assert blog_label.text == 'Blog'

def test_about_btn(browser):
    """Проверяет работоспособность кнопки About"""
    testpage = OperationsHelper(browser)
    testpage.click_about_button()
    time.sleep(3)
    about_page_title = testpage.find_element(TestSearchLocators.ids['LOCATOR_ABOUT_PAGE_H1'])
    assert about_page_title.text == 'About Page'

def test_about_page_label_size(browser):
    """Проверяет размер шрифта заголовка About Page"""
    testpage = OperationsHelper(browser)
    size_of_element = testpage.get_element_property(TestSearchLocators.ids['LOCATOR_ABOUT_PAGE_H1'], 'font-size')
    assert size_of_element == '32px'

# pytest -vv /Users/the_ryuk/Desktop/PythonCurse_2/Selenium_Page_Object_Final_Task/test_UI.py