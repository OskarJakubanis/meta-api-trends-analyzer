import requests
import os
import json
from datetime import datetime

DATA_DIR = "data/raw_api_responses"
os.makedirs(DATA_DIR, exist_ok=True)

def fetch_github_api_trends():
    url = "https://api.github.com/search/repositories"
    params = {
        "q": "created:>2024-01-01",
        "sort": "stars",
        "order": "desc",
        "per_page": 100
    }
    headers = {
        "Accept": "application/vnd.github.v3+json",
        # Dodaj token jeśli masz, by zwiększyć limit API
        # "Authorization": "token YOUR_GITHUB_TOKEN"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def fetch_rapidapi_trends():
    # Przykład - dostosuj do konkretnego API RapidAPI z którego korzystasz
    url = "https://api.rapidapi.com/trends"
    headers = {
        "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",
        "X-RapidAPI-Host": "api.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def save_raw_data(data, source_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{source_name}_{timestamp}.json"
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved raw data from {source_name} to {filepath}")

def main():
    print("Fetching GitHub API trends...")
    github_data = fetch_github_api_trends()
    save_raw_data(github_data, "github")

    # Uncomment jeśli masz dostęp do RapidAPI Trends
    # print("Fetching RapidAPI trends...")
    # rapidapi_data = fetch_rapidapi_trends()
    # save_raw_data(rapidapi_data, "rapidapi")

if __name__ == "__main__":
    main()
