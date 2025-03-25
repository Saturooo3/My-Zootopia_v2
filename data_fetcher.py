import requests
import os
import dotenv
from animals_web_generator import listed_data


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
