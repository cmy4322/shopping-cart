# from fastapi.testclient import TestClient

# from .main import app
# # from .context import src

# client = TestClient(app)

# # def test_read_main():
# #     response = client.get("/health")
# #     assert response.status_code == 200
# #     assert response.json() == {"status": "ok"}

# def test_read_main():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"msg": "Hello World"}

import json
import requests

class TestAPI():
    def test_health(self):
        url = "http://localhost:8004/health"
        response = requests.get(url)
        assert response.status_code == 200

    def test_create_and_delete_cart(self):
        url = "http://localhost:8004/carts/"
        data = {
            "owner": "test_owner"
        }
        headers = {
            "content-type": "application/json",
            "accept": "application/json"
        }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        assert response.status_code == 201

        url = "http://localhost:8004/carts/" + str(json.loads(response.content)["id"])
        headers = {
            "accept": "application/json"
        }
        response = requests.delete(url, headers=headers)
        assert response.status_code == 200

    def test_delete_no_cart(self):
        url = "http://localhost:8004/carts{0}"
        headers = {
            "accept": "application/json"
        }
        response = requests.delete(url, headers=headers)
        assert response.status_code == 404