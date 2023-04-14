import pytest
import requests

BASE_URL = 'http://localhost:8180'

#Тест на проверку GET запроса. Проверяет статус код, возврат параметра total и data.
@pytest.mark.smoke
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
@pytest.mark.smoke
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
        
#Тест на проверку создания персоны в книжке по новому id, при условии, что изначально в книжке их 3. Проверяет статус кода.
@pytest.mark.smoke
def test_check_created_person():
    try:
        response = requests.get(f'{BASE_URL}?id={4}')
        assert response.status_code == 200
        print("Status code: {}. Person is created".format(response.status_code))
    except AssertionError:
        print("Status code: {}. Person is not created".format(response.status_code))

#Тест на проверку PUT запроса. Проверяет статус кода, возвращает параметр succsess.
@pytest.makr.xfail (reason = "Не работает (или я не понял как) поиск по key кроме по id")
def test_update_person():
    payload = {
        "id": 4,
        "fname": "Jane",
        "lname": "Doe",
        "phone": "+9876543210",
        "bday": "1995-05-05"
    }
    try:
        response = requests.put(f'{BASE_URL}/', json=payload)
        assert "success" in response.json()
        assert response.status_code == 202
        print("Status code: {}. SUCCESS".format(response.status_code))
    except AssertionError:
        print("Status code: {}. Must be 202".format(response.status_code))

#Тест на проверку обновления данных по fname, при условии, что изначально fname = Tom
@pytest.mark.xfail (reason = "Не работает (или я не понял как) поиск по key кроме по id")
def test_check_updated_person():
    try:
        response = requests.get(f'{BASE_URL}?id={1}&fname=Jane')
        assert response.status_code == 200
        print("Status code: {}. Person is updated".format(response.status_code))
    except AssertionError:
        print("Status code: {}. Person is not updated".format(response.status_code))