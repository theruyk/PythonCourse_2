import pytest

@pytest.fixture()
def test_positive():
  return "Молоко"

@pytest.fixture()
def test_negative():
  return "Молок"