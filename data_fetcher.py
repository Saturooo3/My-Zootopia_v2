import requests
import os
import dotenv


dotenv.load_dotenv()
API_KEY = os.getenv('API_KEY')


def load_data(animal_name: str):
    """
    gets a name of an animal and return the json file of its data
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)


def serialize_data(animal: dict) -> str:
    """
    gets a dictionary of an animal with its data and
    returns a string with its data formatted
    """
    output = ""
    output += "<li class='cards__item'>"

    output += f"\n<div class='card__title'>{animal['name']}</div>"
    output += "\n<p class ='card__text'>"
    output += f"\n<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n"
    output += "<strong>Locations:</strong><br/>"
    for location in animal["locations"]:
        output += f"\n\t{location}<br/>"
    if "grop" in animal["characteristics"].keys():
        output += f"\n<strong>Group</strong>: {animal["characteristics"]["group"]}<br/>\n"

    output += "</p>\n</li>\n"
    return output


def listed_data(animal, animals_data: list) -> str:
    """
    gets a list of animals data and returns the animals a str with name, diet,
    locations and type of animal for html if the list is not empty
    """
    output = ""
    if len(animals_data) == 0:
        output += f"<h2>The animal '{animal}' doesn't exist.</h2>"
    for animal in animals_data:
        output += serialize_data(animal)
    return output

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
          ...
        },
        'locations': [
          ...
        ],
        'characteristics': {
          ...
        }
    },
    """
    animals_data = load_data(animal_name)
    return listed_data(animal_name, animals_data)
