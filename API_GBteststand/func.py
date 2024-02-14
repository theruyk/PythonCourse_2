from zeep import Client, Settings
import yaml
import requests
import pytest


def get_post(token):
    resource = requests.get(
        "https://test-stand.gb.ru/api/posts",
        headers={"X-Auth-Token": token},
        params={"owner": "notMe"}
    )
    return resource.json()

# Функция для создания нового поста
def create_post(token, title, description, content):
    url = "https://test-stand.gb.ru/api/posts"
    headers = {"X-Auth-Token": token}
    data = {
        "title": title,
        "description": description,
        "content": content
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Функция для получения списка всех постов
def get_posts(token):
    url = "https://test-stand.gb.ru/api/posts"
    headers = {"X-Auth-Token": token}
    response = requests.get(url, headers=headers)
    return response.json()


