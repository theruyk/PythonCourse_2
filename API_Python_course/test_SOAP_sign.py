from zeep import Client

# URL для WSDL
wsdl = "http://dss.cryptopro.ru/verify/service.svc?wsdl"
sign = 'ТУТ ДОЛЖНА БЫЛА БЫТЬ ПОДПИСЬ'

# Создание клиента для SOAP-сервиса
client = Client(wsdl=wsdl)

def test_step1():
    # Предполагаемый вызов метода SOAP-сервиса для проверки подписи
    # 'CMS' - это тип подписи, 'sign' - это переменная, содержащая саму подпись.
    # Ассерт проверяет, что результат вызова метода 'VerifySignature' содержит 'Result' со значением True.
    assert client.service.VerifySignature('CMS', sign)['Result']
