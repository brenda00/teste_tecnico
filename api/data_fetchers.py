import requests

# Módulo para coleta de dados da API

def fetch_planets_data():
    url = "https://swapi.dev/api/planets/"
    planets = []
    while url:
        response = requests.get(url)
        data = response.json()
        planets.extend(data['results'])
        url = data['next']
    return planets

def fetch_characters_data():
    url = "https://swapi.dev/api/people/"
    characters = []
    while url:
        response = requests.get(url)
        data = response.json()
        characters.extend(data['results'])
        url = data['next']
    return characters

def fetch_starships_data():
    url = "https://swapi.dev/api/starships/"
    starships = []
    while url:
        response = requests.get(url)
        data = response.json()
        starships.extend(data['results'])
        url = data['next']
    return starships
