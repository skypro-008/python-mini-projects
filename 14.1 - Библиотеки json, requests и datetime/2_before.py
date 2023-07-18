import requests


def get_data(url):
    response = requests.get(url)
    data = response.json()
    result = {}
    result['name'] = data['name']
    result['language'] = data['language']
    result['forks'] = data['forks_count']
    result['stars'] = data['stargazers_count']
    return result


if __name__ == '__main__':
    URL = 'https://api.github.com/repos/ArjanCodes/betterpython'
    repo_info = get_data(URL)
    print(repo_info)
