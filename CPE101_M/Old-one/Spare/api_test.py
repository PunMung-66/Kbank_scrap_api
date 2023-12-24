import requests

base_url = 'http://localhost:8000'  # Replace with your FastAPI server URL

# Function to handle errors
def handle_error(response):
    if response.status_code >= 400:
        print('Error response:', response.text)

# Test the GET endpoint
def get_data():
  response = requests.get(f'{base_url}/')
  print('GET /data:', response.json())
  handle_error(response)

# Test the GET endpoint with parameter
name = 'Pun_o_o'
def get_data_with_parameter(name):
  response = requests.get(f'{base_url}/read_pocket/{name}')
  print(f'GET /data/read_pocket/{name}:', response.json())
  handle_error(response)

# Test the POST endpoint
login_data = {
    'name': 'Pun_o_o',
    'bank_u': 'Punnawat01',
    'bank_p': 'NonutNovember0!',
}

def add_data_login(login_data):
    response = requests.post(f'{base_url}/login', json=login_data)
    print('POST /data/login:', response.json())
    handle_error(response)

# Test the POST endpoint with JSON data
pocket_data = {
    'Pocket': 'Japan',
    'Amount': 100,
}

def add_pocket(name, pocket_data):
  response = requests.post(f'{base_url}/add_pocket/{name}', json=pocket_data)
  print(f'POST /data/add_pocket/{name}:', response.json())
  handle_error(response)

# Test the DELETE endpoint
pocket_name_to_delete = 'Sunny04'
def delete_pocket(name, pocket_name_to_delete):
  response = requests.delete(f'{base_url}/delete_pocket/{name}/{pocket_name_to_delete}')
  print(f'DELETE /data/delete_pocket/{name}/{pocket_name_to_delete}:', response.json())
  handle_error(response)

add_data_login(login_data)
