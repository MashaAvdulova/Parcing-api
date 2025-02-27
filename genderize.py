from logging import getLevelName

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
# URL = 'https://api.genderize.io/?name=Elenasudo rm -r venv'
# data = get_data(url=URL)
# parse_data(data)

def get_data(url: str):
    url = f'https://api.genderize.io?name={name}'
    response = requests.get(url)
    data = response.json()
    return data

def parse_data(data: dict):
    name = data.get('name').capitalize()
    gender = data.get('gender')
    probability = data.get('probability')
    if name.isalpha():
        if gender == 'female':
            gender_rus = 'женскому'
        elif gender == 'male':
            gender_rus = 'мужскому'
        print(f'Имя {name} относится к {gender_rus} полу с вероятностью {probability: .0%}')
    else:
        print('Имя введено не корректно')

name = input('Введите имя: ')
data = get_data(name)
parse_data(data)

# Дописать программу таким образом, чтобы в случае корректного имени выводилось сообщение
# в формате: Имя Elena относится к женскому полу с вероятностью 99%
# В случае некорректного имени выводилось сообщение Имя введено не корректно.