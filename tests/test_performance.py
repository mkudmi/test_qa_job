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

