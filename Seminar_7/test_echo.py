import subprocess
import logging
import pytest

@pytest.fixture
def setup_logging():
    # Создание и настройка логгера
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('error_test_echo.log')
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    yield logger

def test_echo(setup_logging):
    logger = setup_logging
    logger.debug("Начало теста test_echo")
    expected_output = "Hello, world!"

    try:
        result = subprocess.run(['echo', 'Helloампир, world!'], capture_output=True, text=True)
        logger.debug(f"Echo output: {result.stdout.strip()}")
        assert result.stdout.strip() == expected_output
    except AssertionError:
        logger.error(f"Тест не прошел: ожидаемый вывод - {expected_output}, полученный вывод - {result.stdout.strip()}")
        raise
    except Exception as e:
        logger.exception(f"Ошибка при выполнении subprocess: {e}")

    logger.debug("Конец теста test_echo")

#pytest --alluredir=/Users/the_ryuk/Desktop/PythonCurse_2/results /Users/the_ryuk/Desktop/PythonCurse_2/Seminar_7/test_echo.py
