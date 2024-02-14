from func import get_post
import pytest
from func import get_post,create_post,get_posts

def test_1(login):
    result = get_post(login)['data']
    lst = []

    for item in result:
            lst.append(item['id'])

    print(lst)
    assert 98251 in lst


def test_create_new_post(login):
    title = "Самый красивый заголовок"
    description = "Описание поста"
    content = "Контент"
    new_post = create_post(login, title, description, content)
    assert new_post['description'] == description
    return new_post['id']


def test_check_post_exists(login):
    title = "Самый красивый заголовок"
    description = "Описание поста"
    content = "Контент"
    new_post = create_post(login, title, description, content)
    new_post_id = new_post['id']
    assert new_post['description'] == description

    posts = get_posts(login)['data']
    assert any(post['id'] == new_post_id for post in posts)



    