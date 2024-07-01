import allure
import requests

@allure.feature("Test Delete Users")
class TestPytestDeleteUser:

  @allure.story("Test delete single user")
  @allure.title("Verify test delete single user")
  @allure.description("Verify the delete single user API response status code and data")
  @allure.severity("critical")
  def test_delete_user(self, setup_delete_user, env_config, env_request_data, env_response_data):
    host = env_config["host"]
    id = setup_delete_user
    delete_api = f"/users/{id}"
    get_request_data = env_request_data["deleteUser"]
    get_response_data = env_response_data["deleteUser"]
    header=env_config["headers"]
    response = requests.delete(host + delete_api, headers=header, json=get_request_data)
    assert response.status_code == 200
    assert response.json() == get_response_data

  @allure.story("Test delete not found user")
  @allure.title("Verify test delete not found user")
  @allure.description("Verify the delete not found user API response status code and data")
  @allure.severity("normal")
  def test_delete_not_found_user(self, env_config, env_request_data, env_response_data):
    host = env_config["host"]
    delete_api = env_config["notFoundDeleteUser"]
    get_request_data = env_request_data["deleteUser"]
    get_response_data = env_response_data["notFoundDeleteUser"]
    header=env_config["headers"]
    response = requests.delete(host + delete_api, headers=header, json=get_request_data)
    assert response.status_code == 404
    assert response.json() == get_response_data
