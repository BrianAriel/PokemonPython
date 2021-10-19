from bs4 import BeautifulSoup
import requests
import json
from constants import *


url = "https://pokemondb.net/pokedex/all"

page_response = requests.get(url, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

pokemonData = []

pokemonRows = page_content.find_all("tr")
pokemonDictionary = {}

for row in pokemonRows[1:]:
    stats_html = row.find_all("td")[4:]
    stats_array = list(map(lambda data: int(data.text), stats_html))
    types_html = row.find_all("a", attrs={"class": "type-icon"})

    types_array = list(map(lambda data: TYPES.index(data.text), types_html))

    name = row.find("a", attrs={"class": "ent-name"}).text

    mega_html = row.find("small", attrs={"class": "text-muted"})
    if mega_html:
        name = mega_html.text

    pokemonDictionary[name] = {
        "type1": types_array[0],
        "HP": stats_array[0],
        "Attack": stats_array[1],
        "Defense": stats_array[2],
        "SpAttack": stats_array[3],
        "SpDefense": stats_array[4],
        "Speed": stats_array[5]
    }

    if len(types_array) > 1:
        pokemonDictionary[str(name)]["type2"] = types_array[1]


with open('C:/Users/brian/PycharmProjects/PokemonPython/Database/pokemons.json', 'w') as outfile:
    json.dump(pokemonDictionary, outfile)



