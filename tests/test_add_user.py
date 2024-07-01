import math
import allure
import requests

@allure.feature("Test Add Users")
class TestPytestAddUser:

  @allure.story("Test add single user")
  @allure.title("Verify test add user")
  @allure.description("Verify the add single user API response status code and data")
  @allure.severity("critical")
  def test_add_user(self, env_config, env_request_data, env_response_data, cleanup_add_user):
    host = env_config["host"]
    post_api = env_config["addUser"]
    get_request_data = env_request_data["addUser"]
    get_response_data = env_response_data["addUser"]
    header = env_config["headers"]
    response = requests.post(host + post_api, headers=header, json=get_request_data)
    assert response.status_code == 200
    assert get_response_data.items() <= response.json().items()
    assert 'id' in response.json()
    assert int(math.log10(response.json()['id']))+1 >= 1
    cleanup_add_user.append(response.json()['id'])
