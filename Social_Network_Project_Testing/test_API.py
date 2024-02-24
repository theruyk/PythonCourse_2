import pytest
import logging
from api_client import PostsAPI

def test_post_exists_in_list(posts_api,test_data):
    logging.info("Test 'test_post_exists_in_list' starting")
    result = posts_api.get_post()['data']
    lst = [item['id'] for item in result]
    print(lst)
    assert test_data['expected_post_id'] in lst


def test_create_new_post(posts_api,test_data):
    logging.info("Test 'test_create_new_post' starting")
    new_post = posts_api.create_post(**test_data['post_data'])
    assert new_post['description'] == test_data['post_data']['description']
    return new_post['id']

def test_check_post_exists(posts_api, test_data):
    logging.info("Test 'test_check_post_exists' starting")
    new_post = posts_api.create_post(**test_data['post_data'])
    new_post_id = new_post['id']
    assert new_post['description'] == test_data['post_data']['description']

    posts = posts_api.get_posts()['data']
    assert any(post['id'] == new_post_id for post in posts)


# pytest -vv /Users/the_ryuk/Desktop/PythonCurse_2/Social_Network_Project_Testing/test_API.py