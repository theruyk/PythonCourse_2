import yaml
from api_client import ProfileAPI

# Загрузка данных из YAML файла
with open("/Users/the_ryuk/Desktop/PythonCurse_2/Selenium_Page_Object_Final_Task/test_data.yaml", 'r') as file:
    test_data = yaml.safe_load(file)


def test_authorization_response():
    profile_api = ProfileAPI(test_data['token'])

    response = profile_api.get_profile()

    assert response['id'] == test_data['profile_data']['id']
    assert response['firstName'] == test_data['profile_data']['firstName']
    assert response['lastName'] == test_data['profile_data']['lastName']
    assert response['username'] == test_data['profile_data']['username']

# pytest -vv /Users/the_ryuk/Desktop/PythonCurse_2/Selenium_Page_Object_Final_Task/test_authorization_response.py