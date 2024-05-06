import requests

API_KEY = "CpFgMASCjkqDZ2XAQlKOGqhQM9T57dHT"

def get_top_stories():
    url = f"https://api.nytimes.com/svc/topstories/v2/world.json?api-key={API_KEY}"
    response = requests.get(url)
    return response.text

def main():
    top_stories = get_top_stories()
    print(top_stories)

if __name__ == "__main__":
    main()