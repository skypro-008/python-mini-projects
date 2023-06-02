import json


def json_to_csv():
    try:
        with open('input.json', 'r') as f:
            data = json.load(f)

        output = ','.join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')


if __name__ == '__main__':
    json_to_csv()