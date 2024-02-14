from zeep import Client, Settings
import yaml

with open('/Users/the_ryuk/Desktop/PythonCurse_2/API_yaSpeller/config.yaml', 'r') as f:
  data = yaml.safe_load(f)


def get_sites(word: str) -> str:
    """
    Функция для проверки правописания слова с помощью Yandex Speller API.

    :param word: Слово для проверки.
    :return: Результат проверки правописания.
    """
    url = data['URL']
    setting = Settings(strict=False)
    client = Client(wsdl=data['URL'], settings=setting)
    find_text = client.service.checkText(word)

    return find_text[0]['s']

