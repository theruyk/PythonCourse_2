import yaml
import pytest
import time
from module import Site

with open("/Users/the_ryuk/Desktop/PythonCurse_2/Selenium_crossbrowser/test_data.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture
def path_login():
    # XPath для первого поля ввода, обычно это поле для ввода имени пользователя.
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    return x_selector1


@pytest.fixture
def path_password():
    # XPath для второго поля ввода, обычно это поле для ввода пароля.
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    return x_selector2


@pytest.fixture
def path_button():
    # CSS-селектор для кнопки на веб-странице.
    btn_selector = "button"
    return btn_selector


@pytest.fixture
def path_err_label():
    # XPath для элемента, текст которого необходимо получить.
    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    return x_selector3


@pytest.fixture
def expected_result():
    return '401'

@pytest.fixture
def path_Blog_label():
    x_selector4 = '//*[@id="app"]/main/div/div[1]/h1'
    return x_selector4


@pytest.fixture(scope='function')
def site():
    site_instance = Site(testdata['address'])
    yield site_instance  # Предоставляем экземпляр для использования в тесте
    # Здесь будет выполнена очистка после тестов
    site_instance.close()  # Закрыть браузер после завершения теста

@pytest.fixture
def authorization(site, path_login, path_password, path_button):
    input1 = site.find_element("xpath", path_login)
    input1.send_keys(testdata['login'])

    input2 = site.find_element("xpath", path_password)
    input2.send_keys(testdata['password'])

    btn = site.find_element("css", path_button)
    btn.click()
    return site


@pytest.fixture
def path_create_post_btn():
    x_selector5 = """//*[@id="create-btn"]"""
    return x_selector5

@pytest.fixture
def path_title():
    x_selector6 = """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
    return x_selector6

@pytest.fixture
def path_description():
    x_selector7 = """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
    return x_selector7

@pytest.fixture
def path_content():
    x_selector8 = """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
    return x_selector8

@pytest.fixture
def path_save_btn():
    x_selector9 = """//*[@id="create-item"]/div/div/div[7]/div/button/span"""
    return x_selector9

@pytest.fixture
def path_title_of_created_post():
    x_selector10 = """//*[@id="app"]/main/div/div[1]/h1"""
    return x_selector10