# JSON & Serialization
import json

data = {'name': 'Dev', 'role': 'Data Engineer'}
with open('data.json', 'w') as f:
    json.dump(data, f)
# Read the JSON file

with open('data.json', 'r') as f:
        print(json.load(f))     # Output: {'name': 'Dev', 'role': 'Data Engineer'}
# read json file example

  