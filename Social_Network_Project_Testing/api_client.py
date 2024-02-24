import requests
import logging

class PostsAPI:

    def __init__(self, token):
        self.token = token

    def get_post(self):
        """Функция для получения поста"""
        try:
            resource = requests.get(
                "https://test-stand.gb.ru/api/posts",
                headers={"X-Auth-Token": self.token},
                params={"owner": "notMe"}
            )
            print(resource.json())
            return resource.json()
        except:
            logging.exception("Error occurred while fetching a post")

    def create_post(self, title, description, content):
        """Функция для создания нового поста"""
        try:
            url = "https://test-stand.gb.ru/api/posts"
            headers = {"X-Auth-Token": self.token}
            data = {
                "title": title,
                "description": description,
                "content": content
            }
            response = requests.post(url, headers=headers, json=data)
            return response.json()
        except:
            logging.exception("Error occurred while creating a post")

    def get_posts(self):
        """Функция для получения списка всех постов"""
        try:
            url = "https://test-stand.gb.ru/api/posts"
            headers = {"X-Auth-Token": self.token}
            response = requests.get(url, headers=headers)
            return response.json()
        except:
            logging.exception("Error occurred while fetching posts")
