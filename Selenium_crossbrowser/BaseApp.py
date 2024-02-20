from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging 

class BasePage:
  def __init__(self,driver):
    self.driver = driver
    self.base_url = "https://test-stand.gb.ru/"

  def find_element(self, locator, timeout = 10):
      # Добавляем параметр timeout с значением по умолчанию в 10 секунд.
      return WebDriverWait(self.driver, timeout).until(
    EC.presence_of_element_located(locator),
    message=f"Can't find element by locator {locator}"
)


  def get_element_property(self, locator, property):
      # Этот метод используется для получения свойства CSS элемента на веб-странице.
      # 'property' - название CSS свойства, значение которого мы хотим получить.
      element = self.find_element(locator)
      # Возвращаем значение указанного CSS свойства элемента.
      return element.value_of_css_property(property)

  def go_to_site(self):
    return self.driver.get(self.base_url)

  def find_alert(self):
      """Переключается на всплывающее окно и возвращает его."""
      try:
          # Переключение на алерт и его возврат
          alert = self.driver.switch_to.alert
          logging.info("Alert found.")
          return alert
      except Exception as e:
          # Логирование исключения, если алерт не найден
          logging.error("No alert found.")
          raise e