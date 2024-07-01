import allure
import requests

@allure.feature("Test Get Users")
class TestPytestGetUsers:

  @allure.story("Test get user by id")
  @allure.title("Verify get single user")
  @allure.description("Verify the get single user API response status code and data")
  @allure.severity("critical")
  def test_get_user_by_id(self, env_config, env_response_data):
    host = env_config["host"]
    get_api = env_config["getUserByID"]
    get_response_data = env_response_data["getUserByID"]
    header=env_config["headers"]
    response = requests.get(host + get_api, headers=header)
    assert response.status_code == 200
    assert response.json() == get_response_data

  @allure.story("Test get user by wrong id")
  @allure.title("Verify get single user by wrong id")
  @allure.description("Verify the get single wrong id user API response status code and data")
  @allure.severity("normal")
  def test_get_wrong_user_id(self, env_config, env_response_data):
    host = env_config["host"]
    get_api = env_config["getUserWrongID"]
    get_response_data = env_response_data["getUserWrongID"]
    header=env_config["headers"]
    response = requests.get(host + get_api, headers=header)
    assert response.status_code == 404
    assert response.json() == get_response_data

  @allure.story("Test get user by wrong type")
  @allure.title("Verify get single user by wrong type")
  @allure.description("Verify the get single wrong type user API response status code and data")
  @allure.severity("normal")
  def test_get_wrong_user_type(self, env_config, env_response_data):
    host = env_config["host"]
    get_api = env_config["getUserWrongType"]
    get_response_data = env_response_data["getUserWrongType"]
    header=env_config["headers"]
    response = requests.get(host + get_api, headers=header)
    assert response.status_code == 422
    assert response.json() == get_response_data

  @allure.story("Test get all users")
  @allure.title("Verify get all users")
  @allure.description("Verify the get all users API response status code and data")
  @allure.severity("critical")
  def test_get_all_users(self, env_config, env_response_data):
    host = env_config["host"]
    get_api = env_config["getUsers"]
    get_response_data = env_response_data["getUsers"]
    header=env_config["headers"]
    response = requests.get(host + get_api, headers=header)
    assert response.status_code == 200
    assert get_response_data <= response.json()
