import requests

# def get_data(url: str):
#     response = requests.get(url)
#     data = response.json()
#     return data
#
# def parse_data(data: str):
#     name = data.get('name')
#     gender = data.get('gender')
#     probability = data.get('probability')
#     print(name,gender, probability)
#
# URL = 'https://api.genderize.io/?name=Elena'
# data = get_data(url=URL)
# parse_data(data)

def get_data(url: str):
    url = f'https://api.genderize.io?name={name}'
    response = requests.get(url)
    data = response.json()
    return data

def parse_data(data: dict):
    name = data.get('name')
    gender = data.get('gender')
    probability = data.get('probability')
    print(name,gender, probability)

name = input('Введите имя: ')
data = get_data(name)
parse_data(data)