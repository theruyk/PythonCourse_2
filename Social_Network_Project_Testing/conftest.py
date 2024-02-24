import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import requests
from api_client import PostsAPI
import yaml


@pytest.fixture(scope="session")
def test_data():
    with open('/Users/the_ryuk/Desktop/PythonCurse_2/Social_Network_Project_Testing/test_data.yaml', 'r') as file:
        data = yaml.safe_load(file)
    return data


@pytest.fixture(scope = 'session')
def browser():
    if browser == "firefox":
        # Если browser равен 'firefox', используем GeckoDriverManager для автоматической установки
        # или обновления нужного драйвера Firefox (geckodriver) и создаем объект Service для него.
        service = Service(executable_path=GeckoDriverManager().install())
        # Создаем объект настроек Firefox.
        options = webdriver.FirefoxOptions()
        # Инициализируем драйвер Firefox с указанными сервисом и опциями.
        driver = webdriver.Firefox(service=service, options=options)

    else:
        # Если browser равен 'chrome', используем ChromeDriverManager для аналогичных действий с Chrome.
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit


@pytest.fixture(scope="session")
def login(test_data):
    url = "https://test-stand.gb.ru/gateway/login"
    login_data = {'username': test_data['login'], 'password': test_data['password']}
    response = requests.post(url, data=login_data)
    token = response.json()['token']
    return token


# Фикстура для инициализации класса PostsAPI
@pytest.fixture(scope="session")
def posts_api(login):
    return PostsAPI(login)
