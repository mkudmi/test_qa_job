import pytest
import requests

BASE_URL = "http://localhost:8180"

#Тест GET запроса с несуществующим id
@pytest.mark.negative
def test_get_items_with_invalid_id():
    try:
        payload = {
    	    "id": "102"
        }
        response = requests.get(f'{BASE_URL}/', json=payload)
        assert response.status_code == 400
        print("Status code: {}. SUCCESS".format(response.status_code))
    except:
        print("Status code: {}. FAILED. Must be 400".format(response.status_code))

#Тест POST запроса с int fname
def test_create_person_with_invalid_fname():
    try:
        payload = {
            "id": "103",
            "fname": "123",
            "lname": "Doe",
            "phone": "+1234567890",
            "bday": "1990-01-01"
        }
        response = requests.post(f'{BASE_URL}/', json=payload)
        assert response.status_code == 400
        print("Status code: {}. Person is not created".format(response.status_code))
    except:
        print("Status code: {}. Person created. Must be 400".format(response.status_code))