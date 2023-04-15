import pytest
import requests

BASE_URL = 'http://localhost:8180'

#Проверка на наличие авторизации для GET запроса
def test_authentication_required():
    response = requests.get('https://localhost:8180/')
    assert response.status_code == 401, "Ожидаем 401, Status code {}".format(response.status_code)

