import requests

url = "https://habitica.com"
url_help = 'https://habitica.com/apidoc'
login = 'gergosnoo'
login_id = '23f4d01d-3b70-4f1a-8111-d1bc5d9cd254'
password = '78a8b417-e3be-4bc3-a19b-99d817547063'


auth = login_id, password
auth_headers = {'x-api-user': auth[0], 'x-api-key': auth[1]}

json_payload = {
    "text": "Test Task",
    "type": "todo",
    "alias": "hab-api-tasks2",
    "notes": "This is a test task that was set with the python requests module.",
    "priority": 2,
}
headers = {
    "Content-Type": "application/json",
    "x-api-user": login_id,
    "x-api-key": password,
}

response = requests.post("https://habitica.com/api/v3/tasks/user", json=json_payload, headers=headers)
print(response)
