import requests
from getpass import getpass
from requests.exceptions import Timeout
from requests.adapters import HTTPAdapter

response = requests.get('https://www.engineerspock.com/')
print(response)
print(response.status_code)

if response:
    print('Works!')

from requests import  HTTPError

for url in ['https://www.engineerspock.com/', 'https://www.engineerspocks.com/']:
    try:
        response = requests.get(url)

        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Error:{http_err}')
    except Exception as error:
        print(f"Unknown error: {error}")
    else:
        print('Connected Successfully!')


response = requests.get('https://api.github.com')
data = response.json()
# print(data)

github_response = requests.get('https://api.github.com')
# print(github_response.headers, end='\n')

print(github_response.headers['content-type'])

# placeholder_response = requests.get('http://jsonplaceholder.typicode.com/comments', params=b'postId=1')
# print(placeholder_response.text)

# auth_response = requests.get('https://api.github.com/user', auth=('dima-mazur', getpass()))
# print(auth_response.json())

try:
    response = requests.get('https://www.engineerspock.com/', timeout=1)
except Timeout:
    print('tge request time out')



with requests.Session() as session:
    session.auth = ('dima-mazur', getpass())

    response = session.get('https://api.github.com/user')

print(response.json())


adater = HTTPAdapter(max_retries=3)

with requests.Session() as session:
    session.mount('https://api.github.com', adater)
    session.auth = ('dima-mazur', getpass())

    try:
        session.get('https://api.github.com/user')
    except ConnectionError as error:
        print('Faild connect')
    else:
        print('Ok')