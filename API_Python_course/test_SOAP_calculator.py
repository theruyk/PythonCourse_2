from zeep import Client

# Создаем клиента для тестового SOAP-сервиса калькулятора
client = Client('http://www.dneonline.com/calculator.asmx?WSDL')

def test_add_method():
    # Вызываем метод Add сервиса калькулятора с тестовыми данными
    result = client.service.Add(5, 3)
    
    # Проверяем, что сервис возвращает правильный результат
    assert result == 8

test_add_method()
