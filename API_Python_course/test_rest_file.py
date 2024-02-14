import requests
import pytest
# Создание сессии запросов
s = requests.Session()

def get_sites(lat: float, long: float, radius: int, limit: int = 100) -> list:
    """
    Получить сайты вокруг заданных географических координат с указанным радиусом.
    
    :param lat: Широта для поиска.
    :param long: Долгота для поиска.
    :param radius: Радиус поиска в метрах.
    :param limit: Лимит количества результатов.
    :return: Список названий сайтов.
    """
    # URL для API запроса
    URL = "https://en.wikipedia.org/w/api.php"
    
    # Параметры для API запроса
    PARAMS = {
        "format": "json",
        "list": "geosearch",
        "gscoord": f"{lat}|{long}",
        "gslimit": f"{limit}",
        "gsradius": f"{radius}",
        "action": "query"
    }
    
    # Выполнение GET запроса с использованием сессии
    r = s.get(url=URL, params=PARAMS)
    
    # Получение результатов и преобразование в JSON
    pages = r.json()['query']['geosearch']
    
    # Извлечение названий сайтов из результатов
    sites = [i["title"] for i in pages]
    
    return sites

def test_step1(text1,coord1):
  assert text1 in get_sites(coord1[0],coord1[1], 100), 'Not found'
