from func import get_sites

def test_find_text(test_positive, test_negative ):
  assert test_positive in get_sites(test_negative)