import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

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

