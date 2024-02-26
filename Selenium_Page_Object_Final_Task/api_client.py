import requests
import logging

class ProfileAPI:

    def __init__(self, token):
        self.token = token

    def get_profile(self):
        try:
            resource = requests.get(
                "https://test-stand.gb.ru/api/users/profile/33288",
                headers={"X-Auth-Token": self.token}
            )
            return resource.json()
        except:
            logging.exception("Error occurred while fetching a post")

