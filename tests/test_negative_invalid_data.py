import pytest
import requests

BASE_URL = "http://localhost:8180"

#Тест GET запроса с несуществующим id
@pytest.mark.negative
def test_get_items_with_invalid_id():
    payload = {
    	    "id": "102"
        }
    try:
        response = requests.get(f'{BASE_URL}/', json=payload)
        assert response.status_code == 200
        response_json = response.json()
        assert "data" in response_json
        assert response_json["data"] != [102]
        print("Person is not found. Response code: {}." .format(response.status_code))
    except AssertionError:
        print("Person is not found. Wrong response code {}.".format(response.status_code))

#Тест POST запроса с int fname
@pytest.mark.negative
def test_create_person_with_invalid_fname():
    payload = {
            "id": "103",
            "fname": "123",
            "lname": "Doe",
            "phone": "+1234567890",
            "bday": "1990-01-01"
        }
    try:
        response = requests.post(f'{BASE_URL}/', json=payload)
        assert response.status_code == 400
        print("Status code: {}. Person is not created".format(response.status_code))
    except:
        print("Person CREATED. Wrong response code {}".format(response.status_code))

#Тест PUT запроса с int lname
@pytest.mark.negative
def test_update_person_with_invalid_lname():
    payload = {
            "id": 103,
            "fname": "Jane",
            "lname": 123,
            "phone": "+9876543210",
            "bday": "1995-05-05"
        }
    try:
        response = requests.put(f'{BASE_URL}/', json=payload)
        assert response.status_code == 400
        print("Status code: {}. Person not updated".format(response.status_code))
    except:
        print("Person UPDATED. Wrong response code".format(response.status_code))

#Тест POST запроса с пустыми данными
@pytest.mark.negative
def test_create_person_without_data():
    payload = {

    }
    try:
        response = requests.post(f'{BASE_URL}/', json=payload)
        assert response.status_code == 400
        response_json = response.json()
        assert "success" in response_json
        assert response_json["success"] == False
        print("Person is not created. Response code: {}." .format(response.status_code))
    except AssertionError:
        print("Person is not created. Wrong response code {}.".format(response.status_code))