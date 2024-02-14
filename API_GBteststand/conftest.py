import pytest
import requests
import yaml

with open('/Users/the_ryuk/Desktop/PythonCurse_2/API_GBteststand/config.yaml', 'r') as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    url = "https://test-stand.gb.ru/gateway/login"
    # Используйте ключи 'username' и 'password' из файла config.yaml
    login_data = {'username': data['username'], 'password': data['password']}
    response = requests.post(url, data=login_data)
    return response.json()['token']
