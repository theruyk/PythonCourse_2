from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging 

class BasePage:
  def __init__(self,driver):
    self.driver = driver
    self.base_url = "https://test-stand.gb.ru/"

  def find_element(self, locator, timeout = 10):
      # Добавляем параметр timeout с значением по умолчанию в 10 секунд.
      try:
        element = WebDriverWait(self.driver, timeout).until(
        EC.presence_of_element_located(locator),
        message=f"Can't find element by locator {locator}"
        )
      except:
        logging.exception('Find element exeption')
        element = None
      return element


  def get_element_property(self, locator, property):
      # Этот метод используется для получения свойства CSS элемента на веб-странице.
      # 'property' - название CSS свойства, значение которого мы хотим получить.
      element = self.find_element(locator)
      if element:
      # Возвращаем значение указанного CSS свойства элемента.
        return element.value_of_css_property(property)
      else:
        logging.error(f'Property {property} not found in element with locator {locator}')
        return None

  def go_to_site(self):
    try:
      start_browsing = self.driver.get(self.base_url)
    except:
      logging.exception('Exeption while open site')
      start_browsing = None
    return start_browsing

  def find_alert(self):
      """Переключается на всплывающее окно и возвращает его."""
      try:
          # Переключение на алерт и его возврат
          alert = self.driver.switch_to.alert
          logging.info("Alert found.")
          return alert
      except:
          # Логирование исключения, если алерт не найден
          logging.error("No alert found.")
          return None
          