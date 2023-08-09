import json
import logging

import pandas as pd

logging.basicConfig(filename="titanic.log", level=logging.DEBUG)


def process_data():
    with open('settings.json', 'r') as f:
        settings = json.load(f)

    with open('titanic.csv', 'r') as f:
        df = pd.read_csv(f)

    # Исправлено: учитывается диапазон возраста
    df = df[(df['Sex'] == settings['sex']) & (df['Age'] >= settings['age_from']) & (df['Age'] <= settings['age_to'])]

    total_passengers = df['PassengerId'].count()
    # Исправлено: убран лишний sum()
    total_survivors = df['Survived'].sum()
    total_deaths = total_passengers - total_survivors

    # Исправлено: int64 приведен к int
    result = {
        'sex': settings['sex'],
        'age_from': settings['age_from'],
        'age_to': settings['age_to'],
        'total_survivors': int(total_survivors),
        'total_deaths': int(total_deaths)
    }
    # Исправлено: json.dumps() вместо json.dump()
    return json.dumps(result)


if __name__ == '__main__':
    json_answer = process_data()
    assert json_answer == '{"sex": "male", "age_from": 30, "age_to": 40, "total_survivors": 12, "total_deaths": 12}'
    print(json_answer)
    logging.info('Data processing completed successfully.')
