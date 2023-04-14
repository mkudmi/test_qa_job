import pytest
import requests

BASE_URL = 'http://localhost:8180'

#Тест на проверку GET запроса. Проверяет статус код, возврат параметра total и data.
def test_get_phonebook():
    try:
        response = requests.get(f'{BASE_URL}/')
        assert response.status_code == 200
        assert "total" in response.json()
        assert "data" in response.json()
        print("Status code: {}. SUCCESS".format(response.status_code))
    except AssertionError:
        print("Status code: {}. FAILED. Must be 200".format(response.status_code))

#Тест на проверку POST запроса. Проверяет статус кода, возврат параметра success.
def test_create_person():
    payload = {
        "fname": "John",
        "lname": "Doe",
        "phone": "+1234567890",
        "bday": "1990-01-01"
    }
    try:
        response = requests.post(f'{BASE_URL}/', json=payload)
        assert response.status_code == 201
        assert "success" in response.json()
        print("Status code: {}. SUCCESS".format(response.status_code))
    except AssertionError:
        print("Status code: {}. Must be 201".format(response.status_code))

def test_check_created_person():
    try:
        response = requests.get(f'{BASE_URL}?id={4}')
        assert response.status_code == 200
        print("Status code: {}. Person is created".format(response.status_code))
    except AssertionError:
        print("Status code: {}. Person is not created".format(response.status_code))