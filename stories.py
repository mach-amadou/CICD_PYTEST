import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_top_stories():
    url = f"https://api.nytimes.com/svc/topstories/v2/world.json?api-key={API_KEY}"
    response = requests.get(url)
    return response.json()

def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    top_stories = get_top_stories()
    print(top_stories)
    save_to_json(top_stories, 'top_stories.json')

def sort(filepath, params):
    f = open(filepath)
    data = json.load(f)
    for text in data['results']:
        print()
        if(text['abstract'].find(params) != -1):
            print(text['abstract'])


if __name__ == "__main__":
    sort('top_stories.json', 'rebel')