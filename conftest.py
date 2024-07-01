import pytest
import json
import os
import requests

@pytest.fixture(scope="session")
def env_config(request):
  env = os.getenv('ENV', 'dev')
  with open(f"config/{env}_config.json", "r") as config_file:
    config = json.load(config_file)
  return config

@pytest.fixture(scope="session")
def env_request_data(request):
  # get request data file from different env
  env = os.getenv('ENV', 'dev')
  with open(f"data/{env}_request_data.json", 'r') as request_data_file:
    request_data = json.load(request_data_file)
  return request_data

@pytest.fixture(scope="session")
def env_response_data(request):
  # get response data file from different env
  env = os.getenv('ENV', 'dev')
  with open(f"data/{env}_response_data.json", "r") as response_data_file:
    response_data = json.load(response_data_file)
  return response_data

@pytest.fixture(scope="session")
def cleanup_add_user(env_config, env_request_data, env_response_data):
  row_ids = []
  yield row_ids
  for row_id in row_ids:
    host = env_config["host"]
    delete_api = f"/users/{row_id}"
    get_request_data = env_request_data["deleteUser"]
    get_response_data = env_response_data["deleteUser"]
    header=env_config["headers"]
    response = requests.delete(host + delete_api, headers=header, json=get_request_data)
    assert response.status_code == 200
    assert response.json() == get_response_data

@pytest.fixture(scope="session")
def cleanup_update_user(env_config, env_request_data, env_response_data):
  yield
  host = env_config["host"]
  update_api = env_config["updateUser"]
  get_request_data = env_request_data["updateUserCleanup"]
  get_response_data = env_response_data["updateUser"]
  header=env_config["headers"]
  response = requests.put(host + update_api, headers=header, json=get_request_data)
  assert response.status_code == 200
  assert response.json() == get_response_data

@pytest.fixture(scope="session")
def setup_delete_user(env_config, env_request_data, env_response_data):
  host = env_config["host"]
  post_api = env_config["addUser"]
  get_request_data = env_request_data["deleteUserSetup"]
  get_response_data = env_response_data["deleteUserSetup"]
  header=env_config["headers"]
  response = requests.post(host + post_api, headers=header, json=get_request_data)
  assert response.status_code == 200
  assert get_response_data.items() <= response.json().items()
  data_id = response.json()['id']
  yield data_id