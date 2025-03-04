import data_fetcher


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