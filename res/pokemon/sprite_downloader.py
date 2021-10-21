from bs4 import BeautifulSoup
import requests
import os

url = 'https://pokemondb.net/sprites'

page_response = requests.get(url, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

pokemonData = []

pokemonLinks = page_content.find_all("a", attrs={"class": "infocard"})

for link in pokemonLinks:
    # Treat each pokemon and enter given link
    pokemonName = link['href'].split("/")[2]
    pokemonDetailUrl = url + "/"+pokemonName
    page_response_pokemon = requests.get(pokemonDetailUrl, timeout=5)
    page_content_pokemon = BeautifulSoup(page_response_pokemon.content, "html.parser")
    pokemonSpritesTable = page_content_pokemon.find_all("span", attrs={"class": ["img-sprite-v11"]})

    for sprite in pokemonSpritesTable:
        srcString = ""
        if sprite and "data-src" in sprite.attrs.keys():
            srcString = sprite["data-src"]
        elif sprite and "src" in sprite.attrs.keys():
            srcString = sprite["src"]

        if srcString != "":
            type = srcString.split("/")[5]
            name = srcString.split("/")[6][:-4]
            if type == "back-normal":
                name += "_back.png "
                os.system('curl -o' + name + srcString)
            elif type == "normal":
                name += ".png "
                os.system('curl -o' + name + srcString)