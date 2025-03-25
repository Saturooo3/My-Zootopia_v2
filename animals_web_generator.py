import data_fetcher


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
    animal_name= input("Enter a name of an animal: ")
    serialized_data = data_fetcher.fetch_data(animal_name)
    script = implement_animals_info(serialized_data)
    write_data(script)
    print("Website was successfully generated to the file animals.html")

if __name__ == "__main__":
    main()