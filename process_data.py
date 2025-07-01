import os
import json
import pandas as pd
from glob import glob

RAW_DATA_DIR = "data/raw_api_responses"
PROCESSED_DATA_DIR = "data/processed"
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

def process_github_data():
    # Wczytanie najnowszego pliku GitHub JSON
    files = sorted(glob(os.path.join(RAW_DATA_DIR, "github_*.json")), reverse=True)
    if not files:
        print("Brak plików github do przetworzenia.")
        return
    latest_file = files[0]
    with open(latest_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    items = data.get("items", [])
    if not items:
        print("Brak danych w github JSON.")
        return

    # Wyciągnięcie wybranych kolumn do DataFrame
    df = pd.DataFrame([{
        "repo_name": item["name"],
        "owner": item["owner"]["login"],
        "stars": item["stargazers_count"],
        "forks": item["forks_count"],
        "created_at": item["created_at"],
        "language": item["language"],
        "description": item["description"]
    } for item in items])

    output_path = os.path.join(PROCESSED_DATA_DIR, "github_repos.csv")
    df.to_csv(output_path, index=False)
    print(f"Przetworzono i zapisano dane GitHub do {output_path}")

def main():
    process_github_data()
    # Tutaj dodasz kolejne funkcje przetwarzające inne API

if __name__ == "__main__":
    main()
