import pytest
import requests

BASE_URL = "http://localhost:8180"

#Тест на проверку скорости запроса GET. Выводит кол-во секунд.
@pytest.mark.performance
def test_get_items_performance():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1.0
    print("Response time: {} seconds".format(response.elapsed.total_seconds()))

#Тест на проверку скорости POST запроса. Выводит кол-во секунд
@pytest.mark.performance
def test_post_item_performance():
    payload = {
        "id": "101",
        "fname": "John",
        "lname": "Doe",
        "phone": "+1234567890",
        "bday": "1980-01-01"
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1.0
    print("Response time: {} seconds".format(response.elapsed.total_seconds()))

#Тест на проверку скорости PUT запроса. Выводит кол-во секунд
@pytest.mark.performance
def test_put_item_performance():
    payload = {
        "id": 101,
        "fname": "Jane",
        "lname": "Doe",
        "phone": "+1234567890",
        "bday": "1980-01-01"
    }
    response = requests.put(BASE_URL, json=payload)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1.0
    print("Response time: {} seconds".format(response.elapsed.total_seconds()))
    
#Тест на проверку скорости DELETE запроса. Выводит кол-во секунд
@pytest.mark.performance
def test_delete_item_performance():
    payload = {
        "id": 101
    }
    response = requests.delete(BASE_URL, json=payload)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 1.0
    print("Response time: {} seconds".format(response.elapsed.total_seconds()))