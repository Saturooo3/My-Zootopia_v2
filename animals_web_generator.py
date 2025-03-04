import requests
import json

API_KEY = "V91oA1MxaTuaFB9nzObLhg==v7INuvzcMhLn6D82"


def load_data(name):
    api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)



def serialize_data(animal):
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
    takes a list of animals data and return a str with name, diet,
    locations and type of animal for html
    """
    output = ""
    if len(animals_data) == 0:
        output += f"<h2>The animaal '{animal}' doesn't exist.</h2>"
    for animal in animals_data:
        output += serialize_data(animal)
    return output



def implement_animals_info(animals_str: str) -> str:
    """
    takes a str of animals data of  with name, diet, locations and type
    returns str for .html script
    """
    with open("animals_template.html", "r") as f:
        html_script = f.read()
    html_script_with_data = html_script.replace("__REPLACE_ANIMALS_INFO__", animals_str)
    return html_script_with_data


def write_data(script: str) -> None:
    """
    takes a string and creates a new html file with that str
    """
    with open("animals.html", "w") as f:
        f.write(script)


def main():
    name= input("Enter a name of an animal: ")
    animals_data = load_data(name)
    serialized_data = listed_data(name, animals_data)
    script = implement_animals_info(serialized_data)
    write_data(script)
    print("Website was successfully generated to the file animals.html")

if __name__ == "__main__":
    main()