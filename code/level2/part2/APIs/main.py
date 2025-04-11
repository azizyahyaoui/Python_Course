print("------------------------------------ APIs requesting ----------------------------------------------------")

import requests 


api_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{api_url}/pokemon/{name}"
    response = requests.get(url) #  requests.get(url) return only response code [200,..,404]
    if response.status_code == 200:
        print("OK, Data retrieved.")
        pokemon_info = response.json()
        return pokemon_info
    else:
        print("Error, failed to retrieved pokemon info !")


pokemon_name = input("Enter pokemon name: ")
pokemon_info = get_pokemon_info(pokemon_name)
if pokemon_info:
    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Id: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")

    #     for i, (k, v) in enumerate(pokemon_info.items()):
    #         print(f"{k}: {v}")
    #         if i == 4:
    #             break


print()
print("--------------------------------------------------------------------------------------------------------")