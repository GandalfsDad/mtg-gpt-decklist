import requests
import json

def get_data(url, save = True, save_path = 'bin/data.json'):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if save:
            with open(save_path, 'w') as f:
                json.dump(data, f)
        return data

    else:
        print('Error: Could not get data from url: {}'.format(url))
        return None

def load_data(path = 'bin/data.json'):
    # Load a json file from a path
    with open(path, 'r') as f:
        data = json.load(f)
    return data

