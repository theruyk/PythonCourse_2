import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Импортируем класс Service для работы с сервисом ChromeDriver.
from selenium.webdriver.chrome.service import Service
from module import Site
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


with open("/Users/the_ryuk/Desktop/PythonCurse_2/Selenium_crossbrowser/test_data.yaml") as f:
    testdata = yaml.safe_load(f)

# Создаем экземпляр класса Site, передавая в конструктор значение из словаря testdata по ключу "address".
# Это значение должно быть URL-адресом, который класс Site будет использовать для открытия веб-страницы через WebDriver.


def test_step1(site, path_login, path_password, path_button, path_err_label, expected_result):
    """Проверяет что ошибка при вводе невалидных данных при авторизации соответствует 401"""

    input1 = site.find_element("xpath", path_login)
    input1.send_keys("test")

    input2 = site.find_element("xpath", path_password)
    input2.send_keys("test")

    btn = site.find_element("css", path_button)
    btn.click()

    WebDriverWait(site.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, path_err_label))
    )
    err_label = site.find_element("xpath", path_err_label)

    assert err_label.text == expected_result

def test_step2(site, path_login, path_password, path_button, path_Blog_label):
    """Проверяет успешность авторизации при вводе валидных данных"""

    input1 = site.find_element("xpath", path_login)
    input1.send_keys(testdata['login'])

    input2 = site.find_element("xpath", path_password)
    input2.send_keys(testdata['password'])

    btn = site.find_element("css", path_button)
    btn.click()
    
    # Ждём появления элемента с меткой "Home" и проверяем его текст
    WebDriverWait(site.driver, 10).until(EC.visibility_of_element_located((By.XPATH, path_Blog_label)))
    Blog_label = site.find_element("xpath", path_Blog_label)


    assert Blog_label.text == 'Blog'

def test_step3(site,authorization, path_create_post_btn,
path_title, path_description, path_content, path_save_btn,path_title_of_created_post):
    """Добавляет и проверяет наличие поста"""

    btn1 = site.find_element("xpath", path_create_post_btn)
    btn1.click()

    WebDriverWait(site.driver, 10).until(EC.visibility_of_element_located((By.XPATH, path_title)))
    input1 = site.find_element("xpath", path_title)
    input1.send_keys(testdata['post_title'])

    input2 = site.find_element("xpath", path_description)
    input2.send_keys(testdata['post_description'])

    input3 = site.find_element("xpath", path_content)
    input3.send_keys(testdata['post_content'])

    btn2 = site.find_element("xpath", path_save_btn)
    btn2.click()
    time.sleep(5)

    WebDriverWait(site.driver, 10).until(EC.visibility_of_element_located((By.XPATH, path_title_of_created_post)))
    title_text = site.find_element("xpath", path_title_of_created_post)
    assert title_text.text == testdata['post_title']