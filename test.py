import requests
a = """
Stink""".split()

for val in a:
    data = {
      'guess': val
    }

    response = requests.post('https://techchallenge.withgoogle.com/puzzles/bomb-search/guess', headers=headers, data=data)
    print response.json()
