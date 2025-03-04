import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def serialize_animal(animal):
    """
    takes single element of list with data of animal
    and return a str with the data organized for a html file
    """
    output = ""
    output += "<li class='cards__item'>"

    if animal["name"]:
        name = animal["name"]
        output += f"\n<div class='card__title'>{name}</div>"

    output += "\n<p class ='card__text'>"

    if animal["characteristics"]["diet"]:
        diet = animal["characteristics"]["diet"]
        output += f"\n<strong>Diet:</strong> {diet}<br/>\n"

    if animal["locations"][0]:
        locations = animal["locations"][0]
        output += f"<strong>Location</strong>: {locations}<br/>\n"

    if "type" in animal["characteristics"].keys():
        animal_type = animal["characteristics"]["type"]
        output += f"<strong>Type</strong>: {animal_type}<br/>\n"

    output += "</p>\n</li>\n"

    return output


def transform_data_to_str(animals_data: list) -> str:
    """
    takes a list of animals data and return a str with name, diet,
    locations and type of animal for html
    """
    output = ""

    for animal in animals_data:
        output += serialize_animal(animal)
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
    animals_data = load_data("animals_data.json")
    serialized_animal_str = transform_data_to_str(animals_data)
    script = implement_animals_info(serialized_animal_str)
    write_data(script)


if __name__ == "__main__":
    main()