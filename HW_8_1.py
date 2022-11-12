import requests
from pprint import pprint

def connect_url(main_url):
    response = requests.get(main_url)
    if response.status_code == 200:
        return True
    else:
        print('Error!')


def max_intillegence_superhero_name(url_hero, name_hero_list):
    intillegence_hero = {}
    if connect_url(url_hero):
        response = requests.get(url_hero).json()
        print(response)
        for _ in range(len(response)):
            for name in name_hero_list:
                if response[_]['name'] == name:
                    intillegence_hero[name] = response[_]['powerstats']['intelligence']
        super_superhero = max(intillegence_hero.items(), key=lambda k_v: k_v[1])
        print(super_superhero[0])
        return super_superhero[0]


superhero_name_list = ['Hulk', 'Captain America', 'Thanos']
url = "https://akabab.github.io/superhero-api/api/all.json"
max_intillegence_superhero_name(url, superhero_name_list)

