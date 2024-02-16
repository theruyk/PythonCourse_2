import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Импортируем класс Service для работы с сервисом ChromeDriver.
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Открываем файл с тестовыми данными в формате YAML.
with open("/Users/the_ryuk/Desktop/PythonCurse_2/Selenium_crossbrowser/test_data.yaml") as f:
    # Загружаем содержимое YAML файла в переменную testdata.
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

# Определение класса Site.


class Site:
    def __init__(self, address):
        # Конструктор класса Site с параметром address, который является URL-адресом веб-страницы.

        if browser == "firefox":
            # Если browser равен 'firefox', используем GeckoDriverManager для автоматической установки
            # или обновления нужного драйвера Firefox (geckodriver) и создаем объект Service для него.
            service = Service(executable_path=GeckoDriverManager().install())
            # Создаем объект настроек Firefox.
            options = webdriver.FirefoxOptions()
            # Инициализируем драйвер Firefox с указанными сервисом и опциями.
            self.driver = webdriver.Firefox(service=service, options=options)

        elif browser == "chrome":
            # Если browser равен 'chrome', используем ChromeDriverManager для аналогичных действий с Chrome.
            service = Service(executable_path=ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=service, options=options)

        # Устанавливаем неявное ожидание для всех операций поиска элементов.
        # здесь следует указать время ожидания, например, 3 секунды.
        self.driver.implicitly_wait(1)
        # Максимизируем окно браузера для лучшего обзора содержимого.
        self.driver.maximize_window()
        # Открываем URL, который был передан в конструктор класса.
        self.driver.get(address)
        time.sleep(testdata['sleep_time'])

    def find_element(self, mode, path, timeout=2):
        # Добавляем параметр timeout с значением по умолчанию в 10 секунд.

        # Используем WebDriverWait в сочетании с expected_conditions для явного ожидания.
        wait = WebDriverWait(self.driver, timeout)
        element = None

        if mode == "css":
            # Ждем, пока элемент, найденный по CSS селектору, не станет видимым на странице.
            element = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, path)))
        elif mode == "xpath":
            # Ждем, пока элемент, найденный по XPath, не станет видимым на странице.
            element = wait.until(
                EC.visibility_of_element_located((By.XPATH, path)))

        # Возвращаем найденный элемент или None, если элемент не был найден в течение заданного времени.
        return element

    def get_element_property(self, mode, path, property):
        # Этот метод используется для получения свойства CSS элемента на веб-странице.
        # 'mode' и 'path' - параметры, определяющие, как найти элемент (с помощью CSS селектора или XPath).
        # 'property' - название CSS свойства, значение которого мы хотим получить.

        # Используем ранее определенный метод для поиска элемента.
        element = self.find_element(mode, path)
        # Возвращаем значение указанного CSS свойства элемента.
        return element.value_of_css_property(property)

    def close(self):
        # Этот метод закрывает текущее окно браузера.

        # Вызываем метод close у объекта driver, который закрывает окно браузера.
        self.driver.close()
