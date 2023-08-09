import json
import logging

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

logger.addHandler(ch)


def get_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        logger.error(f"Failed to receive data. Status code: {response.status_code}")
        return None


def save_data_to_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)
        logger.info("Data saved to file")


def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"

    data = get_data_from_api(url)

    if data is not None:
        logger.debug(f"Data received: {data}")
        save_data_to_file('data.json', data)


if __name__ == "__main__":
    main()
