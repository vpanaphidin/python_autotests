import requests
import json

token = '355dbf4fbaf163570e0c27c1dd0cf63c'

response_create = requests.post('https://pokemonbattle.me:5000/pokemons', json={
    "name": "Beautis",
    "photo": "https://purepng.com/public/uploads/large/purepng.com-pokemonpokemonpocket-monsterspokemon-franchisefictional-speciesone-pokemonmany-pokemonone-pikachu-1701527784955yyrne.png"
}, headers = {'Content-Type': 'application/json', "trainer_token": token})

print(response_create.text)


response_change = requests.put('https://pokemonbattle.me:5000/pokemons', json={
    "pokemon_id": '3074',
    "name": "Ginix",
    "photo": ""
}, headers = {'Content-Type': 'application/json', "trainer_token": token})

print(response_change.text)

response_catch = requests.post("https://pokemonbattle.me:5000/trainers/add_pokeball", json={
    "pokemon_id": "3074"
}, headers = {'Content-Type': 'application/json', "trainer_token": token})

print(response_catch.text)