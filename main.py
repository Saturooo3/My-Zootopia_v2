import requests

API_KEY = "V91oA1MxaTuaFB9nzObLhg==v7INuvzcMhLn6D82"


def main():
    name = ''
    api_url = f'https://api.api-ninjas.com/v1/animals?name={name}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    print(response.text)


if __name__ == "__main__":
    main()