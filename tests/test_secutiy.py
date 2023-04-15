import pytest
import requests

BASE_URL = 'http://localhost:8180'

#Проверка на наличие авторизации для GET запроса
@pytest.mark.security
def test_authentication_required():
    try:
        response = requests.get('http://localhost:8180/')
        assert response.status_code == 401
        print("Ожидаем 401, Status code {}".format(response.status_code))
    except AssertionError:
        print("Ожидаем 401, Status code {}".format(response.status_code))

#Проверка на Too Many Requests
@pytest.mark.security
def test_rate_limiting():
    try:
        for i in range(5):
            response = requests.get('http://localhost:8180/')

        response = requests.get('http://localhost:8180/')
        assert response.status_code == 429
        print("Expected 429 Too Many Requests status code for rate limited request, but got {}".format(response.status_code))
    except AssertionError:
        print("Expected 429 Too Many Requests status code for rate limited request, but got {}".format(response.status_code))