#   Connect to an API using Python (PokéAPI Example)

import requests

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    """Fetch Pokémon data from the PokéAPI by name."""
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None


if __name__ == "__main__":
    pokemon_name = "typhlosion"
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        print(f"Name: {pokemon_info['name'].capitalize()}")
        print(f"ID: {pokemon_info['id']}")
        print(f"Height: {pokemon_info['height']}")
        print(f"Weight: {pokemon_info['weight']}")
